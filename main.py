from codificador import codificador_hdb3
from plotter import plotagem

"""
Definição HDB3:

É uma família de códigos semelhante ao AMI, porém evita 
longas sequências de zeros. 
Sequências de mais de “n”(nesse caso, 3) bits nulos sucessivos são substituídos 
por uma marca de violação ("V"),

A regra regra de codificação do HDB3 é substituir toda a
sequência de quatro zeros consecutivos pela sequência
B00V ou 000V, onde B é um pulso em conformidade com a
regra AMI, e V representa um pulso que viola a regra AMI. 
A escolha da sequência B00V ou 000V é feita de tal modo 
que o número de pulsos entre dois pulsos violados 
consecutivos seja sempre impar.
"""

def main():

    # Testando com o conjunto de bits
    conjunto_bits = {
        1: [1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1], # Conjunto de bits da tarefa
        2: [1,1,1,0,1,0,0,1,0,1,0,0,0,0,1,0], #Conjunto de bits da tarefa
        3: [1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    }

    sinal_codificado, rotulos_plot = codificador_hdb3(conjunto_bits[1])
    plotagem(conjunto_bits[1], sinal_codificado, rotulos_plot)

    sinal_codificado, rotulos_plot = codificador_hdb3(conjunto_bits[2])
    plotagem(conjunto_bits[2], sinal_codificado, rotulos_plot)

if __name__ == "__main__":
    main()
