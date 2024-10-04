import time

wait_time = 1  # 1 second
max_tries = 5
attempts = 0

while attempts < max_tries:
    print(f"Attempts = {attempts + 1}, wait time = {wait_time}")
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempts += 1
