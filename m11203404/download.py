import gdown
import zipfile
import os

#params
file_id = '1fb7_athHmHgl9j7f_PSj7K69_ixZS7XH'
file_name = '2023ADLHW1_gDrive.zip'

# download from gDrive
gdown.download(f'https://drive.google.com/uc?id={file_id}', quiet=False)

# extract from .zip
print('---unzip file...---')
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall()


# delete .zip file
os.remove(file_name)
print(f'{file_name} had been removed')