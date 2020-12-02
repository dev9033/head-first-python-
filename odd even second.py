from datetime import datetime
import time
import random
odds = list(range(1, 60, 2))


for i in range(5):
    right_this_second = datetime.today().second
    if right_this_second in odds:
        print("odd second")
    else:
        print("even second")
    wait_time = random.randint(1, 10)
    print(f"waiting for {wait_time}")
    time.sleep(wait_time)
