import os as oss
import subprocess as sp
import re as regex
def read (file_path):

    return 0

def evaluate(filepath,language):
 global x
 if language == 'c':

  file = open (filepath, 'r')
  lines = file.readlines()
  file.close()

   
  #look for patterns
  countgets =0
  # countSTRNC =0
  for line in lines:
    x = regex.search("gets[(].*[)]", line)
    line = line.strip()
    if x:
       countgets = countgets +1


 print( "vulnerabilities found", countgets )


 return 0

def duplicatewc(fileVarName):
    return 0


def fileread(filePath):
  #file = open(filePath, "r")
  sp.call(['C:/Program Files/Notepad++/notepad++.exe', filePath])
  stderr = sp.STDOUT
  print( stderr )

  #lines = file.readlines()
  #file.close()
  #fileshow(lines)
  return filePath

def fileshow(fileName):
    file = open( fileName, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip()
        print ( line )
    return 0

def savefile(im, name):
    return 0