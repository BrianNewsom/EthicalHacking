# Receives data from machine, then sends back the sum of all data interrpeted as unsigned ints
import socket
import struct

HOST='hitchens.cs.colorado.edu'
PORT=1234
BUFFER_SIZE=1024

# Establish socket and connect
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST,PORT))

running_sum = 0
data = ''

# Receive all data from connection (2048 bytes in buffer size)
for i in range(0,2):
	data += sock.recv(BUFFER_SIZE)


for i in range(0, 14, 4):
	# Unpack as unsigned int
	unsigned_int = struct.unpack('<I', data[i:i+4])[0]
	running_sum += unsigned_int

# Now send our running sum to see if we get a response

# Pack in correct byte order using struct
sock.send(struct.pack('<Q', (running_sum)))

# Print returned password
print sock.recv(BUFFER_SIZE)
