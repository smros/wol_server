# Wake-On-LAN
#
# Copyright (C) 2002 by Micro Systems Marc Balmer
# Written by Marc Balmer, marc@msys.ch, http://www.msys.ch/
# This code is free software under the GPL

import struct, socket

def WakeOnLan(ethernet_address):

  # Construct a six-byte hardware address

  addr_byte = ethernet_address.split(':')
  hw_addr = struct.pack('BBBBBB', int(addr_byte[0], 16),
    int(addr_byte[1], 16),
    int(addr_byte[2], 16),
    int(addr_byte[3], 16),
    int(addr_byte[4], 16),
    int(addr_byte[5], 16))

  # Build the Wake-On-LAN "Magic Packet"...

  msg = '\xff' * 6 + hw_addr * 16
  #print hw_addr
  #print msg
  
  # ...and send it to the broadcast address using UDP

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  s.sendto(msg, ('<broadcast>', 9))
  s.close()

# Example use
#WakeOnLan('0:3:93:81:68:b2') 

if __name__ == '__main__':
    # Use macaddresses with any seperators.
    # Family Mac
 #   WakeOnLan('00:1B:63:B4:CF:2C')
    # Server64
 #   WakeOnLan('00:13:D4:78:A6:57')
 #   WakeOnLan('00:50:f2:a2:4f:14')
    # Treadmill Laptop
    WakeOnLan('00:24:1D:16:32:2C')
#    wake_on_lan('0F-0F-DF-0F-BF-EF')
    # or without any seperators.
#    wake_on_lan('0F0FDF0FBFEF')
