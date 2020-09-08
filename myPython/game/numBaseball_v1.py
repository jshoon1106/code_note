# <<업그레이드 된 내용 1>>  자릿수를 정할 수 있다!
import random

def isOverlap(com, target):
    if len(com) != 0:
        for c in com:
            if c == target:
                return True
    return False

n = int(input("몇 자리 숫자로 진행하시겠습니까?: "))
com = []
count = 0
for i in range(n):
    rand = random.randint(1, 9)
    if not isOverlap(com, rand):
        com.append(rand)

while True:
    count += 1
    strike_c = 0
    ball_c = 0
    me = []
    for i in range(n):
        me.append(int(input("{}번째 숫자: ".format(i+1))))
        for j in range(n):
            if me[i] == com[j]:
            # 컴퓨터 숫자와 같은 숫자가 있다면: 스트라이크 or 볼
                if i == j:
                    strike_c += 1
                else:
                    ball_c += 1
                break
    # (1) 숫자를 모두 맞춘 경우: 게임 종료                
    if strike_c == n:
        print("축하!! {}회 만에 맞추셨어요!".format(count))
        break
    # (2) 하나도 못 맞춘 경우: 아웃
    elif (strike_c, ball_c) == (0, 0):
        print("아웃.....")
    # (3) 나머지 경우: ?strike ?ball
    else:
        print("{}strike {}ball".format(strike_c, ball_c))