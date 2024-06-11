class A:
    def __init__(self):
        print("Inside  A")
    
    def fun(self):
        print("Inside Fun A")

class B():
    def __init__(self):
        print("Inside  B")
    
    def fun(self):
        print("Inside Fun B")

class C(A, B):
    def __init__(self):
        print("Inside  C")
    
    def fun(self, a):
        print("Inside Fun C",a)
    
    def fun(self, a, b):
        print("Inside Fun C",a, b)

obj = C()


obj.fun("a")