from os import path, system
import platform

def config_archive(database: str, db_config_path: str = 'env', host: str = '127.0.0.1', port: str = '3306', user: str = 'root', passwd: str= '') -> None:
    '''
    This function create an plan archive with all info you need to connect to your DataBase.

    Parameters:
        - db_config_path (str): path where the archive will be created
        - database (str): the database you will connect
        - host (str): host where your database is
        - port (str): the connection port
        - user (str): user you will log in db
        - passwd (str): your user password to log in db 
    '''
    # Verifing what SO is runing this function
    if platform.system() == 'Windows':
        DIR_SEP = '\\'
    else:
        DIR_SEP = '/'
    
    # If the file path not exists
    if not path.isfile(db_config_path):
        pastas = db_config_path.split(DIR_SEP)[:-1]
        directory = '.'
        for pasta in pastas:
            directory += DIR_SEP + pasta
            if not path.isdir(directory):
                system(f'mkdir {directory}') # Creating directorys

        amb_variables = [
            f'HOST={host}', 
            f'PORT={port}', 
            f'USER_DB={user}', 
            f'PASSWD={passwd}', 
            f'DB={database}'
        ]

        # Creating amb variables with all info for connect to db
        with open(db_config_path, 'w', encoding='utf-8') as file:
            for variable in amb_variables:
                file.write(variable + '\n')

config_archive('', './conf/__env')