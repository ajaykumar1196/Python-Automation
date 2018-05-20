'''
@By Ajay Kumar
@Version 1.0

Python Script to organise and move files of same kind on the desktop to same extension folders.
'''

import os

home_path = os.environ.get('HOME')
desktop_path = 'Desktop'

final_path = os.path.join(home_path, desktop_path)

os.chdir(final_path)

for file in os.listdir(final_path):
    file_name, file_extension = os.path.splitext(file)

    if file_extension in ['.pdf', '.doc', '.docx', '.jpg', '.png', '.ppt', '.jpeg', '.py']:
        if not os.path.exists(os.path.join(final_path, file_extension[1:])):
            os.makedirs(os.path.join(final_path, file_extension[1:].upper()))

        os.rename(final_path + '/' + file, os.path.join(final_path, file_extension[1:]+ '/' + file))
        
