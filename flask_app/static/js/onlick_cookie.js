document.getElementById("link").addEventListener("click", function() {
    document.cookie = 'scrollpos=' + window.pageYOffset;

window.onload = function() {
    let scrollpos = document.cookie.match(/scrollpos=(\d+)/);
    if (scrollpos) {
    window.scrollTo(0, scrollpos[1]);
    }
};
});