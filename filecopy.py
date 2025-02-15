#!/usr/bin/env python3
# CECS 326 - Group Project 1
# Helen Ton

import os
import sys 

def fileCopy(srcFile, destFile):
    '''
    Function: copies data from one file to another
    Parameters:
    - srcFile: file the program is reading data from
    - destFile: file the program is writing the data to 

    '''
    # Create a pipe with file descriptors r for read, w for write
    r, w = os.pipe()

    # Fork a child process
    pid = os.fork()

    # PARENT PROCESS (pid > 0) 
    if pid > 0:
        os.close(r)     # signal pipe that we do not need to read from it

        # Opening source file
        try:
            with open(srcFile, 'r') as source:
                data = source.read()             # reading data from the source file
                os.write(w, data.encode())       # writing data in bytes to the pipe
            os.close(w)                          # signal pipe we are done writing 
        except IOError:
            print("\nERROR: Unable to open and read from source file:", srcFile)
            sys.exit(1)
        
        # Waits for child process to finish running
        os.wait()

        # Output if program executes correctly
        print(f'\nFile successfully copied from {srcFile} to {destFile}! :D')


    # CHILD PROCESS (pid == 0)
    if pid == 0:
        os.close(w) # signal pipe that we do not need to write to it

        # Reading from read end of pipe, rFile - file object
        try:
            rFile = os.fdopen(r)            
            pipeData = rFile.read()   
            # Close file object     
            rFile.close()   
        except:
            print("ERROR: Unable to open and read from pipe")
            os._exit(1) # exit w/ status 1 to indicate error

        # Opening destination file
        try:
            with open(destFile, 'w') as dest:
                dest.write(pipeData)    # writing data from pipe to dest file
        except IOError:
            print("ERROR: Unable to open and write to destination file:", destFile)
            os._exit(1)  # exit w/ status 1 to indicate error

        os._exit(0)  # exit w/ status 0 - child process runs successfully


def main():
    # Takes source file and destination file as inputs
    srcFile = input("Please type the file name you want to read from: " )
    destFile = input("Please type the file name you want to write to: ")

    # Calls the fileCopy function
    fileCopy(srcFile, destFile)

main()