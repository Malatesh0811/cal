

from collections import deque

def bfs(start, connections, values, d):
    """Return total value reachable from start within depth d."""
    visited = set([start])
    q = deque([(start, 0)])
    total_value = values[start]

    while q:
        u, depth = q.popleft()
        if depth == d:
            continue
        for v in connections.get(u, []):
            if v not in visited:
                visited.add(v)
                total_value += values[v]
                q.append((v, depth + 1))
    return total_value

def solve_campaign(connections, costs, values, budget, d):
    selected = []
    total_cost = 0
    total_value = 0

    while True:
        best = None
        best_eff = 0

        for user, cost in costs.items():
            if user in selected or cost + total_cost > budget:
                continue
            gain = bfs(user, connections, values, d)
            eff = gain / cost
            if eff > best_eff:
                best_eff = eff
                best = (user, gain, cost)

        if not best:
            break

        user, gain, cost = best
        selected.append(user)
        total_cost += cost
        total_value += gain

    return selected, total_value, total_cost

def main():
    # Example Input
    connections = {1:[2], 2:[1,3], 3:[2,4], 4:[3,5], 5:[4]}
    costs = {1:50, 2:20, 3:20, 4:60, 5:20}
    values = {1:10, 2:20, 3:30, 4:5, 5:5}
    budget = 100
    depth = 1

    seeds, val, cost = solve_campaign(connections, costs, values, budget, depth)
    print("Chosen Seeds:", seeds)
    print("Total Value:", val)
    print("Total Cost:", cost)

if __name__ == "_main_":
    main()