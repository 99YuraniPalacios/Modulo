import numpy
import os

class Series(object):

    def __init__(self,Max,a):
        self.Max=Max
        self.a=a
        n=len(a)
        
    def get_value(self,x):
        suma=0
        for n in range(self.Max):
            suma+=self.a[n]*x**n
        return suma

    def Get_derivative(self,x):
        deriv=0
        for n in range(1,self.Max):
            deriv+=n*self.a[n]*x**(n-1)
        return deriv

    def GetError(self,x,n):
        if n<0:
            raise ValueError("n should be larger than 0")
        elif n>self.Max-1:
            raise ValueError("n should not be larger than {self.N}")
        else:
            error=x**(n+1)
            return error

    def Clean(self):
        #This funtion is only for seeing is system works
        os.system("ls 2> /dev/null")
        return 0
        
if __name__=="__main__":
    s=Series(3,[1,1/2,1/6])
    print(s.Get_derivative(1))
