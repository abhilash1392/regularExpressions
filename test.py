def print_numbers(x):

    try:
        type(x)!='int'
    except:
        for i in range(x):
            print(i)

if __name__=="__main__":
    print_numbers("two")
    print_numbers(40)
