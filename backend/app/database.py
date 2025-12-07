from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dbconfig import DbConfig

dbConfig = DbConfig()

CONNECTION_STRING = "postgresql+asyncpg://" + dbConfig.getUser() + ":" + dbConfig.getPassword() + "@" + dbConfig.getHost() + ":" + dbConfig.getPort() + "/" + dbConfig.getName()

engine = create_async_engine(CONNECTION_STRING, echo = True)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush  = False,
    bind = engine,
    class_ = AsyncSession
)

Base = declarative_base()







