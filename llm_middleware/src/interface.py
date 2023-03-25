from config import MiddlewareConfiguration
from llm_integration import LLMIntegration
from core import MiddlewareCore
from command_interpreter import CommandInterpreter

class MiddlewareUI:
    def __init__(self, middleware_core):
        self.middleware_core = middleware_core

    def get_user_input(self):
        # Get user input through a web interface, mobile app, or voice
        user_input = input("Please enter your command: ")
        return user_input

    def process_user_input(self):
        user_input = self.get_user_input()
        self.middleware_core.process_user_input(user_input)

# Example of using the components together

if __name__ == "__main__":
    # Configuration
    middleware_config = MiddlewareConfiguration()
    middleware_config.set_llm_credentials('<API_KEY>', '<MODEL_NAME>')
    middleware_config.add_device_configuration({'device_type': 'IoT', 'device_id': '1', 'device_credentials': {'username': 'user', 'password': 'password'}})

    # Middleware core components
    llm_integration = LLMIntegration(middleware_config.llm_credentials['api_key'], middleware_config.llm_credentials['model_name'])
    command_interpreter = CommandInterpreter()

    middleware_core = MiddlewareCore(llm_integration, command_interpreter)

    # Add device connectors based on device configurations
    for device_config in middleware_config.device_configurations:
        if device_config['device_type'] == 'IoT':
            pass
            #device_connector = IoTDeviceConnector(device_config)
            #middleware_core.add_device_connector(device_connector)
        # Add other device connector types as needed

    # User Interface
    middleware_ui = MiddlewareUI(middleware_core)

    while True:
        middleware_ui.process_user_input()
