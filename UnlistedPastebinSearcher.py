

import random
import string
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

Options = Options()
Options.headless=True

x=0
urlinteger=[]
urlIntList=[]
while x<10000:#main counter here
	urlinteger.append(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8)))
	urlIntList.append(urlinteger[x])
	x=x+1
	
class DownloadPages(unittest.TestCase):
	def test(self):	
		y=0	
		print (urlIntList)
		print (type(urlIntList[0]))
		while y < x:
			url=("https://pastebin.com/"+urlIntList[y])
			print (url)
			y=y+1	
			browser = webdriver.Firefox(options=Options)
			browser.get(url)
			if (self.assertTrue('Not Found' in browser.page_source)):
				print (browser.page_source)
			browser.close()
t=DownloadPages()
t.test()
