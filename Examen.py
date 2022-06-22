print('Dame un numero')
A=int(input())
print('Dame un numero')
B=int(input())
if A>B:
    j=True
    A=1
    while j:
        A=A+B
        print(A)
    n=False
if A<B:
    j=True
    B=1
    while j:
        B=A*B
        print(B)
    n=False