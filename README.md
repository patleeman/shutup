# shutup
####Shut that annoying console output up.

Sometimes you just want some peace and quiet.  Influenced by [fuckit.py](https://github.com/ajalt/fuckitpy)

How do I shut this stupid program up?

As a decorator:
    
    from shutup import shutup
    
    @shutup
    annoying_function():
        print("DOING SOMETHING HYUK HYUK")
        does something
        print("YAK YAK YAK YAK")
        returns something
        
As a context manager:

    from shutup import shutup
    
    annoying_function():
        print("DOING SOMETHING HYUK HYUK")
        does something
        print("YAK YAK YAK YAK")
        returns something
        
    with shutup:
        return_value = annoying_function()
        
        
  



Lots of help from [Stack Overflow](Ripped from http://stackoverflow.com/questions/2828953/silence-the-stdout-of-a-function-in-python-without-trashing-sys-stdout-and-resto)


