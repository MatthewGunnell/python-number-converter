# Name: Matthew Gunnell
# Email: mattgunnell05@gmail.com

# This program can be used to convert numbers from different 
# bases, including base 2, 8, 10, and 16. It can also be
# used to convert from those number formats to ASCII.

import converter_methods

# Controls the flow of the program.
def main():

    availableTypes = [ "binary", "decimal", "octal", "hexadecimal", "ascii" ]

    print()
    print()

    run_program( availableTypes )




# Performs the main process of the program
# Parameter: types - The available input types.
def run_program( types ):

    UPPER_BOUNDS = len( types )
    LOWER_BOUNDS = 1


    userInput = 0
    while userInput != 999:
        
        # Displays the input types
        print( "Please Select a Number Format to Convert From" )
        display_input_or_output_types( types )

        # Gets the input type from the user
        userInput = get_input_or_output_type_from_user( UPPER_BOUNDS, LOWER_BOUNDS )

        print()
        print()

        # Runs as long as the user doesn't choose to end the program immediately
        if ( userInput != 999 ):

            # Gets the input type from the list of available types
            chosenTypeToConvertFrom = types[ userInput ]

            # Creates a list with the available output types
            outputTypes = types.copy()
            outputTypes.remove( chosenTypeToConvertFrom )

            # Displays the type to convert to
            print( "Please Select a Number Format to Convert To" )
            display_input_or_output_types( outputTypes )
            
            # Gets the menu number corresponding to the output type from the user
            userOutput = get_input_or_output_type_from_user( UPPER_BOUNDS - 1 , LOWER_BOUNDS )

            print()
            print()

            try:
                # Runs as long as the user doesn't choose to end the program
                if ( userOutput != 999 ):
                    
                    # Gets the output type from the list of available types
                    chosenTypeToConvertTo = outputTypes[ userOutput ]
                    
                    # Gets the value of the number the user wants to convert
                    value = get_value_to_convert( chosenTypeToConvertFrom )

                    print()
                    print()

                    print( "Results:" )
                    print( "---------------------------------------------" )
                    print( f"{chosenTypeToConvertFrom.upper()} --> {chosenTypeToConvertTo.upper()}" )
                    print( "---------------------------------------------" )

                    # Runs if the user chooses to convert from binary
                    if ( chosenTypeToConvertFrom == "binary" ):

                        converter_methods.convertFromBinary( value, chosenTypeToConvertTo )

                    # Runs if the user chooses to convert from decimal
                    elif ( chosenTypeToConvertFrom == "decimal" ): 

                        converter_methods.convertFromDecimal( value, chosenTypeToConvertTo )

                    # Runs if the user chooses to convert from octal
                    elif ( chosenTypeToConvertFrom == "octal" ): 

                        converter_methods.convertFromOctal( value, chosenTypeToConvertTo )

                    # Runs if the user chooses to convert from hexadecimal
                    elif ( chosenTypeToConvertFrom == "hexadecimal" ): 

                        converter_methods.convertFromHexadecimal( value, chosenTypeToConvertTo )

                    # Runs if the user chooses to convert from ASCII
                    elif ( chosenTypeToConvertFrom == "ascii" ): 

                        converter_methods.convertFromASCII( value, chosenTypeToConvertTo )
                    
                    else:
                        print( "Error: Invalid Input" )
                        print( "Please try again" )
                
            
                else:
                    print( "Ending program" )
                    print( "Goodbye!" )
                    quit()
                
            except ValueError:
                print( "Error: Invalid Input" )
                print( "Please: Check your input and try again" )
            except OverflowError:
                print( "Error: Inputted Value is Out of range" )
                print( "Please: Check your input and try again" )
            except TypeError:
                print( "Error: Invalid Input" )
                print( "Please: Check your input and try again" )

        else:
            print( "Ending program" )
            print( "Goodbye!" )
            quit()
        
        print()
        print()



# Displays a menu bar with the optional input or 
# the possible output types
# Parameter: types - A list with the available input/output types.
def display_input_or_output_types( types ):

    print( "---------------------------------------------" )
    
    count = 1
    for each in types:
        if ( each == "ascii" ):
            print( f"{count}.)\t{each.upper()}" )
        elif ( each == "binary" ):
            print( f"{count}.)\t{each.capitalize()} (Unsigned)" )
        else:
            print( f"{count}.)\t{each.capitalize()}" )

        count += 1

    print( "999.)\tEnd Program\n" )



# Gets the input type from the user
# Parameter: UPPER_BOUNDS - The upper bounds of the list
# Parameter: LOWER_BOUNDS - The lower bounds of the list
# Returns: chosenType - The input type the user chooses
def get_input_or_output_type_from_user( UPPER_BOUNDS, LOWER_BOUNDS ):

    chosenType = 0

    isValid = False
    while isValid == False:

        try:

            chosenType = int( input( "Please enter: " ) )

            isValid = validate_user_input( chosenType, UPPER_BOUNDS, LOWER_BOUNDS )

            
        except ValueError:
            print( "Error: Please enter a valid integer\n" )
            isValid = False

    if ( chosenType != 999 ):
        chosenType -= 1

    return chosenType



# Gets the value the user wants to convert
# Parameter - chosenType - The type the user
#        wishes to convert from
# Returns - userInput - The value the user enters
def get_value_to_convert( chosenType ):

    print( "Please enter a value in " + chosenType )
    print( "---------------------------------------------" )

    userInput = input( "Enter: " )

    return userInput


    

# Validates user input for the type to convert
# Parameter: input - The type the user inputs
# Parameter: UPPER_BOUNDS - The upper bounds of the list
# Parameter: LOWER_BOUNDS - The lower bounds of the list
# Returns: isValid - Whether or not the input is valid
def validate_user_input( input, UPPER_BOUNDS, LOWER_BOUNDS ):

    if ( input <= UPPER_BOUNDS ) and ( input >= LOWER_BOUNDS ) or ( input == 999 ):
        return True
    else:
        print( "Error: Please enter a valid integer in the correct range\n" )
        return False



# Calls the main function
if __name__ == "__main__":

    main()
