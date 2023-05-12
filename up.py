import time

def clock():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
