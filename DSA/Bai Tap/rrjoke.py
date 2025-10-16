def distance(d1, d2):
    return min(abs(d1[0] - d2[0]), abs(d1[1] - d2[1]))

def total_path_cost(order, points):
    cost = 0
    for i in range(len(order) - 1):
        cost += distance(points[order[i]], points[order[i + 1]])
    return cost


def solve():
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        points = [tuple(map(int, input().split())) for _ in range(n)]
        arr = []
        arr.append(sorted(range(n), key=lambda i: (points[i][0], points[i][1])))
        arr.append(sorted(range(n), key=lambda i: (points[i][1], points[i][0])))
        arr.append(sorted(range(n), key=lambda i: (points[i][0] + points[i][1], points[i][0])))
        arr.append(sorted(range(n), key=lambda i: (points[i][0] - points[i][1], points[i][1])))
        max_cost = float("inf")
        best_cost = None
        for i in arr:
            cost = total_path_cost(i, points)
            if cost < max_cost or (cost == max_cost and i < best_cost):
                max_cost = cost
                best_cost = i
        results = 0
        for i in best_cost:
            results ^= i+1
        print(results)
    pass

if __name__ == "__main__":
    solve()
