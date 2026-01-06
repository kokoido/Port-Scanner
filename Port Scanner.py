import os, socket




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
    
    
    
    
    
    
    
    
