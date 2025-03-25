def maxmin_select(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    meio = len(arr) // 2

    min_esq, max_esq = maxmin_select(arr[:meio])
    min_dir, max_dir = maxmin_select(arr[meio:])

    menor_valor = min(min_esq, min_dir)
    maior_valor = max(max_esq, max_dir)

    return menor_valor, maior_valor


if __name__ == "__main__":
    lista_exemplo = [3, 1, 7, 9, 2, 8, 10, 4, 6]
    menor, maior = maxmin_select(lista_exemplo)

    print("Lista:", lista_exemplo)
    print("Menor valor: " + str(menor))
    print("Maior valor: " + str(maior))