    # 홀수만 더하기
# T = int(input())
# for tc in range(1,T+1):

#     # 숫자 한 줄 입력 받아서 리스트로 만들기
#     num_list = list(map(int, input().split()))

#     # 홀수의 총합
#     ans = 0

#     for num in num_list:
#         # 입력받은 수 중에 홀수가 있는지 확인
#         if num % 2 == 1:
#             #홀수가 맞다면 아래 코드가 실행될 것.
#             ans = ans + num
#     #반복이 끝나면 합을 출력
#     print(f"#{tc} {ans}")


    # 최대수 구하기
# T = int(input())

# for t in range(1,T+1):
#     n = list(map(int,input().split()))
#     max_num = max(n)
#     print(f"#{t} {max_num}")

#     # 가위바위보
# import random

# computer = "랜덤으로 가위바위보중에 하나"

# user = input()

# 둘 중에 승자를 판별해서 승자를 출력

# if user == "가위":
#     #사용자가 가위를 입력했을 경우
#     #컴퓨터가 가위를 내거나 바위를 내거나 보를 내거나
#     if computer == "가위":
#         print(f"나 : {user} / 컴퓨터 : {computer}")     # 교수님이 풀어주시다 만거,,
        



# i = list(map(int,input().split()))
# a = i[0]
# b = i[1]    # a랑 b는 정수

# if a - b == 1 or a - b == -2:
#     print("A")

# if a - b == 2 or a - b == -1:
#     print("B")



    #자릿수 더하기
# n = int(input())

# #파이썬의 내장함수 중에 sum 이라는 함수가 있다.
# sum_n = 0
# #내장함수와 내가 만든 변수의 이름이 같으면
# #원래 내장함수를 사용할 수 없게 되어버린다. ()

# # 10진수이므로 나머지를 더하기
# while n > 0:
#     sum_n = sum_n + (n % 10)    #sum_n +1 = n % 10
#     n = n // 10 #몫만 구하기

# print(sum_n)

    # 스탬프 찍기
# a = int(input())
# print("#" * a)

    # 몫과 나머지 출력하기
# T = int(input())

# for t in range(1, T+1):
#     i = list(map(int, input().split()))
#     a = i[0]
#     b = i[1]
#     m = a // b
#     n = a % b
#     print(f"#{t} {m} {n}")

    # 서랍의 비밀번호
# N = list(map(int,input().split()))
# p = N[0]
# k = N[1]
# print(p-k+1)

#     # 큰 놈, 작은 놈, 같은 놈
# N = int(input())

# for t in range(1,N+1):
#     n = list(map(int, input().split()))
#     a = n[0]
#     b = n[1]

#     if a > b:
#         s = ">"
#     elif a < b:
#         s = "<"
#     elif a == b:
#         s = "="

#     print(f"#{t} {s}")

#     #중간값 찾기
N = int(input())

n = list(map(int, input().split()))
n.sort() #오름차순 정렬
i = n[N//2]

# print(i)

    #최빈수