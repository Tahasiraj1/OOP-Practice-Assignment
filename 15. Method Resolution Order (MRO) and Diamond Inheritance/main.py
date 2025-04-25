class A:
    def show(self):
        print("Show A")

class B(A):
    def show(self):
        print("Show B")

class C(A):
    def show(self):
        print("Show C")

class D(B, C):
    pass

d = D()
print("\n")
print(d.show())

# Prints the method resolution order of D.
print(D.mro()) # Show B
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# So, when we call d.show(), Python looks for show() in this order:

# D → no method defined here.

# B → ✅ show() found here, so it executes this.

# C → skipped because B already resolved it.

# A → not checked since already resolved.

# object → not needed.


# Diamond Inheritance:

#       A
#     /   \
#    B --> C
#     \   /
#       D
