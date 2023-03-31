from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import traceback
import logging
from app.main import app


class CustomNotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)


@app.exception_handler(CustomNotFoundException)
async def custom_not_found_exception_handler(request: Request, exc: CustomNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logging.error(traceback.format_exc())
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal mothafucka server error"},
    )