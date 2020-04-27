import os;
import shutil;

log = open("renamed files.log",'a');
log.write("This is the log of the renamed files\n"+"*********************************************\n\n\n");

def printer(message):  #This function prints the received message into the log file
	log.write(message);

def movemessageprinter(i,j): #This moves the files received from the rename, creates a message and prints it
	shutil.move(i,j);
	message =  "Renamed\t"+i+" into \n\t\t"+j+"\n";
	printer(message);

def rename(): #This creates the renaming string and calls the real renamer which is movemessageprinter
	files = os.listdir();	
	for i in files:
		if(i[len(i)-3:] == "srt"):

			en = "en";
			mp4 = "mp4";
			j = i;	#This removes the error unedintified variable j;
			if(i[len(i)-6:] == en+".srt"):
				j = i[0:len(i)-7] + ".srt";
				movemessageprinter(i,j)

			elif(i[len(i)-7:] == mp4+".srt"):
				j = i[0:len(i)-7] + "srt";
				movemessageprinter(i,j);
			
def navigator():	#This fx navigates through the current working directory and collects information present in the current directory
	directories = []
	printer("************************************************\n"+"The parent folder is "+os.getcwd()+"\n\n\n");
	for cwd, mindir, files in os.walk(os.getcwd()): #I use this for loop to collect the directories and store them in directories array
		directories.append(cwd);

	for i in directories:	#I use this for loop to navigate through the directories collected above and run the print and rename fx's 
		os.chdir(i);
		printer("Moved onto "+i+"\n");
		rename();

def Main():
	navigator();

Main();


