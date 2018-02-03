
# coding: utf-8

def iterative_bin_search(lists,target):
    
    max_index = len(lists)-1
    min_index = 0
    found = False
    
    while min_index <= max_index and not found:
        mid_index = (max_index + min_index) // 2
        if target == lists[mid_index]:
            print(target,' is found in the list!')
            found = True
            break
        else:
                if target > lists[mid_index]:
                    min_index = mid_index+1
                else:
                    max_index = mid_index-1
                    
    if found == False:
        print(target,' is not found in the list!')

