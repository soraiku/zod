
<h1>Guest Book</h1>
<p>Horòscop</p>

Created pages:
<ul>
  % for visit in visits:
    <li>${visit.zod} - ${visit.frase} - ${visit.data} - ${visit.coment}</li>
  % endfor
</ul>

