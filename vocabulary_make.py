# 단어장 만들기
with open('vocabulary.txt', 'a', encoding='utf-8') as f:
    while True:

        write_eng = input("영어 단어를 입력하세요: ")
        if write_eng == 'q':
            break
        write_kor = str(input("한국어 뜻을 입력하세요: "))
        if write_kor == 'q':
            break
        f.write(f"{write_eng}: {write_kor}\n")
        