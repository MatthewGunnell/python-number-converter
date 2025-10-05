# Name: Matthew Gunnell
# Email: mattgunnell05@gmail.com

# This script contains a library of functions for the 
# number_converter.py program.  They allow that program
# to convert between unsigned binary, decimal, octal, 
# hexadecimal, and ascii.


# Converts a number from binary to the
# type the user chooses
# Parameter - number - The number being converted
# Parameter - type - The type being converted
def convertFromBinary( number, type ):
    
    # Binary to Decimal
    if ( type == "decimal" ):
        output = binaryToDecimal( number )
        print( f"{number} ==> {output} " )

    # Binary to Octal
    elif ( type == "octal" ):
        output = binaryToDecimal( number )
        output = decimalToOctal( output )
        print( f"{number} ==> {output} " )

    # Binary to Hexadecimal
    elif ( type == "hexadecimal" ):
        output = binaryToDecimal( number )
        output = decimalToHexadecimal( output )
        print( f"{number} ==> {output} " )

    # Binary to ASCII
    elif ( type == "ascii" ):
        output = binaryToDecimal( number )
        output = decimalToASCII( output )
        print( f"{number} ==> {output} " )

    else:
        print( "Error: Invalid Input" )
        print( "Please try again" )



# Converts a number from decimal to the
# type the user chooses
# Parameter - number - The number being converted
# Parameter - type - The type being converted
def convertFromDecimal( number, type ):
        
    # Decimal to Binary
    if ( type == "binary" ):
        output = decimalToBinary( number )
        print( f"{number} ==> {output} " )

    # Decimal to Octal
    elif ( type == "octal" ):
        output = decimalToOctal( number )
        print( f"{number} ==> {output} " )

    # Decimal to Hexadecimal
    elif ( type == "hexadecimal" ):
        output = decimalToHexadecimal( number )
        print( f"{number} ==> {output} " )

    # Decimal to ASCII
    elif ( type == "ascii" ):
        output = decimalToASCII( number )
        print( f"{number} ==> {output} " )

    else:
        print( "Error: Invalid Input" )
        print( "Please try again" )



# Converts a number from octal to the
# type the user chooses
# Parameter - number - The number being converted
# Parameter - type - The type being converted
def convertFromOctal( number, type ):

    # Octal to Decimal
    if ( type == "decimal" ):
        output = octalToDecimal( number )
        print( f"{number} ==> {output} " )

    # Octal to Binary
    elif ( type == "binary" ):
        output = octalToDecimal( number )
        output = decimalToBinary( output )
        print( f"{number} ==> {output} " )

    # Octal to Hexadecimal
    elif ( type == "hexadecimal" ):
        output = octalToDecimal( number )
        output = decimalToHexadecimal( output )
        print( f"{number} ==> {output} " )

    # Octal to ASCII
    elif ( type == "ascii" ):
        output = octalToDecimal( number )
        output = decimalToASCII( output )
        print( f"{number} ==> {output} " )

    else:
        print( "Error: Invalid Input" )
        print( "Please try again" )



# Converts a number from hexadecimal to the
# type the user chooses
# Parameter - number - The number being converted
# Parameter - type - The type being converted
def convertFromHexadecimal( number, type ):
    
    # Hexadecimal to Decimal
    if ( type == "decimal" ):
        output = hexadecimalToDecimal( number )
        print( f"{number} ==> {output} " )

    # HexaDecimal to Binary
    elif ( type == "binary" ):
        output = hexadecimalToDecimal( number )
        output = decimalToBinary( output )
        print( f"{number} ==> {output} " )

    # Hexadecimal to Octal
    elif ( type == "octal" ):
        output = hexadecimalToDecimal( number )
        output = decimalToOctal( output )
        print( f"{number} ==> {output} " )

    # Hexadecimal to ASCII
    elif ( type == "ascii" ):
        output = hexadecimalToDecimal( number )
        output = decimalToASCII( output )
        print( f"{number} ==> {output} " )

    else:
        print( "Error: Invalid Input" )
        print( "Please try again" )



# Converts a number from ascii to the
# type the user chooses
# Parameter - number - The number being converted
# Parameter - type - The type being converted
def convertFromASCII( number, type ):
        
    # ASCII to Decimal
    if ( type == "decimal" ):
        output = asciiToDecimal( number )
        print( f"{number} ==> {output} " )

    # ASCII to Binary
    elif ( type == "binary" ):
        output = asciiToDecimal( number )
        output = decimalToBinary( output )
        print( f"{number} ==> {output} " )

    # ASCII to Octal
    elif ( type == "octal" ):
        output = asciiToDecimal( number )
        output = decimalToOctal( output )
        print( f"{number} ==> {output} " )

    # ASCII to Hexadecimal
    elif ( type == "hexadecimal" ):
        output = asciiToDecimal( number )
        output = decimalToHexadecimal( output )
        print( f"{number} ==> {output} " )

    else:
        print( "Error: Invalid Input" )
        print( "Please try again" )



# This function can be used to convert from
# binary to decimal
# Parameter: binaryNumber - The number in binary
# Returns: decimal - The binary number in decimal
def binaryToDecimal( binaryNumber ):

    decimal = int( str( binaryNumber ), 2 )

    return decimal



# This function can be used to convert from
# octal to decimal
# Parameter: octalNumber - The number in octal
# Returns: decimal - The octal number in decimal
def octalToDecimal( octalNumber ):

    decimal = int( str( octalNumber ), 8 )

    return decimal



# This function can be used to convert from
# hexadecimal to decimal
# Parameter: hexadecimalNumber - The number in hexadecimal
# Returns: decimal - The hexadecimal number in decimal
def hexadecimalToDecimal( hexadecimalNumber ):

    decimal = int( str( hexadecimalNumber ), 16 )

    return decimal



# This function can be used to convert from
# ascii to decimal
# Parameter: asciiNumber - The number in ascii
# Returns: decimal - The ascii number in decimal
def asciiToDecimal( asciiNumber ):

    decimal = ord( asciiNumber )

    return decimal



# This function can be used to convert from
# decimal to binary
# Parameter: decimalNumber - The number in decimal
# Returns: binary - The decimal number in binary
def decimalToBinary( decimalNumber ):

    binary = bin( int( decimalNumber ) )

    return binary



# This function can be used to convert from
# decimal to octal
# Parameter: decimalNumber - The number in decimal
# Returns: octal - The decimal number in octal
def decimalToOctal( decimalNumber ):

    octal = oct( int( decimalNumber ) )

    return octal



# This function can be used to convert from
# decimal to hexadecimal
# Parameter: decimalNumber - The number in decimal
# Returns: hexadecimal - The decimal number in hexadecimal
def decimalToHexadecimal( decimalNumber ):

    hexadecimal = hex( int( decimalNumber ) )

    return hexadecimal



# This function can be used to convert from
# decimal to ascii
# Parameter: decimalNumber - The number in decimal
# Returns: ascii - The decimal number in ASCII
def decimalToASCII( decimalNumber ):

    ascii = str( chr( int( decimalNumber ) ) )

    return ascii