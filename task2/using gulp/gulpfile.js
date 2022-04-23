const { src, dest, watch } =  require('gulp');
const minifyJs = require('gulp-uglify');
const minifyCss = require('gulp-clean-css')
const sourceMaps = require('gulp-sourcemaps');
const concat = require('gulp-concat');

const bundleJs = () => {
    return src('./static/js/**/*.js')
        .pipe(sourceMaps.init())
        .pipe(minifyJs())
        .pipe(concat('bundle.js'))
        .pipe(sourceMaps.write())
        .pipe(dest('./dist/static/js/'));
} 
const bundleCss = () => {
    return src('./static/css/**/*.css')
        .pipe(sourceMaps.init())
        .pipe(minifyCss())
        .pipe(concat('bundle.css'))
        .pipe(sourceMaps.write())
        .pipe(dest('./dist/static/css/'));
}

const devWatch = () => {
    watch('./static/js/**/*.js', bundleJs);
    watch('./static/css/**/*.css', bundleCss);

}
exports.bundleJs = bundleJs;
exports.bundleCss = bundleCss;
exports.devWatch = devWatch;