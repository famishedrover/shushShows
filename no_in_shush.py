import requests
from bs4 import BeautifulSoup
import time 
import webbrowser
from shushpart2 import find_ep
#--------------------------------------------------------
url = "http://www.shush.se/index.php?shows"
website = "http://www.shush.se/"
# t0= time()
#--------------------------------------------------------
try :
	print 'Please Wait ...'
	r = requests.get(url)	
except :
	print '\nERROR:Unable to Open "' + url +'"\nCheck your Internet Settings and Try Again Later\n'
	exit()
#--------------------------------------------------------
print 'Connected :'
soup = BeautifulSoup(r.content , "html.parser")
links = soup.find("td" ).find("div")
# count = 0
# for link in links :
# 	count+=1
# 	print count ,link 
# print 'Total Shows on Shush.se = ', len(links)
# --------------------------------------------------------
def search_input(msg) :
	x = raw_input('>'+msg+'(y/n)')
	if (  "yes" in x or x == 'y' or "yay" in x or "ya" in x or "yup" in x) :
		return True
	else :
		return False

def shows_input(count ):
	x = raw_input('>Select Show by Entering the number eg. for 1.The Flash enter "1" without the quotes : ')
	try:
		x = int (x)
	except:
		return -1
	if(x>count or x<1):
		return -1
	return x	

action = True


found = False
count = 0 

while action :
	count = 0
	found = False
	out = []
	outn = []
	search = raw_input('>Search Show :')
	print 'Found Shows : '

	for link in links :
		if search.lower() in link.text.lower() :
			found = True
			count +=1
			out.append( link.find("a").get("href") )
			outn.append(link.text)
			print '{:4>}'.format(count), link.text 
		else :
			pass
	
	if not found :
		print'No matches for ',search 

	t=0
	if count :
		if count == 1:
			print website + out[0]
			
			ans = search_input('Want to open '+outn[0]+ ' ?')
			if ans :
				#webbrowser.open(website + out[0])
				find_ep (website + out[0] , outn[0])
			else:
				pass
		else:	
			r = shows_input(count)
			print website + out[r-1]
			ans = search_input('Want to open '+outn[r-1]+ ' ?')
			if ans :
				#webbrowser.open(website + out[r-1])
				find_ep (website + out[r-1] , outn[r-1])
			else:
				pass

	action = search_input('> Want to Search ?')


	
print 'End.'		








