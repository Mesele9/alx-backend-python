#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio 
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    list_delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    
    for task in tasks:
        delay = await task
        list_delays.append(delay)

    return sorted(list_delays)