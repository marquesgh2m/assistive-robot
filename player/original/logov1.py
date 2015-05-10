import cmd, sys
from turtle import *

from time import *



import pygame
pygame.init()
from pygame.mixer import Sound

#robo = Turtle()

#robo.up()

import math
from playerc import *

import subprocess

from espeak import espeak

espeak.set_voice('pt')
espeak.set_parameter(espeak.Parameter.Rate, 140)

espeak.synth('Ola, Bem Vindo ao Logo interpretador')

var = dict({})

#R = subprocess.call(["player", "/usr/local/share/stage/worlds/simple.cfg"], stdout=None)
#r = subprocess.Popen(["player", "/usr/local/share/stage/worlds/simple.cfg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#programa = Popen(['./teste'], stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)


##################################################
# Create a client object
c = playerc_client(None, 'localhost', 6666)
print "** c.connect() **"
print c.connect()

# Connect it

if c.connect() != 0:
     playerc_error_str()

# Create a proxy for position2d:0
p = playerc_position2d(c,0)
if p.subscribe(PLAYERC_OPEN_MODE) != 0:
     playerc_error_str()

# Retrieve the geometry
# if p.get_geom() != 0:
#     raise playerc_error_str()
# print 'Robot size: (%.3f,%.3f)' % (p.size[0], p.size[1])
# print 'Posicao Inicial'
# c.read() == None
# print 'Robot pose: (%.3f,%.3f,%.3f)' % (p.px,p.py,p.pa)

# Create a proxy for speech:0
s = playerc_speech(c,0)
if s.subscribe(PLAYERC_OPEN_MODE) != 0:
     playerc_error_str()

###########################################s.say('Ola, Bem Vindo ao Logo-like interpretador')

#s.say('oi2')

# Create a proxy for laser:0
r = playerc_ranger(c,0)

if r.subscribe(PLAYERC_OPEN_MODE) != 0:
     playerc_error_str()

# Retrieve the geometry
if r.get_geom() != 0:
     playerc_error_str()



#print 'Ranger pose: (%.3f,%.3f,%.3f)' % (l.pose[0],l.pose[1],l.pose[2])

# laserscanstr = 'Partial laser scan: '
# #r.read() == None
# for j in range(0,5):
#     if j >= r.ranges_count:
#         break
#     laserscanstr += '%.3f ' % r.rnges[j]


# print laserscanstr
# print r.max_range
# print r.min_range
# print r.max_angle
# print r.min_angle

# Create a proxy for blobfinder:0
# b = playerc_ranger(c,0)

# if b.subscribe(PLAYERC_OPEN_MODE) != 0:# print laserscanstr
# print r.max_range
# print r.min_range
# print r.max_angle
# print r.min_angle

#     raise playerc_error_str()

# # Retrieve the geometry
# if b.get_geom() != 0:
#     raise playerc_error_str()
# #print 'Ranger pose: (%.3f,%.3f,%.3f)' % (l.pose[0],l.pose[1],l.pose[2])
# blobscanstr = 'Partial blob scan: '
# r.read() == None
#  for j in range(0,5):
#      if j >= r.blobs_count:
#          break
#      blobscanstr += '%.3f ' % r.info[j]
# print blobscanstr
# #print b.blobs_count

#############################################################

