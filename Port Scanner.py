import os, socket, requests, datetime, time





#this is good but maybe can be fixed or integrated with another function 
def services():
    message = (
        "Choose a service type:\n"
        "1 = Scan ports for your Address\n"
        "2 = Scan ports for a Specific Adress 'example.com'\n"
    )
    try:
        service_choice = int(input(message +  ">>>"))
        if service_choice in (1, 2):
            return service_choice
        else:
            raise ValueError
    except ValueError:
        print("Invalid Input: Please choose an option from the following")
        return services()



hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
s = socket.socket()
ports_scan_log = 


def scanner(target_IP, port):
    s = socket.socket()
    Result = s.connect_ex((target_IP, port))
    if Result == 0:
        s.close()
        return print(f"port: {port} is open")
    else:
        return print(f"port: {port} is not open")


#main function will contain all the necassary componets for the program to work
    #make sure to include time.sleep and date time to the thing
def main():
    TITLE = """


            

         ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
        |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
        | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
        |  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
        |_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
                                                                            by SANDMAN





    """
    print(TITLE)
    scan = services()
    
    
    
    
    
    
    
    
    
