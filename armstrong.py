def armstrong(n):
    d=0
    a=0
    for i in n:
        d+=1
    for i in n:
        a+=int(i)**d
    if a==int(n):
        print("Armstrong number!")
    else:
        print("Not an armstrong number.")
def main():
    n=input("Enter number: ")
    armstrong(n)
main()