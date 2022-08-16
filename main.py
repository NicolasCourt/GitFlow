import json

file_name = 'farmers-protest-tweets-2021-03-5.json'


def one(data):
    lista = []
    for i in data:
        if len(lista) < 10:
            lista.append((i['retweetCount'], i['url']))
            lista = sorted(lista,
                   key=lambda x: x[1])
        else:
            lista.append((i['retweetCount'], i['url']))
            lista = sorted(lista,
                   key=lambda x: x[1])
            lista.pop(0)
    return lista


def two(data):
    lista = []
    for i in data:
        if len(lista) < 10:
            lista.append((i['user']['username'], i['user']['url'], i['user']['statusesCount']))
            sorted(lista,
                   key=lambda x: x[1])
        else:
            lista.append((i['user']['username'], i['user']['url'], i['user']['statusesCount']))
            sorted(lista,
                   key=lambda x: x[1])
            lista.pop(0)
    return lista


def three(data):
    dic = {}
    for i in data:
        if i['date'].split('T')[0] in dic.keys():
            dic[i['date'].split('T')[0]] += 1
        else:
            dic[i['date'].split('T')[0]] = 0
    sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]))
    keys = sorted_dic.keys()[-9:]
    values = sorted_dic.values()[-9:]
    return [(keys[i], values[i]) for i in range(10)]


def four():
    pass


def main():
    file_name = input("Ingrese el nombre del archivo, favor incluir el .json")
    procesed_data = []
    print("cargando archivos porfavor espere")
    for line in open(file_name, 'r'):
        procesed_data.append(json.loads(line))
    exit = False
    while not exit:
        result = ""
        code = int(input("Inserte: \n "
                         "1 para Los top 10 tweets más retweeted. \n "
                         "2 para Los top 10 usuarios en función de la cantidad de tweets que emitieron. \n"
                         "3 para Los top 10 días donde hay más tweets. \n"
                         "4 para Los top 10 hashtags más usados.\n"
                         "5 para SALIR"))

        if code == 1:
            result = one(procesed_data)
        elif code == 2:
            result = two(procesed_data)
        elif code == 3:
            result = three(procesed_data)
        elif code == 4:
            pass
        elif code == 5:
            exit = True
        else:
            print("numero invalido \n")
        print(result)
# Closing file
main()