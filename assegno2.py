indirizzo_IP = input ("Dammi un indirizzo IPv4 (A.B.C.D): ")

#######CONTROLLO SE CI SONO CARATTERI DIVERSI DA (0,..,9)##############

numeri = '123456789.'

for i in indirizzo_IP:

    if i not in numeri:
    
        print("Errore!!! E' stato inserito un carattere non idoneo!!")
        
        indirizzo_IP = input ("Dammi un nuovo indirizzo IPv4 (A.B.C.D): ")
        
        i=0 
        
#######CONTO QUANTI PUNTI CI SONO NELL'INDIRIZZO INSERITO#######
count = 0

for i in indirizzo_IP:
    
    if i in '.':
        
        count = count + 1
        
######SEPARO LE 4 PARTI CHE FORMANO L'INDIRIZZO###########
x = indirizzo_IP.split(".")

######TRASFORMO LE 4 PARTI DA STRINGHE A INTERI######
for i in range(count+1):
    
    x[i] = int(x[i])
    
######MI DICHIATO UNA VARIABILE A 1 CHE USERO' COME VARIABILE DI CONTROLLO#########    
y = 1

######IN UN CICLO FOR ESEGUE I VARI CONTROLLI#######
for i in range(count+1):

    if count != 3:
    
        print("Errore: l'indirizzo non è nella forma A.B.C.D")
        
        y = 0
        
        break
    
    elif ((x[i]>255) | (x[i]<0)):
        
        print("Errore: è stato inserito un numero non compreso fra 0 e 255")
        
        y = 0
        
        break
    
    elif (indirizzo_IP == numeri):
    
        print ("Errore: è stato inserito un carattero incorretto!")
        
        y = 0
        
        break

#######CON LA FUNZIONE FORMAT TRASFORMO L'INDIRIZZO IN BINARIO#####
if (y != 0):
    
    print("Rappresentazioni dell'indirizzo in Binario su 32 bit: ")
    
    print(format(x[0],'b'),format(x[1],'b'),format(x[2],'b'),format(x[3],'b'), sep ="")
    
    

    
