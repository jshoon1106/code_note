
# 숫자 야구 : 숫자를 알아맞추는 게임이다
# 출제자는 숫자를 정한다(기본 3자리)(자리수up -> 난이도up)
# (단 각 자릿수끼리 겹치지 않아야 한다)
# 맞추는 사람은 숫자를 추측하여 말한다
# 맞추는 사람이 말한 숫자와 비교했을 때:
#     1개의 같은 자릿수의 숫자가 같다: 1스트라이크
#     1개의 다른 자릿수의 숫자가 같다: 1볼
#     같은 숫자가 없다: 아웃
# 이런 단서를 가지고 추측하면서 맞추는 게임이다

# 코드 칠때 생각하고 치기
# 머릿속으로 결과를 예상하면서..

import random

while True:
    com1 = random.randint(0, 9)
    com2 = random.randint(0, 9)
    com3 = random.randint(0, 9)

    if com1 == com2:
        continue
    elif com2 == com3:
        continue
    elif com3 == com1:
        continue
    else:               # 조건 없는 반복이 있으면 나가는 조건이 있어야함
        break

while True:
    strike_c = 0
    ball_c = 0
    
    my1 = int(input('1st number: '))
    my2 = int(input('2nd number: '))
    my3 = int(input('3rd number: '))

    if com1 == my1:
        strike_c += 1
    elif com1 == my2 or com1 == my3:    # if-elif-else 중 한 곳의 코드만 실행됨
        ball_c += 1

    if com2 == my2:
        strike_c += 1
    elif com2 == my1 or com2 == my3:
        ball_c += 1

    if com3 == my3:
        strike_c += 1
    elif com3 == my1 or com3 == my2:
        ball_c += 1
    
    if strike_c == 3:
        print('Congratulation!')
        break
    elif (strike_c, ball_c) == (0, 0):
        print('OUT..')
    else:
        print('{}stirke {}ball'.format(strike_c, ball_c))
