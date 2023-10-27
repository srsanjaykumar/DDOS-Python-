<?php

 $arr = ['apple','orange','Grapes',"Omega"];

 for ($data=0; $data < count($arr); $data++) { 
    echo($arr[$data] ."\n");
 }

 foreach ($arr as $key => $value) {
    echo($key." => ".$value ."\n");
 }

 foreach($arr as $fun){
    echo($fun."\n");
 }

?>


<?php

$full =[

    "en" => "English",
    "tam" => "Tamil",
    "mat"=>"Maths",
];


foreach ($full as $key => $value) {
    echo($key." => ".$value ."\n");
}

?> 