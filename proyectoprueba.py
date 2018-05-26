#Cuando elegimos el numero 1 o el 5 no funciona, se queda buscando con el valor introducido pero no encuentra nada, no consigo solucionar el error

import json
from pprint import pprint
import requests
from colorama import Back, Style, Fore, init
init(autoreset=True)
#URL de la api https://market.mashape.com/omgvamp/hearthstone
#Para usar el colorama primero hay que instalarlo
contador3=0

print(Style.BRIGHT +"-----------------------------------------------------------")
print(Style.BRIGHT + "------------------- MENÚ DE HEARTHSTONE -------------------")
print(Style.BRIGHT + "-----------------------------------------------------------")
print(Style.BRIGHT + "1.Saber el nombre de las cartas con un coste de maná a elegir")
print(Style.BRIGHT + "2.Saber el puntaje de vida y ataque de una carta")
print(Style.BRIGHT + "3.Saber el nombre de las cartas de un tipo y contarlas")
print(Style.BRIGHT + "4.Saber la expansión a la que pertenece una carta")
print(Style.BRIGHT + "5.Saber el nombre, vida,tipo y coste de las cartas con ataque...")
print(Style.BRIGHT + "6.Sacar el ID y descripcion de las cartas con raza y especialidad")
print(Style.BRIGHT + "7.Salir")
print(Style.BRIGHT + "8.Ver menú principal")
print(" ")
eleccion=int(input("Elige un número, (8 para ver el menú principal): "))
while eleccion != 7:
	if eleccion == 1:
		mana=str(input("Introduce el coste de mana (0-10): "))
		api1 = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards?cost="+mana,
		headers={
		"X-Mashape-Key": "FzegltnIocmsh3211BaWO5zC9HaDp1WHpBSjsn97fHvf0DGNG8"
		}
		)
		data1=api1.json()
		for datos in data1:
			if datos["cost"] == mana:
				print(Fore.BLUE + Style.BRIGHT + "La carta con nombre ", datos["name"])
				print(" ")

	elif eleccion == 2:
		print(Style.BRIGHT + "Cartas recomendadas")
		print(Style.BRIGHT + "-------------------")
		print(Style.BRIGHT + "Avatar of the Coin")
		print(Style.BRIGHT + "Goldshire Footman")
		print(Style.BRIGHT + "Voidwalker")
		print(Style.BRIGHT + "Leokk")
		print(Style.BRIGHT + "Stormwind Knight")
		print(Style.BRIGHT + "Dread Infernal")
		print(Style.BRIGHT + "Gurubashi Berserker")
		print(Style.BRIGHT + "Earth Elemental")
		print(" ")
		carta2=str(input("Introduce el nombre de la carta: "))
		
		api2 = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/search/"+carta2,
		headers={
 		"X-Mashape-Key": "FzegltnIocmsh3211BaWO5zC9HaDp1WHpBSjsn97fHvf0DGNG8"
 		}
		)
		data2=api2.json()
		for datos2 in data2:
			print(Fore.GREEN + Style.BRIGHT + "El ataque de esta carta es: ", datos2["attack"])
			print(Fore.RED + Style.BRIGHT + "La salud de esta carta es: ", datos2["health"])
			break

	elif eleccion == 3:
		print(Style.BRIGHT + "--Tipos--")
		print(Style.BRIGHT + "---------")
		print(Style.BRIGHT + "Hero")
		print(Style.BRIGHT + "Minion")
		print(Style.BRIGHT + "Spell")
		print(Style.BRIGHT + "Enchantament")
		print(Style.BRIGHT + "Weapon")
		print(Style.BRIGHT + "Hero Power")
		print(" ")
		tipo=input("Introduce el tipo de la carta: ")

		api3 = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/types/"+tipo,
		headers={
		"X-Mashape-Key": "FzegltnIocmsh3211BaWO5zC9HaDp1WHpBSjsn97fHvf0DGNG8"
		}
		)
		data3=api3.json()
		for datos3 in data3:
			contador3=contador3+1
			print(Fore.GREEN + Style.BRIGHT + "Su nombre es: ", datos3["name"])
		print(Fore.RED + Style.BRIGHT + "El total de cartas de este tipo son: ", contador3)

	elif eleccion == 4:

		print(Style.BRIGHT + "Cartas recomendadas")
		print(Style.BRIGHT + "-------------------")
		print(Style.BRIGHT + "Air Elemental")
		print(Style.BRIGHT + "Crystalline Oracle")
		print(Style.BRIGHT + "Abusive Sergeant")
		print(Style.BRIGHT + "Argent Squire")
		print(Style.BRIGHT + "Aya Blackpaw")
		print(Style.BRIGHT + "Blessing of Might")
		print(" ")
		carta4=input("Introduce el nombre de una carta: ")

		api4 = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/search/"+carta4,
		headers={
		"X-Mashape-Key": "FzegltnIocmsh3211BaWO5zC9HaDp1WHpBSjsn97fHvf0DGNG8"
		}
		)
		data4=api4.json()
		for datos4 in data4:
			print(Fore.GREEN + Style.BRIGHT + "Su expansion es: ", datos4["faction"])
			print()
	elif eleccion == 5:
		ataque=input("Introduce los puntos de ataque (0-10): ")

		api5 = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards?attack="+ataque,
		headers={
		"X-Mashape-Key": "FzegltnIocmsh3211BaWO5zC9HaDp1WHpBSjsn97fHvf0DGNG8"
		}
		)
		data5=api5.json()
		for datos5 in data5:
			if datos5 == ataque:
				print(Fore.BLUE + Style.BRIGHT + "El nombre es: ", datos5["name"])
				print(Fore.BLUE + Style.BRIGHT + "Su tipo es: ", datos5["type"])
				print(Fore.BLUE + Style.BRIGHT + "Su coste es: ", datos5["cost"])
				print(Fore.BLUE + Style.BRIGHT + "Su salud es: ", datos5["health"])
				print(" ")

	elif eleccion == 6:
		print(" ")
		print(Style.BRIGHT + "Razas")
		print(Style.BRIGHT + "-------------------")
		print(Style.BRIGHT + "Demon")
		print(Style.BRIGHT + "Dragon")
		print(Style.BRIGHT + "Mech")
		print(Style.BRIGHT + "Murloc")
		print(Style.BRIGHT + "Beast")
		print(Style.BRIGHT + "Pirate")
		print(Style.BRIGHT + "Totem")
		print(" ")
		raza=input("Elige una raza: ")

		print(" ")
		print(Style.BRIGHT + "Calidades")
		print(Style.BRIGHT + "-------------------")
		print(Style.BRIGHT + "Free")
		print(Style.BRIGHT + "Common")
		print(Style.BRIGHT + "Rare")
		print(Style.BRIGHT + "Epic")
		print(Style.BRIGHT + "Legendary")
		print(" ")
		calidad=input("Elige la calidad de carta: ")
		api6 = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/races/"+raza,
		headers={
		"X-Mashape-Key": "FzegltnIocmsh3211BaWO5zC9HaDp1WHpBSjsn97fHvf0DGNG8"
		}
		)
		data6=api6.json()
		for datos6 in data6:
			if datos6["rarity"] == calidad:
				print(Fore.BLUE + Style.BRIGHT + "ID de carta: ", datos6["cardId"])
				if "text" in datos6:
					print(Fore.BLUE + Style.BRIGHT + "Descripcion:", datos6["text"])
				else:
					print(Fore.BLUE + Style.BRIGHT + "Sin descripcion")
					break
				print(" ")
			if datos6["rarity"] != calidad:
				print("No existe cartas con estas características")
				break

	elif eleccion == 8:
		print(Style.BRIGHT +"-----------------------------------------------------------")
		print(Style.BRIGHT + "------------------- MENÚ DE HEARTHSTONE -------------------")
		print(Style.BRIGHT + "-----------------------------------------------------------")
		print(Style.BRIGHT + "1.Saber el nombre de las cartas con un coste de maná a elegir")
		print(Style.BRIGHT + "2.Saber el puntaje de vida y ataque de una carta")
		print(Style.BRIGHT + "3.Saber el nombre de las cartas de un tipo y contarlas")
		print(Style.BRIGHT + "4.Saber la expansión a la que pertenece una carta")
		print(Style.BRIGHT + "5.Saber el nombre, vida,tipo y coste de las cartas con ataque...")
		print(Style.BRIGHT + "6.Sacar el ID y descripcion de las cartas con raza y especialidad")
		print(Style.BRIGHT + "7.Salir")
		print(Style.BRIGHT + "8.Ver menú principal")
		print(" ")

	else:
		print(Fore.RED + Style.BRIGHT +"Opción incorrecta, elige un numero del 1 al 8")
		print()
	eleccion=int(input("Elige un número, (8 para ver el menú principal): "))
print(" ")
print(Fore.BLUE + Style.BRIGHT +"Hasta luego, vuelve pronto")
print(" ")
