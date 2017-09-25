import os 

folderNames = ['Audio', 'Animations', 'Images', 'Materials', 'Plugins', 'Prefabs', 'Resources', 'Scripts', 'Scenes']
dir_path = os.path.dirname(os.path.realpath(__file__))
userInput = input('This will make {0} empty folders in {1}, write "y" to continue\n'.format(folderNames.__len__(), dir_path))
if userInput == 'y' or userInput == 'Y' :
    for f in folderNames:
        fullPath = dir_path + '\\' + f
        print(fullPath)
        if not os.path.exists(fullPath):
            os.makedirs(f)