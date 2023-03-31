from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.chat import chat_router
from app.api.v1.llm_chain import llm_chain_router
from app.api.v1.auth import auth_router

from app.core.config import HOST, PORT, CORS_ORIGINS

from app.core.logger import setup_logger

from models.rate_limiter import RateLimitMiddleware


# Initialize logger
setup_logger()

app = FastAPI()
app.include_router(chat_router)
app.include_router(llm_chain_router)
app.include_router(auth_router, prefix="/auth", tags=["auth"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RateLimitMiddleware)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
