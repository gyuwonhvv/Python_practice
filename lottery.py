# 로또 시뮬레이션
from random import randint

# 내 로또 번호 생성
def generate_numbers(n): 
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

# 로또 당첨번호 생성
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    winning_numbers = sorted(winning_numbers[:6]) + winning_numbers[6:]
    return winning_numbers

# 로또 번호 갯수 비교
def count_matching_numbers(numbers, winning_numbers):
    same_num = list(set(numbers).intersection(winning_numbers))
    return len(same_num)

# 당첨금 확인
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers)
    
    if count == 3:
        return 5000
    elif count == 4:
        return 50000
    elif count == 5:
        return 1000000
    elif count == 6 and winning_numbers[6] in numbers:
        return 50000000
    elif count == 6:
        return 1000000000 
    else:
        return 0
        