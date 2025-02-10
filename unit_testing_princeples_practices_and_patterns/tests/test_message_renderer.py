from app.message import Message
from app.message import MessageRenderer

def test_rendering_a_message():
    sut = MessageRenderer()
    message = Message(
            header="h",
            body="b",
            footer="f",
    )

    html = sut.render(message)

    assert html == "<h1>h</h1><b>b</b><i>f</i>"
