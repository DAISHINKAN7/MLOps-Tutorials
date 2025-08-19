class xenoverse:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Xenoverse!!, How would you like to proceed?
                                1. Press 1 to Sign Up       
                                2. Press 2 to Sign In
                                3. Press 3 to write a post
                                4. Press 4 to message a friend \n""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter youre email here -> ")
        pwd = input("Enter youre password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input('Enter your email/username here -> ')
            pwd = input("Enter youre password here -> ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully !!")
                self.loggedIn = True
            else:
                print("Input correct credentials..")
        
        print("\n")
        self.menu()

obj = xenoverse()
