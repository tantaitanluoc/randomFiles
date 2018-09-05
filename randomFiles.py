import module as bitch
import anydbm
import pickle
import random

db_name = "files_browsed.db"
db = anydbm.open(db_name,"c")
def randomchoose(names,file_block):
	# choose randomly [file_block] files from a file list
	chossen = []
	flag = True
	count = 0
	while(flag):
		if count > file_block:
			flag = False
		else:
			temp = random.choice(names)
			hashed_value = bitch.md5_checksum(temp)
			# store in md5 value so don't worry about the same file but with different names
			if temp not in db:
				chossen.append(hashed_value) 
				count += 1
	return chossen

def copyfile(file,destination):
	cmd = "cp " + file+ " "+destination
	return bitch.pipe(cmd)

def reset_database():
	cmd = "mv " +db_name+" "+db_name+".bak" # backup database
	print "Your database is being reset..."
	return bitch.pipe(cmd)

def scan(dirname="",file_block=5,destination="/home/tantai/ao"):
	names = bitch.walk(dirname)
	chossen = randomchoose(names,file_block)
	for file in chossen:
		db[file] = bitch.get_time()
		copyfile(file,destination)
	print "Done!"


if __name__ == '__main__':
	# scan("/run/media/tantai/DATA/py_test/review/")
	reset_database()




