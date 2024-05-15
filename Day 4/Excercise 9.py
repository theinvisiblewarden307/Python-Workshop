#Excercise: mysum with a default 

def mysum(nums, offset=0):

    '''This function helps find the sum of integers in a list similarly to one of built in function sum'''

    total = offset

    for i in nums:
        total+=i

    return total

x = mysum([100, 200, 300])
print(x)