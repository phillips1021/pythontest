def split_amount(amount, n):
    """
    return a list of numbers with length n that sum to amount
    :param amount: number that list of numbers must sum to
    :param n: length of list of numbers
    :return: list of numbers whose sum is amount
    """
    portion, remain = amount // n, amount % n

    portions = []

    for i in range(n):
        portions.append(portion)

        if remain > 0: # was remain > 1
            portions[-1] += 1
            remain -= 1

    return portions

