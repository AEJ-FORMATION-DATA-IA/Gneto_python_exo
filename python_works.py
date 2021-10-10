

# ARITHMETRIC OPERATIONS
class Operation:
    A = 0
    B = 0

    def set_operands(self, operand1, operand2):
        self.A = operand1
        self.B = operand2

    def addition(self):
        Operation.delay(f'addition of {self.A} and {self.B}')
        return self.A + self.B

    def powerof(self):
        Operation.delay(f'{self.A} power {self.B}')
        return self.A ** self.B

    def multiplication(self):
        Operation.delay(f'multiplication of {self.A} and {self.B}')
        return self.A * self.B

    def division(self):
        if Operation.secure_division(self.A, self.B):
            Operation.delay(f'pure division of {self.A}  by {self.B}')
            return self.A / self.B

    def divise_and_return_int(self):
        if Operation.secure_division(self.A, self.B):
            Operation.delay(f'division int of {self.A} by {self.B}')
            return self.A // self.B

    def modulo(self):
        if Operation.secure_division(self.A, self.B):
            Operation.delay(f'modulo of {self.A} by {self.B}')
            return self.A % self.B

    @staticmethod
    def secure_division(num1, num2):
        try:
            res = num1 / num2
        except ZeroDivisionError:
            print("Division of number 0 is not  allowed ")


    @staticmethod
    def delay(operation):
        print(' ')
        print(operation + ' Program is running')
        loading_dot = ''
        for line in range(6):
            for i in range(12000000):
                pass
            loading_dot += '.'
            print(loading_dot, end="")
        print("", end="\r")
        print("", end="\r")


A = 2
B = 0
op = Operation()
op.set_operands(A, B)

C = op.addition()
print(C)
D = op.multiplication()
print(D)
E = op.powerof()
print(E)
F = op.division()
print(F)
G = op.divise_and_return_int()
print(G)
H = ''
print(" ")
#----------------END OF ARITHMETRIC OPERATIONS


##DCTIONARY CREATION
print("DCTIONARY CREATION")
Operation_dictionary = {}  # init an empty dictionary

Operation_dictionary["C"] = C  # add  data
Operation_dictionary["D"] = D
Operation_dictionary["E"] = E
Operation_dictionary["G"] = G
Operation_dictionary["D"] = 2000  # modifify data
Operation_dictionary.popitem()  # delete the last item

# displaying the current dictionary object
print(Operation_dictionary)

# Display of keys
for key in Operation_dictionary:
    print(f'key {key}')

print(" ")

# Display value
for key in Operation_dictionary:
    print(f'value {Operation_dictionary.get(key)}')

print(" ")

# Display BOTH key/value pair
for key in Operation_dictionary:
    print(f'key/value pair {key}: {Operation_dictionary.get(key)}')

print(" ")
#-----------------END OF DICTIONARY CREATION

### TUPLE CREATION
print("TUPLE CREATION")
tuples = (A, B, C)

print("")
### Warning !!!! tuple cannot be neither modified nor added
#----------------END TUPLE CEATION


# LIST CREATION
print("LIST CREATION")
liste_1 = ["A", "B", "C", "D"]  # init a list_1 with values
liste_2 = [A, B, C, D]
liste_3 = [
    liste_1,
    liste_2
]
liste_1.append("E")  #appendind data
liste_1.append("F")
liste_1.remove("B")
liste_1.pop(liste_1.index("A"))  # remove element A
liste_1.insert(0, "G")  #insert element at position 0

#Print list_1
print(liste_1)

print(" ")

#--------------------END LIST CREATION


# SMALBOT 1

