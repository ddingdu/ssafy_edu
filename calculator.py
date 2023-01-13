"""
i = list(input())  # [1+2]
i = list

op = input()

if op == "+":  # ==: 같다 / !=: 같지 않다
    print("덧셈")
    sum_i = list(i).split("+")
    sum_i = sum(sum_i)
    print(sum_i)
"""

""""
while True:
    a = int(input('n1: '))
    b = int(input('n2: '))

    if a == b == 0:
        print("계산을 종료합니다.")

    c = input('연산자: ')

    if c = "+":
        d = a + b
        print(d)
"""


"""
if op == "-":
    print("뺄셈")

if op == "*":
    print("곱셈")

if op == "/":
    print("나눗셈")

# 숫자 두개 입력 할 때 둘다 0이면 반복 종료
if op == "00":
    break

print(i,op,i)
"""


"""
while True : 
    a = float(input('n1:'))    # float(): 문자를 실수로 바꾸는 함수
    b = float(input('n2:'))
    
    if a == b == 0:    # int(a) and int(b) == 0 도 가능함
        print('종료합니다.')
        break

    c = input('연산자:')


    if c=='*':
        d=a*b
        print('값은', d, '입니다.')
        continue    # 뒤에꺼 무시하고 앞으로 가서 시작 # 반복문 for while 에 쓰는 장치 : (break/continue/pass)
    if c=='+':
        d=a+b
        print('값은', d, '입니다.')
        continue
    if c=='-':
        d=a-b
        print('값은', d, '입니다.')
        continue
    if c=='/':
        d=a/b
        print('값은', d, '입니다.')
        continue

    if c!='+' or c!='-' or c!='*' or c!='/': 
        while True:
            print('연산자를 다시 입력하세요.')
            c = input('연산자:')

            if c=='*':
                d=a*b
                print('값은', d, '입니다.')
                break
            if c=='+':
                d=a+b
                print('값은', d, '입니다.')
                break
            if c=='-':
                d=a-b
                print('값은', d, '입니다.')
                break
            if c=='/':
                d=a/b
                print('값은', d, '입니다.')
                break
"""

"""""
print("                   $$\                     $$\            $$\                         \n                   $$ |                    $$ |           $$ |                        \n $$$$$$$\ $$$$$$\  $$ | $$$$$$$\ $$\   $$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  \n$$  _____|\____$$\ $$ |$$  _____|$$ |  $$ |$$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ \n$$ /      $$$$$$$ |$$ |$$ /      $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|\n$$ |     $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      \n\$$$$$$$\\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      \n \_______|\_______|\__| \_______| \______/ \__| \_______|  \____/  \______/ \__|      \n")
while True:
    print("====== 계산할 두 숫자를 입력해주세요. \n두 수 모두 0을 입력할 경우 종료됩니다. ======")
    a = float(input('n1 : '))
    b = float(input('n2 : '))
    if a == 0 and b==0:
        print("                           /$$\n                          | $$\n  /$$$$$$  /$$$$$$$   /$$$$$$$\n /$$__  $$| $$__  $$ /$$__  $$\n| $$$$$$$$| $$  \ $$| $$  | $$\n| $$_____/| $$  | $$| $$  | $$\n|  $$$$$$$| $$  | $$|  $$$$$$$\n \_______/|__/  |__/ \_______/")
        break
    print("====== 연산자는 [+,-,*,/,//(몫),%(나머지) 중에 입력해주세요. ======")
    cal = input("연산자 : ")

    print('')

    if cal == "+":
        print("결과: " , a+b)
    elif cal == "-":
        print("결과: " , a-b)
    elif cal == "/":
        print(f"결과: {a/b}" if b!=0 else "***** 0으로는 나눌 수 없습니다. *****")
    elif cal == "*":
        print("결과: " , a*b)
    elif cal == "%":
        print(f"결과: {a%b}" if b!=0 else "***** 0으로는 나눌 수 없습니다. *****")
    elif cal == "//":
        print(f"결과: {a//b}" if b!=0 else "***** 0으로는 나눌 수 없습니다. *****")
    else:
        print("연산자는 [+,-,*,/,//(몫),%(나머지) 중에 입력해주세요.")
    
    print("")
"""
