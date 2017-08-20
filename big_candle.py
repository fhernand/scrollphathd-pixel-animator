
#!/usr/bin/env python

import time
import math
import ast

import scrollphathd

fh = open( "big_candle.js", "r" )

x = fh.read()
fh.close()

y = ast.literal_eval(x)

list = []
for s in y:
	list.append(s.splitlines())

def candle(i , j, step):
    return float(list[step][i][j])

scrollphathd.set_brightness(0.4)
timestep = 0
while True:
    if timestep == 176:
      timestep = 0
 
    timestep = timestep + 1

    for x in range(0, scrollphathd.DISPLAY_WIDTH):
        for y in range(2, scrollphathd.DISPLAY_HEIGHT + 2):
            v = candle(x, y, timestep)
            scrollphathd.pixel(x+ 2, y-2, max(0,v/10))

    time.sleep(0.001)
    scrollphathd.show()

