def reversearray(data):
    """
    
    data = "hello world
    results = "dlrow olleh"

    think swap of location
    so define the start index and end index

    """

    data = list(data)

    # start index
    start_index = 0

    # define last index
    end_index = len(data) - 1

    # iterate the swap
    while start_index < end_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1
    
    return ''.join(data)


if __name__ == '__main__':
    n = "hello World"
    rst = reversearray(n)
    print(rst)


