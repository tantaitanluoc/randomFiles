import module as bitch
import anydbm
import pickle
import random

db = anydbm.open("files_browsed.db","c")
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
			if temp not in db:
				chossen.append(temp)
				count += 1
			else:
				print "Duplication found in ",temp
	return chossen


def scan(dirname="",file_block=5):
	names = bitch.walk(dirname)
	chossen = randomchoose(names,file_block)
	for file in chossen:
		db[file] = bitch.get_time()
	print "Done!"


if __name__ == '__main__':
	scan("/run/media/tantai/DATA/py_test/review/")




