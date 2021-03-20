# Returns index of list to take from
def get_max_head(list_of_lists):
    [x.append(-1000) for x in list_of_lists if not x]
    heads = [x[0] for x in list_of_lists]
    m = max(heads)
    return [i for i, j in enumerate(heads) if j == m]

tests = int(input())

def solve(test):
    line = list(map(lambda x: int(x), input().split()))
    n = line[0] # number of stacks
    k = line[1] # number of plates per stack
    p = line[2] # number of plates needed

    stacks = []
    for i in range(n):
        stack = list(map(lambda x: int(x), input().split()))
        stacks.append(stack)

    total = 0

    for i in range(p):
        candidates = get_max_head(stacks)
        idx = candidates[0]
        total += stacks[idx][0] # take head of list
        stacks[idx].pop(0)

    print("Case #" + str(test+1) + ": " + str(total))

for i in range(tests):
    solve(i)