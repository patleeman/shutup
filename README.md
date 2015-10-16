# Shutup v 1.1
###Shutup.py - Silence annoying console output.
####Sometimes you just want some peace and quiet.


####About:
Shutup.py helps you tell your console output to shut up for a minute.


####Installation:
```
# cd to your working directory
git clone https://github.com/patleeman/shutup.git
cd shutup
python setup.py install

```
*pypi eventually...*


#### Usage:
As a decorator to shut up your stupid functions:

```python
import shutup

@shutup.function
def annoying_function():
    print("DOING SOMETHING HYUK HYUK")
    # does something
    print("YAK YAK YAK YAK")
    return something

a = annoying_function()
print(a)
>>> something
```
*Shutup.py silences sys.stdout.write and print calls*

Shut those hoity toity methods up too...

```python
import shutup
import sys

class derp(object):
    def __init__():
        self.value = 2 + 2

    @shutup.method
    def let_me_tell_you(self):
        print("I'm a cool method, ")
        sys.stdout.write("totally not a function in a fancy class scarf")
        return self.value

instance = derp()
print(instance.let_me_tell_you())
>>> 4
```

As a context manager:

```python
import shutup

def annoying_function():
    print("DOING SOMETHING HYUK HYUK")
    # does something
    print("YAK YAK YAK YAK")
    return something

with shutup.context():
    return_value = annoying_function()

print(return_value)
>>>something
```
*Shutup does not affect return values, it just puts a muzzle on the console.*

You can also mute a chunk of code:

```python
import shutup

print("Hi, I have something to tell you:")
shutup.mute()
print("DOING SOMETHING HYUK HYUK")
# does something
print("YAK YAK YAK YAK")
print("yak yak yak" * 1000)
shutup.unmute()
print("Hi, I'm unmuted!")
>>>Hi, I'm unmuted!
```


####WARNINGS:

It is not advisable to use this code. **period**.  However, if you insist on using it to shut up your annoying console output, be advised that when muting or shutting a function up, this function overrides sys.stdout with an empty object so if you're trying to use sys.stdout concurrently while muted, it will get muted.  If you're running anything async or threaded, it may be affected as well.  **BE WARNED**.


####References:
* Lots of help from [Stack Overflow](Ripped from http://stackoverflow.com/questions/2828953/silence-the-stdout-of-a-function-in-python-without-trashing-sys-stdout-and-resto)
* [Influenced](https://gist.github.com/patleeman/e44096f755b6db7b9996) by [fuckit.py](https://github.com/ajalt/fuckitpy) (Except shutup's code is way shittier)


####Bugs:
[BAM -> Issue tracker](https://github.com/patleeman/shutup/issues)

####Contribute:
Rome wasn't built by one slave, help contribute to this worthwhile open source project and make your mark in the annals of free software.  Okay, maybe not, but it looks good on a resume... maybe?
