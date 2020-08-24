def get_HDL_input():
    HDL_input = input("Enter the HDL level: ")
    HDL_value = int(HDL_input)
    return HDL_value

def HDL_analysis(HDL_level):
    if HDL_level > 60:
        return "normal"
    elif 40 <= HDL_level < 60:
        return "Borderline low"
    else:
        return "Low"


def output_result(test_result, analysis):
    print("HDL test result is {}.".format(test_result))
    print("That level is {}.".format(analysis))
    


def HDL():
    test_result = get_HDL_input()
    analysis = HDL_analysis(test_result)
    output_result(test_result, analysis)
    

def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1-HDL Check")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1'"
            HDL()


interface()
