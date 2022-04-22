#Day 6.
#923. 3Sum With Multiplicity

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        res = 0
        arr.sort()
        
        for i,val in enumerate(arr):
            T = target-arr[i]
            j,k = i+1, len(arr)-1
            
            while(j < k):
                #print(arr[j],arr[k],T)
                if arr[j] + arr[k] < T:
                    #print("LOW")
                    j+=1
                elif arr[j] + arr[k] > T:
                    #print("HIGH")
                    k-=1
                elif arr[j] != arr[k]:
                    #print("enter")
                    left = right = 1
                    while j+1 < k and arr[j] == arr[j+1]:
                        left+=1
                        j+=1
                    while k-1 > j and arr[k] == arr[k-1]:
                        right+=1
                        k-=1 
                    res += left * right
                    #print(res)
                    res %= MOD
                    j+=1
                    k-=1
                else:
                    res += ((k-j+1) * (k-j)) / 2
                    #print(res)
                    res %= MOD
                    break
        return int(res)
