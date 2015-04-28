
import statistics

def Reading_File(n):
 f=open("random_numbers.txt","r")
 SUM=0
 nel=0
 lista=[]
 for i in f:
  SUM=SUM+float(i)
  nel=nel+1
  lista.append(float(i))
  deviation=statistics.stdev(lista)
 close("random_numbers.txt")
 print('la suma de los valores es: ',SUM)
 print('la cantidad de valores es: ,',nel)
 print('El promedio es: ',(SUM/nel))
 print('la desviacion estandard es: ',deviation)

Reading_File("random_numbers.txt")