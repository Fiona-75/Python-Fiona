import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# print(os.environ)

# TODO: Use the glob.glob() function to obtain the list of filenames

# do i need to use a list function too? my code gives nothing. what is the actual directory?







# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

