import re
with open("Hera Pheri.srt","r+") as f1,open("hello.txt","w+") as f2:
	data=f1.readlines()
	for i in data:
		i.strip()
		if re.findall("♪|:|Subtitles|[<>@]|Open|Advertise|OpenSubtitles.org|Support|YIYF|VIP|.com",i):
			pass
		elif re.match("^[0-9]",i):
			re.sub("(^[0-9])\s",r'\1 ',i)
		else:
			f2.write(i)
	name=f1.name
	
name=name.replace(".srt",".txt")	

with open("hello.txt","r+") as f1,open(name,"w+") as f2:
	data1=f1.readlines()
	for i in range(len(data1)):
		data1[i].strip()
		data1[i]=re.sub("\n","",data1[i])
		
	cn=0	
	for i in range(0,len(data1),2):
		string=""
		cn+=1
		string=" ".join(map(str,data1[i:i+2]))+"\n"
		f2.write(string)
	