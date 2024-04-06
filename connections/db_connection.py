import os

from sqlalchemy import create_engine, QueuePool
from sqlalchemy.orm import sessionmaker
import time
from sqlalchemy.exc import OperationalError
from connections import Base
from dotenv import load_dotenv


class SessionManager:
    def __init__(self):
        load_dotenv()
        self.Base = Base
        self.engine = None
        self.pool_size = 4
        self.max_overflow = 2
        self.max_retries = 3
        self.retry_interval = 20
        # credentials
        self.env = None
        self.user = os.getenv("USER_NAME")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.port = int(os.getenv("PORT"))
        self.database = os.getenv("DATABASE")

    def create_connection(self):
        self.engine = create_engine(
            f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}",
            poolclass=QueuePool,
            pool_size=self.pool_size,
            max_overflow=self.max_overflow,
            pool_pre_ping=True
        )
        self.Base.metadata.create_all(self.engine)

    def create_session(self):
        self.create_connection()
        for retry_count in range(self.max_retries):
            try:
                Session = sessionmaker(bind=self.engine)
                return Session()
            except OperationalError as e:
                if "Too many connections" in str(e):
                    print(f"Too many connections. Waiting for {self.retry_interval} seconds before retrying...")
                    time.sleep(self.retry_interval)
                else:
                    raise
        raise RuntimeError(f"Unable to establish a database connection after {self.max_retries} retries.")
