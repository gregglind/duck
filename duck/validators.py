# Duck Javascript Library
# https://github.com/gregglind/duck
# 
# Copyright 2010, Gregg Lind
# Dual licensed under the MIT or GPL Version 2 licenses.
# 

'''
Validators.... a minilang for 'duck' expressions....

'''

import re

from duck_logging import logging,get_logger
logger = get_logger()


# eventually make this caching.

# maybe do named tuple?
## obvious this is all a little rough, and merely for demo purposes

## TODO:  what is the 'right way' to change the order, allow people to have
## their own, etc.


# really, want to go with regexen for this rather than a real parser?  
re_function_lt = re.compile('lt_(?P<i1>-?\d+(.\d+)?)', re.X)
def function_lt(i1=None):
    def f(x):
        if not x < float(i1):
            raise Exception
    return f


regexen = [
    (re_function_lt, function_lt, 'less than'),
]


def parse_validator(string,regexen=regexen,eval_=True):
    ''' convert a string into a validator, if possible.

    Args:
        string:  the string to be parsed

        regexen:list of tuples of ('regex',function_factory, [name])

        eval_:  should 'eval' be used to try to guess the function name?
    
    
    Notes:
    
    1. implicit is that
        * the facacde for each factory is all kwargs
        * the function returned
            - takes a single positional value
            - raises for all invalid values

    >>> parse_validator('int').__name__
    'int'
    >>> assert parse_validator('int', [], eval_=False) is None

    '''
    if eval_:
        try:
            f = eval(string)
            if callable(f):
                return f
        except Exception:
            pass
    
    for regex, factory, name in regexen:
        logging.debug('trying: %r %r %r %r', regex, factory, name, string)
        g = regex.search(string)
        if g:
            return factory(**g.groupdict())
    
    return None
