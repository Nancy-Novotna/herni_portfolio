{% extends "main/layout.php" %}
<?php
$pageName = 'Games';
$pageStyle = 'background-color: red;'
    ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ pageName }}</title>
</head>

<body>
    {% block content %}
    {% include "main/text.php" %}
    {% for hra in games %}
    <div class="bg-body-secondary flex-row justify-content-center align-items-center">
        <table>
            <tr class="flex-row">
                <td>{{ hra.title }}</td>
                <td>{{ hra.price }}</td>
            </tr>
        </table>
    </div>
    {% empty %}
    <p>No games found.</p>
    {% endfor %}
    {% endblock %}
</body>

</html>