def main():
    seed = 675248
    N = 100

    nums = random_number(seed, N)
    
    print(nums)
    print('\n')
    dup = {x for x in nums if nums.count(x) > 1}
    print(dup)
    print(len(dup))

def random_number(seed, N):
    nums = [seed]
    for i in range(N):
        num_str = str(nums[-1]**2)
        while len(num_str) != 12:
            num_str = '0' + num_str
        
        num_mid = int(num_str[3:-3])
        nums.append(num_mid)
    
    return nums

if __name__ == '__main__':
    main()