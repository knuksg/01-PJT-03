import sys

sys.stdin = open("_문자열의거울상.txt")

t = int(input())
for i in range(t):
    test_case = list(input())
    rst = ''
    for j in range(len(test_case)):
        if test_case[j] == 'b':
            rst += 'd'
        elif test_case[j] == 'd':
            rst += 'b'
        elif test_case[j] == 'p':
            rst += 'q'
        else:
            rst += 'p'
    print(f'#{i+1} {rst[::-1]}')