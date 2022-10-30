class myclass:
      def __init__(self,z):
        self.name=z
    
      def myfnc(self):
        print(f"hello my name is {self.name}")

myobj=myclass("DS")
myobj.myfnc()

class child:
      def __init__(self,x):            
          self.age=x
      def myfnc(self):
        print(f"my age is {self.age}")
                
obj1=child(23)
obj1.myfnc()

class myclass:
  def __init__(self,z) -> None:
        self.name=z
        
  def myfnce(self):
        print(f"OkE {self.name}")
        
obj2=myclass("RJ")
obj2.myfnce()
