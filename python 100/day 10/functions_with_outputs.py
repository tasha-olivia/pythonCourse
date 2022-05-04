def format_name(f_name, l_name):
    # DOLCSTINGS: Ways to create litle documentation as you are coding
    """ Takes a first and last name and formats it to return the title case of the name """
    if f_name == "" or l_name == "":
        return "You didn't privide valid input."
    formated_f_name =  f_name.title()
    formated_l_name = l_name.title()
    return  f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name: "), input("What is your last name: ")))

