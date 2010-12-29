/*!
 * Duck Javascript Library
 * https://github.com/gregglind/duck
 *
 * Copyright 2010, Gregg Lind
 * Dual licensed under the MIT or GPL Version 2 licenses.
 *
 */


QUnit.specify("Duck Tests", function () {

    describe("Showing off the range of duck features", function () {
        var answers, got;
        answers = [
            ["same keys ok",
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                true, {}],
            ["missing subkey fail",
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                {"a": 1, "b": {"c": 1, "d": []}},
                false, {}],
            ["list wanted, dict gotten, fail",
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                {"a": 1, "b": []},
                false, {}],
            ["extra keys in data, not strict, ok",
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                {"a": 1, "c": true, "b": {"c": 1, "e": null, "d": [], "f": 1}},
                true, {"strict": false}],
            ["extra keys in data, strict will fail",
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                {"a": 1, "c": true, "b": {"c": 1, "e": null, "d": [], "f": 1}},
                false, {"strict": true}],
            ["model is int, data is dict, should fail",
                1,
                {},
                false, {}],
            ["model is int, data is list, should fail",
                1,
                [],
                false, {}],
            ["two empty dicts",
                {},
                {},
                true, {}],
            ["ignore the meta dict",
                {"a": 1, "__duck": {},"b": {"c": 1, "e": null, "d": []}},
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                true, {}],
            ["ignore the meta dict (not called meta!)",
                {"a": 1, "b": {"c": 1, "e": null, "d": []}, "OPTS": {}},
                {"a": 1, "b": {"c": 1, "e": null, "d": []}},
                true, {"meta": "OPTS"}],
            ["if no meta set, obviously the cmp should fail",
                {"a": 1, "__duck": {}, "b": {"c": 1, "e": null, "d": []}},
                {"a": 1, "b": {"c": 1, "e": null, "d": []}}, false,
                {"meta": null}],
    
            // validators
            ['int validator good',
                {'a':Number},
                {'a':1},
                true, {} ],
            ['int validator fails',
                {'a': Number},
                {'a': 'a'},
                false, {}],
            
            // inferred validator, python functions
        
            ['specials, eval python name',
                {'a':'___str'},
                {'a':'abc'},
                true,{}],
    
            // crazy json eval!
            ['specials, eval jscode!  ',
                {'a':'___(function(x) {return true;})'},
                {'a':'abc'},
                true,{}]
    
        ];

        // actual tests
        for (x in answers) {
            given(answers[x]).
                it(answers[x][0], function(label,model,data,ans,kwargs) {
                    kwargs.logger = duck.fakeLogger;
                    got = duck.quack(model,data,kwargs);
                    assert(ans).equals(got);
                });
        }
    });
});
