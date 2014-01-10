<html>
<head>
<title>Horoscopp</title>
</head>
<body>
  <h1>Horoscopo</h1>
  <table>
    <tr>
      % for image in range(imgs):
      <td> <img src="../static/${img[image]}"> </td>
      % endfor
    </tr>
  </table>
  <br/>
  <br/>
  <a href="./zodiac">Realiza tu prediccion para hoy..</a>
</body>
</html>
