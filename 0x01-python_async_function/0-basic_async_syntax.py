#!/usr/bin/env python3
# 0-basic_async_syntax.py

import asyncio
import random


async def wait_random(max_delay=10):
    num = random.random() * max_delay
    await asyncio.sleep(num)
    return num
