class elementpair:

    def twosum(self,nums,target):
        lookup={}

        for i,num in enumerate(nums):
            if target-num in lookup:
                return(lookup[target-num],i)
            lookup[num]=i

value=int(input("Enter the sum for which you want to make this search: "))
nums=[10,20,30,40,50,60,70,80,90]

ans=elementpair().twosum(nums,value)

if ans:
    print("index1=%d,index2=%d" %(ans[0], ans[1]))
else:
    print("No pairs")

