{% extends "main/layout.php" %}
<?php

$pageName = 'Portfolio';
$pageStyle = 'background-color: blue;'

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
</head>

<body>
    {% block content %}
    {% include "main/text.php" %}
    <!-- <div class="align-items-center justify-content-center text-center">
        <h1 class="text-bg-dark rounded-pill">Welcome to my portfolio!</h1>
        <h2 class="text-body">This is the index page.</h2>
    </div> -->

    <br>
    {% for hra in hry %}
    <div>
        <p>{{ hra.name }}: {{ hra.description }}</p>
    </div>
    {% empty %}
    <p>No games found.</p>
    {% endfor %}

    {% endblock %}
</body>

</html>