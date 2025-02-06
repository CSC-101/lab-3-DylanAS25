def inc(m:int) -> int:
    return m+1          # calls m=3 and m=4, returns 4 and 5

def check(n:int) -> bool:
    return n>2          #n=0 returns false, n=1 returns false, n=2 returns false,
    # n=3 returns true, n=4 returns true

answer = [inc(x) for x in range(5) if check (x)]
print(answer)       #answer = [4,5]

