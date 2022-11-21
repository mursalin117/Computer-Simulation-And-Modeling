num_x = []

def main():
    # x = 14
    x = 675248
    n = 100

    num_x.append(x)

    for i in range(n):
        num_new = random_number()

    print(num_x)
    dup = {x for x in num_x if num_x.count(x) > 1}

    print('\n')
    print(dup)
    print(len(dup))

def random_number():
    num = num_x[-1] ** 2
    num_str = str(num).zfill(12)

    middle = int(num_str[3:-3])
    num_x.append(middle)

    return middle    

if __name__ == "__main__":
    main()