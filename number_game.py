# 숫자 맞히기 게임
import random

# 상수 정의
chances = 4
answer = random.randint(1, 20)
    
while chances > 0:
    exm = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(chances)))
    if exm == answer:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(4 - chances + 1))
        break
    elif exm > answer:
        chances -= 1
        print("Down")
    elif exm < answer:
        chances -= 1
        print("Up")

if chances == 0:
    print("아쉽습니다. 정답은 {}였습니다.".format(answer))



