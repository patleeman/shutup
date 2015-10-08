import sys
import shutup

print("testing context manager")
def annoying():
    print("Blah blah blah")
    sys.stdout.write("Blah Blah Blah")
    return 2 + 2

with shutup.shutup():
    value1 = annoying()
print(value1)

print('\n'*2)
print("testing decorator")
@shutup.shutup
def annoying_decorated():
    print("Blah blah blah")
    sys.stdout.write("Blah Blah Blah")
    return 2 + 2

value2 = annoying_decorated()
print(value2)
__author__ = 'patrick'
