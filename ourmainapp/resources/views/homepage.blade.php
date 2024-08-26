<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello this is blade template</h1>
    <a href="/about">go to about</a>
    <p>a great number is</p>
    <ul style="font-size: 1.5em;">
        @foreach ($x as $y)
            <li>{{ $y }}</li>
        @endforeach
    </ul>
    
    
</body>
</html>