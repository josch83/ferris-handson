import functools

from ferris_cli.v2 import ApplicationConfigurator
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

config = ApplicationConfigurator.get()

CONSUMER_MODE = config.get("CONSUMER_MODE", "rw")
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
    config["DB_USERNAME"], config["DB_PASSWORD"], config["DB_HOST"], config["DB_PORT"], config["DB_NAME"]
)


def consumer_mode(modes):
    def f(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if CONSUMER_MODE in modes:
                return func(*args, **kwargs)

        return wrapper

    return f


def _get_engine_session(url, verbose=True):
    print(url, flush=True)
    engine = create_engine(url, pool_pre_ping=True, echo=verbose)
    session = scoped_session(sessionmaker(bind=engine, autoflush=True))
    return engine, session


def db_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _engine, _session = _get_engine_session(SQLALCHEMY_DATABASE_URI, verbose=False)

        kwargs["dbsession"] = _session
        fr = func(*args, **kwargs)
        _session.remove()
        _engine.dispose()

        return fr

    return wrapper
