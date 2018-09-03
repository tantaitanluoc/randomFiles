import os
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

def md5_checksum(filename):
	hash_md5 = hashlib.md5()
	with open(filename,"rb") as fuck:
		for chunk in iter(lambda: fuck.read(4096),b""):
			# read chunks of 4096 bytes sequentially to fit the whole file in memory
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def main():
	print walk("D:\\py_test")
if __name__ == '__main__':
	main()