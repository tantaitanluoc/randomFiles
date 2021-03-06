import module as mdl
import anydbm
import pickle
import random
import sys
import platform

db_name = "files_browsed.db"
db = anydbm.open(db_name,"c")
def randomchoose(names,file_block,type_allowed):
	# choose randomly [file_block] files from a file list
	chosen = []
	flag = True
	count = 0
	while(flag):
		if count >= file_block:
			flag = False
		else:
			temp = random.choice(names)
			hashed_value = mdl.md5_checksum(temp)
			# store in md5 value so don't worry about the same file but with different names
			if hashed_value not in db and mdl.check_suffix(temp,type_allowed):
				db[hashed_value] = mdl.get_time()
				chosen.append(temp) 
				count += 1
	return chosen

def copyfile(file,destination):
	cmd = "cp '" + file+ "' '"+destination+"'"
	return mdl.pipe(cmd)

def reset_database():
	cmd = "mv " +db_name+" "+db_name+".bak" # backup database
	print "Your database is being backup..."
	return mdl.pipe(cmd)

def scan(dirname="",file_block=5,destination="/home/tantai/opt",type_allowed = ".mp4"):
	names = mdl.walk(dirname)
	chosen = randomchoose(names,file_block,type_allowed)
	os = platform.system()
	if os == "Linux":
		for file in chosen:
			copyfile(file,destination)
	else:
		fin = open(destination+"/files.txt","w+")
		for file in chosen:
			fin.write(file+"\n")
	print "Done!"


if __name__ == '__main__':
	if len(sys.argv) > 1 and str(sys.argv[1]) == "reset":
		reset_database()
	else:
		scan("/home/tantai/ao")



