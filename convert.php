<?php

/*
WARNING, code written in a short time, there are many hard-coded things, good luck!
https://www.reddit.com/r/Telegram/comments/mx8upw/i_can_export_telegram_chats_but_can_i_import/gvn9h7s/
*/


$file = file_get_contents("F:\\export\old\chats\chat_170\messages.html");

//var_dump($file);


// the regex will not match the last file (149)

$re = '/<div class="container page_wrap">([\s\S]*)<a href="messages\d*\.html">Next messages part/m';


preg_match_all($re, $file, $matches, PREG_SET_ORDER, 0);

// Print the entire match result
$str = $matches[0][1];
$str = str_replace("<br>", "\n", $str);
$str = strip_tags($str);
$str = html_entity_decode($str, ENT_QUOTES | ENT_HTML5);
$str = explode("\n\nID: ", $str);
//var_dump($str);

$arr = [];
foreach ($str as $s) {
    $datat = explode("\n", explode("Date: ", $s)[1], 2)[0];

    $re = '/\d\d(\d\d)\.(\d\d)\.(\d\d) (\d\d):(\d\d):(\d\d)/m';

    preg_match_all($re, $datat, $matches, PREG_SET_ORDER, 0);

    $arr[]['data'] = $data = "{$matches[0][3]}/{$matches[0][2]}/{$matches[0][1]}, {$matches[0][4]}:{$matches[0][5]}";
    //var_dump($data);

    if(!isset(explode("From: ", $s)[1])) {
        $pos1 = strpos($s, 'Phone call');
        $pos2 = strpos($s, 'Take screenshot');
        $pos3 = strpos($s, 'Score in a game');
        if ($pos1 !== false or $pos2 !== false or $pos3 !== false) {
            //$a = true;
            continue;
        } else {
            exit('error');
        }
    }
    $fromt = explode("\n", explode("From: ", $s)[1], 2)[0];

    // If you want to change the contact name
    //$arr[]['from'] = $from = str_replace('old name', 'new name', $fromt);

    if ( ! isset(explode("Text: ", $s)[1])) {
        // change with your language
        $arr[]['text'] = $text = "<Media omessi>";
    } else {
        $arr[]['text'] = $text = trim(explode("Text: ", $s)[1]);
    }
    echo "{$data} - {$from}: $text\n";
    //var_dump($s);
}


for ($i = 2; $i <= 148; $i++) {
    $file = file_get_contents("F:\\export\old\chats\chat_170\messages{$i}.html");

//var_dump($file);


// the regex will not match the last file (149)

    $re = '/<div class="container page_wrap">([\s\S]*)<a href="messages\d*\.html">Next messages part/m';


    preg_match_all($re, $file, $matches, PREG_SET_ORDER, 0);

// Print the entire match result
    $str = $matches[0][1];
    $str = str_replace("<br>", "\n", $str);
    $str = strip_tags($str);
    $str = html_entity_decode($str, ENT_QUOTES | ENT_HTML5);
    $str = explode("\n\nID: ", $str);
//var_dump($str);

    $a = false;
    $arr = [];
    foreach ($str as $s) {
        if($a == true) {
            exit('aaa');
        }

        $datat = explode("\n", explode("Date: ", $s)[1], 2)[0];

        $re = '/\d\d(\d\d)\.(\d\d)\.(\d\d) (\d\d):(\d\d):(\d\d)/m';

        preg_match_all($re, $datat, $matches, PREG_SET_ORDER, 0);

        $arr[]['data']
            = $data
            = "{$matches[0][3]}/{$matches[0][2]}/{$matches[0][1]}, {$matches[0][4]}:{$matches[0][5]}";
        //var_dump($data);

        //var_dump($s);
        if(!isset(explode("From: ", $s)[1])) {
            $pos1 = strpos($s, 'Phone call');
            $pos2 = strpos($s, 'Take screenshot');
            $pos3 = strpos($s, 'Score in a game');
            if ($pos1 !== false or $pos2 !== false or $pos3 !== false) {
                //$a = true;
                continue;
            } else {
                exit('error');
            }
        }
        $fromt = explode("\n", explode("From: ", $s)[1], 2)[0];

        // If you want to change the contact name
        //$arr[]['from'] = $from = str_replace('old name', 'new name', $fromt);

        if ( ! isset(explode("Text: ", $s)[1])) {
            // change with your language
            $arr[]['text'] = $text = "<Media omessi>";
        } else {
            $arr[]['text'] = $text = trim(explode("Text: ", $s)[1]);
        }
        echo "{$data} - {$from}: $text\n";
        //var_dump($s);
    }
}




// the code is copied from the one above because I'm lazy...


$file = file_get_contents("F:\\export\old\chats\chat_170\messages149.html");

//var_dump($file);


// the regex will not match the last file (149)

$re = '/<div class="container page_wrap">([\s\S]*)<\/div>/m';


preg_match_all($re, $file, $matches, PREG_SET_ORDER, 0);

// Print the entire match result
$str = $matches[0][1];
$str = str_replace("<br>", "\n", $str);
$str = strip_tags($str);
$str = html_entity_decode($str, ENT_QUOTES | ENT_HTML5);
$str = explode("\n\nID: ", $str);
//var_dump($str);

$arr = [];
foreach ($str as $s) {
    $datat = explode("\n", explode("Date: ", $s)[1], 2)[0];

    $re = '/\d\d(\d\d)\.(\d\d)\.(\d\d) (\d\d):(\d\d):(\d\d)/m';

    preg_match_all($re, $datat, $matches, PREG_SET_ORDER, 0);

    $arr[]['data'] = $data = "{$matches[0][3]}/{$matches[0][2]}/{$matches[0][1]}, {$matches[0][4]}:{$matches[0][5]}";
    //var_dump($data);

    if(!isset(explode("From: ", $s)[1])) {
        $pos1 = strpos($s, 'Phone call');
        $pos2 = strpos($s, 'Take screenshot');
        $pos3 = strpos($s, 'Score in a game');
        if ($pos1 !== false or $pos2 !== false or $pos3 !== false) {
            //$a = true;
            continue;
        } else {
            exit('error');
        }
    }
    $fromt = explode("\n", explode("From: ", $s)[1], 2)[0];

    // If you want to change the contact name
    //$arr[]['from'] = $from = str_replace('old name', 'new name', $fromt);

    if ( ! isset(explode("Text: ", $s)[1])) {
        // change with your language
        $arr[]['text'] = $text = "<Media omessi>";
    } else {
        $arr[]['text'] = $text = trim(explode("Text: ", $s)[1]);
    }
    echo "{$data} - {$from}: $text\n";
    //var_dump($s);
}

//var_dump($arr);
