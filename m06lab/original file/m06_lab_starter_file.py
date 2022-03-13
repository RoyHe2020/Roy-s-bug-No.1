# M06 Lab Starter File

def main():
    total = 0.0
    number = 0.0
    counter = 0
    
    infile = open('numbers.txt', 'r')

    for line in infile:
        counter = counter + 1
        number = float(line)
        total += number
        
    infile.close()
    average = total / counter
	print('Average: ', average)

# Call the main function.
main()
