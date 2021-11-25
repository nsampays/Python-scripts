## Create-Movie-folders.py

### To run and debug on the NAS create a virtual drive ....	
## pushd \\Synology_NAS4\Synology_Home2\Media\TV_Shows_1\TV_Comedy\The Simpsons
## IN windows cmd shell ....

## Directory structure PLEX expects ################################
##      
##
##  Great Movies
##      
##          Movie 1 (2001)
##              Movie 1 (2001).mkv
##          Movie 2 (2002)
##              Movie 2 (2002).mkv
##              ....
##             .....
##          
#################################################################

## Possible improvements 
# -- check you are in right dir
# -- Add another layer of hierarchy  
# -- Dealing with old vobs -- prob need to rerip
#  -- Look at Movies and Photos  at some point..

import pathlib
from pathlib import Path
import os
from os import chdir
import shutil

### add path here ----->
#movies_directory = Path("Z:/Media/Movies")

### function to create movie folders for PLEX ########################

def make_movie_dir(movie_name):

## loop through list of movie_files in Movies_directory 
## removing file extention 
## creating a new dir
## then moving file into it.

    for movie in movie_name.iterdir():
        if movie.is_file():                             # check its a file
            p = pathlib.Path(movie)                     # Use Pathlib to remove th file extension
            moviedir = (p.with_suffix(''))              # and assign dir name to hold movie
    
            if not os.path.exists(moviedir):            # Check not already done
                os.mkdir(moviedir)                      # ok make dir
            shutil.move(movie, moviedir)                # move movie file into its own dir.

### end of Function ###################################################            

### Iterate Movies directory putting files into their folders. -- remove commented...

 for folder in movies_directory.iterdir():
      make_movie_dir(folder)
