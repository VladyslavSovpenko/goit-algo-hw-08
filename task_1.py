import heapq


def minimum_cable_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined_length = first + second
        total_cost += combined_length

        heapq.heappush(cables, combined_length)

    return total_cost


cables = [8, 4, 6, 12]
result = minimum_cable_cost(cables)
print(f"Мінімальні загальні витрати: {result}")
