import turtle as tt 

# tt.penup()
# tt.right(90)
# tt.forward(25)
# tt.right(90)
# tt.forward(25)
# tt.right(180)
# tt.pendown()

def make_square(length):
    #drawing a quare with sides of length pixels 
    for i in range(4):
        
        tt.delay(100)
    
        tt.forward(length)
    
        tt.left(90)

def penMove(size):
    tt.penup()
    tt.right(90)
    tt.forward(size)
    tt.right(90)
    tt.forward(size)
    tt.right(180)
    tt.pendown()
make_square(100)
penMove(25)
make_square(150)
penMove(25)
make_square(200)
penMove(25)
make_square(250)