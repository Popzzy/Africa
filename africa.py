from sys import stdout, exit

from colorama import AnsiToWin32, init, Fore

init(wrap=False)
stream = AnsiToWin32(stdout).stream

print(Fore.RED, file=stream)
print("Welcome to Africa, a home to diffrent Animals and people.")
print("The are places you can visit are: \n==>")
print("\tEast Africa")
print("\tWest Africa")
print("\tSouth Africa")

def area_1():
	pri = "Welcame to East Africa."
	pri += "20 territories make up Eastern Africa: Tanzania, Kenya, Uganda, Rwanda, Burundi and South Sudan – in Central East Africa"
	pri += "Are amang members of the East African Community."
	pri += "Would you like to visit: \n\tkenya\n\tuganda\n\ttanzania\n\tsomalia\n\tRwanda\n\tSouth sudan"
	print(Fore.CYAN + pri)
	
	choice_1 = input("->> ")

	if choice_1 == "kenya" or choice_1 == "Kenya":
		kenyans = "Welcame to kenya, a home of pride and culture."
		kenyans += "Kenya is a country in East Africa with coastline on the Indian Ocean."
		kenyans += "It encompasses savannah, lakelands, the dramatic Great Rift Valley and mountain highlands."
		kenyans += "It's also home to wildlife like lions, elephants and rhinos."
		kenyans += " From Nairobi, the capital, safaris visit the Maasai Mara Reserve, known for its annual wildebeest migrations and maasai villages"
		kenyans += "Amboseli National pack for Elephant and views of mount kilimajaro."
		kenyans += "Lake nakuru that has Flamingos in the national pack."
		kenyans += "Nairobi is also home to the National Museum, with exhibits spanning native art to natural history, and the roving Maasai Market."
		kenyans += "Beach resorts line the coast around Malindi, whose vibrant coral reefs make Watamu Marine National Park a popular diving area."
		kenyans += "It’s possible to hike or climb 5,199m-tall Mt. Kenya, whose snowy peaks dominate the central highlands."
		print( Fore.YELLOW + kenyans)
		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.GREEN + option)
		ans = input(".=>> ")
		if ans == "yes" or ans == "y":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()

	elif choice_1 == "Uganda" or choice_1 == "uganda":
		ugandans = "Welcame to Uganda, a home of culture and hardwark"
		ugandans += "Uganda is a landlocked country in East Africa whose diverse landscape encompasses the snow-capped Rwenzori Mountains and immense Lake Victoria."
		ugandans += "Its abundant wildlife includes chimpanzees as well as rare birds."
		ugandans += "Remote Bwindi Impenetrable National Park is a renowned mountain gorilla sanctuary."
		ugandans += "Murchison Falls National Park in the northwest is known for 43m-tall waterfall and wildlife such as hippos." 
		ugandans += "There's hiking and climbing in Mount Elgon National Park, whose namesake extinct volcano rises 4,300m above the park's caves and hot springs."
		print(ugandans)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "y":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()

	elif choice_1 == "Tanzania" or choice_1 == "tanzania":
		tanzanian = "Welcame to tanzania, a home of faith and comminissiam"	
		tanzanian += "Tanzania is an East African country known for its vast wilderness areas."
		tanzanian += "They include the plains of Serengeti National Park, a safari mecca populated by the “big five” game (elephant, lion, leopard, buffalo, rhino),"
		tanzanian += " Kilimanjaro National Park, home to Africa’s highest mountain."
		tanzanian += "Offshore lie the tropical islands of Zanzibar, with Arabic influences"
		print(Fore.RED + tanzanian)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()

	elif choice_1 == 'somalia'or choice_1 == 'Somalia':
		somal = "Somalia, officially the Federal Republic of Somalia, is a country located in the Horn of Africa."
		somal += "It is bordered by Ethiopia to the west, Djibouti to the northwest, the Gulf of Aden to the north"
		somal += "the Guardafui Channel and Somali Sea to the east, and Kenya to the southwest."
		somal += "Capital: Mogadishu"
		somal += "Dialing code: +252"
		somal += "President: Mohamed Abdullahi Mohamed"

		print(Fore.LIGHTRED_EX + somal)
		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()


	elif choice_1 == 'Rwanda' or choice_1 == 'rwanda':
		Rwan = "Rwanda, officially the Republic of Rwanda, is a country in Central Africa and one of the smallest countries on the African mainland."
		Rwan += "Located a few degrees south of the Equator"
		Rwan += "Rwanda is bordered by Uganda, Tanzania, Burundi, and the Democratic Republic of the Congo."
		Rwan += "Capital: Kigali"
		Rwan += "Population: 12.21 million (2017) World Bank"
		Rwan += "Currency: Rwandan franc"
		Rwan +=  "President: Paul Kagame."
		print(For.DEEPMAGENTA_EX + Rwan)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()


	elif choice_1 == 'Burundi' or choice_1 == 'burundi':
		brud = "Burundi, officially the Republic of Burundi"
		brud += "is a landlocked country amid the African Great Lakes region where East Africa converge."
		brud += "It is bordered by Rwanda to the north, Tanzania to the east and southeast"
		brud += "the Democratic Republic of the Congo to the west; Lake Tanganyika lies along its southwestern border."
		brud += "Capital: Gitega"
		brud += "President: Pierre Nkurunziza"
		brud += "Population: 10.86 million (2017) World Bank"
		brud += "Currency: Burundian franc"
		brud += "Official languages: French, English, Kirundi."

		print(Fore.BLACK + brud)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()


	elif choice_1 == 'south sudan' or choice_1 == "South sudan":
		south = "South Sudan, officially known as the Republic of South Sudan."
		south += "is a landlocked country in East-Central Africa."
		south += "It gained independence from the Republic of the Sudan in 2011."
		south += "making it the most recent sovereign state with widespread recognition."
		south += "Its capital and largest city is Juba. "
		south += "Capital: Juba"
		south += "President: Salva Kiir Mayardit"
		south += "Currency: South Sudanese pound"
		south += "Recognised national languages: Bari; Dinka; Luo; Murle; Nuer; Zande; and around 60 other languages."
		print(Fore.LIGTHYELLOW_EX + south)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		


		else:
			over("i hope you enjoyed knowing about africa")
			exit()



