# 함수
import random
def seqSearch(ary, data):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == data:
            pos = i
            break
    return pos

# 변수
dataAry = [random.randint(30, 190) for _ in range(8)]
findData = random.choice(dataAry)

# 메인
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '가 없습니다.', sep='')
else:
    print(findData, '는 ', position, ' 위치에 있습니다.', sep='')