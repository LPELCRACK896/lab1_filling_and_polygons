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


vertices_de_poligono_1 = [V2(165, 380), V2(185, 360) , V2(180, 330) , V2(207, 345) , V2(233, 330) , V2(230, 360) , V2(250, 380),
                        V2(220, 385), V2(205, 410), V2(193, 383)
]
color_poligono_1 = NewColor(1, 0, 0)

rend.filled_polygon(vertices_de_poligono_1, color_poligono_1, color_poligono_1)

rend.glFinish('output.bmp')
print('Fin de programa')