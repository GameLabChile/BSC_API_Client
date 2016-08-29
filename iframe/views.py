from django.shortcuts import render
import time
import rsa
import base64
import json
import urllib2
# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def form(request, player, classid, playerid, timeout):
	sign = ""
	
	url = "https://[server]/api/newalone/"
	teacher = "user given"

	player = player
	timereq = int(time.time()*10)
	esc = int(1)

	keyfile = """Key Given"""

	private_key = rsa.PrivateKey.load_pkcs1(keyfile)

	data = {'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc, 'playerid': int(playerid), 'classid':int(classid) , 'timeout':int(timeout)}
	firma = rsa.sign( json.dumps(data, sort_keys=True) , private_key, 'SHA-1' )
	firma64 = base64.urlsafe_b64encode(firma)
	print  json.dumps(data, sort_keys=True)
	return render(request, 'form.html', {'sign':firma64, 'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc, 'url':url, 'playerid':playerid, 'classid':classid, 'timeout':timeout})