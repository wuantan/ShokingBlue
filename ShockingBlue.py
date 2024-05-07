#Diego Velásquez
import random

print("¿Cuantos son en la casa? (1-5): ")
miembros_familia = int(input(""))
while miembros_familia < 1 or miembros_familia > 5:
    print("Ingrese un numero valido: ")
    miembros_familia = int(input(""))

artefactos = {
    "Hervidor": 5.9, 
    "Microondas": 0.8, 
    "Aspiradora": 4.0,
    "Secadora": 2.1,
    }
consumo_total = 0
miembros_refri = miembros_familia
refri = 0
while miembros_familia != 0:
    consumo_familiar_trimestral = 0
    consumo_familiar = 0
    print("El familiar ", miembros_familia , "utiliza")
    artefacto_familiar= random.sample(list(artefactos.keys()), 3)
    consumo_familiar = sum(artefactos[artefacto] for artefacto in artefacto_familiar)
    print(artefacto_familiar)
    consumo_familiar = consumo_familiar + 7.6
    consumo_familiar_trimestral = consumo_familiar*90
    consumo_familiar_trimestral = round(consumo_familiar_trimestral, 2)
    print("Tiene un consumo de: ", consumo_familiar_trimestral ,"Kw en un trimestre.")
    consumo_total = consumo_total + consumo_familiar_trimestral
    miembros_familia = miembros_familia - 1

consumo_total = round(consumo_total)
print("El Consumo total en Kw de la familia durante un trimestre es: ", consumo_total)