.. _duck:

About Duck
============

Ever find yourself writing code like this?

.. sourcecode:: python

    if 'xycoords' in mydata.getdefault('payload',dict()):
        api_version = 1.3

I have, and it's tedious, fragile, and error prone.  Most of the time, I don't care
about the entirety of a returned :term:`simple data` structure, but of particular parts.
Adding extra is fine!  Removing keys I don't use is fine!

.. sidebar:: if it's good enough, it's good enough

    parts of the data that don't affect me, *don't matter*


Duck makes :term:`verification` of :term:`simple data` objects easy.
Duck is intented to determine when an 'object' is :term:`good enough` to be useful.
That is:

* Does is have the right keys?  The right nesting structure?
* Are the types and values :term:`good enough` to be useful or usable?  Are they
  *wrong enough* that errors should be sent out to the consumer or producer?


Right now, Duck has two useful python modules

* :mod:`duck.jsonduck`
* :mod:`duck.validators`

Duck also includes a javascript version called:

* duck.js

An eventual goal to expand this into a general `**kwargs` processing / guard system
for Python.  That goal might be misguided.


What Duck is Not
------------------

* it's not a json :term:`validator`.  This should be handled by your json decoder.
* it's not a typing system.  At least not in the classical sense.  Duck
  is intended to be used to verify that a data structure is 'good enough'
  to be used by a downstream consumer, and that's it.  


Prinicples
============

* 90/10 is good enough.  Edge cases can get their own special code.
* Practicality over purity
* Assume most people want to do sane things, most of the time.
* get facade `feeling good` first, worry about performance later.

    * Don't worry about caching results
    * Use existing tools
    * if it's worth doing, we can always make it faster later
    * simple tasks should have short code


Duck Anatomy
===============

model.
    An example dict/list/object/whatever with optional additional
    keys.  This is the 'reference'

data.
    Some dictionary/object/whatever to verify it's :term:`good enough`.

quack.
    Does that data 'sound like' the model?  Similar keys and types?
    (cf:  :mod:`duck.jsonduck.quack`)


Examples (Python)
===================


Setup
-------

::

    >>> from duck.jsonduck import quack


Simple
--------
::

    >>> model = {'a': 1, 'b': {'a':1} }
    >>> data = {'a': 1, 'b': {'a': 1,'b': 2}, 'c':1}
    >>> assert quack(model,data)

The data contains the keys in the model.  Applies recursively.


Strict
--------
::

    >>> model = {'a': 1, 'b': {'a':1} }
    >>> data = {'a': 1, 'b': {'a': 1,'b': 2}, 'c':1}
    >>> assert not quack(model,data,strict=True)

The data has some extra keys (`c`, `b:b`) that aren't in the model.


Validators (callables)
------------------------
::

    >>> model = {'a': int}
    >>> data = {'a': 1}
    >>> assert quack(model,data)

Callables are applied on the corresponding datum.  Valid unless the function raises.


Validators (inferred)
------------------------
::

    >>> model = {'a': '___int'}
    >>> data = {'a': 1}
    >>> assert quack(model,data,specials='___')

See :mod:`duck.validators`.  Any string that starts with the `specials` prefix
is sent through :mod:`duck.validators.parse_validator` .  



Examples (JavaScript)
======================


Enabling The Library
--------------------

.. sourcecode:: html

   <script type="text/javascript" src="duck.js"></script>

Simple
--------

.. sourcecode:: javascript

    var model = {'a': 1, 'b': {'a':1} }
    var data = {'a': 1, 'b': {'a': 1,'b': 2}, 'c':1}
    duck.quack(model,data) === true;

The data contains the keys in the model.  Applies recursively.


Strict
--------


.. sourcecode:: javascript

    var model = {'a': 1, 'b': {'a':1} }
    var data = {'a': 1, 'b': {'a': 1,'b': 2}, 'c':1}
    duck.quack(model,data,strict=true) === false

The data has some extra keys (`c`, `b:b`) that aren't in the model.


Validators (callables)
------------------------

.. sourcecode:: javascript

    var model = {'a': Number}
    var data = {'a': 1}
    duck.quack(model,data)

Callables are applied on the corresponding datum.  Valid unless the function raises.

