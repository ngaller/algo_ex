Avs = [
        [[1,3], [4,6], [7,8], [10,15]],
        [[4,5], [7,10], [14, 16]],
        ]

def range_intersect(Avs):
    R = []
    for L in Avs:
        L.reverse()

    while True:
        min = None
        # get the element with the smallest top
        for L in Avs:
            # once a list is empty we'll have no more intersection
            if not L:
                return R
            if not min or L[-1][1] < min[-1][1]:
                min = L
        new = min.pop()
        # now reduce it using the bottom of each element in the list
        for L in Avs:
            if min != L and new[0] < L[-1][0]:
                new = [L[-1][0], new[1]]
        if new[1] > new[0]:
            if not R or R[-1][1] < new[0]:
                R.append(new)
            else:
                R[-1][1] = new[1]

print(range_intersect(Avs))
