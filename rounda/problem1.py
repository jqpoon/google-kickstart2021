tests = int(input())

def solve():
    line = list(map(lambda x: int(x), input().split()))
    n = line[0] # string length
    k = line[1] # goodness score we want

    sample = input()

    first, second = "", ""

    if (n % 2 == 1): # n is odd
        first, second = sample[:n//2], sample[n//2 + 1:]
    else:
        first, second = sample[:n//2], sample[n//2:]

    rev = second[::-1]

    score = 0
    for i in range(n//2):
        if rev[i] != first[i]:
            score +=1

    return abs(k - score)


for i in range(tests):
    count = solve()
    print("Case #" + str(i+1) + ": " + str(count))