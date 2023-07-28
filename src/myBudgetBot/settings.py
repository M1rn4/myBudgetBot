
from fastapi_mail import ConnectionConfig
from pydantic import EmailStr
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class MybudgetbotSettings(BaseSettings):
    BACKEND_HOST:str = "http://localhost:8000"
    #model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_myBudgetBot_settings():
    return MybudgetbotSettings()


class TokensConfig(BaseSettings):
    SECRET_KEY:str = "8e732540695d1c0f0bef041528f31c4d2dfdff2daa0d8dd05eb5bc4f6aeb7d8a"
    JMV_ALGORITHM:str = "HS256"
    TIME_DELTA:int = 2
    #model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_tokens_config()->TokensConfig:
    return TokensConfig()

# class EmailsSettings(BaseSettings):
#     MAIL_USERNAME:str
#     MAIL_PASSWORD:str
#     MAIL_FROM:EmailStr
#     MAIL_FROM_NAME:str
#     MAIL_PORT:int
#     MAIL_SERVER:str
#     MAIL_TLS:bool
#     MAIL_SSL:bool
#     TEMPLATE_FOLDER:str

#     model_config = SettingsConfigDict(env_file=".env")

# @lru_cache()
# def get_email_settings():
#     email_settings=EmailsSettings()
#     return ConnectionConfig(**email_settings.dict())


class DatabaseSettings(BaseSettings):
    DATABASE_USER:str = "myBudgetBot_user"
    DATABASE_PASSWORD:str ="myBudgetBot_password"
    DATABASE_HOST:str = "myBudgetBot_db"
    DATABASE_NAME:str = "myBudgetBot_db"
    DATABASE_PORT:str = "3306"

    #model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_database_string_connection():
    
    database_settings = DatabaseSettings()
    connection_string = "mysql+pymysql://user:password@host:port/database_name"
    
    connection_string=connection_string\
                      .replace("user",database_settings.DATABASE_USER)\
                      .replace("password",database_settings.DATABASE_PASSWORD)\
                      .replace("host",database_settings.DATABASE_HOST)\
                      .replace("port",database_settings.DATABASE_PORT)\
                      .replace("database_name",database_settings.DATABASE_NAME)
      
    return connection_string