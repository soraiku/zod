<html>
<head>
<title>Horoscopp</title>
</head>
<body>
	<style>
	#textarea{

		width:200px;
		height: 100px;
	}
	</style>
    <table>
    <tr>
    	<form action="/guestView" method="post">
    		<input type="hidden" name="zod" value="${horoscop}"><br>
    		<input type="hidden" name="frase" value="${frase}"><br>


    	<td><img src="./static/${imatges}"></td>
    	<td> <h1>${horoscop}</h1></td>
	</tr>
    <tr>
    	<td colspan=2>${frase}</td>
    	

    </tr>
    <tr>
    	<td>	Comentari:<br/>
    			<input id="textarea" type="textarea" name="coment" ><br>
    		
				<input type="checkbox" name="confirm" value="ok"/> Vols sortir al nostre guestBook?
				<br />
				<input type="submit" value="Send">
			</form>
    	</td>
    </tr>
    </table>
</body>
</html>
