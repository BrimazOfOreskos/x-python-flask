import logging
import sys

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.basicConfig,
        datefmt=config.log.DATEFMT,
        format=config.log.FORMAT,
        level=config.log.LEVEL,
        stream=sys.stdout,
    )
