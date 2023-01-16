    # 1939. 아주 간단한 계산기
# t = list(map(int, input().split()))
# a = t[0]
# b = t[1]
#     # 같은 표현 :a,b = map(int,input().split())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)

    # 2047. 신문 헤드라인 : 소문자를 대문자로

    # 2046. 스탬프 찍기
# i = int(input())
# print(i * "#")

    # 2042.서랍의 비밀번호
# a,b = map(int, input().split())
# print(a-b+1)

    # 2025. N줄 덧셈
# t = int(input())

# if t % 2 == 0:
#     i = (t + 1) * (t / 2)
#     print(int(i))
# else:
#     i = t * (t + 1) / 2
#     print(int(i))

    # 2058. 자릿수 더하기
# t = list(map(int, input()))
# a = t[0]
# b = t[1]
# c = t[2]
# d = t[3]
# print(a+b+c+d)

    # 1936. 1대 1 가위바위보
# a,b = map(int,input().split())

# if a == 3 and b == 2:
#     print("A")
# elif a == 3 and b == 1:
#     print("B")
# elif a == 2 and b == 3:
#     print("B")
# elif a == 2 and b == 1:
#     print("A")
# elif a == 1 and b == 2:
#     print("B")
# elif a == 1 and b == 3:
#     print("A")

    # 2027. 대각선 출력하기
# 1.
# print("#++++\n+#+++\n++#++\n+++#+\n++++#")
# 2.
for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end="")
        else:
            print('+', end="")
    print()

    # 2068. 최대수 구하기
# T =  int(input())

# for t in range(1,T+1):
#     num = list(map(int, input().split()))
#     max_num = max(num)
#     print(f"#{t} {max_num}")

    # 1933. 간단한 N 의 약수

    # 2029. 몫과 나머지 출력하기
# T = int(input())

# for t in range(1,T+1):
#     a,b = map(int,input().split())
#     t_ans = a//b
#     t_extra = a%b
#     print(f"#{t} {t_ans} {t_extra}")

    # 2070. 큰 놈, 작은 놈, 같은 놈
# T = int(input())

# for t in range(1,T+1):
#     a,b = map(int,input().split())
#     if a < b:
#         print(f"#{t} <")
#     elif a == b:
#         print(f"#{t} =")
#     else:
#         print(f"#{t} >")

    # 2050. 알파벳을 숫자로 변환
T = list(input())
i = 0
T[0] = i+1

#
print()