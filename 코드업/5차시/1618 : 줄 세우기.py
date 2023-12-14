#몸무게가 가벼운 사람부터 무거운 사람의 순서로 출력한다.
"""
풀이법 1
a = list(map(int,input().split()))

a.sort()
print(*a)
"""
#풀이법 2
a = list(map(int,input().split()))

result = sorted(a)
print(*result)
