from lib.matching_window import matching_window

# Define your lists l1 and l2
main_arr = []
inp_arr = [[1], [1, 2], [1, 2, 3, 4], [3, 4, 5], [4, 5, 6, 7], [0, 1, 2, 3], [3, 4, 5, 8, 6, 7], [5, 9, 6, 7], [5, 9, 6, 7, 0, 0], [3,8,5,9,6]]

for inp in inp_arr:
    window, indices = matching_window(main_arr, inp)
    main_arr = main_arr[:indices[0]] + inp + main_arr[indices[1]:]


print(inp_arr)
print(main_arr)