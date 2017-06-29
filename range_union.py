R = []
Avs = [
        [[1,5], [7,8], [10,15]],
        [[4,5], [7,10], [14, 16]]
        ]

for L in Avs:
    L.reverse()

while Avs:
    min = None
    for L in Avs:
        if not min or L[-1][0] < min[-1][0]:
            min = L
    new = min.pop()
    if not R or R[-1][1] < new[0]:
        R.append(new)
    else:
        R[-1][1] = new[1]
    if not min:
        Avs.remove(min)

print(R)
