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
            
        elif cmd == "echo":
            print(arguments[5:])
            
        elif cmd == "type":
            if commands[1] in ["echo", "exit", "type"]:
                print(f"{commands[1]} is a shell builtin")
            else:
                print(f"{commands[1]}: not found")
                
        else:
            print(f"{cmd}: command not found")
        
        
    


if __name__ == "__main__":
    main()
