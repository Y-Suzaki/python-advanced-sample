import time
import random


base_time = 2
base_range = 0.5
wait_time = random.uniform(base_time - base_range, base_time + base_range)

print(str(wait_time)+"秒後に処理を開始します")
time.sleep(wait_time)
print("処理を開始しました")
