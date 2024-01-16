#!/usr/bin/env python3
""" async comprehension """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure runtime"""
    start = time.perf_counter()
    coroute = []
    for i in range(4):
        coroute.append(async_comprehension())
    await asyncio.gather(*coroute)
    end = time.perf_counter()
    return end - start
