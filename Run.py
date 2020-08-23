import os
import getpass

addedFiles = []
oldPath = 'Data\\Old\\'
newPath = 'Data\\New\\'
files = ['ProgramFiles.txt', 'ProgramFilesx86.txt', 'ProgramData.txt', 'AppData.txt']
username = getpass.getuser()

def Create_Folders():
    if (not os.path.exists('Data')):
        os.mkdir('Data')
    if (not os.path.exists('Data\\Old')):
        os.mkdir('Data\\Old')
    if (not os.path.exists('Data\\New')):
        os.mkdir('Data\\New')
    

def Get_Old_Files():
    os.system(f'dir /s /b "C:\\Program Files" > {oldPath}{files[0]}')
    os.system(f'dir /s /b "C:\\Program Files (x86)" > {oldPath}{files[1]}')
    os.system(f'dir /s /b "C:\\ProgramData" > {oldPath}{files[2]}')
    os.system(f'dir /s /b "C:\\Users\\{username}\\AppData" > {oldPath}{files[3]}')

def Get_New_Files():
    os.system(f'dir /s /b "C:\\Program Files" > {newPath}{files[0]}')
    os.system(f'dir /s /b "C:\\Program Files (x86)" > {newPath}{files[1]}')
    os.system(f'dir /s /b "C:\\ProgramData" > {newPath}{files[2]}')
    os.system(f'dir /s /b "C:\\Users\\{username}\\AppData" > {newPath}{files[3]}')

def Check_Files():
    for file in files:
        with open(f'{oldPath}{file}', 'rt') as f:
            oldFilesTmp = f.read()
        with open(f'{newPath}{file}', 'rt') as f:
            newFilesTmp = f.read()
            
        newFiles = newFilesTmp.split('\n')
        oldFiles = oldFilesTmp.split('\n')

        for i in range(0,len(newFiles)):
            try:
                oldFiles.index(newFiles[i])
            except:
                addedFiles.append(newFiles[i])
                print('[+] Added: ' + newFiles[i])

    with open('Result.txt', 'w') as f:
        for file in addedFiles:
            f.write(file + '\n')

if __name__=='__main__':
    Create_Folders()
    Get_Old_Files()
    print('[+] Please install the new program!')
    print('Press ENTER keys to continue...')
    input()
    Get_New_Files()
    Check_Files()
    print('\n[+] Done!!!')
    print('Press ENTER keys to continue...')
    input()

    
    
