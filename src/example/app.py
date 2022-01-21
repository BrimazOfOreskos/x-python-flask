import atexit
import logging

from flask import Flask

from .config import Settings
from .containers import Container


def on_shutdown() -> None:
    logging.info("Shutting down app worker")


def create_app() -> Flask:
    container = Container()
    container.config.from_pydantic(Settings())
    container.init_resources()

    logging.info("Starting app worker")

    atexit.register(on_shutdown)

    app = Flask(__name__)
    app.container = container

    # TODO: Add app loaders and route controllers.

    return app
