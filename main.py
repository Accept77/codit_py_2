en = "a"

while en != "q" :
    en = input("영어 단어를 입력하세요:")
    if en == "q" :
        break
    kor = input("한국어 뜻을 입력하세요:")
    with open('vocabulary.txt', 'a', encoding="UTF-8") as f :
        f.write(f"{en}: {kor}\n")