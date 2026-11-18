{% extends "main/layout.php" %}
<?php
$pageName = 'Games';
$pageStyle = 'background-color: red;';

$sqlGenre = "SELECT `games`.`title`, `genre`.`type` FROM `games`, `genre`, `filter_genre` WHERE `filter_genre`.`id_game`=`games`.`id_game` AND `filter_genre`.`id_genre`=`genre`.`id_genre`;";
$resultsGenre = mysqli_query($conn, $sqlGenre);
?>
<!-- <?php
if ($resultCheckGenre > 0) {
    while ($row = mysqli_fetch_assoc($resultsGenre)) {
        echo '|' . $row['type'] . '|' . PHP_EOL;
    }
}
?> -->
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
    <div class="flex-column flex-row" style="width: 500px; grid-auto-columns: 50px;">
        <div class="border rounded-3 overflow-auto">
            <table class="table table-striped mb-0">
                <thead>
                    <th>Game</th>
                </thead>
                {% for hra in games %}
                <tbody>
                    <td>
                        {{ hra.title }}:
                        {% if hra.price == 0 %}
                        Free!
                        {% else %}
                        {{ hra.price }} euro
                    </td>
                    {% endif %}

                    {% empty %}
                    <p>No games found.</p>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <br>

        <div class="border rounded-3 overflow-auto">
            <table class="table table-striped mb-0">
                <thead>
                    <tr>
                        <th>Tags</th>
                    </tr>
                </thead>
                {% for genre in genres %}

                <tbody>
                    <tr>
                        <td>{{ genre }}</td>
                    </tr>
                </tbody>
                {% endfor %}
            </table>
        </div>
    </div>

    {% endblock %}
</body>

</html>