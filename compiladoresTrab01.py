""""
Crie um analisador léxico de uma calculadora. O objetivo será criar uma tabela  de tokens e seus tipos:
As operações da calculadora são: +, -, *, /, ** (potenciação)
A calculadora deve aceitar números inteiros positivos e negativos
Serão aceitos parênteses
Veja o seguinte exemplo: Sequência de tokens para o exemplo Exemplo de expressão aritmética 42 + (675 * 31) - 20925

O TRABALHO DEVE:
Criar uma tabela de tokens
O analisador léxico deve realizar tratamentos de erros notificando através de mensagens o erro léxico, por exemplo:
A sentença a2+(3-5) retornaria uma mensagem do tipo: caractere inválido.
Você pode definir que a sentença precisa terminar com algum caractere
Opcional: Elimine os comentários definidos na sua linguagem
""""

import re 
#delititado por espaço
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
        numeros.append('PARETESQ') #mudar por uma funçaõ lambda
for i in teste:
    if re.search(r'\)', i):
        numeros.append('PAREDIR') #mudar por uma funçaõ lambda
        
for i in teste:
    if re.findall(r'[a-zA]', i):
        numeros.append('Variavel')
for i in teste:
    if re.findall(r'+ - ')