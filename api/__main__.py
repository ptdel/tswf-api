from flask import Flask
from config import settings
from bp.routes import api
from bp.error_handlers import error_handlers

#: The Flask application
app = Flask(__name__)

#: Registering API routes from a blueprint
app.register_blueprint(error_handlers)

#: Registering error handlers as a blueprint
app.register_blueprint(api)

#: application entry-point
if __name__ == "__main__":
    app.run(
        host=settings.server.host,
        port=settings.server.port,
        debug=settings.server.debug,
    )
