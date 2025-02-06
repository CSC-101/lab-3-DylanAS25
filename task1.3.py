def check(n:int) -> bool:
    return n>2      # 0(false), 1 (false), 2(False), 3(True), 4(True)

answer = [x for x in range(5) if check(x)]
print(answer)   #answer = [3,4]