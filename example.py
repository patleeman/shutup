from shutup import shutup

@shutup
def doing_stuff():
    print("Shut a whole function up")
    a = 3.1415
    return a

a = doing_stuff()


def doing_more_stuff():
    print("Shut part of a function up")

    with shutup:
        print("ANNOYING OUTPUT HERE")
        print("Hue Hue Hue")

    b = 123456
    return b

b = doing_more_stuff()

# todo: This doesn't work yet'
def doing_even_more_stuff():
    def innie():
        print("hur dur dur")
        return 2+2

    print("shut up a function call")
    value = shutup(innie)
    print(value)

c = doing_even_more_stuff()