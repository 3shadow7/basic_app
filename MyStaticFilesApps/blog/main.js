// it work
var pixl_go = 0;
var t;
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("header").style.top = "0px";
        document.getElementById("switch-border").style.top = "3.2em";
document.getElementById("switch-border").style.right = "1.5em";
    } else {
        document.getElementById("header").style.top = "-50px";
document.getElementById("switch-border").style.top = "1.5em";
document.getElementById("switch-border").style.right = "1.5em";       
      //  document.getElementById("header").style.top = "-50px";
    }
    prevScrollpos = currentScrollPos;
}

