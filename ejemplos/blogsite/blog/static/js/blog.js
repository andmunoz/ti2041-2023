function setCookie(key, value) {
    document.cookie = `${key}=${value};`;
}

function getCookie(key) {
    let cookies = document.cookie.split(';');
    for (i=0; i<cookies.length;i++) {
        let cookie = cookies[i].split('=');
        if (cookie[0] == key) {
            return cookie[1];
        }
    }
    return '';
}

function setMode(mode) {
    document.querySelector('html').setAttribute('data-bs-theme', mode);
}

function updateTheme() {
    let mode = getCookie('mode');
    if (mode == 'dark')
        mode = 'light';
    else
        mode = 'dark';
    setMode(mode);
    setCookie('mode', mode);
}

let mode = getCookie('mode');
setMode(mode);