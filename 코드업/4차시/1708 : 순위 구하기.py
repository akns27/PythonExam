n = int(input())
scores = list(map(int, input().split()))

ranked_scores = sorted(scores, reverse=True)
ranks = [ranked_scores.index(score) + 1 for score in scores]


for i in range(n):
    print(scores[i], ranks[i])

"""
정렬 및 순위 계산:

ranked_scores = sorted(scores, reverse=True): 점수 리스트를 내림차순으로 정렬합니다.

ranks = [ranked_scores.index(score) + 1 for score in scores]: 각 점수에 대한 순위를 계산합니다.
ranked_scores.index(score)는 해당 점수가 정렬된 리스트에서 어느 위치에 있는지 인덱스를 반환합니다.

+ 1은 인덱스를 1부터 시작하는 순위로 변환합니다. 인덱스가 0에서부터 시작하므로 랭크가 1부터 시작하도록 1을 더해줌
"""