import cmd, sys
from turtle import *

from time import *



import pygame
pygame.init()
from pygame.mixer import Sound

#robo = Turtle()

#robo.up()

import math
from playercpp import *

import subprocess

from espeak import espeak

###################################################################################
#########INICIALICACAO DOS DEVICES DO ROBO#########################################
###################################################################################
espeak.set_voice('pt')
espeak.set_parameter(espeak.Parameter.Rate, 140)

espeak.synth('Ola, Bem Vindo ao Logo interpretador')

var = dict({})

#cria o cliente e conecta
c = PlayerClient('localhost', 6666)

#criando proxy para position2d:0 :)
p = Position2dProxy(c,0)
#pega a geometria do device 
p.RequestGeom()

#cria proxy pro speech:0
s = SpeechProxy(c,0)

#cria proxy pro ranger:0
#r = RangerProxy(c,0)
#r.RequestGeom()



###############################################################################
######################PROGRAMA PRINCIPAL######################################
###############################################################################

class Logo(cmd.Cmd):
    intro = 'Bem Vindo ao Logo-like interpretador.   Tecle help ou ? para listar os comandos.\n'
    prompt = '(%) '
    file = None

    #funcao 'andar para frente' do robo
    def do_para_frente(self,arg):
    	'Move o robo para frente por uma distancia especifica: PARA_FRENTE 10'
    	audio = pygame.mixer.Sound("/home/carloscrbs/fx_stepStair.wav")
        t = parse(arg)
        espeak.synth('Para Frente %d'%t)
        for i in range(0,*parse(arg)):
        	p.SetSpeed(1,0)
        	audio.play()
        	sleep(.5)
        p.SetSpeed(0,0)
    
    def do_para_tras(self,arg):
        'Move o robo para tras por uma distancia especifica: PARA_TRAS 10'
        audio = pygame.mixer.Sound("/home/carloscrbs/fx_stepStair.wav")
        t = parse(arg)
        espeak.synth('Para Tras %d'%t)
        for i in range(0, *parse(arg)):
            p.SetSpeed(-1,0)
            audio.play()
            sleep(.5)
        p.SetSpeed(0,0)

    def do_para_direita(self,arg):
        'Vira o robo para a direita por um dado numero de graus:  PARA_DIREITA 20'
        audio = pygame.mixer.Sound("/home/carloscrbs/fx_stepStair.wav")
        t = parse(arg)
        espeak.synth('Para Direita %d graus'%t)
        for i in range(0, *parse(arg)):
            p.SetSpeed(0,  -10.0 * math.pi / 180.0)
            sleep(0.1)
        p.SetSpeed(0,0)





    do_pf = do_para_frente  
    do_pt = do_para_tras 
    do_pd = do_para_direita


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))



if __name__ == '__main__':
    Logo().cmdloop()
