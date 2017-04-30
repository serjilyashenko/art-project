module.exports = (function () {
    var path = {
        sourceJavascript: './static_source/javascript',
        sourceStyles: './static_source/styles',
        semantic: './static_source/semantic/dist',
        nodeModules: './node_modules/',
        dist: './static/build'
    };

    var config = {
        path: path,
        clean: [
            'assets.json',
            './static/build/*.{js,css}'
        ],
        appStyles: [
            path.semantic + '/semantic.css',
            path.sourceStyles + '/app.less'
        ],
        appJavascript: [
            path.nodeModules + '/jquery/dist/jquery.js',
            path.semantic + '/semantic.js',
            path.sourceJavascript + '/app.js'
        ]
    };

    return config;
}());
