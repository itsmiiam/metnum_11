'''
MIA AMALIA (2200319)
METODE BAGI DUA
no. 1
b. f(x) = e^x - x
'''
#Metode Bagi Dua
import numpy as np

# Fungsi untuk mencari akar dengan metode biseksi
def my_bisection(func, a, b, tol=1e-6, max_iterations=100):
    iterations = 0
    while iterations < max_iterations:
        c = (a + b) / 2
        # Memeriksa apakah akar ditemukan atau toleransi terpenuhi
        if func(c) == 0 or (b - a) / 2 < tol:
            return c
        # Memeriksa tanda fungsi untuk menentukan interval berikutnya
        if np.sign(func(c)) == np.sign(func(a)):
            a = c
        else:
            b = c
        iterations += 1
    return None

# Fungsi yang akan dicari akarnya: f(x) = e^x - x
f = lambda x: np.exp(x) - x

# Mencari akar dengan toleransi 0.1
r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

# Mencari akar dengan toleransi 0.01
r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))
