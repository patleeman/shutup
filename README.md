# Shutup v 1.0
####Shut that annoying console output up.  Sometimes you just want some peace and quiet. 

So, you may be asking yourself: How do I shut this stupid program up?  Here's how:

Installation:
```
# cd to your working directory
git clone https://github.com/patleeman/shutup.git
cd shutup
python setup.py install

```
pypi eventually...


As a decorator:

```python
from shutup import shutup

@shutup
annoying_function():
    print("DOING SOMETHING HYUK HYUK")
    does something
    print("YAK YAK YAK YAK")
    returns something
    
a = annoying_function()
print(a)
>>> something
```
        
As a context manager:

```python
from shutup import shutup

annoying_function():
    print("DOING SOMETHING HYUK HYUK")
    does something
    print("YAK YAK YAK YAK")
    returns something
    
with shutup:
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
* Influenced by [fuckit.py](https://github.com/ajalt/fuckitpy) (Except shutup's code is way shittier)


####Bugs:
[BAM -> Issue tracker](https://github.com/patleeman/shutup/issues)

####Contribute:
Rome wasn't built by one slave, help contribute to this worthwhile open source project and make your mark in the annals of free software.  Okay, maybe not, but it looks good on a resume... maybe?