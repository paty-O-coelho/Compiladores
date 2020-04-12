Analisador Léxico 
Links:
•	Vídeo (https://web.microsoftstream.com/video/fa8b9433-641d-43b8-89b4-bf035a82986a)

Como baixar e executar:
•	Requisitos: Anaconda para Python 3.7 (https://www.anaconda.com/distribution/)       
•	Uso a partir do jupyter notebook já incluído com a instalação do Anaconda                       

Descrição:
•	Objetivo: criar um analisador léxico de uma calculadora com impressão em uma tabela de tokens
•	Contexto de uso do programa: o programa funciona de maneira que o usuário, terá de dar a entrada com uma sequência, sendo ela uma expressão aritmética/expressão regular 
•	Funcionamento: o programa apresenta uma entrada para digitação de uma expressão, a partir da digitação dela, se tem a verificação para possíveis erros relacionados a caracteres, caso haja algum tipo de caractere letra, sendo ele maiúsculo ou minúsculo terá a impressão de um erro. Não sendo esse o caso, ele irá remover os excessos de espaços da expressão e adicionar em uma nova lista com uma separação de cada token. A partir disso é informado o que é aceito da expressão, no caso números, parênteses e operações matemáticas, e em seguida são adicionados seus respectivos valores e tipos em diferentes listas. Ao final o programa cria uma tabela, com recebimento de 3 lista sendo elas o Lexema, Tipo e o Valor.
•	Condições: para o funcionamento do programa é necessário que haja sempre um “espaço” entre qualquer sentença
•	Possível falha: O programa não conta com uma tabela dinâmica

Testes:
•	+ 1 * 2
•	+ 5 ** 2 - ( 4 )
•	-5 - -7
•	- ( 8 + 12 ) ** 1 * 3 / -4
•	a 2 + ( 3 – 5 )
•	1 + 2 / b
 
Linguagem, bibliotecas:
•	Linguagem utilizada: Python, pois se trata de uma linguagem simples, boa e de conhecimento dos contribuidores 
•	Bibliotecas: import re, é relacionado a todo tipo de expressão regular no qual foi utilizada para identificação e pesquisa no programa. import pandas, utilizada para a execução e visualização da tabela de tokens

Contribuidores:
•	Antônia Patrícia Coelho Sampaio (https://github.com/paty-O-coelho)
•	Matheus Felipe Buffon Falavigna (https://github.com/matheusfalavigna)
