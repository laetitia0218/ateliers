def recur(n: int) -> None:
    for i in range(1, n + 1):
        if i % 12 == 0:
            print("FizzBuzz", i)
        elif i % 3 == 0:
            print("Fizz", i)
        elif i % 4 == 0:
            print("Buzz",i)
        else:
            print(i)

        
    
    
print(recur(24))

    
