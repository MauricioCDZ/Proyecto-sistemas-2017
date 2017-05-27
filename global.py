##prueba global
globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(2)     # No need for global declaration to read value of globvar

set_globvar_to_one()
print(globvar)
