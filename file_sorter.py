import os;
import shutil;

#os.chdir('F:/videos/Programming/[FreeCourseSite.com] Udemy - Complete WordPress Development Themes and Plugins Course/01 Getting Ready for WordPress Development');
filenames = os.listdir();

for i in filenames:
	original_name = i;
	num = original_name[0:3];
	name_end = original_name[4:];
	
	if(name_end[(len(name_end)-3): ] == "srt"):
		name_end_without_en = name_end[0:(len(name_end)-7)]+".srt";
	else:
		name_end_without_en = name_end;

	if(int(num)):
		lesson_num = int(num)-1;
		new_name = "Lesson "+str(lesson_num)+". "+name_end_without_en;

		shutil.copy(original_name,new_name);



