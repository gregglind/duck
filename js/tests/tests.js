/*!
 * Duck Javascript Library
 * https://github.com/gregglind/duck
 *
 * Copyright 2010, Gregg Lind
 * Dual licensed under the MIT or GPL Version 2 licenses.
 *
 */

(function () {
    var all_test_files, x;
    
    all_test_files = [
        '../duck.js',  // import duck!
        'test_duck.js',
    ];
    for (x in all_test_files) {
        document.write('<script type="text/javascript" src="'+ all_test_files[x] + '"></script>');
    }
})()
