from pathlib import Path
import os
import shutil
#showlist of all items 
def show_list_of_all_items():
    path = Path('')
    items = list(path.iterdir())
    for i,items in enumerate(items):
        if items.is_file():
            print(f'{i+1}. File = {items.name}')
        elif items.is_dir():
            print(f'{i+1}. Folder = {items.name}')


#create a file
def createAfile():
    try:
        show_list_of_all_items()
        name = input('Enter the name of the file: ')
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input('Enter what you want: ')
                fs.write(data)
                print('Your file is created successfully.')
        else:
            print('File is already exists.')
    except Exception as err:
            print(f'An error occured as {err}')

#read a file
def readAfile():
    try:
        show_list_of_all_items()
        name = input('Enter the name of the file: ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
                print('You have readed you file successfully.')
        else:
            print('fILE IS NOT EXISTS.PLEASE CREATE A NEW FILE')
    except Exception as err:
        print(f'An error occured as {err}')

#update a file
def updateAfile(): 
    show_list_of_all_items()
    name = input('Which file do you want to update: ')
    p = Path(name)
    if p.exists() and p.is_file():
        try: 
            print('Enter 1 for rename.')
            print('Enter 2 for overwrite.')
            print('Enter 3 for appending.')

            res = int(input('Enter your response: '))

            if res == 1 :
                name2 = input('Enter the new name of the file: ')
                p2 = Path(name2)
                p.rename(p2)

            elif res == 2:
                with open(p,'w') as fs:
                    data = input('Enter the updated content : ')
                    fs.write(data)
            elif res == 3:
                with open(p,'a') as fs:
                    data = input('What you want to append: ')
                    fs.write(data)
                
            print('Your file is updated successfully.')
        except Exception as err:
            print(f'An error occured as {err}')

#delete a file
def deleteAfile(): 
    try: 
        show_list_of_all_items()
        name = input('Which file do you want to delete: ')
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print('Your file is deleted successfully.')
        else:
            print('File is not existed')
    except Exception as err:
        print(f'An error occurred as {err}')
#create a folder 
def createAfolder():
    try:
        show_list_of_all_items()
        folderName = input('Enter the folder name: ')
        p = Path(folderName)
        if not p.exists():
            os.mkdir(p)
            print('your folder is created successfully.')
        else:
            print('Your folder already existed.')
    except Exception as err:
        print(f'An error occurred as {err}')
#rename a folder 
def renameAfolder():
    try: 
        show_list_of_all_items()
        folderName = input('Which folder do you want to rename: ')
        p = Path(folderName)
        if p.exists() and p.is_dir():
            folderName2 = input('Enter the new folder name : ')
            p2 = Path(folderName2)
            p.rename(p2)
            print('Renamed successfully')
        else:
            print('Your folder does not exist.')
    except Exception as err:
        print(f'An error occurred as {err}')
#delete a folder
def delete_folder():
    try:
        show_list_of_all_items()
        folderName = input('Which folder do you want to delete: ')
        p = Path(folderName)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print('Your folder is deleted successfully.')
        else:
            print('Folder does not exist')
    except Exception as err:
        print(f'An error occurred as {err}')    
        



print('press 1 for create a file.')
print('press 2 for read a file.')
print('press 3 for update a file.')
print('press 4 for delete a file.')
print('press 5 for create a folder.')
print('press 6 for rename a folder.')
print('press 7 for delete a folder.')
 
choice = int(input('Enter the what you want to perform: '))

if choice == 1:
    createAfile()
elif choice == 2:
    readAfile()
elif choice == 3:
    updateAfile()
elif choice == 4:
    deleteAfile()
elif choice == 5:
    createAfolder()
elif choice == 6:
    renameAfolder()
elif choice == 7:
    delete_folder()


