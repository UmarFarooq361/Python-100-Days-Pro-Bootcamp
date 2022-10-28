def titleCase(s1 , s2):
    if s1 == "" or s2 == "":
        return "Invalid input"
    f_name = s1.title()
    l_name = s2.title()
    return f"{f_name} {l_name}"
#calling functions
# output = titleCase("UMER" , "faROoq")

output = titleCase(input("What is your first name ? ") , input("What is your last name ? "))

print(output)

