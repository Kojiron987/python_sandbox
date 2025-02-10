from dataclasses import dataclass

@dataclass
class Message:
    header: str
    body: str
    footer: str

class MessageRenderer:

    def render(self, message: Message):
        return f"<h1>{message.header}</h1><b>{message.body}</b><i>{message.footer}</i>"
