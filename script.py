import setup_path
import airsim
import sys
import time
import socket

places = {'01': [[airsim.Vector3r(21.23,-413.24,-101.9),
                 airsim.Vector3r(21.23,-1321.04,-257.5),
                 airsim.Vector3r(21.32,-1875.14,-257.5),
                 airsim.Vector3r(-262.3,-2459,-257.5)], [-280,-2630,-257.5,10, 50], [airsim.Vector3r(-262.3,-2459,-257.5),
                                                                                     airsim.Vector3r(21.32,-1875.14,-257.5),
                                                                                     airsim.Vector3r(21.23,-1321.04,-257.5),
                                                                                     airsim.Vector3r(21.23,-413.24,-50)]]}

class ReachArea():
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', 7000)
        print('starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)

        # Listen for incoming connections
        self.sock.listen(1)

        # Wait for a connection
        print('Waiting for a connection')
        self.connection, self.client_address = self.sock.accept()
    
    def take_off(self):
        client = airsim.MultirotorClient()
        client.confirmConnection()
        client.enableApiControl(True)

        print("arming the drone...")
        client.armDisarm(True)

        state = client.getMultirotorState()
        if state.landed_state == airsim.LandedState.Landed:
            print("taking off...")
            client.takeoffAsync().join()
        else:
            client.hoverAsync().join()

        time.sleep(1)

        state = client.getMultirotorState()
        if state.landed_state == airsim.LandedState.Landed:
            print("take off failed...")
            sys.exit(1)


    def going_to(self, array, final_pos):
        drone_state = client.getMultirotorState()
        print("Going to destination...")
        result = client.moveOnPathAsync(array,                           
                                32, 200,
                                airsim.DrivetrainType.ForwardOnly, airsim.YawMode(False,0), 20, 1).join()
        time.sleep(2)
        client.moveToPositionAsync(final_pos[0], final_pos[1], final_pos[2], final_pos[3], final_pos[4]).join()
        time.sleep(5)

    def landing(self, z):
        print("Come down quickly...")
        client.moveToZAsync(z, 3).join()
        client.hoverAsync().join()
        print("Landing...")
        client.landAsync().join()
        client.armDisarm(False)
        client.enableApiControl(False)
    
    def turn_back(self, data):
        self.take_off()
    
        # AirSim uses NED coordinates so negative axis is up.
        z = -258
        print("Make sure we are hovering at {} meters...".format(-z))
        client.moveToZAsync(z, 6).join()
    
        self.going_to(places[data.hex()][2], [-1.2, -9.5, -50, 10, 50])
        self.landing(-0.5)

    
    def move(self, data):
        self.take_off()
    
        # AirSim uses NED coordinates so negative axis is up.
        z = -50
        print("Make sure we are hovering at {} meters...".format(-z))
        client.moveToZAsync(z, 6).join()

        initial_position = airsim.Vector3r(21.4, 166.10, -20.9)  # Adjust these values as needed with the initial position
        client.simSetVehiclePose(airsim.Pose(initial_position, airsim.Quaternionr()), True)
    
        self.going_to(places[data.hex()][0],places[data.hex()][1])
        self.landing(-130)


drone_reaching = ReachArea()

try:
    print('connection from', drone_reaching.client_address)
    client = airsim.MultirotorClient()
    client.confirmConnection()
    client.enableApiControl(True)

    client.armDisarm(False)
    client.enableApiControl(False)
    print("Waiting for message...")

    # Receive the data in small chunks and retransmit it. While True can be removed
    data = drone_reaching.connection.recv(16)
    
    if data.hex() in places:
       drone_reaching.connection.sendall(b'Received: Going to destination')
       drone_reaching.move(data)
       # Send the encoded message
       drone_reaching.connection.sendall(b'Arrived to destination')
       time.sleep(5)
       drone_reaching.connection.sendall(b'Turning back home')
       drone_reaching.turn_back(data)
       drone_reaching.connection.sendall(b'Arrived to home')
    else:
        print("Destination not in dataset")
       
finally:
    print("Finished, closing connection")
    # Clean up the connection
    drone_reaching.connection.close()
   

