
<html>
<head></head>
<body>
    <pre><?php
        $str = $_SERVER["REQUEST_URI"];
        preg_match('/#(.+)$/', $str, $res);
        var_dump(parse_url($str));
    ?></pre>

    <p id="dispArea" style="width: 480px;
                            word-wrap: break-word;" 
                            >dummydummydummydummydummy
    </p>

    <script>
    var hash = window.location.hash;
    var id_token = (hash.split('&'))[0]
    document.getElementById("dispArea").innerText=id_token;
    </script>
</body>    
</html>

