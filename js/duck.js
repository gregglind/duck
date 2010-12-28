if (typeof Array.isArray === "undefined") {
    Array.isArray = function (arg) {
        return Object.prototype.toString.call(arg) === "[object Array]";
    };
}


// [[],{},'a',function(){},true].map(function(x){return typeof(x);})
// ["object", "object", "string", "function", "boolean"]

hasOwn = Object.prototype.hasOwnProperty;


duck = (function(){
    // cf:  jquery class2type?
    typish = function(thing){
        if (Array.isArray(thing)) {
            return 'array';
        } else {
            return typeof(thing);
        }
    };


    quack_defaults = {
        meta: '__duck',
        strict: false,
        version: 1,
        logger: console,
        special: '___'
    };

    quack = function(model,data,options){
        if (options === undefined) {
            options = quack_defaults;
        }
        
        var mytype;
        var dtype;
        var name;
        var logger;
    
        logger = options.logger;

        mtype = typish(model);
        dtype = typish(data);

        logger.log(mtype);
        logger.log(model);
        logger.log(dtype)
        logger.log(data);
        
        if (mtype === 'string') {
            // does it start with the special string?
            if (model.indexOf(options.special) == 0) {
                // an 'always true
                // eventually need a 'eval(model.slice(options.special.length)))' bit
                model = function(){ return true; };
                mtype = typish(model);  // function!
            }
        }

        if ((mtype === 'array') || (dtype === 'array')) {
            if (mytype === dtype) {
                return true;
            } else {
                return false;
            }
        } else if (mtype === 'object' || dtype==='object') {
            // loop over the keys
            if (mtype !== dtype) {
                return false;
            }
            // we need to add on strictness and whatnot here.
            // return all((quack(model[k],data[k],**rargs) for k in k1))
            for ( name in model ) {
                if (!(name in data)) {
                    logger.log(name);
                    return false;
                }
                if (! quack(model[name],data[name],options)) {
                    return false;
                }
            return true;
            }
        } else if (mtype === 'function') {
            // call it on the data, what should happen here, given
            // js exceptions and the like!
            mtype(data);
            return true;
        }  else {
            return true;
        }
        return true;
    };

    return {
        'quack':  quack,
        'quack_defaults': quack_defaults,
        'typish':  typish
    };
}());



/*
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

    1.  validation... if the 'type' if 'function like', we try the function
        on the data.  Unless it raises, we view this as 'valid'
    2.  specials... maybe a django like minilang?  ___between_0_10?
        ___length_5_10 ?   (basic implementation is in ``validators``.)
        Three (3) undescores is hideous, but at least it is configurable hideousness.

    >>> model = {'a': 1, 'b': []}
    >>> data = {'a': 13, 'b': [1,2,3,4,5], 'c':True}
    >>> data_bad = {'d':1}
    >>> assert quack(model,data)
    >>> assert not quack(model,data_bad)
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
            #print k1,k2,'false'
            return False
    
    # both lists - good enough!
    elif mtype is list:
        if dtype is list:
            #print 'both lists, true'
            return True
        else:
            #print 'm is list, d isnt, false'
            return False

    # I think 'callable' is close to right here,
    # since json doesn't like callables as data
    # this will be different in python / guarding
    # TODO, revisit.
    elif callable(model):
        #print 'callable'
        try:
            model(data)
        except Exception, exc:
            #print 'invalid', exc
            return False
        return True

    else:
        #print 'not list or dict', model, data
        return True
*/
