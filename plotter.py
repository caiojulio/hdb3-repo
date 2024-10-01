import numpy as np
import matplotlib.pyplot as plt

def plotagem(bits, sinal_codificado, rotulos):
    """
    Plota a codificação HDB3 com base na sequência de bits fornecida e exibe os rótulos 'B' e 'V'.

    Args:
        bits (list): A sequência de bits a ser plotada.
    """
    # Codifica os bits usando a regra HDB3
    
    # Configura o tempo para o gráfico (1 segundo por bit)
    t = np.arange(0, len(sinal_codificado), 0.005)

    # Cria o sinal NRZ-L (nível alto para '1' e nível baixo para '0')
    signal = np.repeat(sinal_codificado, 200)  # Repetimos os valores para cada intervalo de tempo

    # Ajusta o sinal para ser mostrado entre 0 e 1 (para o eixo y)
    signal = (np.array(signal) + 1) / 2  # Converte -1 para 0 e +1 para 1

    # Plota o sinal
    plt.step(t, signal, where='post', linewidth=2)

    # Configurações do gráfico
    plt.ylim(-0.1, 1.5)
    plt.xlim(0, len(bits))  # O eixo x vai de 0 até o número de bits
    plt.title("Codificação HDB3")
    plt.grid(True)

    # Adiciona os bits no topo do gráfico
    for i, bit in enumerate(bits):
        plt.text(i + 0.5, 1.25, str(bit), fontsize=12, ha='center')  # Posiciona os bits acima do gráfico

    # Adiciona os rótulos 'B' e 'V' apenas para os pulsos de conformidade e violação
    for i, rotulo in enumerate(rotulos):
        if rotulo == 'B':  # Se for um pulso de conformidade
            plt.text(i + 0.5, 0.7, 'B', fontsize=12, ha='center', color='green')
        elif rotulo == 'V':  # Se for um pulso de violação
            plt.text(i + 0.5, 0.7, 'V', fontsize=12, ha='center', color='red')

    # Desenha linhas verticais para separar cada bit no gráfico
    for i in range(len(bits)):
        plt.axvline(x=i, color='gray', linestyle='--', linewidth=1)

    # Define os valores do eixo x para representar o tempo em segundos
    plt.xticks(np.arange(0, len(bits)+1, 1), labels=np.arange(0, len(bits)+1, 1))

    # Define os valores do eixo y para serem 0 e 1
    plt.yticks([0, 1], labels=['0', '1'])

    plt.xlabel('Tempo')
    plt.ylabel('Nível do sinal')

    plt.show()