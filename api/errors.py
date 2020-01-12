from werkzeug.exceptions import HTTPException


class InternalError(HTTPException):
    """
    Just a basic internal server error (500) to throw.
    """

    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 500


class BadRequest(HTTPException):
    """
    Something about the request was malformed.
    """

    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 400


class Unauthorized(HTTPException):
    """
    The client isn't authorized to make this request.
    """

    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 403


class MethodNotAllowed(HTTPException):
    """
    Using for queue being empty but someone trying to effect it
    like voting to skip on an empty queue
    """

    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 405
