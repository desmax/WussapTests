window.onload = function() {
    document.getElementById('color').onkeyup = function() {
        document.getElementById('color_appearance').style.background = this.value;
    };
};
