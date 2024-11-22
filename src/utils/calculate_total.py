def calculate_total(prices: list):
    if len(prices) == 0:
        return 0
    return prices[0] + calculate_total(prices[1:])
