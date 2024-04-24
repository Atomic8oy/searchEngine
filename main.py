from app import app
import uvicorn

from config import (
    UVICORN_HOST, UVICORN_PORT, DEBUG
)

def main():
    try:
        uvicorn.run(
            "main:app",
            host=UVICORN_HOST,
            port=UVICORN_PORT,
            log_level=10 if DEBUG else 20
        )
    except FileNotFoundError:  # to prevent error on removing unix sock
        pass
    

if __name__ == "__main__":
    main()