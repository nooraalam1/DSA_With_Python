def bubble_sort(l):
    for i in range(len(l)):
        swap = False
        for j in range(len(l) - 1 - i):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                swap = True
        if swap == False:
            break
    return l

l = [40,10,0,5,3,6]
bubble_sort(l)
print(l)