def main():
    m = int(input("m: "))
    energy(m)

def energy(m):
    c = int(300000000)
    e = m*c**2
    print(e)

main()
