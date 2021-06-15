from contract import Contract
import pickle

question = "Enter the name of the sales associate or q to quit: "
mainmenu = "\nMain Menu:\nA)dd calculations to an existing file\nL)oad a file and view results\nP)rint current results\nR)eset and perform new TAR calculations\nS)ave current calculations to a file\nQ)uit:\n"
nofile = "\nThe file doesn't exists\n"
nocalc = "\nThere are no calculations to display\nLoad a file or perform new calculations\n"
defaultFile = 'contractFile'
def validate(vString):
    while True:
        try:
            if int(float(vString)) >=0:
                vString = int(float(vString))
                break
            else:
                vString = input("Non-numeric values are not accepted. Please provide a numeric value:\n")
        except ValueError:
                vString = input("Negative values are not accepted. Please provide a positive value:\n")
    return vString

def getParam():
    N = str(input("What is the name of the business for this contract?\n"))
    B = float(validate(input("What is the monthly advertising budget (b)?\n")))
    S = float(validate(input("What is the agreed Digital Advertising Setup Fee?\n")))
    return N, B, S
   
def printResults(contractList):
    Ff = TR = Cc = 0
    print("**********\n\nThe Results of Total Revenue and Commission Calculations\n\n**********")
    print("{:20}{:30}{:20}{:20}{:20}{:20}{:20}".format("Associate", "Business", "Budget", "Setup Fee", "Mgmt Fee", "Annual Revenue","Commission"))

    for row in contractList:
        print(row)
        Ff += row.F()
        TR += row.TAR()
        Cc += row.C()

    print("**********\n")
    print("\nThe total monthly management fee is (f) = ${0:.2f}.".format(Ff))
    print("The total annual revenue for all the projects is (TAR) = ${0:.2f}.".format(TR))
    print("The total commission to all the sales associates is (c) = ${0:.2f}.".format(Cc))

def ask_info(contractList):
    print(question)
    putInfo = input()
    while (putInfo.lower() != "q"):
        N, B, S = getParam()
        newContract = Contract(putInfo, N, B, S)
        contractList.append(newContract)
        print(question)
        putInfo = input()
    printResults(contractList)

def load_data(fileName='contractList'):
    contractList = []
    with open(fileName, 'rb') as fp:
        contractList = pickle.load(fp)
    return contractList

def store_data(contractList,fileName='contractList'):
    with open(fileName, 'wb') as fp:
        pickle.dump(contractList, fp)

def main():
    print('Sales and Sales Associate Commission Tracker by William Stephens, Abraham Osman and Megan osorio')
    done = False;
    while not done:
        menu = input(mainmenu)
        if menu.lower() == "a":
            try:
                ask_info(contractList)
            except UnboundLocalError:
                print(nocalc)
        elif menu.lower() == "l":
            while True:
                try:
                    fileName = input("Enter a file name. Hit enter for the default file ({}): ".format(defaultFile))
                    if fileName:
                        contractList = load_data(fileName)
                    else:
                        contractList = load_data()
                    if contractList:
                        printResults(contractList)
                except FileNotFoundError:
                    print("Please provide a valid file name.")
        elif menu.lower() == "p":
            try:
                printResults(contractList)
            except UnboundLocalError:
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif menu.lower() == "r":
            contractList = []
            ask_info(contractList)
        elif menu.lower() == "s":
            try:
                fileName = input("Enter a file name. Hit enter for the default file ({}): ".format(default_file))
                if fileName:
                    store_data(contractList, fileName)
                else:
                    store_data(contractList)
            except UnboundLocalError:
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif menu.lower() == "q":
            done = True

if __name__ == '__main__':
    main()

