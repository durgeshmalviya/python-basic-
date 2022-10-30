class myclass:
      def __init__(self,z):
        self.name=z
    
      def myfnc(self):
        print(f"hello my name is {self.name}")

class child(myclass):
    def __init__(self,a):
     self.city=a
     myclass.__init__(self,a) 
    def myfnc1(self):
              print(f"I am from {self.city}" )
  
        
obj=myclass("durgesh") 
obj.myfnc()
obj1=child( " BPL ")
obj1.myfnc1()




