# class Welcome: 
#     def __init__(self,name= "Welcome to"):
#         self.a = name    

#     def sy_hello(self,n):
#         print(self.a + n)

# cw = Welcome()
# cw.sy_hello('Kayu')
#=======================================================================================    
# t = '%(a)s %(b)s %(c)s'
# print(t % dict(a='Welcome', b= 'to', c = 'kayu'))
#=======================================================================================    
# x = "abcdef"
# i = "a"
# while i in x[:-1]:
#     print (i, end = " ")
#=======================================================================================    
# print([i.lower() for i in "TURING"])
#=======================================================================================    
# print ("WELCOME TO KAYU".capitalize())
#=======================================================================================    
# data = [1,2,3,4,5]
# data.pop()
# print (data)
# data.pop(2)
# print (data)
#=======================================================================================    
#'The {} Side {} {}'.format('bright','side','life')
#=======================================================================================    
# Print the multiplication tables for first 10 multiples

# n = int(input().strip())
    
# for i in range(1,11):
#     print ("{} x {} = {}".format(n,i,n*i))
#=======================================================================================    

# import sys


# def main():  
#     #inp = sys.stdin.readline() 
#     # print (inp)
#     N = int(sys.stdin.readline() )
#     P = int(sys.stdin.readline() )
#     day = []
#     for i in range(50):
#         for j in range(1, N+1):
#             if (i == 0):
#                 if (P == 5000*j):
#                     print (j)
#                     day[0] = 5000 * j
#                     print (day[0])
#             else:
#                 day[i] = day[i-1] + 5000 + i
#                 print (day[i])
#                 if (day[i] == P):
#                     print (j)
             
#     # for i in range(1,t):
#     #     s = list(inp[i].strip())

#     # for j in range(t-1):
#     #     print (s[j])



# # To create a empty dictionary
# dict1 = {}
# print ("Empty dictionary looks like: ", dict1)

# # Dictionary created with dict()
# dict2 = dict({1:'This', 'two':'is', 3:'sample'})
# print (dict2)

# # New element added to existing dictionary
# dict2[4] = 'new'
# print (dict2)

from collections import defaultdict
dict_list = defaultdict(list)
list1 = [(3,3),(3,33),(1,11),(2,2)]

for key, val in list1:
    dict_list[key].append(val)

dict_list[1].append(111)
dict_list[2].append(2)
dict_list[1].append(1)

print(dict_list)

for i in dict_list:
    print ("Maximum value of key %d is %d " % (i, max(dict_list[i])))

print("Maximum of all keys: ", max(dict_list))

print(dict_list)
dict_list[1].remove(11)     # This removes the mentioned value from the key
print("After [1:11] removal: ")
print(dict_list)

dict_list[3].clear()        # This removes all the values of the key
print("After clearing entire 3 key's values: ")
print(dict_list)

# pop() is same as remove but we need to give the index of the value to be removed and a receiver to get the value
item = dict_list[2].pop(0)  
print ("Removed item is: ", item)
print(dict_list)

# del is used to remove the entire key-value pair
del dict_list[3]
print("After deleting the entire key 3")
print(dict_list)
    # print (max(data_dict[1]))

# if __name__ == '__main__':
#     main()


                        
    
    