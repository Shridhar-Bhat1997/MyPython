# python interpreter sets "special variables", one of which is __name__
# python will assign the __name__ variable a value of '__main__' if its
# initial module being run


def main():
    print("Hello! world")

if __name__=='__main__':
    main()
   