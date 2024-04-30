import socket

beacon_port = 27319

def get_myIP():
    
    return "127.0.0.1" # local host
    return socket.gethostbyname(socket.gethostname())

def packetize(recipient, sender, data):
    
    message = ""
    
    message += pack_line("RECIPIENT", recipient)
    message += pack_line("SENDER", sender)
    
    if type(data) == dict:
        for key in data:
            message += pack_line(key, data[key])
            
    if type(data) == tuple:
        key = data[0]
        lines = data[1].split()
        for line in lines:
            message += pack_line(key, line)
        #print("<MSG>\n%s</MSG>" % message)        
    return message.encode()
    
def pack_line(key, value):
    
    return "%s:%s\n" % (key.upper(), value)

def unpack_line(line):
    
    sep = line.find(':')
    
    if sep < 0:
        return (None, line)
    key = line[:sep]
    value = line[sep+1:]
    
    return (key, value)

def depacketize(packet):
    
    lines = packet.decode().split('\n')

    (key, recipient) = unpack_line(lines[0])
    (key, sender) = unpack_line(lines[1])
    
    data = {}
    for line in lines[2:]:
        (key, value) = unpack_line(line)
        if key != None:
            data[key] = value

    return recipient, sender, data

if __name__ == "__main__":
    
    data = {"AGE":59, "instrument":"trumpet"}
    
    packet = packetize("sue", "fred", data)
    
    (recipient, sender, r_data) = depacketize(packet)
    
    print(recipient)
    print(sender)
    for k in r_data:
        print(k, ':', r_data[k], sep='')
        