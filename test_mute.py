import sys
import shutup

def annoying():
    a = 1
    print("1")
    sys.stdout.write("2\n")

    shutup.mute()
    a += 1
    print("3")
    sys.stdout.write("4\n")
    shutup.unmute()

    a += 1
    print("5")
    sys.stdout.write("6\n")

    return a

print("returns are not affected: {}".format(annoying()))