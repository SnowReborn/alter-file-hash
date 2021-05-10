import hashlib
def add_content():
	global enc, del_or_add, path
	if del_or_add == 'add':
		ffile = open(path, 'a+b')
		ffile.write(b'added_content')
		ffile.seek(0)
		sha256finger = enc(ffile.read()).hexdigest()
		print("The sha256 fingerprint is : {}".format(sha256finger))
		ffile.close()
def delete_content():
	global enc, del_or_add, path
	if del_or_add == 'del':
		ffile = open(path, 'a+b')
		ffile.seek(-13,2) # 2 means end of the line, 1 means current 0 means start
		#-13 char corr to added_content
		if ffile.read() == b'added_content':
			ffile.seek(-13,2)
			ffile.truncate()
		ffile.seek(0)
		sha256finger = enc(ffile.read()).hexdigest()
		print("The sha256 fingerprint is : " + sha256finger)
		ffile.close()
def main():
	global enc, del_or_add, path
	while True:
		enc= hashlib.sha256
		del_or_add = input("add or del?\n")
		path = input("path of the file excluding quotes\n")
		if del_or_add == "add":
			add_content()
		if del_or_add == "del":
			delete_content()
		if input("press any key to exit, else press R to continue\n") != 'r':
			break
main()
