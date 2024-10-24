#!/usr/bin/env python3
"""
exercise.py
"""
import redis


class Cache:
    """Definition of class use for caching data."""

    def __init__(self) -> None:
        """
        Initialise a  Cache class by connecting to redis and,
        remove all data in the connected database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
