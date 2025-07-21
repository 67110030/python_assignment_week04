from utilities import string_operations as so, calculator as cal 
def main():
    
    sample_string = "hello World"
    print("Original String:", sample_string)
    print("Reversed String:", so.reverse_string(sample_string))
    print("Capitalized String:", so.capitalize_string(sample_string))
    print("Lowercase String:", so.lowercase_string(sample_string))
    print("Uppercase String:", so.uppercase_string(sample_string))

    print("Addition:", cal.add(5, 3))
    print("Subtraction:", cal.subtract(10, 4))
    print("Multiplication:", cal.multiply(6, 7))
    print("Division:", cal.divide(8, 2))
main()
    