class Logo(cmd.Cmd):
    intro = 'Bem Vindo ao Logo-like interpretador.   Tecle help ou ? para listar os comandos.\n'
    prompt = '(%) '
    file = None

    

    # ----- basic commands -----
    def do_para_frente(self, arg):
        'Move o robo para frente por uma distancia especifica:  PARA_FRENTE 10'
        audio = pygame.mixer.Sound("/home/carloscrbs/fx_stepStair.wav")
	#audio.play()
	
	#nome = 'direita'
	
	#s.say('Para Frente')
	t = parse(arg)

	espeak.synth('Para Frente %d'%t)
	#robo.forward(*parse(arg))

	for i in range(0,*parse(arg)):
		if c.read() == None:
    			raise playerc_error_str()
  		p.set_cmd_vel(1.0, 0.0, 0.0, 1)
		audio.play()
		sleep(.5)
        print "getstall:" , p.Stall()
  		#print 'Robot pose: (%.3f,%.3f,%.3f)' % (p.px,p.py,p.pa)

        # Now stop
        p.set_cmd_vel(0.0, 0.0, 0.0, 1)

        # laserscanstr = 'Partial laser scan: '
        # for j in range(0,5):
        #     if j >= r.ranges_count:
        #         break
        #     laserscanstr += '%.3f ' % r.ranges[j]
        # print laserscanstr
        # print r.ranges_count
        # print r.max_range
        # print r.min_range
        # print r.max_angle
        # print r.min_angle
        # print r.frequency

    def do_para_tras(self, arg):
        'Move o robo para tras por uma distancia especifica:  PARA_TRAS 10'

	#audio = pygame.mixer.Sound("/home/carloscrbs/winsounds/audio/Windows Logoff Sound.wav")
	#audio.play()
        #s.say('Para Tras')
	t = parse(arg)

	espeak.synth('Para Tras %d'%t)
	#robo.back(*parse(arg))
	for i in range(0,*parse(arg)):
  		if c.read() == None:
    			raise playerc_error_str()
  		p.set_cmd_vel(-1.0, 0.0, 0.0, 1)
  		#print 'Robot pose: (%.3f,%.3f,%.3f)' % (p.px,p.py,p.pa)

        # Now stop
        p.set_cmd_vel(0.0, 0.0, 0.0, 1)	


    def do_para_direita(self, arg):
        'Vira o robo para a direita por um dado numero de graus:  PARA_DIREITA 20'
	#audio = pygame.mixer.Sound("/home/carloscrbs/winsounds/audio/logout.wav")
	#audio.play()

	#robo.right(*parse(arg))
	#s.say('Para Direita')
	t = parse(arg)

	espeak.synth('Para Direita %d graus'%t)

	for i in range(0,*parse(arg)):
  		if c.read() == None:
    			raise playerc_error_str()
 		p.set_cmd_vel(0.0, 0.0, -10.0 * math.pi / 180.0, 1)
