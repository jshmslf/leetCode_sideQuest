def arrayMaker(start, number, steps):
    arr = []
    for i in range(start, number+1, steps):
        arr.append(i)
        
    return print(f"{arr}")

start = int(input("start with>> "))
number = int(input("upto>> "))
steps = int(input("steps (must not be zero)>> "))
arrayMaker(start, number, steps)