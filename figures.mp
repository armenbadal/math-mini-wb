prologues := 3;
outputtemplate := "%j-%c.png";
outputformat := "png";
outputformatoptions := "format=gray antialias=best";

beginfig(126)
  u:=5mm;
  pickup pencircle scaled 0.2mm;

  for i=0 step u until 16u:
    draw (i,0)--(i,4u);
  endfor;

  for i=0 step u until 4u:
    draw (0,i)--(16u,i);
  endfor;
endfig;

beginfig(125)
  u:=5mm;

  for i=0 step u until 16u:
    draw (i,0)--(i,8u);
  endfor;

  for i=0 step u until 8u:
    draw (0,i)--(16u,i);
  endfor;
endfig;

end
