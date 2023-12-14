"""
d = [] # []를 이용하여 아무것도 없는 리스트 만들기
for i in range(20) :
  d.append([]) #리스트안에 다른 리스트 널기
  for j in range(20) :#j는 열
    d[i].append(0)#i는 행, 20X20짜리 바둑판을 만들고 0으로 초기화해주기
#행은 가로, 열은 세로 (분단 줄 셀때를 기억)

n = int(input())#돌의 개수 n을 입력받기
for i in range(n) :#n번 만큼
  x, y = input().split()
  d[int(x)][int(y)] = 1 #좌표값 x,y 입력받아서 1넣기

#사각형 모양 출력하기

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end = ' ')#공백두고
  print()#줄바꿈



1. 0이 들어간 바둑판 만들기 -> []으로 리스트를 일단 만들고 []안에 append를 써서 리스트를 넣고, 열과 행을 만들고(20X20) 0을 넣기
2. 좌표값 입력 받아서 1 넣기 -> x,y 입력받고, 입력받은 게 있는거에 1로 바꿔주기
3. 사각형 모양 출력하기 -> 이중 for문을 써서 출력하기

아래에는 리스트 컴프리헨션을 이용하여 업그레이드 한 코드

"""
# 돌의 개수 n 입력받기
n = int(input())
 # 20x20 크기의 2차원 리스트 생성 및 0으로 초기화
d = [[0 for i in range(20)] for j in range(20)]#[0]짜리 칸을 20번 만듦


# 돌을 놓을 좌표 입력받고 바둑판에 1로 표시
for i in range(n):
    x,y = map(int,input().split())
    d[x][y] = 1 

 # 바둑판 출력
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print()