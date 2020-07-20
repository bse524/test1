a = input("입력하세요: ")

if a.isalpha():
    print("문자입니다.")
elif a.isnumeric():
    print("숫자입니다.")
else:
    print("기타입니다.")