.. warning::

    In Javascript, in version 0.1.x of Duck, this is incomplete.  One of the
    version 0.2.x goals is to figure out what idiom this should use:  


Validators (inferred)
------------------------

..sourcecode:: javascript

    var model = {'a': '___int'}
    var data = {'a': 1}
    duck.quack(model,data,specials='___') === true

    


.. note::

    **duck.validators** knows the aliases of (some of) the simple python
    type functions.  

Details:
==========

In 0.1, objects are compared in this order.

* Keys:  both must be have keys.
* Lists:  both must be list-like.
* callables:  if a value is a 'callable' (i.e, a function), use it as a validator.
* everything else (bool, float, None, etc.):  types here are all equivalent enough.
  
  * '___strings'.  By default, strings starting with '___' are interpreted
    as 'validators', and Duck will attempt to construct a function based on
    them.  Notable, it will try to 'eval' it, so `___int` implies ``int``.
    This feature is experimental, and I am not sure if it's a good idea or not.
    The JS library knows the basic Python type functions, aliased to their
    JS equivalents.


Alternatives
===============

* JSON Schema
* Abstract Base Classes
* Zope.interfaces
* XSD - convert your json into xml and verify it there.  


FAQ
=========


Feature X Doesn't Work
--------------------------

You are probably correct.  Many parts of this are young.  File a bug with
with a test case, on GitHub at https://github.com/gregglind/duck/issues, please.  


You suck, and your code is stupid
-----------------------------------------

some variations::

    a) Duck Typing doesn't mean that
    b) Your grammar is inconsistent / incomplete
    c) Stop GUESSING! Be EXPLICIT

As described in the Principles above, Duck is meant to be practical before pure.
I don't mind inferring the common cases, and assuming programmers are sane.
For completeness, nearly all the "magic" can be turned off or overriden.


Unicode?
------------

Nobody uses it, don't worry about it!  Oh wait, yes, I should make that
consistent.  Once I think about the non-``dict``, non-``list`` types,
I am sure the details there will be formalized. 


What's with the stupid (or more politely, silly) names?
----------------------------------------------------------

I like silliness.  In future versions, maybe having saner names for things
could be a priority.  Part of the reason for names like :mod:`duck.jsonduck.typish`
is to remind me that these are dangerous, magical, unreliable functions.
They might bite.


How can I contribute?
-----------------------

Nothing in ``Duck`` is particularly hard to code.  The only new technology here is
how the facade feels.  Feedback on how Duck should 'feel' is extremely welcome.

* What kind of guard systems do you use?
* What kinds of validation are tedious and error-prone?
* What is 'too much work' during coding?



Future Directions
=====================

Duck is a young project, and there are many parts needing field testing,
executive decisions, and honing.  Among the questions under consideration:

* How 'smart' should the verification be?  How much should it guess/infer?
* should the 'strict' argument in jsonduck.quack be a dict of 'features',
  like 'guess_list', 'strict_keys' or the like?
* offer jsonschema output
* more / different / better validators?



Contributors Policy
======================
 
I value contributions from everyone, regardless of age, sex, neurotypical status,
orientation, nationality, experience level, or education.  Coding is
democratic, and Great Ideas can come from anywhere.


License
===========

Duck is licensed under the MIT Licence or the GPL v.2 licence.
Use whichever suits your needs.

The MIT License is recommended for most projects. It is simple and easy to
understand and it places almost no restrictions on what you can do with a Duck project.

If the GPL suits your project better you are also free to use a Duck project under that license.

You don't have to do anything special to choose one license or the
other and you don't have to notify anyone which license you are using.
You are free to use a Duck project in commercial projects as long as
the copyright header is left intact.

(Documentation is all licensed under Creative Commons.)

Licenses
------------
* `MIT Licence <http://github.com/jquery/jquery/blob/master/MIT-LICENSE.txt>`_ (`More Information <a href="http://en.wikipedia.org/wiki/MIT_License">`_)
* `GPL <a href="http://github.com/jquery/jquery/blob/master/GPL-LICENSE.txt">`_ (`More Information <a href="http://en.wikipedia.org/wiki/GNU_General_Public_License">`_) 

