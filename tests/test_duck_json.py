from testing_utils import *

from duck import jsonduck

answers = [
    ('same keys ok',
        dict(a=1,b=dict(c=1,d=[],e=None)),
        dict(a=1,b=dict(c=1,d=[],e=None)),
        True,{}),
    ('missing subkey fail',
        dict(a=1,b=dict(c=1,d=[],e=None)),
        dict(a=1,b=dict(c=1,d=[])),
        False,{}),
    ('list wanted, dict gotten, fail',
        dict(a=1,b=dict(c=1,d=[],e=None)),
        dict(a=1,b=[]),
        False,{}),
    ('extra keys in data, not strict, ok',
        dict(a=1,b=dict(c=1,d=[],e=None)),
        dict(a=1,b=dict(c=1,d=[],e=None,f=1), c=True),
        True,{'strict': False},),
    ('extra keys in data, strict will fail',
        dict(a=1,b=dict(c=1,d=[],e=None)),
        dict(a=1,b=dict(c=1,d=[],e=None,f=1), c=True),
        False,{'strict': True},),

    # meta should be ignored
    ('ignore the meta dict',
        dict(a=1,b=dict(c=1,d=[],e=None), __duck={} ),
        dict(a=1,b=dict(c=1,d=[],e=None)),
        True,{}),
    ('ignore the meta dict (not called meta!)',
        dict(a=1,b=dict(c=1,d=[],e=None),OPTS={}),
        dict(a=1,b=dict(c=1,d=[],e=None)),
        True,{'meta':'OPTS'}),
    ('if no meta set, obviously the cmp should fail',
        dict(a=1,b=dict(c=1,d=[],e=None), __duck={} ),
        dict(a=1,b=dict(c=1,d=[],e=None)),
        False,{'meta':None}),

    ## callables / validators
    ('int validator good',
        dict(a=int),
        dict(a=1),
        True,{}),
    ('int validator good',
        dict(a=int),
        dict(a='a'),
        False,{}),
]



def test_model_data_answer_kwarg():
    for label,model,data,answer,kwargs in answers:
        yield check_model_data_answer_kwarg, label, model,data,answer,kwargs

def check_model_data_answer_kwarg(label,model,data,answer,kwargs):
    nt.assert_equal(jsonduck.quack(model,data,**kwargs), answer)
