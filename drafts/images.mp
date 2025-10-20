prologues := 3;
outputtemplate := "%j-%c.png";
outputformat := "png";
outputformatoptions := "format=png dpi=600 antialias=best";

hppp := 0.4;
vppp := 0.4;

def dottedgrid =
  for x = 0 upto 15:
    for y = 0 upto 15:
      drawdot (x*5mm, y * 5mm);
    endfor;
  endfor;
enddef;

beginfig(1)
  mu := 10mm;
  dottedgrid;

  drawarrow (0, 0) -- (8mu, 0);
  drawarrow (0, 0) -- (0, 8mu);
  for d = 1 upto 15:
    draw (d*5mm, -0.5mm) -- (d*5mm, 0.5mm);
    label.bot(decimal d infont defaultfont scaled 0.6pt, (d*5mm, -0.5mm));
    draw (-0.5mm, d*5mm) -- (0.5mm, d*5mm);
    label.lft(decimal d infont defaultfont scaled 0.6pt, (-0.5mm, d*5mm));
  endfor;
endfig;

beginfig(2)
  mu := 10mm;
  dottedgrid;

  drawarrow (0, 4mu) -- (8mu, 4mu);
  drawarrow (4mu, 0) -- (4mu, 8mu);
endfig;

end
