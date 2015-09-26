import urllib
import os 
import re

class Apple() : 
	def __init__(self, url, html_status = '', html_content = '') :
		self.url = url
		self.html_status = html_status
		self.html_content = html_content

	def scraper(self) : 
		self.html_status = urllib.urlopen(self.url) 
		self.html_content = self.html_status.read()

	def regex(self) : 
		regex = '<span id="yfs_l84_aapl">(.+?)</span>'	
		pattern = re.compile(regex) 
		price = re.findall(pattern, self.html_content)
		print 'Stock price : ' + str(price)

	def file_writer(self) : 
		fileopen = open('finance.txt', 'w')
		fileopen.write(self.html_content)
		fileopen.close()
		#os.system('subl finance.txt')

	def dir_check(self) : 
		## changing the directory to the required folder 
		curr_dir = os.getcwd() 
		if curr_dir == '/home/tasdik/Dropbox/projects/web_scraper/txt_files' : 
			print 'writing inside the file'
			self.file_writer()
		else : 
			os.chdir('/home/tasdik/Dropbox/projects/web_scraper/txt_files')
			self.file_writer()

def main():
	obj = Apple('http://finance.yahoo.com/q?s=AAPL')
	obj.scraper()
	obj.dir_check()
	obj.regex()

if __name__ == '__main__' : 
	main()