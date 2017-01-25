import requests 
from bs4 import BeautifulSoup
import webbrowser 


website = "http://www.shush.se/"

def search_input(msg) :
	x = raw_input('>'+msg+'(y/n)')
	if (  "yes" in x or x == 'y' or "yay" in x or "ya" in x or "yup" in x) :
		return True
	else :
		return False

def find_ep (givenurl , showname) :
	url = givenurl
	try :
		print 'Please Wait ...'
		r = requests.get(url)	
	except :
		print '\nERROR:Unable to Open "' + url +'"\nCheck your Internet Settings and Try Again Later\n'
		return

	print 'Connected :'
	soup = BeautifulSoup(r.content , "html.parser")
	linksall = soup.find("td" ).find_all("div")

	out = []
	outn = []
	links = linksall[2].find_all("a")
	for link in links :
		outn.append(link.text.replace(showname + ' ', ''))
		print link.text.replace(showname + ' ', '')
		out.append(website + link.get("href"))

	print 'Enter Season Number :'
	x = raw_input()
	print 'Enter Episode Numeber :'
	y = raw_input()
		
	count = 0
	for i in outn :
		if ('Season ' + x + ' Episode: '+y in i ) :
			# print out[count]
			ans = search_input("Want to open in Browser?")
			if ans :
				try :
					webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(out[count])
				except :
					print 'Google-Chrome is not installed'
					webbrowser.open(out[count])
			else :
				pass
		count += 1

	# print 'x is : ' , x 
	# print 'y is : ' , y

	# for i in outn :
	# 	print i

	










