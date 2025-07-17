def findelement (arr,key,start,end):
    if start<=end:
        mid=(start+end)//2
        if (key==arr[mid]):
            print("found")
        elif key<arr[mid]:
            findelement(arr,key,start,mid-1)
        else:
            findelement(arr,key,mid+1,end)

if __name__ =='__main__':
    arr=list(map(int, input("enter numbers by space : ").split()))
    print(arr)
    key=int(input("key: "))
    n=len(arr)
    findelement(arr,key,0,n-1)
