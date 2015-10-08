import sys
import shutup

print("testing with context")
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

print('\n'*2)
print("testing wrapper")
def annoying_wrapper():
    print("Blah blah blah")
    sys.stdout.write("Blah Blah Blah")
    return 2 + 2

value3 = shutup.shutup(annoying_wrapper)()
print(value3)
