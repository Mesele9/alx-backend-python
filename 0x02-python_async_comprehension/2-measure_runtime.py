#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather and return the total run
    time. """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
