import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "30042007")
    SQLALCHEMY_DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql://postgres:30042007@localhost:5432/tarefas_3a")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
