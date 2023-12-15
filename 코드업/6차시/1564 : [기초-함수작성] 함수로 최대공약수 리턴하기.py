
a, b = map(int, input().split())

while(a%b != 0):
  a, b = b, a%b#64, 32

print(b)
"""
def f(a,b):
    while(b!=0):
      a, b = b, a%b#32, 2
    return a

a, b = map(int, input().split())
print(f(a,b))
"""