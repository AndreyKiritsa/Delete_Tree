def inputData(): #считывание входных данных
    with open('input.txt') as file:
        count = file.readline()
        slovInput = {}
        slovDel = {}
        for i in range(int(count)):
            line = file.readline().split()
            slovInput[i+1] = line[0] #словарь для узлов верева
            slovDel[int(line[0])] = tuple(line[1::]) #словарь, где ключ - ключ вершины, значения - ссылки на детей вершины
        countDel = file.readline().strip() #количество удаляемых вершин
        numberDel = list(map(int,file.readline().split())) #какие вершины необходимо удалить
    return slovInput, slovDel, countDel, numberDel

def delBranch(dataCheck, dataDel, numberDel):
    result = []
    delMass = []
    vaIndex = []
    for i in numberDel: # поиск всей удаляемой ветки
        if i in dataDel: # есть ли вершина в дереве поиска
            vaIndex.extend(dataDel[i]) #список детей у вершины
            delMass.append(i)   #удаляемые элементы
            while len(vaIndex) != 0:    #подсчёт количества удаляемых рёбер в дереве поиска (подсчёт вседо удалемого дереве, всех его узлов и детей)
                if int(vaIndex[0]) != 0: #если ребёнок у вершины существует
                    ind = dataCheck[int(vaIndex[0])] #удаляемый ребёнок у вершины
                    if int(ind) in dataDel: #существует ли данный узел
                        delMass.append(int(ind)) #добавить элемент для удаления
                        vaIndex.extend(dataDel[int(ind)]) #добавить ссылки на детей удаляемого узла
                    del vaIndex[0] #удалить ссылку на ребёнка узла
                else:
                    del vaIndex[0] #удалить ссылку на ребёнка узла, если она 0
        for j in delMass: #удалить всё дерево подсчитанное в цикле while
            del dataDel[j]
        delMass = [] #очисть массив
        request = str(len(dataDel)) #запись количесво ключей вершин после процесса удаления поддерава
        result.append(request) # запись в массив окончательного результата
    return result

def printData(data): #запись результата
    with open('output.txt', 'w', encoding = 'utf8') as file:
        file.write('\n'.join(data))

def main():
    dataCheck, dataDel, countDel, numberDel = inputData()
    result = delBranch(dataCheck, dataDel, numberDel)
    printData(result)

if __name__ == '__main__':
    main()