with open("results.txt") as file:
	lines = file.readlines()



string = ""

for i in lines:
	string += i


for i in lines:
	print(i)

all_lines = []
for i in lines:
	all_lines.append(i.split())


#print(all_lines)

list = string.split()

#print(list)
dic_countries = []
number_of_countries = 3

my_dict = {"France":[],"Sweden":[],"Germany":[]};
for country_number in range(number_of_countries):

	#print(list[country_number])



	country = list[country_number]



	for i in range(len(all_lines)):


		if country_number == 0 and i >0:

			my_dict["France"].append((all_lines[i][0], (all_lines[i][3])))

		if country_number == 1 and i >0:
			my_dict["Sweden"].append((all_lines[i][1], (all_lines[i][3])))

		if country_number == 2 and i >0:
			my_dict["Germany"].append((all_lines[i][2], (all_lines[i][3])))




print(my_dict)