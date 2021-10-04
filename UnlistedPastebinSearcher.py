#The following is a .py file which aims to find unlisted pastebins by generating random strings. The 
#python code is below and it sure could use some improvements, so feel free to comment any 
#changes you made or found useful that helped the functionality. You essentially just leave this script 
#running until you are satisfied and I have found nothing with it so far, but I wanted to post the code 
#here in case someone else finds it useful

#Needed libraries are below:

import random
import string
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

#The following 2 options lines allow for our python selenium browser to run in the background

Options = Options()
Options.headless=True

#The following lines generate a “counter” size of array of random 8 digit strings that can #contain letters or numbers
x=0
urlinteger=[]
urlIntList=[]
while x<10000:#main counter here
	urlinteger.append(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8)))
	urlIntList.append(urlinteger[x])
	x=x+1
	
	
#These final lines will make the 8 digit random string into a url which is accessed through selenium, 
#finally any active pages without 'Not Found' located in the pages source will have their current page 
#source printed in the output, so naturally if you leave this script on long enough it should find something

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
