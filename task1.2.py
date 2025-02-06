
def square(n:int) -> int:
    return n*n          #1,4,9,16

squares = [square(x) for x in [1,2,3,4]]
print(squares)      #[1,4,9,16]