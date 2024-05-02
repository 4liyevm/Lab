def ardici_seriyani_hesabla(a, n):
    sonuc = []
    carpim = 1
    for i in range(1, n+1):
        carpim *= a
        if i % 2 == 0:
            carpim *= -1
        sonuc.append(carpim)
    return sonuc

# Nümunə
a = 2
n = 5
print(ardici_seriyani_hesabla(a, n))