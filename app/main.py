import sys
import os
import subprocess


def main():
    while(True):
        try:
            arguments = input("$ ").strip()
        except EOFError:
            break  

        if not arguments:
            continue
        
        commands = arguments.split()
        cmd = commands[0]
        
        path_env = os.environ.get("PATH", "")
        paths = path_env.split(os.pathsep)
        file_in_path = False
        
        for directory in paths:
            full_path = os.path.join(directory, cmd)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                file_in_path = True
                path_of = full_path
                break
            
        if cmd == "exit":
            if len(commands) > 1 and commands[1] == "0":
                break
            else:
                raise SystemExit
            
        elif cmd == "echo":
            print(arguments[5:])
            
        elif cmd == "type":
            if len(commands) < 2:
                print("type: missing argument")
                continue
            
            target = commands[1]

            # 1. Check if builtin
            if target in ["echo", "exit", "type"]:
                print(f"{target} is a shell builtin")
                continue
            
            # 2. Search PATH directories
            path_env = os.environ.get("PATH", "")
            paths = path_env.split(os.pathsep)
            found = False
            
            for directory in paths:
                full_path = os.path.join(directory, target)
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    print(f"{target} is {full_path}")
                    found = True
                    break

            if not found:
                print(f"{target}: not found")
                
        elif file_in_path:
            print(f"Program was passed {len(commands)} args (including program name).")
            arg = 0
            for c in commands:
                if arg == 0:
                    print(f"Arg #{arg} (program name): {c}")
                else:
                    print(f"Arg #{arg}: {c}")
                arg += 1
                
            try:
                result_shell = subprocess.run(commands, capture_output=True, text=True)
                if result_shell.stdout.strip():
                    print(result_shell.stdout.strip())
                if result_shell.stderr.strip():
                    print(result_shell.stderr.strip(), file=sys.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Shell command failed with error: {e}")
            
                
        else:
            print(f"{cmd}: command not found")
        
        
    


if __name__ == "__main__":
    main()
