import re

regex = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$',
    flags=re.M
)

senhas = '''
VÁLIDAS
=8M/d<7sZDi4
202*WPM">ulv
9R6>z([3XmlK
\zPj/HZv053?
Tv9y2Y,M%&b2

SEM MINÚSCULAS
2#FG68)2W!Q?
-IS)4/45_LJ9
'2(K;9I}2XJ7
2P>=03QW&1R'
Z90=|S{B45Q.

SEM MINÚSCULAS E NÚMEROS
(<O&L:^}XGQF
+GH^\^S}R~LN
{FH&_/}FOMW-
^[EI#^ECNL'@
G;!;B@I>C~PX

SEM NÚMEROS CARACTERES E MINÚSCULAS
HJPBQURCYFSP
IANQPCLJQQGC
SPOHVHCNQJFN
UXIVPYGEBYPX
PRJJYPKAHRJG

QUANTIDADE INVÁLIDA (6)
m(7lJ5
$c9Js5
0zH|d8
m8D#t5
03ynD^
'''

for i in regex.findall(senhas):
    print(i)
