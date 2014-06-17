var scripts = [];

function loadScripts() {
    function callbackAndLoad() {
        if (scripts.length > 0)
        {
            loadScripts();
        }

        // Handle memory leak in IE
        /*
        script.onload = script.onreadystatechange = null;
        if ( head && script.parentNode ) {
            head.removeChild( script );
        }
        */
    }

    if (scripts.length == 0)
    {
        // nothing to load
        return;
    }

    var head = document.getElementsByTagName("head")[0],
        script = document.createElement("script");
    script.type = "text/javascript";

    if (typeof script.onreadystatechange === "object") { // IE
        script.onreadystatechange = function () {
            if ((script.readyState === "loaded" ||
                script.readyState === "complete") &&
                script.loaded === undefined)
            {
                callbackAndLoad();
                // Clear src to prevent double callbacks.
                // IE is weird! http://stackoverflow.com/a/6946720/648162
                script.loaded = true;
            }
        };
    } else { // onload (rest of the lot)
        script.onload = callbackAndLoad;
    }
    
    script.src = scripts[0];
    scripts.splice(0, 1);
    head.appendChild(script);
}
