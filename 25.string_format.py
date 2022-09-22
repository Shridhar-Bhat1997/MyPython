# str.format() --> optional method that gives users more control when displaying output...

animal="tiger"
item="sun"

print("The "+animal+" jumped over the "+item)

print("The {} jumped over the {}".format("cow","moon"))

# {} acts as a placeholder for the variable or the value.

name="Rome"

print("Hello, my name is {}".format(name))

print("Hello, my name is {:10},Nice to meet you".format(name))

number=3.1437899
print("The number pi is {:.3f}".format(number))

number2=76
print("The binary number is {:b}".format(number2))
print("The octal number is {:o}".format(number2))
print("The hexadecimal number is {:X}".format(number2))





