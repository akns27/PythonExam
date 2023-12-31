"""
주사위는 각 면에 1~6까지 적혀 있는 정육면체이다.

이런 주사위 2개를 굴려 합이 k가 나오는 경우를 조사하려고 한다.

예를 들어, 주사위 두개를 굴려 5가 나오는 경우는 1 4, 2 3, 3 2, 4 1 이다.

그리고 주사위를 하나만 굴리는 경우는 없다.
___
출력

합이 k가 되는 두 주사위의 눈이 출력된다. 

첫 번째 출력되는 수는 첫번째 주사위의 눈이고, 두 번째 출력되는 수는 두번째 주사위의 눈이다.

출력은 첫번째 주사위의 눈이 작은 수에서 큰 순서로 출력한다.
"""

k = int(input())

for i in range(1, 7):
  for j in range(1,7):
    if (i+j == k):
      print(i, j)

#i와 j는 정수 값을 가지므로, k도 정수 값을 가져야 합니다. k가 문자열이면 i + j == k 조건문은 항상 False가 됩니다. 따라서, k를 정수로 형변환해주지 않으면 for 루프는 한 번도 실행되지 않습니다.
