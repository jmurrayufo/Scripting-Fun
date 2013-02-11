

class Foo:
   def __init__(self,a,b,c):
      self.a=a
      self.b=b
      self.c=c
   def __str__(self):
      return "%d,%d,%d"%(self.a,self.b,self.c)
   def __repr__(self):
      return "%d,%d,%d"%(self.a,self.b,self.c)

x = list()

x.append(Foo(1,2,3))
x.append(Foo(2,5,8))
x.append(Foo(3,6,9))
x.append(Foo(4,7,10))

for i in x:
   if i.a==1:
      print i