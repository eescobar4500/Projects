import os
import os.path
import collections 
from pathlib import Path
import glob

#def main():

#Todo 
#****************************************************************************
#  (Navagate Directories)                                                    #
#* ----------------------                                                    #
#*                                                                           #
#* -- Find the number of files in each directory                             #
#* -- List the file type in each directory                                   #  #* -- Scan Directory paths using recursion 				     #	#* 									     #
#*                         						     # 
#*                                                                           #
#*****************************************************************************

#Function
def traversing_dir_paths (Dir_elements):
 
 #Getting current directory
 curr_dir=os.getcwd() 
 #Initialize/Reset counter
 count=0

 for element in Dir_elements:
   #Check if the element is a directory, else file
   if os.path.isdir(element):
         
     #List of elements of directory 
     curr_dir_list=os.listdir(element)
     
     #Change directory path to work on 
     os.chdir(element)
     
     #Recursively traversing all directories/sub directories  
     traversing_dir_paths(curr_dir_list)
   else:
     #Counter for number of files
     count=count+1
      
    
 print('(' + "In Directory"+'):')  
 print(curr_dir)

 print('('+"Within Directory"+'):')
 print(Dir_elements)    

 print('('+"Number of Files"+'):')
 print(count)
 
 print("(Number of File Types in each Directory):")
 print(" "+"Below: {'': #} Can indicate Total # of File Types with No Ext and/or a Dir")
 
 #Create path from current dir for pathlib
 path_curr=Path(curr_dir)
 #Pathlib module to count number of file type in each directory 
 print(collections.Counter(p.suffix for p in path_curr.iterdir()))
 
 #Extra Space
 print(" ")
 
 #Reset to home directory   
 os.chdir(home_dirpath)
 

#Get current working directory
home_dirpath=os.getcwd()

#Directory elements listing
dir_list=os.listdir(home_dirpath)

#Calling function
traversing_dir_paths(dir_list)


#if __name__=="__main__":
 #  main()
