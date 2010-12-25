#!/usr/bin/env python

'''
JSON Validator, designed to be easy to use, even at the cost of generality.
If you want 'can handle anything' got to json schema or xsd or such!
If you want 'can handle most things, and it's not that hard to set up',
come here!

'''

def _nothing(*args,**kwargs):
    pass

class FakeLogger(object):
    def __getattr__(x):
        return _nothing

fakeLogger=FakeLogger()

function_type = type(lambda x:x)

def typish(thing):
    '''
    primitive, silly way of determining which of the major 'ducktypes'
    a thing is most like.

    Args:
        thing, the thing to determine
    
    Returns:
        a 'type'
    
    >>> map(typish,[dict(),list(),'a',1,None,False,lambda x:x])
    [<type 'dict'>, <type 'list'>, <type 'str'>, <type 'int'>, <type 'NoneType'>, <type 'bool'>, <type 'function'>]
    '''
    types = set([type(None),list,dict,bool,str,unicode,type(lambda x:x),int,float,set])
    if type(thing) in types:
        return type(thing)
    
    if thing is None:
        return type(None)
    try:
        thing + 1
        return float # could be int too... fine for now
    except TypeError, exc:
        try:
            thing + 'a'
            return str
        except TypeError:
            try:
                thing['a']
                return dict
            except TypeError, exc:
                try:
                    thing[-1]
                    return list
                except:
                    return bool



def iteratey(thing):
    '''
    iterate, or not, depending on the typish of the thing
    '''
    if typeish(thing):
        pass

'''
Obviously there is some impedence mismatch here between json objects
and python ones.  this is is version 0 code, and needs to be play-tested quite
a bit before it's useable.


v 0:
    only check keys and types

future:
    callables?  validation?

'''


class QuackError(Exception): pass

# version 0.0, assume it's all dicts everywhere....
def quack(model,data,meta='__duck',strict=False,version=1,logger=fakeLogger,
    special='___'):
    ''' is the data 'same enough' as the model?
    
    Args:
        model:  the 'reference' structure
        data:  the 'to be compared'
        meta:  the name of the key/attribute where 'meta' info, like
            options, etc. are in the model
        special:  if not None, anything prefixed with this will be treated
            as a 'special', invoking the (tbd?) minilang.  

    Notes:
    [1] validation... if the 'type' if 'function like', we try the function
        on the data.  Unless it raises, we view this as 'valid'
    [2] specials... maybe a django like minilang?  ___between_0_10?
            ___length_5_10 ?
        3 undescores...hideous, but at least it is configurable hideousness.
    '''
    rargs = dict(meta=meta,strict=strict,version=version,logger=logger)
    def same_typish(thing1,thing2):
        return typish(thing1) == typish(thing2)

    mtype,dtype = typish(model),typish(data)
    
    # maybe set up a delegation table for
    # pairings like:
    # {(dict,dict):  recurse...
    # {(list,str}):  False...}
    # tbd!

    # check for specials... v.0!
    # yes, lots of strong assumptions here!
    def check_special(thing, special=special):
        try:
            thing.startswith(special)
            cmd = thing.lstrip(special)
            # get special, for now, nothing!
            return _nothing
        except Exception, exc:
            return None

    _spec = check_special(model,special)
    if _spec:
        model = _spec
    
    ## normal handling...

    # both dicts, recurse
    if mtype is dict:
        if dtype is not dict:
            return False
    
        k1,k2 = set(model.keys()), set(data.keys())
        if meta is not None:
            if meta in k1:
                theseopts = model[meta]
                k1.remove(meta)
        if strict:
            if k1 != k2:
                return False
            else:
                return True
        
        # non strict
        if k1 <= k2:
            return all((quack(model[k],data[k],**rargs) for k in k1))
        else:
            print k1,k2,'false'
            return False
    
    # both lists - good enough!
    elif mtype is list:
        if dtype is list:
            print 'both lists, true'
            return True
        else:
            print 'm is list, d isnt, false'
            return False

    # I think 'callable' is close to right here,
    # since json doesn't like callables as data
    # this will be different in python / guarding
    # TODO, revisit.
    elif callable(model):
        print 'callable'
        try:
            model(data)
        except Exception, exc:
            print 'invalid', exc
            return False
        return True

    else:
        print 'not list or dict', model, data
        return True



'''



Duck

D<

A guard system for python

* Can also infer the properties of an object by analysing the ast
  (maybe even by using a fake object, the 'always responder' or 'Adaptable'),
    and changing all functions to have no effects.....

  good for figuruing out the parts of an object?
    



Quack!


def quack(model,data):
    for k in data:
        if callable(d)
    check that keys are same, etc.


{'some':'dict'}


# look at os.path.walk!....




Duck.json version 1:

are all keys the same
is each type the same?
for each key, if value is callable, does corresponding callable return non-false
'__meta' for meta stuff
* how to handle meta on lists?

'__fn_gt_5' and the like for 'fake functions'

choice?  oneof?  other pyparsing constructs?


Duck.fake_function(string):
    return fn
    

Duck.validate(model,data):
    
'''
