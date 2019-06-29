for _ in range(int(input())):
    elephants,candies = map(int,input().split())
    a = [int(a) for a in input().split()]
    summ = sum(a)
    if summ < candies:
        print('Yes')
    else:
        print('No')
