<!DOCTYPE html>
<html>
<head>
<script type = "text/javascript" src = "client.js"></script>
</head>
<body onload = "post(document.getElementById('content').innerHTML)">
<div id = "content">
	<?php 
		print($_POST["input"]);
	?>
</div>
</body>
</html>