window.onload = function() {
    document.getElementById('color_input').onkeyup = function() {
        var colorRegexp  = /(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$|^[a-zA-z]{3,}$)/i;
        if(!colorRegexp.test(this.value)) {
            return false;
        }

        document.getElementById('color_appearance').style.background = this.value;
        document.getElementById('color_current').innerHTML = 'Current color is <b>' + this.value + '</b>';
    };
};
