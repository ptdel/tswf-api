from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

#: The blueprint object for error handlers
error_handlers = Blueprint("error_handlers", __name__)


@error_handlers.app_errorhandler(HTTPException)
def http_error_handler(error):
    """ Generic HTTP error handler, this formats Error messages into a
    more friendly JSON response.

    :param HTTPException error: The HTTP exception
    :return: JSON readable error messages
    :rtype: json
    """
    return (
        jsonify(
            dict(
                error=dict(
                    (k, getattr(error, k))
                    for k in dir(error)
                    if not callable(getattr(error, k)) and not k.startswith("__")
                )
            )
        ),
        error.code,
    )


@error_handlers.app_errorhandler(Exception)
def unexpected_error_handler(error):
    """ Generic error handler that formats non-HTTP and unhandled exceptions
    into a more friendly JSON response.

    :param Exception error: the unhandled exception
    :return: JSON readable error messages
    :rtype: json
    """
    resp = {"code": 500, "description": [str(_) for _ in error.args]}
    return jsonify(dict(error=str(resp))), 500
