for i in range(int(input())):
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    max_count = max(count.values())
    winner = min(num for num, c in count.items() if c == max_count)
    print(winner)

