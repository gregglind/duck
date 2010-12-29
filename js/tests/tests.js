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
