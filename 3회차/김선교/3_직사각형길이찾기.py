import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())
for i in range(t):
    test_case = list(map(int, input().split()))
    test_dic = {}
    for j in test_case:
        test_dic[j] = test_dic.get(j, 0) + 1
    for j in test_dic:
        if test_dic[j] == 1:
            print(f'#{i+1} {j}')
            break
    else:
        print(f'#{i+1} {j}')