#!/usr/bin/env python3


class T:
	def __init__(self, x):
		self.x = x
		
class C(T):
	def __init__(self,x,t):
		super().__init__(x)
		self.t = t
c = C(12, 3)
print(c.x)
# class T:
    # def __init__(self, x):
        # self.x = x

    # def _x(self):
        # return "hello world from python programming!!!!"


# def main():
    # """Main function to demonstrate the T class."""
    # t = T(1)
    # print(t._x())
    # return "Helloo"


# if __name__ == "__main__":
    # main()
    
