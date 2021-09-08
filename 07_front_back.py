"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def split_string(s):
    if len(s) % 2 == 0:
        tamanho_frente_s = len(s)/2 
        tamanho_tras_s = len(s)/2
    else:
        tamanho_frente_s = (len(s)/2) + 1
        tamanho_tras_s = len(s)/2 + 1

    return tamanho_frente_s, tamanho_tras_s

def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    tamanho_frente_a, tamanho_tras_a = split_string(a)
    tamanho_frente_b, tamanho_tras_b = split_string(b)

    return ''.join([a[:int(tamanho_frente_a)], b[:int(tamanho_frente_b)], a[int(tamanho_tras_a):], b[int(tamanho_tras_b):]])

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
