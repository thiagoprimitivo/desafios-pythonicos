"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def file_to_string(filename):
    #Ler o arquivo
    file = open(filename, "r")

    #Remove as quebras de linhas e espaços
    string_file = file.read().replace('\n', '').replace(' ', '')

    #Coloca todo o texto em minúsculo
    words_lower = string_file.lower()

    #Ordena em ordem alfabética
    return sorted(words_lower)

def create_dictionary(words):
    word_to_print = ''
    dictionary = {}
    count = 1

    for w in words:
        if w != word_to_print:
            word_to_print = w
            count = 1
            dictionary[w] = count
        else:
            count += 1
            dictionary[w] = count

    return dictionary


def print_words(filename):

    words = file_to_string(filename) 

    dictionary = create_dictionary(words)

    for d in dictionary:
        print(d, '', dictionary[d])


def print_top(filename):

    words = file_to_string(filename) 

    dictionary = create_dictionary(words)

    dictionary_top = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    for word in dictionary_top: 	
        print(word[0], word[1])

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
