import threading
import time
import atexit
from concurrent.futures import ThreadPoolExecutor

def never_gonna_end():
    while True:
        print("I am will never end")
        time.sleep(1)

print(f"atexit._ncallbacks()={atexit._ncallbacks()}")

class TrueDameonThreads(ThreadPoolExecutor):
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown(wait=False)

with TrueDameonThreads() as executor:
    end_plz = executor.submit(never_gonna_end)
    time.sleep(5)
    print("Attempting to cancel!")
    end_plz.cancel()

print("Clearing atexit functions xD")
atexit._clear()
print("Done!")
