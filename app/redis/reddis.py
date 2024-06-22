import os

import aioredis

REDIS_URL = os.getenv("REDIS_URL")


async def get_redis():
    return await aioredis.create_redis_pool(REDIS_URL)
