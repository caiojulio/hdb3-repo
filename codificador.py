def codificador_hdb3(bits):

    #Informações para montar gráfico
    sinal = [] #polaridade dos pulsos (1 para cima, -1 para baixo, 0 para representar ausência de pulso)
    rotulos = [] #Lista destinada a guarda rótulo de cada pulso (B, V ou None)
    c_zeros = 0 #Variavel destinada a registrar sequências de zeros 

    pulsos = 0 #variavel para armazenar quantidade de pulsos
    polaridade_atual = -1 #variavel destinada a armazenar o ultimo valor de polaridade do pulso de bit

    for bit in bits:

        if bit == 1: # analise bit 1
            pulsos += 1
            polaridade_atual *= -1
            sinal.append(polaridade_atual)
            rotulos.append(None)

            c_zeros = 0 # para certificar de que não haverá rotulagem invalida

        else: # analise bit 0
            c_zeros += 1
            if c_zeros == 4: #oportunidade de substituição (B00V, 000V)
                if pulsos % 2 == 0: 
                    sinal[-3:] = [-polaridade_atual, 0, 0, -polaridade_atual]
                    rotulos [ -3:] = ['B', None, None, 'V']
                    polaridade_atual *= -1
                else:
                    sinal[-3:] = [0, 0, 0, polaridade_atual]
                    rotulos[-3:] = [None, None, None, 'V']
                pulsos = 0
                c_zeros = 0

            else:
                sinal.append(0)
                rotulos.append(None)
                
    print(pulsos)
    return sinal, rotulos
