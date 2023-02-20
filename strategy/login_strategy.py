from .strategy import Strategy
from message.messages_codes import LOGIN, LOGIN_OK, LOGIN_KO
from message.messages_factory import MessagesFactory


class LoginStrategy(Strategy):
    def __init__(self, message):
        super().__init__(message)

    def reply(args=None):
        import random
        login_or_not_login = random.randint(0,99)
        if login_or_not_login <= 49:
            # ok login
            output_message = MessagesFactory.create(LOGIN_OK, "LOGIN_OK")
        else:
            output_message = MessagesFactory.create(LOGIN_KO, "LOGIN_KO")
        return output_message
        
