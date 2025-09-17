def rank_array(arr):
    highest = 0
    rank = 1
    max_index = 0
    tmp_arr = arr.copy()
    count = 0
   
    while count < len(arr):
        
        highest = max(arr)
        max_index = arr.index(highest)
        tmp_arr[max_index] = rank
        arr[max_index] = -9999

        if max(arr) != highest:
            rank += 1

        count += 1
    return tmp_arr


ex_arr = [8, 5, 5, 6, 10]
print(rank_array(ex_arr))