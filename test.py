from numpy import *
x1 = -2
x2 = 3
w1 = mat([[1, 4], [2, 5], [3, 6]])
w2 = mat([7, 8, 9])
x = mat([[-2, ], [3, ]])
ydk = 200
epsilon = 0.0005
n = 0
while n < 3:
    yj = w1*x
    yk = w2*yj
    fin = ydk-yk
    fin = array(fin)[0][0]
    Deltawjk1 = array(yj)*epsilon*fin
    Deltawjk2 = Deltawjk1 + array(w2).T
    w2 = array(w2).T * array(x).T
    Deltawij = epsilon*fin*w2
    Deltawij = Deltawij+w1
    w1 = mat(Deltawij)

    w2 = mat(Deltawjk2).T


    n = n+1
    print("This is the", n)
    print("yj=", yj)
    print("w2=", w2)
    print("x=", x)
    print("Deltawjk1=", Deltawjk1)
    print("Deltawjk2=", Deltawjk2)
    print("Deltawij=", Deltawij)
    print("fin=", fin)
    if (n < 3):
        print("The next circle")
    else:
        print("This is end")

