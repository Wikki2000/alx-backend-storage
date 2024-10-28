import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Clear the list if it exists
r.delete('mylist')

# RPUSH example
r.rpush('mylist', 'A')
r.rpush('mylist', 'B')
print("After RPUSH:", r.lrange('mylist', 0, -1))  # Outputs: [b'A', b'B']

# LPUSH example
r.lpush('mylist', 'C')
print("After LPUSH:", r.lrange('mylist', 0, -1))  # Outputs: [b'C', b'A', b'B']

# LRANGE example
all_elements = r.lrange('mylist', 0, -1)
print("LRANGE mylist:", [elem.decode('utf-8') for elem in all_elements])  # Decoding bytes to str

# LLEN example
length = r.llen('mylist')
print("Length of mylist:", length)  # Outputs: 3

# LSET example
r.lset('mylist', 1, 'D')  # Changing the second element (index 1) to 'D'
print("After LSET:", r.lrange('mylist', 0, -1))  # Outputs: [b'C', b'D', b'B']

# LPOP example
popped_value = r.lpop('mylist')
print("Popped value:", popped_value.decode('utf-8'))  # Outputs: C
print("After LPOP:", r.lrange('mylist', 0, -1))  # Outputs: [b'D', b'B']

# RPOP example
popped_value = r.rpop('mylist')
print("Popped value:", popped_value.decode('utf-8'))  # Outputs: B
print("After RPOP:", r.lrange('mylist', 0, -1))  # Outputs: [b'D']

