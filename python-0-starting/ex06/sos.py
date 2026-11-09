import sys 

def translate(): 
    """"This function translates a string into morse code"""
    NESTED_MORSE = {
    'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
    'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
    'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
    'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
    'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
    'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
    'Y': '-.-- ', 'Z': '--.. ',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/ '
    }

    if len(sys.argv) != 2: 
        sys.exit("AssertionError: the arguments are bad")
    try: 
        text = sys.argv[1].upper()
        result = ""

        for i in range(0, len(text)): 
            if text[i] in NESTED_MORSE: 
                result = result + NESTED_MORSE[text[i]]
            else: 
                sys.exit("AssertionError: Value Not found")
    except ValueError: 
        sys.exit("AssertionError: the arguments are bad")
    
    print(result)

def main(): 
    translate()

if __name__=="__main__":
    main()

