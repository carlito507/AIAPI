from fastapi import FastAPI, Depends, HTTPException, status
from routes.chat import chat_router
from routes.llm_chain import llm_chain_router
from routes.auth import auth_router
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from slowapi.errors import RateLimitExceeded


app = FastAPI()
app.include_router(chat_router)
app.include_router(llm_chain_router)
app.include_router(auth_router, prefix="/auth", tags=["auth"])

# CORS
origins: list[str] = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def rate_limit_exception_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,  # HTTP status code for "Too Many Requests"
        content={"detail": "Too many requests"},
    )


# Rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exception_handler)


@app.middleware("http")
async def add_rate_limiting(request, call_next):
    response = await call_next(request)
    await app.state.limiter.check_rate_limit(request)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
