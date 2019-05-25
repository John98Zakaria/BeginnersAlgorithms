def binominaleff(n, k, mem=dict()):
    if (k == 0 or n == k):  # Base Case
        mem[(n, k)] = 1
        return 1

    if (n, k) not in mem:  # If the coefficient  isn't in the list
        mem[(n, k)] = binominaleff(n - 1, k - 1, mem) + binominaleff(n - 1, k, mem)  # Add coefficient to the list
        mem[(n, n - k)] = mem[(n, k)]  # add the complementary coefficient to the list n choose k = n choose n-k

    return mem[(n, k)]
