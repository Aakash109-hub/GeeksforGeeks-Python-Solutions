
class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
        
        if n == 1:
            return 0
            
        if arr[0] > arr[1]:
            return 0
        
        if arr[n-1] > arr[n-2]:
            return n-1
            
        l, h = 1, n-2
        
        while l <= h:
            m = l +(h - l)//2
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            
            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                h = m -1
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
