# Código Por Armando Cerda
import collections
import re

def menu():
    ans=True
    data = ""
    while ans:
        print ("""
        1. Evaluar TTN
        2. Evaluar APC
        """)
        ans = input("¿Qué gen quieres evaluar? ") 
        if ans=="1": 
          print("\n Evaluando TTN") 
          with open ('ttn.fasta', 'r') as file:  
            data = file.read().replace('\n', '')   # String total de ACTG del Gen. 
          break

        elif ans=="2":
          print("\n Evaluando APC")  
          with open ('apc.fasta', 'r') as file:
            data = file.read().replace('\n', '')   # String total de ACTG del Gen.
          break

        elif ans !="":
          print("\n Not Valid Choice Try again")
    return(data)
            
def evaluacion():
  data=menu()
  longitud = len(data)                               # Total de A,C,T,G en data 
  acidos        = ['A','C','T','G']
  recurr_acidos =  ["(A+A)*","(C+C)*","(T+T)*","(G+G)*"]

  print("\n La cantidad total de ACTG es:",longitud)
  dna = collections.Counter(data)

  print("\n Cantidad presente en el gen de cada ácido núcleico:")
  
  for i in range (0,4):
    acid    = dna[acidos[i]]
    percent = (acid/longitud)*100
    print (" ",acidos[i],"-", acid, "or", "{:.2f}".format(percent), "%" )

  print("\n")

  for i in range (0,4):

    cadena         = recurr_acidos[i]
    recurrencia    = max(re.compile(cadena).findall(data))
    length         = len(recurrencia)
    cantidad       = data.count(recurrencia)

    if length>0:
      print(acidos[i], "tiene series de nucleótidos repetidos consecutivos:")
      print("La cadena más larga es", recurrencia)
      print("Son",length, acidos[i])
      if cantidad == 1:
        print("Aparece", cantidad, "vez en el gen.")
      elif cantidad>1:
        print("Aparece", cantidad, "veces en el gen.")
      print("\n")
    elif length==0:
      print(acidos[i], "no tienetiene series de nucleótidos repetidos consecutivos.")
  evaluacion()

evaluacion()