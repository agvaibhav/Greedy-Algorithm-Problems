class water_connection():
    def __init__(self):
        self.sp=[0]*1000
        self.ep=[0]*1000
        self.dp=[0]*1000

    def dfs(self,ans,w):
        if self.dp[w]<ans:
            ans=self.dp[w]
            
        if self.ep[self.ep[w]]==0:
            return self.ep[w],ans
        
        return self.dfs(ans,self.ep[w])


    def solve(self,n,p,arr):
        
        a=[]
        b=[]
        d=[]
            
        for i in range(p):
            tank=arr[i][0]
            tap=arr[i][1]
            dia=arr[i][2]

            self.ep[tank]=tap
            self.sp[tap]=tank
            self.dp[tank]=dia

        for i in range(n):
            if self.sp[i]==0 and self.ep[i]!=0:
                ans=float('inf')
                w,ans=self.dfs(ans,i)
                
                a.append(i)
                b.append(w)
                d.append(ans)

        print(len(a))
        for i in range(len(a)):
            print(a[i],end=" ")
            print(b[i],end=" ")
            print(d[i])


n=9
p=6
arr=[[7,4,98],[5,9,72],[4,6,10],[2,8,22],[9,7,17],[3,1,66]]
obj=water_connection()
obj.solve(n,p,arr)


        

    
