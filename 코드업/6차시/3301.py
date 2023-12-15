"""
어떤 가게의 욕심쟁이 점원은 거스름돈을 나눠줄때 거스름돈의 개수를 적게해서 주고자 한다.

거스름돈을 입력 받아 점원이 줄 수 있는 최소 거스름돈의 개수를 출력하시오.

예를 들어 54520원인 경우,

거스름돈으로 50000원권 1장, 1000원권 4장, 500원 1개, 10원 2개 해서 총 8개이다.

"""
a = int(input())
count = 0#화폐 개수를 세기 위한 변수

for i in [50000,10000,5000,1000,500,100,50,10]:#사용 가능한 화폐를 for문에 넣고
  if a// i != 0:#a를 i로 나눈 몫이 0이 아니면 = 나눌 수 있다면
    count += a//i#count에 a를 i로 나눈 몫을 추가 = 거스름돈 개수 추가
    a = a % i#a값을 a를 i로 나눈 나머지로 변경 = 나머지 남은 돈 구하기
print(count)#count 값 출력

#greedy는 항상 최적의 값이 나오지는 않는다.
