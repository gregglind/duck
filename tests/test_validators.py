import re

from testing_utils import *

from duck import validators

regexen_answers = [
    ('lt 5 int',
    validators.re_function_lt, 'lt_5', {'i1': '5'}),
    ('lt 5.001 float',
    validators.re_function_lt, 'lt_5.0001', {'i1': '5.0001'}),
    ('lt -5 int',
    validators.re_function_lt, 'lt_-5', {'i1': '-5'}),
]

def test_regexen():
    for label,regex,input,groupdict in regexen_answers:
        yield check_regexen, label, regex, input, groupdict

def check_regexen(label,regex,input,groupdict):
    s = regex.search(input)
    if s:
        got = s.groupdict()
    else:
        got = None
    nt.assert_equal(got,groupdict)



parse_answers = [
    ('lt 5 function', 'lt_5', validators.function_lt(5),{}),
    ('nonsense', 'nothing_matches_this_10',None, {}),
    ('int', 'int', int,{}),

]

# how to test if two functions are identical?
# what should this test be?  __name__ is OK, but spoofable.
def test_parse_validator():
    for label,string,fn,kwargs in parse_answers:
        yield check_parse_validator, label,string,fn,kwargs

def check_parse_validator(label,string,fn,kwargs):
    got = validators.parse_validator(string,**kwargs)
    if callable(got):
        nt.assert_equal(got.__name__,fn.__name__)
    else:
        nt.assert_equal(got,fn)

        

