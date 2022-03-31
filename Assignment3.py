
# Assignment
#1.pattern programming using recursion 
#2.remove all string from a list using recurssion
#3.binarry search using recurssion
# 4.update one by one
 # {"1":"surendra","2":"priyanka","3":"rahul","4":"zini"}
#  1.surendra1
# 2.priyanka2

#5.update 
    # {"1":"surendra","2":"priyanka","3":"rahul","4":"zini"}
    # o/p- 1.surendra1
            # 2.




"""
*
**
***
****



"""

# pattern 
# def pattern1(num):
#     if(num==5):
#         return
#     else:
#         print(num*"*")
#         pattern1(num=num+1)    




# def pattern2(num):
#     if(num==0):
#         return
#     else:
#         print(num*"*")
#         pattern2(num=num-1)



# pattern2(5)   

# 2.removing string in list 

# def rmString(l,i):
#     if(i==len(l)):
#         return
#     if(type(l[i])==str):
#         print("removed ",l[i])
#         print(i)
#         l.pop(i)
#         rmString(l,i)
#     else:
#         rmString(l,i+1)    
        
        


# l=["rahhul","priyanka",5,"zini",12,70] 
# rmString(l,0)

# print(l)


# binary search


# def bSearch(l,f,last,num):
#     mid=int((f+last)/2)
#     if(f>last):
#         print("not found")
#         return
#     if(num==l[mid]):
#         print(f"found at index{mid}")
#         return
#     elif(num<l[mid]):
#         bSearch(l,f,mid-1,num)
#     else:
#         bSearch(l,mid+1,last,num)        







# l=[2,3,4,5,8,9,10,20,30]
# bSearch(l,0,len(l)-1,11)


# 4.update one by one 
def dUpdate1(num,d):
    try:
        d[num]=f"{d[num]}{num}"
        print(f"{num} {d[num]}")
        dUpdate1(num+1,d)
    except Exception  as e:
        return






# 5.update dict 


# def dUpdate(num,d):
#     try:
#         d[num]=f"{d[num]}{num}"
#         print(d)
#         dUpdate(num+1,d)
#     except Exception  as e:
#         return





d={1:"surendra",2:"priyanka",3:"zini",4:"rahul",5:"naman"}
dUpdate1(1,d)


