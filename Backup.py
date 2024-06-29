'''Q4. In DevOps, performing regular backups of important files is crucial:

●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script should copy all files from the source directory to the destination directory.

●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

Sample Command:

python backup.py /path/to/source /path/to/destination

By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.
'''

import shutil, os, sys, time, datetime


n = len(sys.argv)
if n<3:
    sys.exit("Please give arguments from comamnd-line")

pathSrc = sys.argv[1]
pathDest = sys.argv[2]

try:   
    dir_listSrc = os.listdir(pathSrc)
except FileNotFoundError:
    print('File not found. Please check the path : '+pathSrc)

try:
    dir_listDest = os.listdir(pathDest)
except FileNotFoundError:
    print('File not found. Please check the path : '+pathDest)

for fileSrc in dir_listSrc:
    fullFileSrc = os.path.join(pathSrc, fileSrc)
    fullFileDest = os.path.join(pathDest, fileSrc)
    if os.path.isfile(fullFileSrc):
        if os.path.isfile(fullFileDest):
            ts = str(datetime.datetime.now())
            fileSrcName = fileSrc.split(".")[0]
            fileSrcExt = fileSrc.split(".")[1]
            fullFileDest = os.path.join(pathDest, fileSrcName+"_"+ts+"."+fileSrcExt)
        shutil.copy(fullFileSrc, fullFileDest)


