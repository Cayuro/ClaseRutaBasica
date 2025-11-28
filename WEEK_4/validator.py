def valid_only_txt(msg):
    while True:
        txt = input(f"Enter the {msg}")
        if txt.replace(' ','').isalpha():
            return txt
    
def valid_text(msg):
    while True:
        txt : str = input(f"Enter the {msg}")
        if txt.isalnum():
            return txt
        
def valid_num(msg):
    while True:
        try:
            num = int(input(f"Enter the number of {msg}"))
            if 0> num <30:
                return num
        except ValueError:
            print("Only numbers allowed")