def area_2():
	print("Welcame to west Africa.")
	print("West Africa is the westernmost region of Africa.")
	print("The United Nations defines Western Africa as the 16 countries.")
	print("Benin, Burkina Faso, Cape Verde, The Gambia, Ghana, Guinea, Guinea-Bissau, Ivory Coast, naigeria")
	print("The population of West Africa is estimated at about 362 million people as of 2016")
	print("The most common west Africa countries are.")
	print("Ghana")
	print("Nigeria")
	print("Ivory coast")
	print("Would like to visit: \nGhana \tNigeria \nIvory coast \tBenin \nBurkina Faso \tCape Verde \nThe Gambia \tGhana \nGuinea \tGuinea-Bissau")

	choice_2 = input("->>")

	if choice_2 == "Ghana" or choice_2 == "ghana":
		ghanns = "Welcame to Ghana"
		ghanns += "Ghana, a nation on West Africa’s Gulf of Guinea, is known for diverse wildlife"
		ghanns += "old forts and secluded beaches, such as at Busua."
		ghanns += "Coastal towns Elmina and Cape Coast contain posubans (native shrines)"
		ghanns += "colonial buildings and castles-turned-museums that serve as testimonials to the slave trade."
		ghanns += "North of Cape Coast, vast Kakum National Park has a"

		print(Fore.LIGHTRED_EX + ghanns)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()


	elif choice_2 == "Nigeria" or choice_2 == "nigeria"	:
		naiga = "Welcame to Nigeria"
		naiga += "Nigeria, an African country on the Gulf of Guinea"
		naiga += "has many natural landmarks and wildlife reserves"
		naiga += "Protected areas such as Cross River National Park and Yankari National Park have waterfalls, dense rainforest, savanna and rare primate habitats."
		naiga += "One of the most recognizable sites is Zuma Rock, a 725m-tall monolith outside the capital of Abuja that’s pictured on the national currency."
		print(Fore.LIGHTGREEN_EX + naiga)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()


	elif choice_2 == "Ivory coast" or choice_2 == "Ivory coast":
		ivory = "Welcame to Ivory coast"
		ivory += "Also called Côte d'Ivoire found in West African."
		ivory += "with beach resorts, rainforests and a French-colonial legacy."
		ivory += "Abidjan, on the Atlantic coast, is the country’s major urban center."
		ivory += "Its modern landmarks include zigguratlike, concrete La Pyramide and St. Paul's Cathedral, a swooping structure tethered to a massive cross."
		ivory += "North of the central business district, Banco National Park is a rainforest preserve with hiking trails"
		print(Fore.LIGHTRED_EX + ivory) 

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")

			exit()

	elif choice_2 == "Benin" or choice_2 == "benin":
		ben = "Benin, a French-speaking West African nation, is a birthplace of the vodun (or “voodoo”) religion."
		ben += "And home to the former Dahomey Kingdom from circa 1600–1900."
		ben += "In Abomey, Dahomey's former capital, the Historical Museum occupies two royal palaces"
		ben += "with bas-reliefs recounting the kingdom’s past and a throne mounted on human skulls."
		ben += "To the north, Pendjari National Park offers safaris with elephants, hippos and lions." 		
		ben += 'capital: Porto-Novo'
		ben += "population: 11.18 million"
		ben += "President: Patrice Talon"

		print(Fore.DEEPBLUE_EX + ben)
		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")

			exit()


	elif choice_2 == ""	



	else:
		over("i hope you enjoyed and learnt alot about Africa")
		exit()

