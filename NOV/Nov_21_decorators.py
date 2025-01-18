def add_extra_security(func):
    def wrapper():
        print("1.Before function is called.")
        print("2.Add helmet,gloves,knee guards,license")
        func()
        print("3.After function is called.")
        print("4.Secure driving.Leave all the item.")
    return wrapper()
@add_extra_security
def driving_scooty():
    print("Normal function")
    print("I am driving a scooty.")

@add_extra_security
def drive_ola_scooter():
    print("ola")