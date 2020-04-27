Modules and their usage
os
	os.getcwd(); #Returns the current working directory
	os.listdir();	#lists the directories which are present in the current path
	os.chdir('path');	#Used to change the current path into the path specified
	os.mkdir('path'); #used to create folders in the current path
	os.path.getsize('path');  #shows the size of the files in the current path
	os.path.exists('path');	#Checks if the path specified exists for both folders and files
	os.path.isdir('path'); #Checks if the path specified is a folder
	os.path.isfile('path'); #Checks if the file specified is a file
	os.walk('path'); #Scans the current directory and collects three array's one for current working directory, one for directories and one for files
	os.unlink('path') #Deletes a file at a path
	os.rmdir('path') #Deletes a folder at a path if it contains nothing inside


opening, reading, creating text_files;
	Filename = open('path_and_filename','opening_method'); #This creates an instance Filename which will be used to manipulate files with the opening_method specified this can be 'a'-for append, 'r' -for read, and 'w' -for write method
	Filecontent = Filename.read(); #This reads the contents of the filename and stores it in the Filecontent variable
	Filecontent_including_spaces_and_newlines = Filename.readlines(); #This reads the contents of the filename including the spaces and newlines and stores it in the File_content_including_spaces_and_newlines variable
	Filename.write('message'); #This writes into the Filename a message specified
	Filename.close(); #This closes the instance of the filename variable


shutil
	shutil.copy('source', 'destination');	#This coppies the source file(include the extension) into the destination specified, the destination can also include the file extension 
	shutil.move('source','destination');	#This moves source file (include the extension) into the destination specified, the destination can also include the file extension
	shutil.rmtree('filename or foldername'); #This deletes everything in the folder including eveything in it
	

Data types

#Lists
name = []; #This initializes an empty list
name += ["hamis"] #This adds the name hamis at the 0'th index
name += ["ally"] #This adds the value ally at the 1'st index
name[0] = "salum" #This modifies the value of hamis to salum at index 0
name = ["hamis", "ally", "salum"]; #This initializes the list with three values

#Turples
name = (); #This initializes an empty turple
name = ["hamis", "ally", "salum"]
#Turples do not support modification so name[0] = "aally" will fail

#Dictionaries
name = {}; #This initializes an empty dictionary
name["first"] = "Hamis";
name["second"] = "Ally";
name["third"] = "Salum";
