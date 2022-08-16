import json

file_name = 'farmers-protest-tweets-2021-03-5.json'
# Opening JSON file
f = open(file_name)
print(f)
# returns JSON object as 
# a dictionary
data = json.load(f)
for i in data:
    print(i)
# Iterating through the json
# list

def one():
    pass

def two():
    pass
def three():
    pass
def four():
    pass
def main():
    exit = False
    while not exit:
        code = int(input("Inserte: \n "
                         "1 para Los top 10 tweets más retweeted. \n "
                         "2 para Los top 10 usuarios en función de la cantidad de tweets que emitieron. \n"
                         "3 para Los top 10 días donde hay más tweets. \n"
                         "4 para Los top 10 hashtags más usados.\n"
                         "5 para SALIR"))

        if code == 1:
            pass
        elif code == 2:
            pass
        elif code == 3:
            pass
        elif code == 4:
            pass
        elif code == 5:
            exit = True
        else:
            print("numero invalido \n")
# Closing file
f.close()