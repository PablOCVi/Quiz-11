def check_banana(a):
 txt=open("bananas.txt",'r')
 cantidad=0
 for i in txt:
  r=i.lower()#convierte las palabras a letras minusculas
  sub=r.find('banana')#busca la palabra dentro del archivo
  while sub !=-1:
   cantidad=cantidad+1
   sub=r.find('banana',(sub+1))
 return(cantidad)
 close("bananas.txt")

Potatoe=check_banana('banana.txt')
print("la palabra banana aparece ",Potatoe," veces en el archivo")