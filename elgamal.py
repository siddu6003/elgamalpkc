" " " function to generate key " " "

"""generates the group <zp*,x>"""
def gen(g, p):
    E = []
    """creating an empty set"""
    my_set = set(E)
    for x in range(1, p):
        """num=g^x mod p"""
        num = pow(g, x, p)
        my_set.add(num)
    return len(my_set)


" " "Inverse mod calculator " " "


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x


print("receiver side key generation")
print(" ")

p = int(input("Select a large prime number: "))

if len(bin(p)) < 129:
    for x in range(1, p):
        if gen(x, p) == (p - 1):
            E1 = x
            break
print("e1(Generator): ", E1)
while (1):
    d = int(input("Enter a private key: "))
    if d <= (p - 2) and d >= 1:
        break

E2 = pow(E1, d, p)
print("public key: (", E1, ",", E2, ",", p, ")")
print("private key(d): ", d)
print(" ")
# Encryption

print("sender side i.e Alice")
print(" ")
while (1):
    r = int(input("Select a random number(1<r<(p-2))"))
    if r <= (p - 2) and r >= 1:
        break

while (1):
    msg = int(input("Enter your msg(1<msg<(p-2)): "))
    if msg >= 1 and msg <= (p - 2):
        break

C1 = pow(E1, r, p)
C2 = pow((pow(E2, r) * msg), 1, p)

# Decrypt
de_msg = pow((modInverse(pow(C1, d), p) * C2), 1, p)

print("Encrypt msg: ", C1, C2)
print(" ")
print("receiver side decryption")
print(" ")
print(de_msg)
