import os
import time
import hashlib
def walk(dirname):
	names = []
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)
		if(os.path.isfile(path)):
			names.append(path)
		else:
			names.extend(walk(path))
	return names

def check_suffix(filename,suffix):
	return filename.endswith(suffix)

def md5_checksum(filename):
	hash_md5 = hashlib.md5()
	with open(filename,"rb") as fuck:
		for chunk in iter(lambda: fuck.read(4096),b""):
			# read chunks of 4096 bytes sequentially to fit the whole file in memory
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def get_time():
	return time.asctime(time.localtime(time.time())) # =))

def pipe(cmd):
	bash = os.popen(cmd)
	result = bash.read()
	status = bash.close()
	assert status is None # to makes sure the bash shell command works fine
	return result,status

def main():
	print walk("D:\\py_test")
if __name__ == '__main__':
	main()