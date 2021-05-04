import random
import csv
import time
import matplotlib.pyplot as plt

LeidoEx = 0

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        self.jognomes = []
        self.cor = ''
    def golde(self):
        return self.jogadores[random.randint(0, len(self.jogadores)-1)]

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.extimes = []

def jogar(timeA, timeB):
    global LeidoEx
    for t in Times:
        if t.nome == timeA:
            TimeA = t
        if t.nome == timeB:
            TimeB = t
    Agols = random.randint(0, 4)
    Bgols = random.randint(0, 4)
    for i in range(Agols):
        jog = TimeA.golde()
        if TimeB.nome in jog.extimes:
            LeidoEx += 1
            print('LEI DO EX! // ', jog.nome, ' contra ', TimeB.nome )
            time.sleep(3)
        else:
            print('GOOOL DE ', jog.nome, ' contra ', TimeB.nome)
    for i in range(Bgols):
        jog = TimeB.golde()
        if TimeA.nome in jog.extimes:
            LeidoEx += 1
            print('LEI DO EX! // ', jog.nome, ' contra ', TimeA.nome )
            time.sleep(3)
        else:
            print('GOOOL DE ', jog.nome, ' contra ', TimeA.nome)
    print('Placar final\n\n{0:} {1:} x {2:} {3:}'.format(TimeA.nome, Agols, Bgols, TimeB.nome))

jogadores = []
jnames = []
with open('ExTim.txt', 'r', encoding='utf8') as ExTims:
    ET = csv.reader(ExTims)
    for line in ET:
        j = Jogador(line[0])
        n = 0
        while line[n + 1] != '':
            j.extimes.append(line[n+1])
            n += 1
        jogadores.append(j)
        jnames.append(j.nome)
ExTims.close()
Times = []
tnames = []
with open('TimEle.txt', 'r', encoding = 'utf8') as Elencos:
    TimEle = csv.reader(Elencos)
    for line in TimEle:
        t = Time(line[0])
        n = 0
        for i in range(1, 13):
            if i == 12:
                t.cor = line[i]
            else:
                jogador = line[i]
                for j in jogadores:
                    if j.nome == jogador:
                        t.jogadores.append(j)
                        t.jognomes.append(j.nome)
        Times.append(t)
        tnames.append(t.nome)
Elencos.close()

Casas = []
Foras = []
with open('Rodada2.txt', 'r', encoding= 'utf8') as Jogos:
    Rodada = csv.reader(Jogos)
    for line in Rodada:
        c = line[0]
        f = line[1]
        Casas.append(c)
        Foras.append(f)
Jogos.close()

def Abs_Contra():
    #Porcentagem Absoluta de chance de sofrer Lei do Ex
    global Times
    timenomes = []
    porcentagens = []
    cores = []
    for i in range(len(Times)):
        timeA = Times[i]
        timenomes.append(timeA.nome)
        cores.append(timeA.cor)
        LeiExChance = 0
        for j in range(len(Times)):
            if Times[j] != timeA:
                timeB = Times[j]
                for k in timeB.jogadores:
                    if timeA.nome in k.extimes:
                        LeiExChance += 1
        LeiExPct = LeiExChance*100/(19*11)
        porcentagens.append(LeiExPct)
        print('Chances do {0:} sofrer a Lei do Ex: {1:.1f} %'.format(timeA.nome, LeiExPct))
    plt.bar(timenomes, porcentagens, color = cores)
    plt.title('Chances absolutas de sofrer a Lei do Ex')
    plt.xlabel('Times')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Chances')
    for c, d in enumerate(porcentagens):
        plt.text(c-.25, d + .25, s= str(round(d, 1)) + ' %', color = cores[c] )
    plt.show()

