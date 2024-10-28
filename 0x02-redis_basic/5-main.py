#!/usr/bin/env python3
""" Main file """
from redis import Redis

get_page = __import__('web').get_page

url = "http://127.0.0.1:5002/chatwik/account/login"
client = Redis()

print(get_page(url))
print(client.get(f"count:{url}"))
