__author__ = 'Tibbers'
import sys
from time import time
# from VideoStream import VideoStream


import VideoStream
HEADER_SIZE = 12

class RtpPacket:

	def __init__(self):
		self.header = bytearray(HEADER_SIZE)

	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""

		timestamp = int(time())
		self.header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		header = bytearray(HEADER_SIZE)
		header[0] = (header[0]|version<<6)&0xC0    				
		header[0] = (header[0] | padding << 5) 				
		header[0] = (header[0] | extension << 4)              
		header[0] = (header[0] | (cc & 0x0F))                 

		header[1] = (header[1] | marker << 7)                 
		header[1] = (header[1] | (pt & 0x7f))                 
		
		header[2] = (seqnum & 0xFF00) >> 8                    
		header[3] = (seqnum & 0xFF)                           
		header[4] = (timestamp >> 24)                         
		header[5] = (timestamp >> 16) & 0xFF
		header[6] = (timestamp >> 8) & 0xFF
		header[7] = (timestamp & 0xFF)
		header[8] = (ssrc >> 24)                              
		header[9] = (ssrc >> 16) & 0xFF
		header[10] = (ssrc >> 8) & 0xFF
		header[11] = ssrc & 0xFF
		self.header = header

		self.payload = payload

	def decode(self, byteStream):
		"""Decode the RTP packet."""

		#print byteStream[:HEADER_SIZE]
		self.header = bytearray(byteStream[:HEADER_SIZE])   #temporary solved

		self.payload = byteStream[HEADER_SIZE:]



	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)

	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]  #header[2] shift left for 8 bits then does bit or with header[3]
		return int(seqNum)

	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)

	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)

	def getPayload(self):
		"""Return payload."""
		return self.payload

	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload