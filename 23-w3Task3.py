import turtle as tt 

def make_square(length):
    #drawing a quare with sides of length pixels 
    for i in range(4):
        
        tt.delay(100)
    
        tt.forward(length)
    
        tt.left(90)


make_square(100)
make_square(150)