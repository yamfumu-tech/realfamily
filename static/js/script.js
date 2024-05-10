window.onscroll = function() {
    stickyHeader();
};

const header = document.getElementById("sticky-header");
const sticky = header.offsetTop;

function stickyHeader() {
    if (window.pageYOffset > sticky); {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}