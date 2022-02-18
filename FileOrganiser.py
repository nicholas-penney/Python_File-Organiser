###########################
#                         #
#     Nicholas Penney     #
#                         #
###########################

# Makes 5 folders and moves files of that type into them.

import os
import shutil

# File and Directory
rootDir = os.path.dirname(os.path.abspath(__file__))
exeFileDir = (__file__)

# Get the exe file name on its own
trimFilePath = len(rootDir) + 1  # so that it takes off the final backslash
exeFile = exeFileDir[(trimFilePath):]  # just the file name remaining

########################

# Contine with moving?
print('\nChecking ' + rootDir + ' for files.')
choice = input('Is this correct? Y or N: ')  # Confirm program run.
choice = str.lower(choice)  # Change input to lower case.

########################

# Exit
if choice != 'y':
    pause = input('Program manually terminated...')  # Exit the program

########################

# User chose to move files
else:
    print('\nMoving files now...')  # Program is running

    print('\nDefining extensions.')
    imgTypes = ['jpg', 'jpeg', 'png', 'tiff', 'tif', 'eps', 'gif', 'bmp', 'raw', 'cr2', 'nef', 'orf', 'sr2']  # Decalre file types for each folder
    vidTypes = ['wmv', 'mp4', 'mov', 'avi', 'flv', 'wmv', 'swf']
    mp3Types = ['mp3', 'MP3', '3gp', 'aac', 'flac', 'm4a', 'wav', 'wma']
    docTypes = ['pdf', 'doc', 'docx', 'docm', 'dotx', 'dotm', 'odt', 'xls', 'xlt', 'xlm', 'xlsm', 'xlsx', 'xltx', 'xltm', 'ppt', 'pps', 'pptx', 'pptm', 'ppsx', 'sldx', 'sldm']
    exeTypes = ['zip', 'rar', 'exe', 'msu', 'json']
    print('Extensions defined.')

    print('\nCreating folders.')
    imgFolder = rootDir + r'\Images'  # Makes Image folder, etc etc
    if os.path.exists(imgFolder):
        print('Images folder already exists.')
    else:
        os.makedirs(imgFolder)

    vidFolder = rootDir + r'\Video'
    if os.path.exists(vidFolder):
        print('Video folder already exists.')
    else:
        os.makedirs(vidFolder)

    mp3Folder = rootDir + r'\Music'
    if os.path.exists(mp3Folder):
        print('Music folder already exists.')
    else:
        os.makedirs(mp3Folder)

    docFolder = rootDir + r'\Documents'
    if os.path.exists(docFolder):
        print('Documents folder already exists.')
    else:
        os.makedirs(docFolder)

    exeFolder = rootDir + r'\Exes'
    if os.path.exists(exeFolder):
        print('Exes folder already exists.')
    else:
        os.makedirs(exeFolder)

    print('Folders created.')
    subFolderDir = []


    ########################


    # Check file for extensions and duplicates
    print('\nAnalysing files.')

    for file in os.listdir(rootDir):
        subFolderFileDupe = False  # Reset flag
        if file == exeFile:  # Skip program file
            continue

        # Img 	# Create array for target folder to check file duplicates
        subFolderDir = os.listdir(imgFolder)	# Array built of target dir
        for x in subFolderDir:					# Scroll through target dir array
            if x == file:						# Find duplicate file
                subFolderFileDupe = True		# Flag
                break							# Dupe found, stop loop
        if subFolderFileDupe == True:			# Duplicate found, leave current file in root
            continue

        for img in imgTypes:  					# Run through image extension array
            if file.endswith(img):  			# Image type found
                full = rootDir + '\\' + file  	# Precise file directory
                shutil.move(full, imgFolder)  	# Move file to new folder.

        # Vid 	# Create array for target folder to check file duplicates
        subFolderDir = os.listdir(vidFolder)
        for x in subFolderDir:
            if x == file:
                subFolderFileDupe = True
                break
        if subFolderFileDupe == True:
            continue

        for vid in vidTypes:
            if file.endswith(vid):
                full = rootDir + '\\' + file
                shutil.move(full, vidFolder)

        # MP3 	# Create array for target folder to check file duplicates
        subFolderDir = os.listdir(mp3Folder)
        for x in subFolderDir:
            if x == file:
                subFolderFileDupe = True
                break
        if subFolderFileDupe == True:
            continue

        for mp3 in mp3Types:
            if file.endswith(mp3):
                full = rootDir + '\\' + file
                shutil.move(full, mp3Folder)

        # Doc 	# Create array for target folder to check file duplicates
        subFolderDir = os.listdir(docFolder)
        for x in subFolderDir:
            if x == file:
                subFolderFileDupe = True
                break
        if subFolderFileDupe == True:
            continue

        for doc in docTypes:
            if file.endswith(doc):
                full = rootDir + '\\' + file
                shutil.move(full, docFolder)

        # Exe 	# Create array for target folder to check file duplicates
        subFolderDir = os.listdir(exeFolder)
        for x in subFolderDir:
            if x == file:
                subFolderFileDupe = True
                break
        if subFolderFileDupe == True:
            continue

        for exe in exeTypes:
            if file.endswith(exe):
                full = rootDir + '\\' + file
                shutil.move(full, exeFolder)

    print('Files successfully moved.')
    pause = input('\n\nProgram terminating...')

########################
