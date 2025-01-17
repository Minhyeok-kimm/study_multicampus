# 함수 > 범용적 함수
def add_data(friend):
    katok.append(None) # 빈 칸 추가
    klen = len(katok)
    katok[klen - 1] = friend # 데이터 입력

def insert_data(position, friend):
    # 1단계: 빈 칸 추가
    katok.append(None)
    # 2단계: 한 칸씩 뒤로 미루기
    klen = len(katok)
    for i in range(klen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계: 추가
    katok[position] = friend

def delete_data(position):
    # 1단계: 데이터 지우기
    katok[position] = None
    # 2단계: 한칸 씩 앞으로 당기기
    klen = len(katok)
    for i in range(position, klen-1):
        katok[i] = katok[i+1]
        katok[i+1] = None
    # 3단계: 마지막 칸 삭제
    del katok[klen-1]

# 변수
katok = []

#메인
add_data('다현')
add_data('졍연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)

add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)