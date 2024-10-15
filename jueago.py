#campo minado

import random

def gera_matriz(n, m):
    matriz = []
    for _ in range(n):
        matriz.append([])
        for _ in range(m):
            matriz[-1].append(0)
    return matriz

def marca_bomba(matriz, n, m):
    bomba = (random.randint(0, n - 1), random.randint(0, m - 1))
    matriz[bomba[0]][bomba[1]] = 9
    return bomba

def marca_minas(matriz, bomba, n, m):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= bomba[0] + i < n and 0 <= bomba[1] + j < m:
                matriz[bomba[0] + i][bomba[1] + j] += 1
            elif bomba[0] + i < 0 or bomba[0] + i >= n or bomba[1] + j < 0 or bomba[1] + j >= m:
                continue
            elif matriz[bomba[0] + i][bomba[1] + j] == 9:
                continue
        for j in range(-1, 2):
            if 0 <= bomba[0] + i < n and 0 <= bomba[1] + j < m:
                matriz[bomba[0] + i][bomba[1] + j] += 1
                if matriz[bomba[0] + i][bomba[1] + j] == 9:
                    continue
                marca_minas(matriz, (bomba[0] + i, bomba[1] + j), n, m)
            elif bomba[0] + i < 0 or bomba[0] + i >= n or bomba[1] + j < 0 or bomba[1] + j >= m:
                continue
            elif matriz[bomba[0] + i][bomba[1] + j] == 9:
                continue
            elif matriz[bomba[0] + i][bomba[1] + j] > 0:
                continue
        for j in range(-1, 2):
            if 0 <= bomba[0] + i < n and 0 <= bomba[1] + j < m:
                matriz[bomba[0] + i][bomba[1] + j] += 1
                if matriz[bomba[0] + i][bomba[1] + j] == 9:
                    continue
                marca_minas(matriz, (bomba[0] + i, bomba[1] + j), n, m)
            elif bomba[0] + i < 0 or bomba[0] + i >= n or bomba[1] + j < 0 or bomba[1] + j >= m:
                continue
            elif matriz[bomba[0] + i][bomba[1] + j] == 9:
                continue
            elif matriz[bomba[0] + i][bomba[1] + j] > 0:
                continue
            elif matriz[bomba[0] + i][bomba[1] + j] == 0:
                matriz[bomba[0] + i][bomba[1] + j] = -1
                marca_minas(matriz, (bomba[0] + i, bomba[1] + j), n, m)
    return matriz

def imprime_matriz(matriz, n, m):
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 9:
                print("B", end=" ")
            elif matriz[i][j] == 0:
                print(".", end=" ")
            elif matriz[i][j] > 0:
                print(matriz[i][j], end=" ")
        print()

def jogar_campo_minado(n, m):
    matriz = gera_matriz(n, m)
    bomba = marca_bomba(matriz, n, m)
    matriz = marca_minas(matriz, bomba, n, m)
    imprime_matriz(matriz, n, m)
    print()
    
    while True:
        x, y = map(int, input("Digite as coordenadas (linha, coluna): ").split())
        if 0 <= x < n and 0 <= y < m:
            if matriz[x][y] == 9:
                print("Você acertou uma bomba!")
                break
            elif matriz[x][y] == 0:
                matriz[x][y] = -1
                marca_minas(matriz, (x, y), n, m)
                imprime_matriz(matriz, n, m)
                print()
            else:
                imprime_matriz(matriz, n, m)
                print()
        else:
            print("Coordenadas inválidas!")

jogar_campo_minado(5, 5)