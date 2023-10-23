def matching_window(l1, l2):
    # Determine the size of the window
    window_size = len(l2) + 1

    # Initialize an empty array to store matching windows
    matching_window = []
    matched_window_indices = []

    # Loops thrice while reducing window size from right because :
    #       (1) either the frame is updated ( no change in size of window and l2 )
    #       (2) or a block is added at the end ( which means matching window has lesser size )
    #       (3) or if else block is added at the end ( if else block has 2 elements inserted at a time )
    for i in range(0, 3):
        if len(matching_window) == 0:
            window_size -= 1
            # searching for matching windows while reducing both the window size and input size
            # detects elements inserted at the end
            for i in range(len(l1) - window_size + 1):
                window = l1[i: i + window_size]
                # Check whether the first and last elements of the window match l2
                if len(window) > 0 and window[0] == l2[0] and window[-1] == l2[window_size - 1]:
                    # If they match, append the elements inside the window to the matching_window array
                    if len(l1[i: window_size]) < len(l2):
                        matching_window = l1[i: i + window_size + 1]
                        matched_window_indices = [i, i + window_size + 1]
                    else:
                        matching_window = window
                        matched_window_indices = [i, i + window_size]

            # searching for matching windows while keeping the input size constant
            # detects elements inserted in between
            for i in range(len(l1) - window_size + 1):
                window = l1[i: i + window_size]
                # Check whether the first and last elements of the window match l2
                if len(window) > 0 and window[0] == l2[0] and window[-1] == l2[-1]:
                    # If they match, append the elements inside the window to the matching_window array
                    if len(l1[i: window_size]) < len(l2):
                        matching_window = l1[i: i + window_size]
                        matched_window_indices = [i, i + window_size]
                    else:
                        matching_window = window
                        matched_window_indices = [i, i + window_size]
    # Loops twice while reducing window size from left because :
    #       (1) either a block is added at the beginning ( which means matching window has lesser size )
    #       (2) or an if else block is added at the beginning ( if else block has 2 elements inserted at a time )
    # TODO : It is enough to loop twice since check for the exact window has been done earlier in the previous loop
    window_size = len(l2) + 1
    for i in range(0, 3):
        if len(matching_window) == 0:
            window_size -= 1
            # searching for matching windows while reducing both the window size and input size ( input window is taken by ignoring item from the left each iteration )
            # detects elements inserted at the beginning
            for i in range(len(l1) - window_size + 1):
                window = l1[i: i + window_size]
                # Check whether the first and last elements of the window match l2
                if len(window) > 0 and window[0] == l2[len(l2) - window_size] and window[-1] == l2[-1]:
                    # If they match, append the elements inside the window to the matching_window array
                    if len(l1[i: window_size]) < len(l2):
                        matching_window = l1[i - 1 if i - 1 >= 0 else i: i + window_size]
                        matched_window_indices = [i - 1 if i - 1 >= 0 else i, i + window_size]
                    else:
                        matching_window = window
                        matched_window_indices = [i, i + window_size]
    if len(matching_window) == 0:
        matching_window = l1
        matched_window_indices = [0, len(l1)]

    return matching_window, matched_window_indices