def Pon_Contra():
    ##### Porcentagem de chance de sofrer Lei do Ex Levando em conta a posição do Ex Jogador
    global Times
    timenomes = []
    porcentagens = []
    cores = []
    for i in range(len(Times)):
        timeA = Times[i]
        timenomes.append(timeA.nome)
        cores.append(timeA.cor)
        LeiExChance = 0
        for j in range(len(Times)):
            if Times[j] != timeA:
                timeB = Times[j]
                for k in timeB.jogadores:
                    if timeA.nome in k.extimes:
                        l = timeB.jogadores.index(k)
                        if l < 5:
                            LeiExChance += 1
                        elif l >= 5 and l < 9:
                            LeiExChance += 2
                        else:
                            LeiExChance += 3
        LeiExPct = LeiExChance*100/(19*11)
        porcentagens.append(LeiExPct)
        print('Chances do {0:} sofrer a Lei do Ex: {1:.1f} %'.format(timeA.nome, LeiExPct))
    plt.bar(timenomes, porcentagens, color = cores)
    plt.title('Chances ponderadas de sofrer a Lei do Ex.')
    plt.xlabel('Times')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Chances')
    for c, d in enumerate(porcentagens):
        plt.text(c-.5, d + .25, s= str(round(d, 1)) + ' %', color = cores[c] )
    plt.show()


def Sim(timeA, timeB, n):
    #Simula o jogo entre times A e B n vezes e retorna a porcentagem de ocorrências da Lei do Ex
    #Retorna os placares das partidas hipotéticas
    global Times
    LdEs = []
    for i in range(n):
        LeidoEx = 0
        for t in Times:
            if t.nome == timeA:
                TimeA = t
            if t.nome == timeB:
                TimeB = t
        Agols = random.randint(0, 4)
        Bgols = random.randint(0, 4)
        for i in range(Agols):
            jog = TimeA.golde()
            if TimeB.nome in jog.extimes:
                LeidoEx += 1
        for i in range(Bgols):
            jog = TimeB.golde()
            if TimeA.nome in jog.extimes:
                LeidoEx += 1
        print('Placar final\n\n{0:} {1:} x {2:} {3:}'.format(TimeA.nome, Agols, Bgols, TimeB.nome),
              '/n Ocorrências da Lei do Ex: {:}'.format(LeidoEx))
        LdEs.append(LeidoEx)
    pct = 100*sum(LdEs)/n
    print('Probabilidade de ocorrer a Lei do Ex nesta partida: {:.1f} %'.format(pct))

def Sim_noScore(timeA, timeB, n):
    #Simula n partidas entre o timeA e o timeB n vezes e retorna a porcentagem de ocorrência da Lei do Ex
    #Não retorna o placar das partidas hipotéticas
    global Times
    LdEs = []
    for i in range(n):
        LeidoEx = 0
        for t in Times:
            if t.nome == timeA:
                TimeA = t
            if t.nome == timeB:
                TimeB = t
        Agols = random.randint(0, 4)
        Bgols = random.randint(0, 4)
        for i in range(Agols):
            jog = TimeA.golde()
            if TimeB.nome in jog.extimes:
                LeidoEx += 1
        for i in range(Bgols):
            jog = TimeB.golde()
            if TimeA.nome in jog.extimes:
                LeidoEx += 1
        LdEs.append(LeidoEx)
    pct = 100*sum(LdEs)/n
    print('Probabilidade de ocorrer a Lei do Ex nesta partida: {:.1f} %'.format(pct))

def Abs_Favor():
    #Porcentagem de chance de se beneficiar da Lei do Ex
    global Times
    timenomes = []
    porcentagens = []
    cores = []
    for i in range(len(Times)):
        timeA = Times[i]
        timenomes.append(timeA.nome)
        cores.append(timeA.cor)
        LeiExChance = 0
        for j in range(len(Times)):
            if Times[j] != timeA:
                timeB = Times[j]
                for k in timeA.jogadores:
                    if timeB.nome in k.extimes:
                        LeiExChance += 1
        LeiExPct = LeiExChance*100/(19*11)
        porcentagens.append(LeiExPct)
        print('Chances do {0:} se beneficiar da Lei do Ex: {1:.1f} %'.format(timeA.nome, LeiExPct))
    plt.bar(timenomes, porcentagens, color = cores)
    plt.xlabel('Times')
    plt.title('Chances de se beneficiar da Lei do Ex')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Chances')
    for c, d in enumerate(porcentagens):
        plt.text(c-.5, d + .25, s= str(round(d, 1)) + ' %', color = cores[c] )
    plt.show()

