def generate_binary_strings(n, result= ""):


    #Base case
    if len(result) == n:
        print(result)
        return
    
    #Append 'F' to the string and recurse
    generate_binary_strings(n, result + "F")

    #Append 'T' to the string and recurse
    generate_binary_strings(n, result + "T")

generate_binary_strings(4)

