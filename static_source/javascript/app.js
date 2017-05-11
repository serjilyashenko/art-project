document.addEventListener("DOMContentLoaded", function (event) {
    document.querySelectorAll('img').forEach(function (img) {
        img.onerror = function () {
            this.className += ' error';
        };
    })
});
