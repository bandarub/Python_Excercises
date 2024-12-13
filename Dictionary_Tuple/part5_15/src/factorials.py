def factorials(n: int):
    def fact(x: int) -> int:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    
    return {i: fact(i) for i in range(1, n + 1)}

if __name__ == "__main__":
    result = factorials(5)
    print(result[1])
    print(result[3])
    print(result[5])
