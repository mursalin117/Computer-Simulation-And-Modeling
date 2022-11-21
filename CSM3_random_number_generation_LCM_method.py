def main():
    x0 = 1
    a = 1103515245
    c = 4312345
    m = 2**32
    N = 50000

    nums = random_number(x0, a, c, m, N)

    print("Random Numbers: ")
    print(nums)
    print('\n')
    dup = {x for x in nums if nums.count(x) > 1}
    print(dup)
    print(len(dup))

def random_number(x0, a, c, m, N):
    nums = [x0]
    for i in range(N):
        x_temp = (a * nums[-1] + c) % m
        nums.append(x_temp)
    
    return nums

if __name__ == '__main__':
    main()