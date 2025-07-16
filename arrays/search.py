def findelement (arr,key,n):
    for i in range(n):
        if key==arr[i]:
            print(f"{key} is key")

if __name__ =='__main__':
    arr=[10,12,30]
    n=len(arr)
    findelement(arr,12,n)