class SmallBot1(Operation):
    response = 0
    counter = 0

    dict_question = {
        1: "Entrez votre premier  (1) Nombre ",
        2: "Entrez votre deuxième (2) Nombre "
    }

    dict_response = {}

    def __init__(self):
        self.op = Operation()  # instance of Operation class

        # super().__init__

    def ask_question(self, i):
        print(SmallBot1.dict_question[i+1])
        self.response = input('>')
        print("")

    def start(self):
        print('''

              # WELCOME TO IGS CHATBOT 1 

              ''')
        while self.counter < 2:
            self.ask_question(self.counter)
            #print(isinstance(self.response, int))
            if self.check_number():
                self.dict_response[self.counter] = self.response
                self.counter = self.counter + 1
                #self.ask_question()
            else:
                if self.counter == 1:
                    print("###Erreur  Votre deuxième (2)  nombre n' est pas un entier ")
                else:
                    self.counter = 0
                    print("###Erreur  Votre premier (1)  nombre n' est pas un entier ")
        else:
            self.op.set_operands(self.dict_response[0], self.dict_response[1])
            print(f'{self.dict_response[0]} + {self.dict_response[1]} = {self.op.addition()}')

    def check_number(self):
        try:
            self.response = int(self.response)
            return True
        except ValueError:
            return False


#SMALLBOT 2
class SmallBot2(Operation):
    response = 0
    counter = 0

    dict_question = {
        1: "Entrez votre premier  (1) Nombre ",
        2: "Entrez votre deuxième (2) Nombre "
    }

    dict_response = {}

    def __init__(self):
        self.op = Operation()  # instance of Operation class

        # super().__init__

    def ask_question(self, i):
        print(SmallBot1.dict_question[i + 1])
        self.response = input('>')
        print("")

    @staticmethod
    def compare_numbers(num1, num2):
        if num1 > num2:
            return 1
        elif num1 == num2:
            return 0
        else:
            return -1

    def start(self):
        print('''
               # WELCOME TO IGS CHATBOT 2
               ''')
        while self.counter < 3:
            self.ask_question(self.counter)
            # print(isinstance(self.response, int))
            if self.check_number():
                self.dict_response[self.counter] = self.response
                self.counter = self.counter + 1
                # self.ask_question()
                if self.counter == 2:
                    self.counter = 3
            else:
                if self.counter == 1:
                    print("###Erreur  Votre deuxième (2)  nombre n' est pas un entier ")
                else:
                    self.counter = 0
                    print("###Erreur  Votre premier (1)  nombre n' est pas un entier ")
        else:
            resp = SmallBot2.compare_numbers(self.dict_response[0], self.dict_response[1])
            self.op.delay(f'comaraison of {self.dict_response[0]} and {self.dict_response[1]}')
            if resp == 1:
                print(f'Le nombre {self.dict_response[0]} est superieur à {self.dict_response[1]} =>  {self.dict_response[0]} > {self.dict_response[1]} :')
            elif resp == -1:
                print(f'Le nombre {self.dict_response[0]} est inferieur à {self.dict_response[1]} =>  {self.dict_response[0]} < {self.dict_response[1]} :')
            else:
                print(f'Le nombre {self.dict_response[0]} est egal à  {self.dict_response[1]} =>  {self.dict_response[0]} = {self.dict_response[1]} :')
            # self.op.set_operands(self.dict_response[0], self.dict_response[1])
            # print(f'{self.dict_response[0]} + {self.dict_response[1]} = {self.op.addition()}')

    def check_number(self):
        try:
            self.response = int(self.response)
            return True
        except ValueError:
            return False


chatbot = SmallBot1()
chatbot2 = SmallBot2()

###################### I M P L E M E N T A T I O N #############################

command = ''

welcome = '''
    ###### WELCOME TO CHATBOX ######
    Choose one program to run         
    Type <1> for  SmallBot1 (addition of  two numbers )
    Type <2> for  SmallBot2 (comparaison of  two numbers )
    -------------------------------
    -------------------------------
    Type <help> for help
    Type <quit> to end the program
'''
while command != 'quit':
    print(welcome)
    command = input('> ')
    if command == '1':
        chatbot.start()
    elif command == '2':
        chatbot2.start()
    elif command == 'help':
        print('''
            ######  CHATBOX  HELP ######
            Choose one program to run         
            Type <1> for  SmallBot1 (addition of two numbers )
            Type <2> for  SmallBot2 (comparaison of  two numbers )
            -------------------------------
            -------------------------------
            Type <help> for help
            Type <quit> to end the program
        ''')
        command = input('> ')
    elif command == 'quit':
        print("Program ended......See you later")

    else:
        print("This command is not recongnized")
        print('''
            Type <help> for getting help
        ''')
        command = input('> ')
else:
    print("Program ended......See you later")


#--------------------- END SMALLBOT
