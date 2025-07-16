def findelement ():
    arr=list(map(int, input("enter numbers by space : ").split()))
    print(arr)
    key=int(input("key: "))
    n=len(arr)
    for i in range(n):
        if key==arr[i]:
            print(f"{key} is key")

if __name__ =='__main__':
    findelement()
