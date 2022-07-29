import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())
for i in range(t):
    test_case = list(map(int, input().split()))
    cnt = 0
    for j in range(len(test_case)):
        if j % 2 == 0:
            cnt += test_case[j]*2
        else:
            cnt += test_case[j]
    rst = 10 - (cnt % 10)
    if rst != 10:
        print(f'#{i+1} {rst}')
    else:
        print(f'#{i+1} 0')