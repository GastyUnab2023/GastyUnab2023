#def saludar():
    
   # print("hola gasty como estas")
    
#saludar()
#Crear una funion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "Amor"
    print(f"Hola {nombre} , como estas {adjetivo}")
        
saludar("Abigail","mUJer")
saludar("Gasty","hombre")
saludar("Gustavo","NoBinario")