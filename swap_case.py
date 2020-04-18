def swap_case(s):
    new_output = ""
    for i in s:
        if i.islower():
            new_output = new_output + str(i).upper()
            #new_output.join(s.upper())
        else:
            new_output = new_output + str(i).lower()
    return new_output

if __name__ == '__main__':
    output = input("Type the the text: ")
    print(swap_case(output))
