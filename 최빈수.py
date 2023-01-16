    # 1204. 최빈수 구하기
T = int(input())

for tc in range(1,T+1):
    t = int(input())   # ???? 왜 필요 ???

    scores = list(map(int, input().split()))

    score_cnt = [0] * 101  # ??? 무슨 의미 ??

    max_score = 0
    for score in scores:
        # score 인덱스에 있는 값을 1증가
        score_cnt[score] += 1

    #최빈수
    max_score = max(score_cnt)

    asn = 0

    # i 는 점수
    # 뒤에서 부터 찾기 
    # 100부터 시작해서 0까지 -1 씩 증가
    for i in range(100,0,-1):
        if score_cnt[i] == max_score:
            print(f"#{tc} {i}")
            break