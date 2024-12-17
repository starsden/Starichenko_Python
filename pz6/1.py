def main(A):
    return max(A[i] for i in range(0, len(A), 2))

A = [3, 1, 9, 5, 7, 6, 4]
print(main(A))