def area_3():
	print("welcame to Southern Africa Countries.")
	print("This are the southernmost region of the African continent,")
	print("comprising the countries of Angola, Botswana,Lesotho, Malawi, Mozambique, Namibia,South Africa, Swaziland, Zambia, and Zimbabwe.")
	print("The island nation of Madagascar is excluded because of its distinct language and cultural heritage.")
	print("would you like to visit:\n\tSouth Africa\n\tZimbabwe\n\tMalawi")

	choice_3 = input("=>> ")

	if choice_3 == "South Africa" or "south africa":
		sA = "Welcame to south Africa"
		sA += "South Africa is a country on the southernmost tip of the African continent,"
		sA += "marked by several distinct ecosystems."
		sA += "Inland safari destination Kruger National Park is populated by big game."
		sA += "The Western Cape offers beaches, lush winelands around Stellenbosch and Paarl,"
		sA += "craggy cliffs at the Cape of Good Hope, forest and lagoons along the Garden Route, and the city of Cape Town, "
		sA += "beneath flat-topped Table Mountain."
		print(sA)

		pop = "\n\tCapitals: Cape Town, Pretoria, Bloemfontein."
		pop += "Dialing code: +27"
		pop += "President: Cyril Ramaphosa"
		pop += "Points of interest: Kruger National Park, Table Mountain"
		print(Fore.LIGHTRED_EX + "pop")
		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)		
		ans = input("=>> ")
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()

	elif choice_3 == "Zimbabwe" or choice_3 == "zimbabwe":
		zim = "Welcame to Zimbabwe" 
		Zim += "Zimbabwe is a landlocked country in southern Africa."
		zim +="Known for its dramatic landscape and diverse wildlife, much of it within parks, reserves and safari areas."
		zim += "On the Zambezi River, Victoria Falls make a thundering 108m drop into narrow Batoka Gorge,"
		zim += "where there’s white-water rafting and bungee-jumping."
		zim += "Downstream are Matusadona and Mana Pools national parks, home to hippos, rhinos and birdlife"
		print(zim)

		print()
		pop = "Capital: Harare"
		pop += "President: Emmerson Mnangagwa"
		pop += "Population: 16.53 million (2017) World Bank"
		pop += "Currencies: United States Dollar, South African rand"
		pop += "Points of interest: Hwange National Park"
		print(pop)

		ans = input("=>> ")

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		if ans == "yes" or ans == "Yes":
			print("which part of africa would you like to visit")
			print("\n\twest africa\n\teast africa\n\tsouth africa")
			place = input("==> ")
			if place == "west africa" or place == "West Africa":
				area_2()

			elif place == "east africa" or place == "East Africa":
				area_1()
			elif place== "south africa" or place == "South Africa":
				area_3()
			elif place == "yes" or place == "y":
				area_1()	

			else:
				over('i hope you learnt alot about Africa .')
				exit()		
		else:
			over("i hope you enjoyed knowing about africa")
			exit()

	elif choice_3 == "Malawi" or choice_3 == "malawi":
		mal = "Malawi, a landlocked country in southeastern Africa,"
		mal += "is defined by its topography of highlands split by the Great Rift Valley and enormous Lake Malawi."
		mal += "The lake’s southern end falls within Lake Malawi National Park –"
		mal += "sheltering diverse wildlife from colorful fish to baboons – and its clear waters are popular for diving and boating."
		mal += "Peninsular Cape Maclear is known for its beach resorts"	
		print(mal)

		print()
		pop = "Capital: Lilongwe"
		pop += "President: Peter Mutharika"
		pop += "Currency: Malawian kwacha"
		pop += "Points of interest: Liwonde National Park, Majete Wildlife Reserve,"
		pop += "Official languages: English, Chewa"
		print(pop)

		option = "\nWould you like to now more about africa(yes/no)"
		print(Fore.BLUE + option)
		answ = input("==> ")
		if answ == "west africa" or answ == "West Africa":
			area_2()

		elif answ == "east africa" or answ == "East Africa":
			area_1()
		elif answ == "south africa" or answ == "South Africa":
			area_3()
		elif answ == "yes" or answ == "y":
			area_1()	

		else:
			over('i hope you learnt alot about Africa .')
			exit()		

	else:
		over("i hope you enjoyed and learnt alot about Africa")
		exit()


def over(reason):

	print(reason,"\nHope you enjoyed")

def Africa_infor():
	print(Fore.MAGENTA + "Africa is a continent that has 54 countries.")
	print ("which part would you like to visit")

	choice = input('=>> ')

	if choice == "East Africa" or choice == 'east africa':
		area_1()

	elif choice == "West Africa" or choice == 'west africa':
		area_2()
	elif choice == "South Africa" or choice == "south africa":
		area_3()
	else:
		print("Hey! you can always try this game same time.")			


Africa_infor()		

