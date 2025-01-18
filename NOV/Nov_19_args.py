def print_mul_arguments(*args):
    # *args -> List
    for i in args:
        print(i)

def make_pizza(*toppings):
    # *args -> List
    for i in toppings:
        print(i)

print_mul_arguments(1,2,3,4,5,6,"Ahmad")
make_pizza("corn","onion")
