# 함수
def openBox():
    global count
    print('상자 열기')
    count -= 1
    if count == 0:
        print('** 선물 넣기 **')
        return
    else:
        openBox()
        print('상자 닫기##')
    return

# 메인
count = 10
openBox()