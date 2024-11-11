# Press the green button in the gutter to run the script.

def get_avg(my_list: list[float]) -> float:
    sum_of_list = 0
    for num in my_list:
        sum_of_list += num
    avg = sum_of_list / len(my_list)
    return avg

def get_sum_std(my_list, avg):
    std = []
    sum_std = 0
    for num in my_list:
        temp = abs(avg - num)
        std.append(temp)
        sum_std += temp
    return sum_std

def get_mad(my_list):
    avg = get_avg(my_list)
    sum_std = get_sum_std(my_list, avg)
    mad_of_list = sum_std / len(my_list)
    return mad_of_list


# def mad_function(numbers: list) -> float:

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers)
    print(f'len: {len(numbers)}')
    print(f'sum: {sum(numbers)}')
    print(f'avg: {get_avg(numbers)}')
    print(f'sum_std: {get_sum_std(numbers, get_avg(numbers))}')
    print(f'mad: {get_mad(numbers)}')

