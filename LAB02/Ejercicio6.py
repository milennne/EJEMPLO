def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4]))
print(sum_list([5, 10, 15]))
print(sum_list([]))
