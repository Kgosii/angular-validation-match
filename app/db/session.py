from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

settings = get_settings()

database_url = settings.DATABASE_URL

engine = create_async_engine(database_url, future=True, echo=settings.ENV == "dev")

AsyncSessionLocal = sessionmaker(
	bind=engine,
	expire_on_commit=False,
	class_=AsyncSession,
	autoflush=False,
	autocommit=False,
)

async def get_db() -> AsyncSession:
	async with AsyncSessionLocal() as session:
		yield session