def poly_naif(coeffs, x):
    res = 0
    for i in range(len(coeffs)):
        res += coeffs[i] * (x ** i)
    return res

def poly_horner(coeffs, x):
    res = coeffs[-1]
    for i in range(len(coeffs) - 2, -1, -1):
        res = res * x + coeffs[i]
    return res

coeffs = [1, -3, 2]
x = 5

print("Méthode naïve : ", poly_naif(coeffs, x))
print("Méthode Horner : ", poly_horner(coeffs, x))
