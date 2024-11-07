import re
import sys
import os

def check_match(filename):
    pattern = r'([0-9]+\.[0-9]+)[x(?-i)]([0-9]+\.[0-9]+)'
    return re.search(pattern, filename)

def rename_file(fmatch, filename, dir_path):
    replaced_portion = fmatch[0].replace('.', ',')
    new_name = filename[:fmatch.span()[0]] + replaced_portion + filename[fmatch.span()[1]:]

    old_path = os.path.join(dir_path, filename)
    new_path = os.path.join(dir_path, new_name)
                
    os.rename(old_path, new_path)

    print(f'[+] Fixed {filename}')

def dim_fix(path):

    try:
        dir = os.fsencode(path)
        changes = 0

        for file in os.listdir(dir):
            filename = os.fsdecode(file)

            fmatch = check_match(filename)
            if fmatch: 
                rename_file(fmatch, filename, path)
                changes +=1
            
        if changes == 0: print("[+] No files to be changed!")
    except FileNotFoundError:
        print(f'[-] Can\'t find provided path: {path}')

def main():
    if len(sys.argv) == 1:
        print("[!] Usage: python3 dim_fixer.py <path>")
        return 
   
    dim_fix(sys.argv[1]) 

if __name__ == "__main__":
    main()