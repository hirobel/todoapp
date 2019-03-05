    # vi test.php
    <?php
    $str = $_SERVER["REQUEST_URI"];
    preg_match('/#(.+)$/', $str, $res);
    var_dump(parse_url($str));
