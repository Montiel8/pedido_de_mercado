"""
Name: mercado.py
Author: Arturo Montiel
Created: 
Purpose: Read and display a text file
"""

# Constant for filename
FILE_NAME = 'mercado.txt'

def main ():
    # Catch any exceptions
    try:
        # Open a file for writing
        with open (FILE_NAME, 'w') as mercado_file:

            mercado_file.write (f"Nayeli selling record.\n") 

            item =input("Please enter the item you are looking for: ")

            mercado_file.write(f"The item is: {item}")

            # Get three numbers from the user.
            numberl = int (input ('Enter the number of items you want: '))
            number2 = int (input ('Enter the amount that you are hoping to pay: '))


            # Write the numbers to the file using Fstrings
            mercado_file.write (f' {numberl}\n')
            mercado_file.write (f' {number2}\n')

            # Let the user know it worked
            print ('Data was written to mercado.txt')

    # Let the user know there was trouble
    except:

        print ('There was trouble writing to the file.')

# Call the main function
if __name__ == "__main__":
    main ()