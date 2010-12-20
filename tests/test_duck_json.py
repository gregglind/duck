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
]



def test_model_data_answer_kwarg():
    for label,model,data,answer,kwargs in answers:
        yield check_model_data_answer_kwarg, label, model,data,answer,kwargs

def check_model_data_answer_kwarg(label,model,data,answer,kwargs):
    nt.assert_equal(jsonduck.quack(model,data,**kwargs), answer)
