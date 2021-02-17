from time import sleep
from os import listdir
from os import makedirs
from os.path import exists
from os.path import join
from os.path import isfile
from os.path import basename
from shutil import move


extensions_filders = { # add what ext and foldername to move those files to here
    # 'ext': 'myfolder' 
    'py':'python',
    'txt': 'text',
    'mp3': 'music',
    'torrent': 'torrents',
    'mp4': 'video'
}

def shift(name, dirname):
    '''This is moves files shift(name_of_file, folder_name)'''
    check_path = join(dirname,name)
    if name == basename(__file__):
        pass
    elif not exists(check_path) and isfile(name):
        makedirs(dirname,exist_ok=True)    
        move(name, dirname)
        print(f'[MOVED] {name} to {check_path}')
    else:
        print(f'{check_path} File already exists ')


while True:
    '''This will run indefinitely to check files and sleep for 10 seconds'''
    files = listdir()
    for fil in files:
        for key, value in extensions_filders.items():
            if fil.endswith(key):
                shift(fil, value)
            elif isfile(fil):
                shift(fil,'others')

    sleep(10)
