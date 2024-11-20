from src.config import settings


def get_db_url(
        user: str = settings.db.user,
        password: str = settings.db.password,
        host: str = settings.db.host,
        port: int = settings.db.port,
        name: str = settings.db.name
) -> str:
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"


DB_URL: str = get_db_url()
