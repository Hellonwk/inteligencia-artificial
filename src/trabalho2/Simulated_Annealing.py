# Autora: Sabrina Eloise Nawcki 
# Curso: BCC - Inteligencia artificial

import random

class otimizacao:
    def __init__(self):
        self.p = 0
        self.m = 0

        self.acoes = (
            ("p++", "m++"),
            ("p++", "m--"),
            ("p++", "m"  ),
            ("p--", "m++"),
            ("p--", "m--"),
            ("p--", "m"  ),
            ("p"  , "m++"),
            ("p"  , "m--"),
            ("p"  , "m"  )
        )

        self.acoes_validas = []
        self.custo_real = 0
        self.custo = 0

        self.lucro = self.calcula_lucro()
        self.lucro_anterior = 0
        self.estado_inicial()

    def estado_inicial(self):
        self.geraAcoes()

    def calcula_lucro(self):
        return 1000 * self.p + 1800 * self.m

    def valida_acao_teste_objetivo(self, p, m):
        if (p >= 0 and m >= 0):
            if(p <= 40 and m <= 30):
                if((20 * p + 30 * m) <= 1200):
                    return True
        return False

    def teste_objetivo(self):
        if (self.p >= 0 and self.m >= 0):
            if(self.p <= 40 and self.m <= 30):
                if((20 * self.p + 30 * self.m) == 1200):
                    return True
        return False

    def valida_acao(self, acao):
        p = self.p
        m = self.m
        if(acao == ("p++", "m++")):
            p += 1
            m += 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p++", "m--")):
            p += 1
            m -= 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p++", "m"  )):
            p += 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p--", "m++")):
            p -= 1
            m += 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p--", "m--")):
            p -= 1
            m -= 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p--", "m"  )):
            p -= 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p"  , "m++")):
            m += 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p", "m--")):
            m -= 1
            return self.valida_acao_teste_objetivo(p, m)
        if(acao == ("p", "m")):
            return self.valida_acao_teste_objetivo(p, m)

        return False

    def geraAcoes(self):
        acoes = list(self.acoes)

        for acao in self.acoes: #Para toda acao existente
            if not self.valida_acao(acao): #Se o movimento for invalido
                acoes.remove(acao) #Remove a acao de acoes validas
        self.acoes_validas = acoes

    def realiza_acao(self, acao):
        if(acao == ("p++", "m++")):
            self.p += 1
            self.m += 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        if(acao == ("p++", "m--")):
            self.p += 1
            self.m -= 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        if(acao == ("p++", "m"  )):
            self.p += 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        if(acao == ("p--", "m++")):
            self.p -= 1
            self.m += 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        if(acao == ("p--", "m--")):
            self.p -= 1
            self.m -= 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        if(acao == ("p--", "m"  )):
            self.p -= 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        if(acao == ("p"  , "m++")):
            self.m += 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        if(acao == ("p", "m--")):
            self.m -= 1
            self.lucro_anterior = self.lucro
            self.lucro = self.calcula_lucro()
            return
        return

    def acao(self):
        acao_random = random.randrange (0,len(self.acoes_validas))
        self.realiza_acao(self.acoes_validas[acao_random])
        self.custo += 1
        self.custo_real += 1

    def toString(self):
        print("Foram produzidos %d monociclos e %d patinetes" % (self.m, self.p))
        print("O lucro total da empresa foi de %d reais" % self.lucro)

    
def simulated_annealing():
    problem = otimizacao()
    current = [problem]
    while True:
        current[0].acao()
        current[0].geraAcoes()
        if(current[0].teste_objetivo() or len(current[0].acoes_validas) == 0):
            return current


def main():
    estado_final = simulated_annealing()
    print("Utilizando Simulated Annealing:")
    print ("Estado Final:")
    estado_final[0].toString()

if __name__ == '__main__':
	main()

