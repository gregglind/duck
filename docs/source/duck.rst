./duck:

About Duck
-------------

Duck makes object *verficiation* easy.  Duck is intented to determine when
an 'object' is 'complete enough' to be useful.

Right now, Duck has one module `jsonduck`.  An eventual goal to expand this
into a general `**kwargs` processing / guard system.  That goal might be
misguided.


What Duck is Not:

* it's not a json validator.  This should be handled by your json decoder
* it's not a typing system.  At least not in the classical sense.  Duck
  is intended to be used to verify that a data structure is 'good enough'
  to be used by a downstream consumer.


Prinicples
--------------

* 90/10 is good enough.  Edge cases can get their own special code.
* Practicality over purity
* Assume most people want to do sane things, most of the time.
* facade first, performance later.

    * Don't worry about caching results
    * Use existing tools
    * if it's worth doing, we can always make it faster later



Duck Anatomy
---------------

* model.  An example dict/list/object/whatever with optional additional
  keys.  This is the 'reference'
* data.  Some dictionary/object/whatever to verify it's 'good enough'
* quack.  Does that data 'sound like' the model?  Similar keys and types?


Examples
-----------


Details:

* Keys
* Lists
* callables:  if a value is a 'callable' (i.e, a function),
* everything else
  
  * '___strings'.  By default, strings starting with '___' are interpreted
    as 'validators', and Duck will attempt to construct a function based on
    them.  Notable, it will try to 'eval' it, so `___int` implies `int`.
    This feature is experimental, and I am not sure if it's a good idea or not.




Alternatives
---------------

JSON Schema
Abstract Base Classes
Zope.interfaces
XSD - convert your json into xml and verify it there.  



FAQ
-----


* X Doesn't Work

You are probably correct.  Many parts of this are young.  File a bug with
with a test case, please!


You suck, and your code is stupid::

    a) Duck Typing doesn't mean that
    b) Your grammar is inconsistent / incomplete
    c) Stop GUESSING!


* Unicode?
Nobody uses it, don't worry about it!  Oh wait, yes, I should make that
consistent.


* What's with the stupid names?

I like silliness.  In future versions, maybe having saner names for things
could be a priority.  


* How can I contribute?
Nothing in Duck is particularly hard to code.  The only new technology here is
how the facade feels.  Feedback on how Duck should 'feel' is extremely welcome.



Future Directions
-------------------

Duck is a young project, and there are many parts needing field testing,
executive decisions, and honing.  Among the questions under consideration:

* How 'smart' should the verification be?  How much should it guess/infer?
* should the 'strict' argument in jsonduck.quack be a dict of 'features',
  like 'guess_list', 'strick_keys' or the like?
* offer jsonschema output
* more / different / better validators?



Contributors Policy
-----------------------
 
  I value contributions from everyone, regardless of age, sex, neurotypical status,
  orientation, nationality, experience level, or education.  Coding is
  democratic, and Great Ideas can come from anywhere.


License
--------

Duck is licenced under the same terms as Python itself.  


