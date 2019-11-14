Problema das moedas1
S�o dados os seguintes elementos do dom�nio do problema:

h� 12 moedas de apar�ncia visual id�ntica;
cada uma das 12 moedas est� disposta em uma ordem inicial de apresenta��o;
11 delas tem o mesmo peso;
1 delas tem peso diferente, podendo ser mais leve ou mais pesada;
h� uma balan�a convencional de dois pratos de equil�brio bilateral dispon�vel para uso.
A descri��o geral do que constitui a solu��o autom�tica de uma inst�ncia de problema qualquer no dom�nio apresentado acima significa determinar, com a simula��o de no m�ximo de 3 (tr�s) utiliza��es da balan�a, as seguintes informa��es:

a posi��o inicial da moeda diferente;
o peso relativo da moeda diferente (se � mais leve ou mais pesada).
Implemente um programa em linguagem Prolog capaz de resolver inst�ncias de problema nesse dom�nio. O programa deve computar a solu��o por meio da simula��o de uso da balan�a. A ativa��o do resolvedor deve ocorrer por meio do predicado tern�rio moeda_diferente. Ele deve permitir a instancia��o da posi��o e do peso relativo (�Mais pesada� ou �Mais leve�) da moeda diferente a partir de uma lista din�mica com 12 valores inteiros positivos representando os pesos absolutos de cada uma das 12 moedas.

Para exemplificar o comportamento do predicado moeda_diferente, veja o que segue:

?- moeda_diferente([2,2,2,2,3,2,2,2,2,2,2,2], Posicao, Peso).
Posicao= 5
Peso= Mais pesada ?no
yes


http://www.inf.ufpr.br/alexd/ia/T1_IA_2015_2.pdf (problema adaptado)