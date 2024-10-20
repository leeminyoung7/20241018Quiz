# Quiz 1
import random

def lotto_number():
    results=[]
    while len(results)<6:
        ran_num = random.randint(1,45)
        if ran_num not in results:
            results.append(ran_num)
    return results
number = lotto_number()
print(f"6개 숫자는 {number} 입니다.")
