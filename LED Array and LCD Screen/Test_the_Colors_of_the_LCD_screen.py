import st7565
import time

r = 100
g = 100
b = 0
glcd = st7565.Glcd(rgb=[21, 20, 16])
glcd.init()

while True:
    glcd = set_backlight_color(r,g,b)
    if r == 100 and g == 100: r = 99
    if g == 100 and b == 100: g = 99
    if b == 100 and r == 100: b = 99
    if r == 100 and b > 0 and g == 0: b -= 1
    if r == 100 and  b == 0 and g < 100: g += 1
    if g == 100 and r > 0 and b == 0: r -= 1
    if g == 100 and  r == 0 and b < 100: b += 1
    if b == 100 and g > 0 and r == 0: g -= 1
    if b == 100 and  g == 0 and r < 100: r += 1
