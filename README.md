# Shutup v 1.1
###Shutup.py - Silence annoying console output.
####Sometimes you just want some peace and quiet.

Shutup.py helps you tell your console output to chill the fuck out and shut upfor a minute.  


Installation:
```
# cd to your working directory
git clone https://github.com/patleeman/shutup.git
cd shutup
python setup.py install

```
pypi eventually...


As a decorator to shut up your stupid functions:

```python
import shutup

@shutup.function
annoying_function():
    print("DOING SOMETHING HYUK HYUK")
    does something
    print("YAK YAK YAK YAK")
    returns something
    
a = annoying_function()
print(a)
>>> something
```

Shut those hoity toity methods up too...

```python
class derp(object):
    @shutup.method
    def yammering_decorate_method(self):
        print("I'm a cool method, ")
        sys.stdout.write("totally not a function in a fancy class scarf")
        return self.output

```

As a context manager:

```python
import shutup

annoying_function():
    print("DOING SOMETHING HYUK HYUK")
    does something
    print("YAK YAK YAK YAK")
    returns something
    
with shutup.context():
    return_value = annoying_function()
    
print(return_value)
>>>something
```    
*Shutup does not affect return values, it just puts a muzzle on the console.*

You can also mute a chunk of code:
        
```python
from shutup import mute, unmute


print("Hi, I have something to tell you:")
mute()
print("DOING SOMETHING HYUK HYUK")
does something
print("YAK YAK YAK YAK")
print("yak yak yak" * 1000)
unmute()
print("Hi, I'm unmuted!")


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