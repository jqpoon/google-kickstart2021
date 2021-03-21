tests = int(input())

def check_ok(arr, r, c, x, y):
    val = arr[y][x]
    top = True
    bottom = True
    left = True
    right = True

    if y != 0:
        top = val - arr[y-1][x] <= 1
    if x != 0:
        left = val - arr[y][x-1] <= 1
    if x != c - 1:
        right = val - arr[y][x+1] <= 1
    if y != r - 1:
        bottom = val - arr[y+1][x] <= 1

    return top and bottom and left and right

def solve():
    line = list(map(lambda x: int(x), input().split()))
    r = line[0] # rows
    c = line[1] # columns

    arr = []
    for i in range(r):
        row = list(map(lambda x: int(x), input().split()))
        arr.append(row)

    arr_ok = []
    for i in range(r):
        arr_ok.append([])
        for j in range(c):
            arr_ok[i].append([])

    for i in range(r):
        for j in range(c):
            arr_ok[i][j] = check_ok(arr, r, c, j, i)

    count = 0
    is_ok = True
    for i in range(r):
        for j in range(c):
            is_ok = is_ok and arr_ok[i][j]
            if (not is_ok):
                count += 1
    
    # Do some kind of dynamic thing here

    return count

for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))