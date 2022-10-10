# python interpreter sets "special variables", one of which is __name__
# python will assign the __name__ variable a value of '__main__' if its
# initial module being run

import module_one

print(__name__)
print(module_one.__name__)