

'''

'''

def _nothing(*args,**kwargs):
    pass

class FakeLogger(object):
    def __getattr__(x):
        return _nothing

fakeLogger=FakeLogger()


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
def quack(model,data,meta='__duck',strict=False,version=1,logger=fakeLogger):
    ''' is the data 'same enough' as the model?
    
    Args:
        model:  the 'reference' structure
        data:  the 'to be compared'
        meta:  the name of the key/attribute where 'meta' info, like
            options, etc. are in the model
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

    # both dicts, recurse
    if mtype is dict:
        if dtype is not dict:
            return False
    
        k1,k2 = set(model.keys()), set(data.keys())
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
