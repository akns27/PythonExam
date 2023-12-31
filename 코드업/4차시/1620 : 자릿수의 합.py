def f(k):
  res = int(0)
  while k > 0:# 1은 참 -> 무한 루프, true라도 상관 X
    res += (k%10)#이 코드는 res에 10의 자리를 더하기(즉 숫자 한자리 씩 더하기)
    k //= 10  #k의 자릿수를 1 줄여준다
  return res #res값 반환

n = int(input())
while n>10:#n이 한자리 수일때까지 판별
  n = f(n)
print(n)


#자릿수의 합이 한자리가 될때까지 계산하여 출력한다.
"""

res += (k%10) 코드는 res 변수에 k의 10의 자리를 더하는 코드입니다.

k%10은 k의 10의 자리를 나타내는 코드입니다. 예를 들어, k = 12345인 경우 k%10은 5가 됩니다.

res += (k%10)은 res 변수에 k%10의 값을 더하는 코드입니다. 예를 들어, res = 0인 경우 res += (k%10)은 res = 0 + 5 = 5가 됩니다.

따라서 위 코드는 res 변수에 k의 10의 자리를 계속 더하여 k의 각 자리수의 합을 구하는 코드입니다.
_____________

k //= 10 코드는 k를 10으로 나누어 k의 자릿수를 줄이는 코드입니다.

// 연산자는 몫을 구하는 연산자입니다. 예를 들어, k = 12345인 경우 k // 10은 1234가 됩니다.

k //= 10은 k에 k // 10의 값을 대입하는 코드입니다. 예를 들어, k = 12345인 경우 k //= 10은 k = 1234가 됩니다.

따라서 위 코드는 k의 자릿수를 1 줄여주는 코드입니다.
"""