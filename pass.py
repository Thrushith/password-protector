from cryptography.fernet import Fernet


#enter the password below 
key_pass = "password"


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master = input("Enter the KEY password: ")

key = load_key()
fer = Fernet(key)
if master==key_pass:
    def view():
        with open("passwords.txt", "r") as f:
            for line in f.readlines():   
                data = line.rstrip()
                user,pas = data.split("|")    
                print("user:",user,", password:",fer.decrypt(pas.encode()).decode())
                # user , passw = data.split("|")
                # print("user:",user ,",password:",passw)
    def add():
        name = input("name:")
        passwrd = input("password:")
        with open("passwords.txt", "a") as f:
            f.write(name + "|" + fer.encrypt(passwrd.encode()).decode() + "\n")

    while True:
        mode = input("add value or view value (add,view) if not q to quit: ")
        if mode=="q":
            break
        if mode=="view":
            view()
        elif mode=="add":
            add()
        else:
            print("Invalid")   
            continue
else:
    print("!!!!!!!!Invalid password!!!!!!!!!!")