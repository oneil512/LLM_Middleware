class MiddlewareCore:
    def __init__(self, llm_integration, command_interpreter):
        self.llm_integration = llm_integration
        self.command_interpreter = command_interpreter
        self.device_connectors = []

    def add_device_connector(self, device_connector):
        self.device_connectors.append(device_connector)

    def process_user_input(self, user_input):
        llm_response = self.llm_integration.get_llm_response(user_input)
        device_commands = self.command_interpreter.interpret_llm_response(llm_response)

        for command, device_connector in zip(device_commands, self.device_connectors):
            device_connector.send_command(command)
