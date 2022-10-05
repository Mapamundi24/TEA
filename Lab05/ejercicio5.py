str = "X-DSPAM-Confidence:0.847"
inicio =str.find(":")+1
fin = len(str)
numero = float(str[inicio:fin])
#print(inicio, fin)
#print(str[inicio:fin])
#print(type(str[inicio:fin]))
print(type(numero))

