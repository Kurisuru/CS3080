def myroot(x, root=2):

    y = x**(1/root)
    
    return y

value = int(input("Enter a number: "))
            
print ("Value of root is %f is %f" % (value, myroot(value, 3)))
            
print ("Value of root is %f is %f" % (value, myroot (value)))