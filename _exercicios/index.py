valor = "teste"
valor = "{:@>10}".format(valor)
valor = "{:-<20}".format(valor)
#print(valor)

stringi = "loremo ipsumo dolor ipsum"
#print(stringi.count("o"))

maior = 0
letra_m = ""
for letra in stringi:
    conta = stringi.count(letra)
    letra_m = letra
    if conta > maior:
        maior = conta
        letra_m = letra

#print(maior, letra_m)


def func(**kwargs):
    idade = kwargs.get("idade") or "n informda"
    #print (idade)

func(idade=None)
func(idade=False)
func(idade=True)
func(idade="")
func(idade=0)
func(idade="0")
func(idade="24")
func(idade=34)


v = "valor 1"
def func2():
    pass
    global v
    print(v)
    v = "valor 2"
    print(v)

#func2()

lista = ["php",  "js", "java"]
for k, l in enumerate(lista):
    continue
    print(k, l)

dic = {"php":"PHP",  "js":"JS", "java":"JAVA"}
for k, l in dic.items():
    continue
    print(k, l)


from time import time, sleep

def velocidade(funcao: func) -> func:
    def interna(*args, **kwars):
        start = time()
        r = funcao(*args, **kwars)
        end = time()
        tempo = (end - start) * 1000
        print (f"{funcao.__name__} demorou {tempo:.2f}")
        return r
    return interna

@velocidade
def principal():
    sleep(5)

#principal()