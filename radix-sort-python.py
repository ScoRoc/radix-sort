
def radix_sort(arr):
    # if List is empty or 1 number
    if len(arr) == 0 or len(arr) == 1:
        return arr

    # define number of buckets
    bucket_count = 10
    buckets = [[] for __ in range(bucket_count)]

    # function to get max number of digits in a number
    max_digits = 0
    def get_max_digits(num):
        nonlocal max_digits
        num_count = num
        counter = 0
        while num_count > 0:
            digit = num_count % 10
            num_count = (num_count - digit) / 10
            counter += 1
            if (counter > max_digits):
                max_digits = counter
    
    # get max number of digits in the list
    for n in arr:
        get_max_digits(n)

    ##################################
    #  Finding max_digits as string  #
    ##################################
    # converting each number in list to a string
    # and finding length of string(number) to find max_digits
    # max_digits = 0
    # for n in arr:
    #     if (len(str(n)) > max_digits):
    #         max_digits = len(str(n))
    ##################################

    # new sorted list
    sorted_arr = arr

    # determines which digit to sort by
    which_digit = 1

    # loops thru for each digit through max_digits
    for d in range(max_digits):
        # loops thru each num in arr
        for n in sorted_arr:
            # adds num at current digit to appropriate bucket
            buckets[(n // which_digit) % 10].append(n)
        print('~~~~Buckets at', d + 1, 'digit:', buckets)
        print('')
        # increments to next digit
        which_digit *= 10
        # clears sorted_arr so it receives a clean push
        sorted_arr = []
        # pushes sorted order for current digit into sorted_arr
        for b in range(len(buckets)):
            sorted_arr += buckets[b]
            # clears buckets for next sort
            buckets[b] = []

    print('Final Sorted List:')
    print('----------------')
    print(sorted_arr)

my_arr = [74, 2545, 21, 306, 42, 879, 33, 562, 4078, 93, 1395, 461, 50, 747, 124, 8359, 84, 6487, 246, 648, 2070 ]

radix_sort(my_arr)
