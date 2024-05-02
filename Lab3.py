def musbet_cemi_olan_setrin_nomresi(A):
    n, m = len(A), len(A[0])
    for i in range(n):
        cem = sum(A[i])
        if cem > 0:
            return i + 1
    return -1  # Əgər belə bir sətr tapılmazsa

# Nümunə
A = [[-1, 2, -3], [4, -5, 6], [-7, 8, 9]]
print(musbet_cemi_olan_setrin_nomresi(A))