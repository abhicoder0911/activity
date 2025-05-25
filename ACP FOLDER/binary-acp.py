def binary(n):
    if n>1:
        binary(n//2)
    print(int(n%2), end=" ")
dec=float(input("enter a number: "))
binary(dec)
print()