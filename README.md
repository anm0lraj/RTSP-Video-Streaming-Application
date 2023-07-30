# IMPLEMENTATION OF CLIENT – SERVER STREAMING APPLICATION USING RTSP IN PYTHON

# Description of Files
VideoStream.py</br>
The main function of this file is to open an read the video file in form of byte stream. Moreover, it is also used to read a frame of the video and return the frame number for tracking purposes.</br>
</br>
ServerWorker.py</br>
Whenever a new client comes, a new thread is started to process the requests sent from Client.</br>
The request includes the request type, required file name, ... Server-Worker also response to Client by sending the needed video one frame by one and reply to determine if the request is valid or not.</br>
</br>
Server.py</br>
This file containing the server creates a socket and receives the the client information. It will forward the data to the ServerWorker.py to handle the request processing.</br>
</br>
Server_App.py</br>
This is the main GUI Application to initiate the Server.py which takes the input from user. This accepts Server Port Number from user.</br>
</br>
RtpPacket.py</br>
The main function of this file is to demonstrate the mechanism to encode the variables of a RTP packet such as version, padding, extension, contributing sources (cc), sequence number , marker, payload type(pt), source identifier(ssrc) into a RTP packet and how to decode it. Moreover, it also provides the packet payload and the packet itself. The picture below shows the number of bits needed for each field and we will base on that to set the bits for the header.</br>
</br>
Client.py</br>
The main function of this file is to set up the graphical user interface including 7 buttons (SETUP, PLAY, PAUSE, RESTART, FORWARD, BACKWARD and TEARDOWN) and 1 label (FRAMES). After that, it will connect to the server through the created socket and can begin to send the request to the server.</br>
</br>
ClientLauncher.py</br>
This function is used to get the server’s name, server port, the client RTP port and the video file name to initiate the application.</br>
</br>
Client_App.py</br>
This is the main GUI Application to initiate the ClientLauncher.py which takes the input from user. It takes the IP Address, Server Port Number, Client Port Number and Media File Name.</br>
