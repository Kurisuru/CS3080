import socket
import threading
import time
import random
import protocol
import string
import uuid

print_lock = threading.Lock()

def beacon(ip_address, beacon_port, manager_port):

    broadcast_port = random.randrange(21000, 22000)
    beacon = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    beacon.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    beacon.bind((ip_address, broadcast_port))

    datagram = protocol.packetize('BROADCAST', 'BEACON',
                                  {'MANAGER':' %05d' % (manager_port)})

    print("BEACON is broadcasting from:", ip_address, broadcast_port)
    print("BEACON is broadcasting on  :", ip_address, beacon_port)
    while(True):
    
        beacon.sendto(datagram, ("255.255.255.255", beacon_port))
        time.sleep(0.1)            

def random_name(length):
    
    letter_count = len(string.ascii_lowercase)
    name = ''
    for i in range(length):
        name += string.ascii_lowercase[random.randrange(letter_count)]
    return name
    
def manager(ip_address, manager_port):
    
    print("MANAGER is listening on ", ip_address, manager_port)
    manager_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    manager_server.bind((ip_address, manager_port))
    manager_server.setblocking(False)
    
    global ports # KEY = port number, VALUE = port name
    
    launch_time = time.time()
    config_time_limit = 10.0
    active_time_limit = 20.0
    network_joining = False
    network_settled = False
    network_active = False
    network_shutdown = False
    network_state = "INI"
    gathered = 0;
    
    fp = open('topology.txt', 'wt')
    
    fp.write('--------------------------------------\n')
    fp.write('SEED: %s\n' % (hex(uuid.getnode())[2:].upper()))
    fp.write('--------------------------------------\n')

    print("Waiting for port request.")
    while True:
        packet = None
        try:
            packet, addr = manager_server.recvfrom(4096)
            (recipient, sender, message) = protocol.depacketize(packet)
        except BlockingIOError:
            pass
        except ConnectionResetError:
            pass
        
        if not packet == None:
            print("%03d: RECEIVED:" % (len(ports)), recipient, sender, message)
            if 'HELLO' in message:
                network_state = "JOINING"
                config_timeout = time.time() + config_time_limit
                new_name = random_name(8)
                new_port = random.randrange(40000, 50000)
                while new_port in ports:
                    new_port = random.randrange(40000, 50000)
                ports[new_port] = new_name
                msg = {}
                msg["USENAME"] = ports[new_port]
                msg["USEPORT"] = "%05d" % (new_port)
                print("MANAGER: TO", addr, "MESSAGE:", msg)
                #time.sleep(0.5)
                manager_server.sendto(protocol.packetize('', 'MANAGER', msg), addr)

            if 'TABLE' in message:
                data = packet.decode()
                print_lock.acquire()
                gathered += 1
                if data.find('TABLE:') >= 0:
                    print('--------------------------------------')
                    print('NODE:', sender, 'PORT:', addr[1])
                    print('--------------------------------------')
                    for entry in data.split()[2:]:
                        print(entry[entry.find(':')+1:])
                    print('--------------------------------------')
                print_lock.release()
                fp.write('--------------------------------------\n')
                fp.write('NODE: %s   PORT: %d\n' % (sender, addr[1]))
                fp.write('--------------------------------------\n')
                for entry in data.split()[2:]:
                    fp.write(entry[entry.find(':')+1:] + '\n')
                fp.write('--------------------------------------\n')

        if network_state == "JOINING" and time.time() > config_timeout:
            print("Network appears to have settled with %d nodes." % (len(ports)))
            network_state = "SETTLED"
            
        if network_state == "SETTLED":
            print("Configuring network")
            connections = create_network_map(ports)
            print("Configuring nodes")
            fp.write('--------------------------------------\n')
            fp.write('MAP:\n')
            fp.write('--------------------------------------\n')
            for port in connections:
                fp.write('NODE: %s (%s)\n' % (port, ports[port]))
                for neighbor in connections[port]:
                    fp.write('   NEIGHBOR: %d (%s)\n' % (neighbor, ports[neighbor]))
                    manager_server.sendto(protocol.packetize(ports[port], 'MANAGER', {'NEIGHBOR':neighbor}), (addr[0], port))
            network_state = "ACTIVE"
            active_timeout = time.time() + active_time_limit
                
        if network_state == "ACTIVE" and time.time() > active_timeout:
            print("Gathering Route Tables")
            network_state = "GATHER"
            network_gather = True
            for port in ports:
                manager_server.sendto(protocol.packetize(ports[port], 'MANAGER', {'DUMP':''}), (addr[0], port))

        if network_state == "GATHER":
            if gathered >= len(ports):
                network_state = "SHUTDOWN"
                
        if network_state == "SHUTDOWN":
            print("NETWORK IS SHUTDOWN")
            fp.close()
            while(True):
                pass
            
# This function returns a dictionary in which the key is a node's assigned port number
# and the value is a set containing that node's neighbors.
def create_network_map(ports):
    
    neighbors = 1
    
    port_list = list(ports.keys())
    
    connections = {}
    # Ensure network is fully connected
    print("Ensure network is fully connected.")
    for i in range(len(port_list)):
        connections[port_list[i]] = set([port_list[(i+1) % len(port_list)]])

    # Pick random nodes to connect to
    print("Pick random nodes to connect to.")
    for port in connections:
        for i in range(neighbors):
            connections[port].add(random.choice(port_list))
        connections[port].discard(port)
    
    return connections
    
        
if __name__ == '__main__':
    
    ports = {}
    
    server_IP = protocol.get_myIP()
    beacon_port = protocol.beacon_port
    manager_port = random.randrange(20000,21000)

    beacon_thread = threading.Thread(target = beacon,
                                     kwargs={"ip_address":server_IP,
                                             "beacon_port":beacon_port,
                                             "manager_port":manager_port}) 
    beacon_thread.start()
    
    manager_thread = threading.Thread(target = manager,
                                     kwargs={"ip_address":server_IP,
                                             "manager_port":manager_port}) 
    manager_thread.start()
    