def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fibs = [0, 1]
        for i in range(2, length):
            fibs.append(fibs[-1] + fibs[-2])
        print(fibs)
