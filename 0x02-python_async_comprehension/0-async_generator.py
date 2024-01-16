#!/usr/bin/env python3
""" generate float """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """await for multiprocessing"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
