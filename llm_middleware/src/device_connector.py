class DeviceConnectorBase:
    def __init__(self, device_config):
        self.device_config = device_config

    def connect(self):
        # Establish connection with the device
        pass

    def send_command(self, command):
        # Send command to the device
        pass

    def receive_data(self):
        # Receive data from the device
        pass
