import math
class Solution:
    def micsandjury (self, N, M, teams):
        #using binary search
        low=1
        high=max(teams)
        ans=high
        while(low<=high):
            mid=(low+high)//2                  #I HAVE DONE THIS AFTER LEARNING FROM YOUR APPROACH SIR
            parts=0
            for i in teams:
                parts+=math.ceil(i/mid)
            if(parts<=N):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        N = int(str[0])
        M = int(str[1])
        teams = input().split()
        for itr in range(M):
            teams[itr] = int(teams[itr])

        ob = Solution()
        print(ob.micsandjury(N,M,teams))
# } Driver Code Ends
© 2021 GitHub, Inc.
