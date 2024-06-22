import logging
import os

import sentry_sdk
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.routers import auth

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)  # Enable SQL logging if needed
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

app = FastAPI()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
)

app.add_middleware(SentryAsgiMiddleware)

# Include the auth router
app.include_router(auth.router, prefix="/auth")


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    logging.info("Starting up the application")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    logging.info("Shutting down the application")
    await engine.dispose()


# Increase logging level
uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
