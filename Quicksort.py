global stuff

def printer(stuffs):
    print("Array: ")
    j = 0
    for i in stuffs:
        print(i)
    while(j < len(stuffs)):
        print(stuffs[j])
        j = j + 1


def partition(p, r):
    global stuff
    pivot = stuff[r]

    while p < r:
        while stuff[p] < pivot:
            p = p + 1

        while stuff[r] > pivot:
            r = r - 1

        if stuff[p] == stuff[r]:
            p = p + 1
        elif p < r:
            temp = stuff[p]
            stuff[p] = stuff[r]
            stuff[r] = temp


    return r

def quicksort(p, r):
    global stuff
    if p < r:
        j = partition(p, r)
        quicksort(p, j-1)
        quicksort(j+1, r)


stuff = [500, 700, 800, 100, 300, 200, 900, 400, 1000, 600]
quicksort(0, 9)
printer(stuff)
