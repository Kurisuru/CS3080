import socket
import random
import threading
import protocol
import time

ipv4_addr = protocol.get_myIP()

setup_lock = threading.Lock()
print_lock = threading.Lock()

print_lock = threading.Lock()

def tprint(s):

    print_lock.acquire()
    print(s)
    print_lock.release()

def find_manager():

    # Establish initial contact with BEACON to get port number for manager
    beacon_port = protocol.beacon_port
    
    setup_lock.acquire() # Needed to share beacon port on local_host

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipv4_addr, beacon_port))

    beacon_found = False
    while not beacon_found:
        data, addr = sock.recvfrom(4096)
        (recipient, sender, message) = protocol.depacketize(data)
        if "BEACON" == sender:
            if "MANAGER" in message:
                manager_port = int(message["MANAGER"])
                manager_addr = (addr[0], manager_port)
                beacon_found = True
    sock.close()                
    setup_lock.release()
    
    return manager_addr

def join_network(manager_address):
    
    # Use a random port number until the manager assigns a permanent one
    port = random.randrange(23000, 24000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipv4_addr, port))

    # Request a node name and port number from the manager
    node_port = -1
    while node_port < 0:
        datagram = protocol.packetize("MANAGER", "UNKNOWN", {"HELLO":''})
        sock.sendto(datagram, manager_address)
        datagram, addr = sock.recvfrom(4096)
        (recipient, sender, message) = protocol.depacketize(datagram)
        if ("USENAME" in message) and ("USEPORT" in message):
            node_name = message["USENAME"]
            node_port = int(message["USEPORT"])
    sock.close()

    return (node_name, node_port)

def router(router_number):

    neighbors = {}
    stable_window = 5.0

    # Find the manager and join the network
    manager_address = find_manager()
    (node_name, node_port) = join_network(manager_address)
    
    tprint("%02d [%s] PORT: %5d" % (router_number, node_name, node_port))
    
    # Create the final socket for the router on the assigned port            
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipv4_addr, node_port))

    while True:
        
        # Wait for a message
        datagram, addr = sock.recvfrom(4096)
        (recipient, sender, message) = protocol.depacketize(datagram)
        
        # IF message is from MANAGER
            # IF it's a NEIGHBOR notification
                # Send a LINK message to the neighbor
            # IF it's a DUMP request
                # Send a message with the routing table entries to the MANAGER
                
        # ELSE the message is from a NEIGHBOR                
            # IF it's a LINK message and sender is not in neighbors list
                # Add sender's node name and port number to neighbors list
                # IF the recipient was UNKNOWN
                    # Reply with a LINK message to the sender
            # IF it's an EXCHANGE message
                # FOR EACH entry
                    # IF the destination is not in forwarding table or is shorter
                        # Update forwarding table
                # IF the forwarding table was modified
                    # Send a table summary to each neighbor
            
if __name__ == '__main__':
    
    nodes_in_network = 32
    threads = []
    for i in range(nodes_in_network):
        threads.append(threading.Thread(target = router, args = [i]))
    for thread in threads:
        thread.start()
        