#		p.set_cmd_vel_car(0.5,0.5,20.0 * math.pi / 180.0)
		#print 'Robot pose: (%.3f,%.3f,%.3f)' % (p.px,p.py,p.pa)

        # Now stop
        p.set_cmd_vel(0.0, 0.0, 0.0, 1)


    def do_para_esquerda(self, arg):
        'Vira o robo para a esquerda por um dado numero de graus:  PARA_ESQUERDA 20'
	#audio = pygame.mixer.Sound("/home/carloscrbs/winsounds/audio/Windows Logon Sound.wav")
	#audio.play()

	#robo.left(*parse(arg))
	#s.say('Para Esquerda')

	t = parse(arg)

	espeak.synth('Para Esquerda %d graus'%t)

	for i in range(0,*parse(arg)):
  		if c.read() == None:
    			raise playerc_error_str()
		p.set_cmd_vel(0.0, 0.0, 10.0 * math.pi / 180.0, 1)
		#print 'Robot pose: (%.3f,%.3f,%.3f)' % (p.px,p.py,p.pa)

	   # Now stop
        p.set_cmd_vel(0.0, 0.0, 0.0, 1)


    def do_repita(self, line):
        'Comando laco de recepcao:  REPITA n [ com1 : com2 : com3 ]'
        str1 = line.split('[')
        str2 = str1[1].rstrip(']')
        arg = str1[0]

        for i in range(0,*parse(arg)):
            self.cmdqueue.extend(str2.split(':'))


    def do_faca(self, line):
        'Comando de atribuicao de variavel:  FACA n = x'
        #global var

        str1 = line.split(' = ')

        self.variavel = str1[0]
        self.valor = int(str1[1])

        var_aux = dict({self.variavel : self.valor})
        var.update(var_aux)

        print self.variavel
        print self.valor
        print var


    def do_conteudo(self, arg):
        'Retorna o conteudo de uma variavel:  CONTEUDO x'
        print var.get(arg)


    def do_se(self, line):
        'Comando condicional:  SE [x] [= ! < >] [n] [ com1 : com2: com3 ]'

        str1 = line.split('[')
        str2 = str1[1].rstrip(']')

        str_aux = str1[0].split()

        self.op1 = str_aux[0]

        self.op2 = str_aux[2]

        if var.has_key(self.op2):
            print "SIM"
            self.op2 = var.get(self.op2)
        else:
            print "NAO"
            self.op2 = int(self.op2)
        
        
        self.operacao = str_aux[1] 

        if self.operacao == '=':
            print "IGUAL"
            if var.get(self.op1) == self.op2:
                self.cmdqueue.extend(str2.split(':'))
        elif self.operacao == '!':
            print "DIFERENTE"
            if var.get(self.op1) != self.op2:
                self.cmdqueue.extend(str2.split(':'))
        elif self.operacao == '>':
            print "MAIOR"
            if var.get(self.op1) > self.op2:
                self.cmdqueue.extend(str2.split(':'))
        elif self.operacao == '<':
            print "MENOR"
            if var.get(self.op1) < self.op2:
                self.cmdqueue.extend(str2.split(':'))

        
        print self.op1 
        print self.op2 
        print type(self.op2)
        print self.operacao
        print var.get(self.op1)       


    def do_posicao_x(self, arg):
        'Informa posicao X do robo: POSICAO_X'
        if c.read() == None:
                raise playerc_error_str()

        print 'Posicao X: (%.3f) Angular: (%.3f)' % (p.px,p.pa * 180.0 / math.pi)
	espeak.synth('Posicao X: %d. Posicao Angular: %d graus.'% (p.px, p.pa * 180.0 / math.pi))


    def do_posicao_y(self, arg):
        'Informa posicao Y do robo: POSICAO_Y'
        if c.read() == None:
                raise playerc_error_str()

        print 'Posicao Y: (%.3f) Angular: (%.3f)' % (p.py,p.pa * 180.0 / math.pi)
	espeak.synth('Posicao Y: %d. Posicao Angular: %d graus.'% (p.py, p.pa * 180.0 / math.pi))

    def do_posicao_xy(self, arg):
        'Informa posicao XY do robo: POSICAO_XY'
        if c.read() == None:
                raise playerc_error_str()

        print 'Posicao XY: (%.3f,%.3f) Angular: (%.3f)' % (p.px,p.py,p.pa * 180.0 / math.pi) 
	espeak.synth('Posicao X: %d. Posicao Y: %d. Posicao Angular: %d graus'% (p.px, p.py, p.pa * 180.0 / math.pi))
	  
    def do_posicao_angular(self, arg):
	'Informa posicao ANGULAR do robo: POSICAO_ANGULAR'
        if c.read() == None:
                raise playerc_error_str()

        print 'Posicao Angular: (%.3f)' % (p.pa * 180.0 / math.pi) 
	
	espeak.synth('Posicao Angular: %d graus'% (p.pa * 180.0 / math.pi))
	

    def do_bye(self, arg):
        'Acaba com a execucao do interpretador:  BYE'
        print('Obrigado por usar o Logo-like interpretador')
	    # Clean up
        #self.close()
        #bye()
        p.unsubscribe()
        s.unsubscribe()
        r.unsubscribe()
        c.disconnect()

        return True
    

    # ----- record and playback -----
    def do_gravar(self, arg):
        'Salva os comandos futuros num arquivo:  GRAVAR file.cmd'
        self.file = open(arg, 'w')
    
    def do_ler(self, arg):
        'Le comandos de um arquivo:  LER rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


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

