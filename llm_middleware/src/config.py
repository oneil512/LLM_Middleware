class MiddlewareConfiguration:
    def __init__(self):
        self.llm_credentials = {}
        self.device_configurations = []

    def set_llm_credentials(self, api_key, model_name):
        self.llm_credentials = {'api_key': api_key, 'model_name': model_name}

    def add_device_configuration(self, device_config):
        self.device_configurations.append(device_config)
