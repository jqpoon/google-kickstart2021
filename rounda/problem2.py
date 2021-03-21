tests = int(input())

def get_segments_row(row, c, idx):
    segments = set()
    start = -1
    end = -1
    for i in range(c):
        # skip 0s
        if not row[i]:
            if (start != -1 and end != -1 and start != end):
                segments.add(((idx, start), (idx, end), end - start + 1))
            start = -1
            end = -1
            continue
        
        # start of segment
        if (start == -1):
            start = i
            end = i
            continue
        
        end += 1

    if (start != -1 and end != -1 and start != end):
        segments.add(((idx, start), (idx, end), end - start + 1))

    return segments

def get_segments_col(col, r, idx):
    segments = set()
    start = -1
    end = -1
    for i in range(r):
        # skip 0s
        if not col[i]:
            if (start != -1 and end != -1 and start != end):
                segments.add(((start, idx), (end, idx), end - start + 1))
            start = -1
            end = -1
            continue
        
        # start of segment
        if (start == -1):
            start = i
            end = i
            continue
        
        end += 1

    if (start != -1 and end != -1 and start != end):
        segments.add(((start, idx), (end, idx), end - start + 1))

    return segments

def augment_row(segment): # input: ((x1,y1), (x2,y2), len, expanded)
    new_segments = set()
    start = segment[0]
    end = segment[1]
    length = segment[2]

    y1 = start[0]
    x1 = start[1]
    y2 = end[0]
    x2 = end[1]
    assert(y1 == y2)

    new_segments.add((start, (y1, x1 + 1), 2))
    new_segments.add(((y1, x2 - 1), end, 2))

    if (length > 3):
        left_remainder = (start, (y1, x2 - 1), length - 1)
        right_remainder = ((y1, x1 + 1), end, length - 1)
        new_segments.add(left_remainder)
        new_segments.add(right_remainder)
        new_segments.update(augment_row(left_remainder))
        new_segments.update(augment_row(right_remainder))

    return new_segments

def augment_col(segment): # input: ((y1,x1), (y2,x2), len, expanded)
    new_segments = set()
    start = segment[0]
    end = segment[1]
    length = segment[2]

    y1 = start[0]
    x1 = start[1]
    y2 = end[0]
    x2 = end[1]
    assert(x1 == x2)

    new_segments.add((start, (y1 + 1, x1), 2))
    new_segments.add(((y2 - 1, x2), end, 2))

    if (length > 3):
        left_remainder = (start, (y2 - 1, x2), length - 1)
        right_remainder = ((y1 + 1, x1), end, length - 1)
        new_segments.add(left_remainder)
        new_segments.add(right_remainder)
        new_segments.update(augment_col(left_remainder))
        new_segments.update(augment_col(right_remainder))

    return new_segments

def solve():
    line = list(map(lambda x: int(x), input().split()))
    r = line[0] # rows
    c = line[1] # columns

    # list of columns
    arr = []
    for i in range(c):
        arr.append([])

    # generate row segments
    row_segments = set()
    for i in range(r):
        row = list(map(lambda x: x == '1', input().split()))
        row_segments.update(get_segments_row(row, c, i))

        for j in range(c):
            arr[j].append(row[j])

    # augment row segments
    temp = set()
    for row in row_segments:
        if row[2] > 2:
            temp.update(augment_row(row))

    row_segments.update(temp)

    # generate col segments
    col_segments = set()
    for i in range(c):
        col_segments.update(get_segments_col(arr[i], r, i))

     # augment col segments
    temp2 = set()
    for col in col_segments:
        if col[2] > 2:
            temp2.update(augment_col(col))

    col_segments.update(temp2)
    
    # calculate Ls
    count = 0
    for hori in row_segments:
        for vert in col_segments:
            if hori[0] == vert[0] or hori[0] == vert[1] or hori[1] == vert[1] or hori[1] == vert[0]:
                if hori[2] == 2 * vert[2] or vert[2] == 2 * hori[2]:
                    count += 1

    return count

for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))