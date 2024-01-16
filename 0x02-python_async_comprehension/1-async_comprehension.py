#!/usr/bin/env python3
""" usign random generator from task 0 to create a random list """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """return async random"""
    return [random async for random in async_generator()]
