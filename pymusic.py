from decimal import *
import winsound
getcontext().prec = 100
pi = str(Decimal(22) / Decimal(7))
for j in pi:
    if j == '.':
        winsound.Beep(415, 200)
    else:
        winsound.Beep(int(j)*150, int(j)*100)
        print(pi)
        print(int(j)*200)
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
