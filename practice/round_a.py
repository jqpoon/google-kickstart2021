tests = int(input())

for i in range(tests):
    nb = input().split()
    n = int(nb[0])
    b = int(nb[1])

    costs = list(map(lambda x: int(x), input().split()))
    costs.sort(reverse=True)

    count = 0
    while b > 0 and costs:
        cheapest = costs.pop()
        b -= cheapest
        if (b >= 0):
            count += 1
        
    print("Case #" + str(i+1) + ": " + str(count))