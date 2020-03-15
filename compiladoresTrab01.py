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
exemplo = '42 + (675 * 31) -20925 + a'
table_of_operations = {'*':'Mutiplicacao', '**':'Potenciacao',
'+':'soma', '-':'subtracao', '/': 'divisao'}

numeros=[]
teste =re.split(r' ', exemplo)
for i in teste:
    if re.search(r'(?i)\d',i,re.I): #um jeito de nao pegar os parenteses
        numeros.append(i)
for i in teste:
    if re.search(r'\(', i):
        numeros.append('PARETESQ') #mudar por uma fun�a� lambda
for i in teste:
    if re.search(r'\)', i):
        numeros.append('PAREDIR') #mudar por uma fun�a� lambda
        
for i in teste:
    if re.findall(r'[a-zA]', i):
        numeros.append('Variavel')
for i in teste:
    if re.findall(r'+ - ')