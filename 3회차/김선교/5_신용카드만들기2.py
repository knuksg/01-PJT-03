import sys

sys.stdin = open("_신용카드만들기2.txt")

t = int(input())
for i in range(t):
    test_case = list(input())
    cnt = 0
    for j in range(len(test_case)):
        if j == 0 and test_case[j] not in ['3', '4', '5', '6', '9']:
            print(f'#{i+1} 0')
            break
        elif test_case[j] == '-':
            cnt = cnt
        else:
            cnt += 1
    if cnt == 16:
        print(f'#{i+1} 1')
    elif 0 < cnt :
        print(f'#{i+1} 0')
    else:
        continue