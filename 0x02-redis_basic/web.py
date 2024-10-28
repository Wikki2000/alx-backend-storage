#!/usr/bin/env python3
"""
web.py
"""
import redis
import requests
from typing import Callable


def count_calls(func: Callable):
    """
    Count how many times a page is visited.

    :func - The function to be decorated.
    :rtype - The wrapper function.
    """
    def wrapper(url: str) -> str:
        """
        Count how many times a pages is visited and,
        cache it html content for 10 seconds.

        url: The visited URL of page to be cache.
        """
        client: Redis = redis.Redis()
        client.incr(f"count:{url}")

        html_content: str = func(url)
        if html_content:
            client.setex(f"result:{url}", 10, html_content)
        return html_content
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    Get HTML content of a page.

    :url - The URL of page to get it HTML content.
    :rtype - The HTML content of a page.
    """
    return requests.get(url).text
