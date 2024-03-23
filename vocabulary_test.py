# 고급단어장
import random

with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    vocab = {line.strip().split(": ")[0]: line.strip().split(": ")[1] for line in f}

# 문제 내기
while True:
    # 랜덤한 문제 받아 오기
    english_word = random.choice(list(vocab.keys()))
    korean_word = vocab[english_word]

    # 유저 입력값 받기
    guess = input(f"{korean_word}: ")
    
    # 프로그램 끝내기
    if guess == 'q':
        break

    # 정답 확인하기
    elif guess == english_word:
        print("정답입니다!\n")
    else:
        print(f"아쉽습니다. 정답은 {english_word}입니다.")


with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        vocab = {line.strip().split(": ")[0]: line.strip().split(": ")[1]}