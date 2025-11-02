import sys



def main():
    while(True):
        arguments = input("$ ")
        commands = arguments.split(" ")
        cmd = commands[0]
            
        if cmd == "exit":
            exit_status = commands[1]
            if(exit_status == "0"):
                break
            else:
                raise
            
        if cmd == "echo":
            print(arguments[5:])
                
        else:
            print(f"{cmd}: command not found")
        
        
    


if __name__ == "__main__":
    main()
