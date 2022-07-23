import math
from gl import Renderer, NewColor, V2
width, height = 1024, 512
rend = Renderer(width, height)

"""
#----Punto----- 
rend.glClearColor(1, 0,0)
rend.glSecondaryColor(0, 0, 1)
rend.glClear() #Poner esto antes de dibujar puntos, porque sino lo borra (o reemplaza más bien)
 """

""" 
#---Window y viewport----
rend.glViewPort(math.floor(width/4), math.floor(height/4), math.floor(width/2), math.floor(height/2))
rend.glClearColor(0, 1, 0)
rend.glClear()
rend.glClearViewPort(NewColor(1, 0, 0))  
"""
#Lineas
# y = mx+b
v1 = V2(0, 250)
v0 = V2(250, 0)
rend.glClear()


vertices_de_poligono_1 = [
    V2(165, 380), V2(185, 360) , V2(180, 330) , V2(207, 345) , V2(233, 330) , V2(230, 360) , V2(250, 380),
    V2(220, 385), V2(205, 410), V2(193, 383)
]
vertices_de_poligono_2 = [
    V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)
]
vertices_de_poligono_3 = [
    V2(377, 249), V2(411, 197), V2(436, 249)
]
vertices_de_poligono_4 = [
    V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52), 
    V2(750, 145), V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230),
    V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180)
]
vertices_de_poligono_5 = [
    V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)

]
color_poligono_1 = NewColor(1, 0, 0)
'''
Para el metodo que use es importante el orden de aqui en adelante

'''
rend.filled_polygon(vertices_de_poligono_4, color_poligono_1, color_poligono_1, [vertices_de_poligono_5])
rend.filled_polygon(vertices_de_poligono_1, color_poligono_1, color_poligono_1)
rend.filled_polygon(vertices_de_poligono_2, color_poligono_1, color_poligono_1)
rend.filled_polygon(vertices_de_poligono_3, color_poligono_1, color_poligono_1)

rend.glFinish('output.bmp')
print('Fin de programa')