# 함수
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num-1)

# 메인
print(addNumber(10))