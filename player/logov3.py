import cmd, sys
from turtle import *

from time import *



#import pygame
#pygame.init()
#from pygame.mixer import Sound

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

#variavel do auto assist
asst = False

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

#cria proxy pro Blobfinder
#b = BlobfinderProxy(c,0)


###############################################################################
######################PROGRAMA PRINCIPAL######################################
###############################################################################

class Logo(cmd.Cmd):
    intro = 'Bem Vindo ao Logo-like interpretador.   Tecle help ou ? para listar os comandos.\n'
    prompt = '(%) '
    file = None

    #funcao 'andar para frente' do robo
    def do_para_frente(self,arg):
        if arg == "":
            print "No arguments!!"
            espeak.synth("Comando invalido")
        else:     
            'Move o robo para frente por uma distancia especifica: PARA_FRENTE 10'
            audio = pygame.mixer.Sound("/home/carloscrbs/fx_stepStair.wav")
            t = parse(arg)
            espeak.synth('Para Frente %d'%t)
            for i in range(0,*parse(arg)):
                c.Read()
                print p.GetStall()
                p.SetSpeed(1,0)
                audio.play()
                sleep(.5)
                #print 'stall: %d \n' % p.GetStall()
            p.SetSpeed(0,0)
    
    #funcao 'andar para tras' do robo
    def do_para_tras(self,arg):
        if arg == "":
            print "No arguments!!"
            espeak.synth("Comando invalido")
        else:
            'Move o robo para tras por uma distancia especifica: PARA_TRAS 10'
            audio = pygame.mixer.Sound("/home/carloscrbs/fx_stepStair.wav")
            t = parse(arg)
            espeak.synth('Para Tras %d'%t)
            for i in range(0, *parse(arg)):
                p.SetSpeed(-1,0)
                audio.play()
                sleep(.5)
            p.SetSpeed(0,0)

    #funcao 'virar X graus para a direita' do robo
    def do_para_direita(self,arg):
        if arg == "":
            print "No arguments!!"
            espeak.synth("Comando invalido")
        else:
            'Vira o robo para a direita por um dado numero de graus:  PARA_DIREITA 20'
            audio = pygame.mixer.Sound("/home/carloscrbs/fx_stepStair.wav")
            t = parse(arg)
            espeak.synth('Para Direita %d graus'%t)
            for i in range(0, *parse(arg)):
                p.SetSpeed(0,  -10.0 * math.pi / 180.0)
                sleep(0.1)
            p.SetSpeed(0,0)

    #funcao 'virar X graus para a esquerda' do robo
    def do_para_esquerda(self,arg):
        if arg == "":
            print "No arguments!!"
            espeak.synth("Comando invalido")
        else:
            'Vira o robo para a esquerda por um dado numero de graus: PARA_ESQUERDA 20'
            t = parse(arg)
            espeak.synth('Para Esquerda %d graus'%t)
            for i in range(0,*parse(arg)):
                p.SetSpeed(0,  10.0 * math.pi / 180.0)
                sleep(.1)
            p.SetSpeed(0,0)

  
    def do_get_info(self,arg):
        
        numblob = b.GetCount()
        centreR = (b.GetWidth()/2)*1.25
        centreL = (b.GetWidth()/2)*0.75

        for i in range(0,numblob):
           blob = b[i]

           if blob.color == '#FFA500':
               espeak.synth('Existe um orange em frente')
           else:
               espeak.synth('Existe um dark blue em frente')

           if blob.x > centreR:
               espeak.synth('a direita')
           elif blob.x < centreL:
               espeak.synth('a esquerda')

           espeak.synth('do robo')

    def do_auto_assist(self,arg):
        
        if arg == '1':
            asst = True
            print "Auto assistencia ATIVADA"
            espeak.synth("Auto assistencia ATIVADA")
        elif arg == '0':
            asst = False
            print "Auto assistencia DESATIVADA"
            espeak.synth("Auto assistencia DESATIVADA")
        else:
            print "Comando invalido"
            espeak.synth("Comando invalido")

    do_auto = do_auto_assist
    do_info = do_get_info
    do_pf = do_para_frente  
    do_pt = do_para_tras 
    do_pd = do_para_direita
    do_pe = do_para_esquerda
    do_f = do_para_frente 
    do_t = do_para_tras 
    do_d = do_para_direita
    do_e = do_para_esquerda

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))



if __name__ == '__main__':
    Logo().cmdloop()
