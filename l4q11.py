'''  Altere o programa anterior, intercalando 3 vetores de 10 elementos cada'''
def intercalar_vetores(vetor1, vetor2):
    resultado = []
    for index in range(10):
        resultado.append(vetor1[index])
        resultado.append(vetor2[index])
    return resultado


if __name__ == '__main__':
    vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    resultado = intercalar_vetores(vetor1, vetor2)
    print(resultado)