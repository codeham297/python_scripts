import os;
import shutil;

log = open('srt_file_renamer_without_en_with_move_old_feature.log','a');

def printer(message):
	log.write(message);


def rename():	
	files = os.listdir();	
	for i in files:
		if(i[len(i)-3:] == "srt"):
			if(i[len(i)-7:] == "mp4.srt"):
				j = i[0:len(i)-7] + "srt";
				message =  "Renamed\t"+i+" into \n\t\t"+j+"\n";
				printer(message);
				shutil.move(i,j);

def navigator():
	lfiles = os.listdir();
	folder = os.getcwd();
	log.write("***************************************************\n"+"The parent folder is "+folder+"\n\n\n");
	rename();
	for l in lfiles:
		if(os.path.isdir(l)):
			os.chdir(l);
			lfiles = l;
			folder = lfiles;
			log.write("\n"+"The directory in the folder moved to "+folder+"\n\n");
			rename();
			os.chdir("../");


def Main():
	navigator();

Main();
