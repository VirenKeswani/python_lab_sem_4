#menu driven progam 
#sum of a list
def sum_list(n):
    sum = 0
    for i in range (len(n)):
        sum = sum + int(n[i])
    print("the sum is ",sum)
    #product of all the elements

def prod_list(n):
    prod = 1
    for i in range (len(n)):
        prod = prod * int(n[i])
    print("the product is ",prod)

def evensum(n):
    evensum = 0
    for i in range (0,len(n),2):
        evensum = evensum + int(n[i])
    print("the even sum is ",evensum)

#add elements to the list
def addelement(n):
    n.append(input("enter the element to be added"))
    print(n)
