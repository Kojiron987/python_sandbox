from unittest.mock import MagicMock

from app.gateway import EMailGateway, Controller


def test_sending_a_greetings_email():

    mock = MagicMock(spec=EMailGateway)

    sut = Controller(mock)

    sut.greet_user("user@email.com")

    mock.send_greetings_email.assert_called_once_with("user@email.com")


