def customers_without_computer(N, S):
    occupied = set()
    walked_away = 0
    for customer in S:
        if customer not in occupied:
            occupied.add(customer)
        else:
           
            occupied.remove(customer)

    
    walked_away = N - len(occupied)

    return walked_away

# Example 1
N1 = 3
S1 = "GACCBDDBAGEE"
output1 = customers_without_computer(N1, S1)
print("Example 1 Output:", output1)  # Output: 1