def Pon_Favor():
    ##### Porcentagem de chance de se beneficiar da Lei do Ex Posição ON
    global Times
    timenomes = []
    porcentagens = []
    cores = []
    for i in range(len(Times)):
        timeA = Times[i]
        timenomes.append(timeA.nome)
        cores.append(timeA.cor)
        LeiExChance = 0
        for j in range(len(Times)):
            if Times[j] != timeA:
                timeB = Times[j]
                for k in timeA.jogadores:
                    if timeB.nome in k.extimes:
                        l = timeA.jogadores.index(k)
                        if l < 5:
                            LeiExChance += 1
                        elif l >= 5 and l < 9:
                            LeiExChance += 2
                        else:
                            LeiExChance += 3
        LeiExPct = LeiExChance*100/(19*11)
        porcentagens.append(LeiExPct)
        print('Chances do {0:} se beneficiar da Lei do Ex: {1:.1f} %'.format(timeA.nome, LeiExPct))
    plt.bar(timenomes, porcentagens, color = cores)
    plt.title('Chances ponderadas de se beneficiar da Lei do Ex.')
    plt.xlabel('Times')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Chances')
    for c, d in enumerate(porcentagens):
        plt.text(c-.5, d + .25, s= str(round(d, 1)) + ' %', color = cores[c] )
    plt.show()

#print(Casas)
#print(Foras)

def Rodada_Geral():
    global Casas
    global Foras
    global Times
    Confrontos = []
    Probs = []
    cores = []
    for i in range(10):
        ExA = 0
        ExB = 0
        for t in Times:
            if t.nome == Casas[i]:
                timeA = t
        for u in Times:
            if u.nome == Foras[i]:
                timeB = u
        Conf = timeA.nome[:3].upper() + ' x ' + timeB.nome[:3].upper()
        Confrontos.append(Conf)
        cores.append(timeA.cor)
        for j in timeB.jogadores:
            if timeA.nome in j.extimes:
                ExA += 1
        for k in timeA.jogadores:
            if timeB.nome in k.extimes:
                ExB += 1
        prob = 100*(ExA + ExB)/20
        Probs.append(prob)
    print(Confrontos)
    print(Probs)
    plt.bar(Confrontos, Probs, color = cores)
    plt.title('Chances de ocorrer a Lei do Ex.')
    plt.xlabel('Jogos')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Chances')
    for c, d in enumerate(Probs):
        plt.text(c-.5, d + .25, s= str(round(d, 1)) + ' %', color = cores[c] )
    plt.show()

def Rodada_Ponderada():
    global Casas
    global Foras
    global Times
    Confrontos = []
    Probs = []
    cores = []
    for i in range(10):
        ExA = 0
        ExB = 0
        for t in Times:
            if t.nome == Casas[i]:
                timeA = t
        for u in Times:
            if u.nome == Foras[i]:
                timeB = u
        Conf = timeA.nome[:3].upper() + ' x ' + timeB.nome[:3].upper()
        Confrontos.append(Conf)
        cores.append(timeA.cor)
        for j in timeB.jogadores:
            if timeA.nome in j.extimes:
                l = timeB.jogadores.index(j)
                if l < 5:
                    ExA += 1
                elif l >=5 and l < 9:
                    ExA += 2
                else:
                    ExA += 3
        for k in timeA.jogadores:
            if timeB.nome in k.extimes:
                m = timeA.jogadores.index(k)
                if m < 5:
                    ExB += 1
                elif m >=5 and m < 9:
                    ExB += 2
                else:
                    ExB += 3
        prob = 100*(ExA + ExB)/20
        Probs.append(prob)
    print(Confrontos)
    print(Probs)
    plt.bar(Confrontos, Probs, color = cores)
    plt.title('Chances de ocorrer a Lei do Ex.')
    plt.xlabel('Jogos')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Chances')
    for c, d in enumerate(Probs):
        plt.text(c-.5, d + .25, s= str(round(d, 1)) + ' %', color = cores[c] )
    plt.show()

#Abs_Contra()
#Pon_Contra()
#Abs_Favor()
#Pon_Favor()
#Rodada_Geral()
#Rodada_Ponderada()