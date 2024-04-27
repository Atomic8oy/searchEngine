from decouple import config
from dotenv import load_dotenv

load_dotenv()

MYSQL_URL = config("MYSQL_URL", default="mysql+pymysql://root@localhost:3306/searchEngine")

UVICORN_HOST = config("UVICORN_HOST", default="0.0.0.0")
UVICORN_PORT = config("UVICORN_PORT", default=8000)


DEBUG = config("DEBUG", default=False)