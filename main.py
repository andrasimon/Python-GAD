if __name__ == '__main__':
    my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
    asc_sorted_list = my_list.copy()
    asc_sorted_list.sort()
    print('Ascending sorted list:', asc_sorted_list)
    desc_sorted_list = my_list.copy()
    desc_sorted_list.sort(reverse=True)
    print('Descending sorted list:', desc_sorted_list)
    print('Even numbers in my_list:', asc_sorted_list[1::2])
    print('Odd numbers in my_list:', asc_sorted_list[::2])
    print('Multiples of 3 in my_list:', asc_sorted_list[2::3])
