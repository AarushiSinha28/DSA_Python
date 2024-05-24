def binary_search(alist, key): 
    if len(alist) > 0:
        mid = len(alist) // 2

        if alist[mid] ==key:
            return True

        if key < alist[mid]:
            return binary_search(alist[:mid], key)

        if key > alist[mid]:
            return binary_search(alist[mid + 1:], key)

    else:
        return False 
    
print(binary_search([10, 20, 30, 40], 20))
print(binary_search([20,61,85,73,94,29],10))
print(binary_search([10,26,91,34,76,55,8,23,64],3))
print(binary_search([10,20,82,73,90],5))
