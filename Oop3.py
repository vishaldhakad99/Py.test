class Father:
    def property(self):
        print("Father Property")

    def business(self):
        print("Father Business")


class Son(Father):
    def study(self):
        print("Son Studies")


class Daughter(Father):
    def dance(self):
        print("Daughter Dances")


class GrandChild(Son, Daughter):
    def gaming(self):
        print("GrandChild Gaming")


g = GrandChild()

g.property()
g.business()
g.study()
g.dance()
g.gaming()