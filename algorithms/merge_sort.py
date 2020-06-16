def merge_arrays(arr_1, arr_2):
    arr = []
    idx_1 = idx_2 = 0
    while idx_1 < len(arr_1) and idx_2 < len(arr_2):
        if arr_1[idx_1] < arr_2[idx_2]:
            arr.append(arr_1[idx_1])
            idx_1 += 1
        else:
            arr.append(arr_2[idx_2])
            idx_2 += 1
    arr += arr_1[idx_1:]
    arr += arr_2[idx_2:] 
    
    return arr


def merge_sort(arr):
    """TIme complexity: O(nlog(n)), auxiliary space complexity: O(n)"""
   
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge_arrays(left, right)
    return arr


def merge_sort_2(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort_2(left) 
        right = merge_sort_2(right) 
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0) 
            else: 
                values.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
                  
    return values 

if __name__ == "__main__":
    print(merge_sort([1, 5, 2, 6, 2, 3, 2, 9, 1]))
    print(merge_sort_2([1, 5, 2, 6, 2, 3, 2, 9, 1]))
    print(merge_arrays([1], [1, 2]))
