from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 255, 255 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'script', edges, polygons, transform, screen, color )
#parse_file( 'myscript', edges, polygons, transform, screen, color )
