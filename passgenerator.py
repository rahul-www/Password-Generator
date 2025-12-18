## A Python base code for Generating Strong Passwords
import random ## import random, string for (generating random characters, and string to borrow letters,digits,punctuations)
import string
def password_generator():## Main Code for Generating passworda
    print("-------Password Generator---------")

   ## Most crucial part of the code "THE POOL"
   ## char_pool is the collection of all the Characters that we need for generating a Strong Password
      ## 1. Letters(string.ascii_letters)
      ## 2. Numbers(string.digits)
      ## 3. symbols(string.punctuations)
    char_pool = string.ascii_letters + string.digits + string.punctuation
    length = int(input("\nEnter the legth of the password:"))## crucial for taking user input for Password length
    password = [] ## Empty list
## Main Loop for generating passwords according to length user provided
## Runs length times
    print("\nPassword: ", end="")
    for i in range(length):
        ## Takes one character at a time form the pool
        char = random.choice(char_pool)
        ## Adds the charcter to the password
        password.append(char)
        ## crucial for gluing the charcters together
        ## We use (join) for this, '' means put notting between them
        generated_password =''.join(password)
        print(generated_password, end="")
    print()
if __name__ == "__main__":  
  password_generator()   
