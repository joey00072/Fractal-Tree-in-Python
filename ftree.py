import pygame
from pygame.draw import line	
from math import sin,cos,radians

pygame.init()

HIGHT,WITDH = 700,800

BLACK =(0,0,0)
WHITE =(255,255,255)
BLUE  =(0,0,255)
RED   =(255,0,0)

surface = pygame.display.set_mode((WITDH,HIGHT))


def ftree(pos,length,angle,turn_angle,depth,color,split):
	if depth==0:
		return
	x,y=pos
	new_x= x+ cos(radians(angle))*length 
	new_y= y- sin(radians(angle))*length
	line(surface,color,pos,(int(new_x),int(new_y)))

	new_pos = (new_x,new_y)
	length=0.69*length
	color1=color2=color
	if split:
		color1=BLUE
		color2=RED
	ftree(new_pos, length,(angle+turn_angle), turn_angle, depth-1, color1,False)
	ftree(new_pos, length,(angle-turn_angle), turn_angle, depth-1, color2,False)





RUN = True
turn_angle=0
INIT_POS = (WITDH//2,HIGHT)
while RUN:
	surface.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN=False
	ftree(INIT_POS,200,90,turn_angle,9,WHITE,True)	
	turn_angle+=0.1
	pygame.display.update()