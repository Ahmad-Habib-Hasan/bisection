
def my_function(x):
    func = pow(x , 2)-2
    return func



a = 1 
b = 2
c  = 0 ;

if(my_function(a)< 0 and my_function(b)> 0)or (my_function(a)> 0 and my_function(b)< 0):
    for i in range(0 , 25):
        c = (a+b)/2 
        function_a = my_function(a)
        function_b = my_function(b)
        function_c = my_function(c)
        
        print("a:"+str(a))
        print("b:"+str(b))
        print("c:"+str(c))
        print("----------")
        if(function_c < 0 and function_a < 0)or (function_a>0 and function_c>0):
            a = c
        else:
            b = c
