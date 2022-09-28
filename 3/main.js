window.onload = function() {
    document.getElementById('color-code').onkeyup = function() {
        var result;
        var colorRegExp  = /(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$|^[a-zA-z]{3,}$)/i;

        if(!colorRegExp.test(this.value)) {
            result = 'Invalid color';
        } else {
            result = 'Current color is <b>' + this.value + '</b>';
            document.getElementById('color-appearance').style.background = this.value;
        }

        document.getElementById('info').innerHTML = result;
    };
};
