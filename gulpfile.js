var gulp = require('gulp');
var gulpif = require('gulp-if');
var clean = require('gulp-clean');
var concat = require('gulp-concat');
var less = require('gulp-less');
var autoprefixer = require('gulp-autoprefixer');
var minifyCss = require('gulp-minify-css');
var uglify = require('gulp-uglify');
var rev = require('gulp-rev');
var runSequence = require('run-sequence');
var config = require('./gulp.config');

gulp.task('clean', function () {
    return gulp.src(config.clean, {read: false})
        .pipe(clean());
});

gulp.task('styles:vendor', function () {
    return runStyles(config.vendorStyles, 'vendor.css', false);
});

gulp.task('styles:vendor:build', function () {
    return runStyles(config.vendorStyles, 'vendor.css', true);
});

gulp.task('styles:app', function () {
    return runStyles(config.appStyles, 'app.css', false);
});

gulp.task('styles:app:build', function () {
    return runStyles(config.appStyles, 'app.css', true);
});

gulp.task('scripts:vendor', function () {
    return runScripts(config.vendorJavascript, 'vendor.js', false);
});

gulp.task('scripts:vendor:build', function () {
    return runScripts(config.vendorJavascript, 'vendor.js', true);
});

gulp.task('scripts:app', function () {
    return runScripts(config.appJavascript, 'app.js', false);
});

gulp.task('scripts:app:build', function () {
    return runScripts(config.appJavascript, 'app.js', true);
});


// with minification
gulp.task('build', function () {
    runSequence('clean', 'styles:vendor:build', 'styles:app:build', 'scripts:vendor:build', 'scripts:app:build');
});

// without minification
gulp.task('default', function () {
    runSequence('clean', 'styles:vendor', 'styles:app', 'scripts:vendor', 'scripts:app');
});


function runStyles(files, fileName, minify) {
    return gulp.src(files)
        .pipe(concat(fileName))
        .pipe(less())
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))
        .pipe(gulpif(minify, minifyCss()))
        .pipe(rev())
        .pipe(gulp.dest(config.path.dist))
        .pipe(rev.manifest('assets.json', {
            cwd: './',
            merge: true
        }))
        .pipe(gulp.dest('./'));
}

function runScripts(files, fileName, minify) {
    return gulp.src(files)
        .pipe(concat(fileName))
        .pipe(gulpif(minify, uglify()))
        .pipe(rev())
        .pipe(gulp.dest(config.path.dist))
        .pipe(rev.manifest('assets.json', {
            cwd: './',
            merge: true
        }))
        .pipe(gulp.dest('./'));
}
