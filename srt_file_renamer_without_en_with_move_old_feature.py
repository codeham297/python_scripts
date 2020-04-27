def rename():
	import os;
	import shutil;
	
	files = os.listdir();
	if(not(os.path.isdir('newsrt'))):
		os.mkdir('newsrt');
	if(not(os.path.isdir('oldsrt'))):
		os.mkdir('oldsrt');
	for i in files:
		if(i[len(i)-3:] == "srt"):
			if(i[len(i)-6:] == "en.srt"):
				j = i[0:len(i)-7] + ".srt";
				j = 'newsrt/'+j;
				shutil.copy(i,j);
				k = 'oldsrt/'+i;
				shutil.move(i,k);

rename();