prologues := 3;
outputtemplate := "%j-%c.png";
outputformat := "png";
outputformatoptions := "format=png dpi=600 antialias=best";

hppp := 0.4;
vppp := 0.4;

beginfig(1)
  pair vc;
  u := 10mm;
  draw fullcircle scaled 2u;
  draw fullcircle scaled 1pt;

  for angle = 0 step 30 until 330:
    vc := dir(angle);
    draw 0.9*u * vc -- 1.1*u * vc;
  endfor;

  label("12", (0, 1.3u));
  label("3", (1.3u, 0));
  label("6", (0, -1.3u));
  label("9", (-1.3u, 0));
endfig;

end
