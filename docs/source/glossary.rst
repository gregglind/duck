.. _glossary:

**********
Glossary
**********

.. note::

    This glossary is intentionally sloppy about using Javascript / JSON / Python
    terms for various data structures interchangeably.  It's all :term:`simple data`,
    which is a central idea to this entire project.  When the particulars matter,
    they will be indicated.


..  glossary::
    :sorted:

    simple data
        objects made up ints, floats, strings, arrays (lists), dicts (hashes),
        booleans, NULLs, and the like.  No references, no pointers.

        These are the sorts of data structures that are great for YAML and JSON
        and the like, and which make up the bread-and-butter of most data
        exchange.

    simple data structure (SDS)
        a 'thingy' made up of :ref:`simple data`

    verification
        Is the SDS :term:`good enough`?  Contract with :term:`validation`.

    validation
        The process for determining if the code is syntactically valid JSON / Python / (whatever).
        Contrast with :term:`verification`
    
    good enough
        As beauty is in the eye of the beholder, this is deliberately slippery.
        Do the objects have the right(-enough) keys/properties?  Are the types close?
        Does the nesting structure look the same, etc.?
        
        variant spellings:  "Good Enough(tm)", "Just F**n Works".

    model.
        An example dict/list/object/whatever with optional additional
        keys.  This is the 'reference'
    
    data.
        Some dictionary/object/whatever to verify it's 'good enough'
    
    quack.
        Does that data 'sound like' the model?  Similar keys and types?
        (cf:  :mod:`duck.jsonduck.quack`)
