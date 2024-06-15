def sum(nums):
    """
    array = [1,2,3,4]
    sum = 10


    """
    sum = 0

    for num in nums:
        sum += num
    return sum 


if __name__ == '__main__':
    n = [1,2,3,4]
    rst = sum(n)
    print(rst)
    
