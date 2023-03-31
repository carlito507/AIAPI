from aiocache import SimpleMemoryCache
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.models.exceptions import CustomNotFoundException

import logging

logger = logging.getLogger(__name__)
cache = SimpleMemoryCache()


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get the client IP address
        ip = request.client.host
        # Get the current number of requests for this IP
        current = await cache.get(ip)
        # If the IP is not in cache, set it to 0
        if current is None:
            current = 0
        # If the IP has made more than 10 requests, raise an exception
        if current >= 200:
            logger.warning(f"Rate limit exceeded for IP {ip}")
            raise CustomNotFoundException("Too many requests")
        # Increment the number of requests for this IP
        await cache.set(ip, current + 1, 3600)
        response = await call_next(request)
        # Otherwise, call the next middleware
        return response
