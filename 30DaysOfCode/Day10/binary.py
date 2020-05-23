if __name__ == '__main__':
    n = int(input())
    max_counter = 0
    one_counter = 0
    while n != 0:
        factor = n // 2
        remainder = n % 2
        n = factor
        if remainder == 1:
            one_counter +=1
            max_counter = max(max_counter, one_counter)
        else:
            one_counter = 0

    print(max_counter)