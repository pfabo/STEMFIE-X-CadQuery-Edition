from IPython.display import *
from IPython.display import SVG
from lib import *
import os

def convert_to_image(comp, file_name):
    fp = open(file_name+'.svg', 'w')
    fp.write(comp.obj.toSvg())
    fp.close()
    os.system('magick  -density 1200 ' + file_name + '.svg ' + file_name + '.png ')
    return file_name + '.png'


