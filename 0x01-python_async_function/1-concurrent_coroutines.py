#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n
    times with the specified max_delay, wait_n should return the list
    of all the delays (float values) in ascending order."""
    list_delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        list_delays.append(delay)

    return sorted(list_delays)
