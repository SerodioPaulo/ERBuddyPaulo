import st7565
import xglcd_font as font

neato = font.XglcdFont('/home/pi/Pi-ST7565/fonts/Neato5x7.c', 5, 7) #5, 7 refers to the pixel size of each character. This file must exist
glcd = st7565.Glcd(rgb=[21, 20, 16]) #Don't change these numbers
glcd.init()

glcd.draw_string('abcdefghijklmnopqrstu', neato, 0, 0, spacing=1)
glcd.draw_string('ABCDEFGHIJKLMNOPQRSTU', neato, 0, 8, spacing=1)
glcd.draw_string('0123456789,.;/[]!@#$%', neato, 0, 16, spacing=1)

glcd.draw_string('abcdefghijklmnopqrstu', neato, 0, 24,spacing=1,invert=1)
glcd.flip()

