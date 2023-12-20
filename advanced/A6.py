#Create the custom python classes which has methods and attributes and implement
#single inheritance, multiple inheritance and multilevel inheritance

# Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent: {self.name}")

class Child(Parent):
    def __init__(self, name, child_name):
        super().__init__(name)
        self.child_name = child_name

    def display_child(self):
        print(f"Child: {self.child_name}")

# Multiple Inheritance
class FirstParent:
    def method_one(self):
        print("Method One from FirstParent")

class SecondParent:
    def method_two(self):
        print("Method Two from SecondParent")

class MultipleChild(FirstParent, SecondParent):
    def combined_method(self):
        print("Combined Method from MultipleChild")

# Multilevel Inheritance
class Grandparent:
    def grandparent_method(self):
        print("Grandparent Method")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent Method")

class ChildWithGrandparent(Parent):
    def child_method(self):
        print("Child Method")


# Single Inheritance
child_instance = Child("ParentName", "ChildName")
child_instance.display()        
child_instance.display_child()  

# Multiple Inheritance
multiple_child_instance = MultipleChild()
multiple_child_instance.method_one()        
multiple_child_instance.method_two()        
multiple_child_instance.combined_method()   

# Multilevel Inheritance
child_with_grandparent_instance = ChildWithGrandparent()
child_with_grandparent_instance.grandparent_method()   
child_with_grandparent_instance.parent_method()         
child_with_grandparent_instance.child_method()          
