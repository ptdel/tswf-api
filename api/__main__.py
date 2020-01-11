from flask import Flask
from config import settings
from bp.routes import api
from bp.error_handlers import error_handlers

app = Flask(__name__)

app.register_blueprint(error_handlers)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(
        host=settings.server.host,
        port=settings.server.port,
        debug=settings.server.debug,
    )
