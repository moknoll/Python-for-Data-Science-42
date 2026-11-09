import sys

def building(): 
    """ Function to count occurence of character in arguments"""
    if len(sys.argv) == 1: 
        print("Please provide a string argument")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    text = sys.argv[1]
    
    if not text:
        print("What is the text to count?")
        return
    
    upper_count = 0
    lower_count = 0
    num_count = 0
    punct_count = 0
    space_count = 0

    for i in range(0, len(text)):
        if text[i].isupper():
            upper_count+=1
        elif text[i].islower():
            lower_count+=1
        elif text[i].isnumeric():
            num_count+=1
        elif text[i] in (".", ",", ":"): 
            punct_count+=1
        elif text[i].isspace(): 
            space_count+=1

    total = upper_count + lower_count + num_count + punct_count + space_count
    print(f"The Text contains {total} characters:")
    print(f"{upper_count} upper letters")   
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{num_count} digits")



def main():
    """This is a doctring"""
    building()

if __name__ == "__main__":
    main()