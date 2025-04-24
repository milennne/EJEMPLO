
def sliding_window_maximum(nums, k):
    #SI LA LISTA ESTA VACIA O K ES MENOR O IGUAL A 0 O K ES MAYOR QUE LA LONGITUD DE LA LISTA, RETORNA UNA LISTA VACIA
    if not nums or k <= 0 or k > len(nums):
        return [] #NO HAY NINGUN "MAXIMO"/VENTANA QUE RETORNAR

    result = [] #AQUI VAMOS A GUARDAR LOS MÁXIMO DE CADA VENTANA
    deque = [] #AQUI VAMOS A GUARDAR LOS ÍNDICES DE LOS ELEMENTOS EN LA VENTANA (NO LOS VALORES)
    #SON LOS ELEMENTOS CANDIDATOS QUE ESTAN EN LA VENTANA QUE PUEDEN SER EL MÁXIMO.
    for i in range(len(nums)): #RECORRE CADA INDICE DE LA LISLA NUMS.
        
        #MIENTRAS EL DEQUE NO ESTA VACIO Y EL PRIMER INDICE GUARDADO EN EL DEQUE ESTÉ AFUERA DE LA VENTANA ACTUAL, ELIMINA EL PRIMER ÍNDICE DEL DEQUE.
        while deque and deque[0] < i - k + 1:
            deque.pop(0) #SE ENCARGA DE ELIMINAR LOS ÍNDICES QUE ESTAN FUERA DE LA VENTANA (QUE NO SON CANDIDATOS A SER MÁXIMO)
        #    
        while deque and nums[deque[-1]] < nums[i]:
            deque.pop()
        #AGREGA EL INDICE ACTUAL AL DEQUE
        deque.append(i)
        if i >= k - 1:
            result.append(nums[deque[0]])
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximum(nums, k))