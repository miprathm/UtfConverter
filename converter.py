import os
import traceback
path = os.path.join("E:/","","","") 

outputpath = os.path.join(path,"output")

print("start")
log = ''
missings ='' 
for scriptFile in os.listdir(path):
	print(" Processing  : "+scriptFile)
	log += "\n Processing : "+scriptFile
	try:
		binaryFile = open(os.path.join(path,scriptFile),'rb+')
		binary=binaryFile.read()
		binary = binary.replace(b'\x00',b'')
		binaryFile.close()
		outputFile = open(os.path.join(outputpath,scriptFile),'w')
		outputFile.write(str(binary,'latin-1','ignore'))
		outputFile.close()
	except Exception as e:
		print("Error in : "+scriptFile)
		log += traceback.format_exc()
		missings += scriptFile+"\n"
		
logfile = open('file.log','w')
logfile.write(log)
logfile.close()
missing_file = open('missing_file.txt','w')
missing_file.write(missings)
missing_file.close()		
	
