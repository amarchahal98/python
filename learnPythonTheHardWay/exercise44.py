class Parent(object):
    def override(self):
        print("PARENT IMPLICIT()")

class Child(Parent):
    def override(self):
        print("CHILD OVERRIDE()")

dad = Parent()
son = Child()

dad.override()
son.override()

