Create a terminal cli app

Create an executable on MacOS and symlink it to the usr/local/bin

* Create filename without an extension
    * in said filename import libfile and make a new file in the same dir called libfile.py
    * all business logic code can live in libfile.py
* In libfile.py use argparser to read args for your command line app
* For the filename without the extension make sure to add the following boilerplate code 	
    #!/usr/bin/env python3
	import libfile 	
	libfile.main()

* In terminal make this file an executable by running 
    “chmod +x file”
* For this executable add a symlink to PATH so the it can be called on the terminal
    * run echo $PATH to get a list of colon separated directories in PATH
    * if usr/local/bin does not exist, run mkdir for this
    * add a symlink to this PATH by running the terminal command 
    “sudo ln -s path/to/executable usr/local/bin”
* Now running file name directly on the terminal should work fine
* Add sub parsers to argparser and link it to functions with business logic