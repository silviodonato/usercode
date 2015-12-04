<html>
<head>
<meta http-equiv="Content-Type" content="text/html">
<title>Show images in folder</title>
<style type="text/css">
body {
    margin: 0 auto 20px;
    padding: 0;
    background: white;
#    background: #acacac;
    text-align: center;
}
td {
    padding: 0 0 50px;
    text-align: center;
    font: 9px sans-serif;
}
table {
    width: 100%;
}
img {
    display: block;
    margin: 20px auto 10px;
    max-width: 200px;
    outline: lightgrey solid 2px ;
}
#img:active {
#    max-width: 100%;
#}
#a:focus {
#    outline: none;
#}
</style>
</head>
<body>
 
<?php
$colums = 3;
$folder = './';
$filetype = '*.png';
	$files = glob($folder.$filetype);
	$count = count($files);
	echo $count;
	echo $folder;
	echo '<table>';
	for ($i = 0; $i < $count; $i++) {
	    echo "\n";
	    if ($i%$colums==0) {echo '<tr>'; echo "\n";}
	    echo '<td>';
	#    echo '<a name="'.$i.'" href="#'.$i.'"><img src="'.$files[$i].'" /></a>';
	#<a href=".$files[$i]."><img style="border:0;" src="smiley.gif" alt="HTML tutorial" width="42" height="42">

	    echo '<a href="'.$files[$i].'"><img src="'.$files[$i].'" /></a>';
	    echo substr($files[$i],strlen($folder),strpos($files[$i], '.')-strlen($folder));
	    echo '</td>';
	    if ($i%$colums==($colums-1)) {echo "\n"; echo '</tr>'; }
	}
	echo '</table>';
?>
