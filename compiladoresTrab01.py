""""
Crie um analisador l�xico de uma calculadora. O objetivo ser� criar uma tabela  de tokens e seus tipos:
As opera��es da calculadora s�o: +, -, *, /, ** (potencia��o)
A calculadora deve aceitar n�meros inteiros positivos e negativos
Ser�o aceitos par�nteses
Veja o seguinte exemplo: Sequ�ncia de tokens para o exemplo Exemplo de express�o aritm�tica 42 + (675 * 31) - 20925

O TRABALHO DEVE:
Criar uma tabela de tokens
O analisador l�xico deve realizar tratamentos de erros notificando atrav�s de mensagens o erro l�xico, por exemplo:
A senten�a a2+(3-5) retornaria uma mensagem do tipo: caractere inv�lido.
Voc� pode definir que a senten�a precisa terminar com algum caractere
Opcional: Elimine os coment�rios definidos na sua linguagem
""""

import re 
#delititado por espa�o
exemplo = '42 + ( 675 * 31 ) -20925 + a ** B c D'

table_of_operations = {'*':'Mutiplicacao', '**':'Potenciacao',
'+':'soma', '-':'subtracao', '/': 'divisao'}

#
string=[]
numero=[]
operations=[]
a=[]
teste =re.split(r' ', exemplo)

#aqui estamos usando um regex para encontrar todos os numero (\d)
#e inserir eles na em x1, usando uma fun��o lambda e a filter (abaixo fazemos um cast de filter para list)
x1= filter(lambda i: re.search(r'(?i)\d',i,re.I), teste)
numeros= list(x1)
#usando expressao regular para encontrar o (
x2 =filter(lambda i:re.search(r'\(', i),teste)
x_2=list(x2)

#usando expressao regular para encontrar o (
x3 =filter(lambda i:re.search(r'\)', i),teste)
x_3=list(x3)

x4= filter(lambda i:re.findall(r'[A-Z-a-b]', i),teste)
x_4=list(x4)
 #operacoes       
for i in teste:
    if re.findall(r'[A-Z-a-b]', i):#problema ta no regex
        string.append(i) #ele ta pegando o valor negativo -20925

#DEU PROBLEMA AQUI        
#x5=filter(lambda i:re.findall(r'[+ / * - ** =]',i),exemplo)
#x_5=list(x5)

#AQUI FUNCIONOU DIREITO
for i in teste:
    if re.findall(r'[+ / * - ** =]',i):
        operations.append(i)
   