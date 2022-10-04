import zipfile

def bruteForceArchive(filename):
  with zipfile.ZipFile(filename) as archivefile:
    passwordlist = open('dictionary.txt').read().splitlines()
    for currentpassword in passwordlist:
      try:
        archivefile.extractall(pwd=bytes(str(currentpassword), 'utf-8'))
        print(currentpassword + " is the CORRECT password")
        return True
      except RuntimeError:
        print(currentpassword + " was an incorrect password")

bruteForceArchive('protected.zip')
