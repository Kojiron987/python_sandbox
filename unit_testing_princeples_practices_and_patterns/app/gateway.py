class EMailGateway:

    def send_greetings_email(self, to: str):
        print(to)

    def send_receipt(self, to: str, name: str, quantity: int):
        pass


class Controller:

    def __init__(self, gateway: EMailGateway):
        self.gateway = gateway

    
    def greet_user(self, to: str):
        self.gateway.send_greetings_email(to)
