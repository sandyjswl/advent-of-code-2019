
def read_input():
	with open('input_1.txt', 'r') as f:
		content = f.readlines()
	content = [x.strip() for x in content] 
	content = [int(x) for x in content]
	return content


def main():
	inputs = read_input()
	total = 0
	for module in inputs:
		fuel_needed = int((module/3)) - 2
		total = total + fuel_needed

	print(total)


def calculate_fuel(mass):
	fuel_needed = int((mass/3)) - 2
	if fuel_needed<0:
		return 0
	return fuel_needed + calculate_fuel(fuel_needed)	

def second():
	inputs = read_input()
	total = 0
	for module in inputs:
		fuel_needed = 	calculate_fuel(module)
		total = total + fuel_needed
	print(total)	

if __name__ == '__main__':
	second()