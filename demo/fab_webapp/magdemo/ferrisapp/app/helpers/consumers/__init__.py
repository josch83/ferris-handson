"""
This module provides functionality related to consumer mode and database handling.

- The `consumer_mode` decorator is provided to conditionally execute a function based on the consumer mode.
- The `ConsumerBaseHandler` class serves as a base class for consumer handlers and provides database handling
    functionality.

"""

import functools

from ferris_cli.v2 import ApplicationConfigurator
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

config = ApplicationConfigurator.get()

CONSUMER_MODE = config.get("CONSUMER_MODE", "rw")

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{config['DB_USERNAME']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:"
    f"{config['DB_PORT']}/{config['DB_NAME']}"
)


def consumer_mode(modes):
    """
    Decorator to conditionally execute a function based on the consumer mode.

    Args:
        modes (list[str]): List of consumer modes in which the decorated function should execute.

    Returns:
        function: Decorated function.

    Example:
        @consumer_mode(['rw', 'ro'])
        def my_function():
            # Function code

    """

    def decorated_function(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if CONSUMER_MODE in modes:
                return func(*args, **kwargs)

        return wrapper

    return decorated_function


class ConsumerBaseHandler:
    """
    Base class for consumer handlers that provides database handling functionality.

    Attributes:
        _engine (sqlalchemy.engine.Engine): Database engine object.
        _session (sqlalchemy.orm.session.Session): Database session object.
        dbsession (sqlalchemy.orm.session.Session): Alias for the database session object.

    """

    def __init__(self):
        self._engine, self._session = self._get_engine_session(SQLALCHEMY_DATABASE_URI, verbose=False)

        self.dbsession = self._session

    def __del__(self):
        self._session.remove()
        self._engine.dispose()

    def _get_engine_session(self, url, verbose=True):
        """
        Create the database engine and session objects.

        Args:
            url (str): Database connection URL.
            verbose (bool, optional): Flag indicating whether to enable verbose logging. Defaults to True.

        Returns:
            sqlalchemy.engine.Engine: Database engine object.
            sqlalchemy.orm.session.Session: Database session object.
        """
        engine = create_engine(url, pool_pre_ping=True, echo=verbose)
        session = scoped_session(sessionmaker(bind=engine, autoflush=True))
        return engine, session
