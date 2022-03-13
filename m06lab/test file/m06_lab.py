#Athor: Ruodong He
#Date: 03/02/2022
#Description: M06 Lab

def main():
    total = 0.0
    number = 0.0
    counter = 0
    filename = "numbers.txt"
    #IOError could occu when opening a file that doean't exist.
    try:
        infile = open(filename, 'r')

        for line in infile:
            counter = counter + 1
            #ValueError could occur when reading data from the file.
            number = float(line)
            total += number
        # Close the file.
        infile.close()
    except IOError:
        print('An error occured trying to read the file', end = ' ')
        print(filename, '.', sep = '')
    except ValueError:
        print('Non-numeric data found in the file', end=' ')
        print(filename, '.', sep = '')
    
    else:    
        #ZeroDivisionError could occur here.
        try:
            average = total / counter
        except ZeroDivisionError:
            # Catch the divide by zero exception.
            print('Cannot divide by zero.\n')
        else:
            print('Average: ', average)
    finally:
        print('Processing complete. No errors detected.')

# Call the main function.
main()
