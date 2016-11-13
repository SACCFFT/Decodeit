from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from backend.models import*
from backend.forms import *

def decrypt(key, text):
	text = text.lower()
	plain = ""
	for c in text:
		if c.isalpha():
			plain += key[ord(c)-ord('a')]
		elif c.isspace():
			plain += c
	return plain

def freq(text):
	frequency=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for c in text:
		if c.isalpha():
			frequency[ord(c)-ord("a")]+=1
	freqStr=""
	for i in frequency:
		freqStr+=str(i)
	return str(frequency)

class HomePage(View):
    def get(self, request):
		
		players = Player.objects.all()
		playerList = []
		context = {}
		context["players"] = players
		context["member"] = request.user.username
		return render(request, 'index.html', context)

class LoginPage(View):
	def get(self, request):
		return render(request, 'login.html')

	def post(self, request):
		username = request.POST['userid']
		password = request.POST['pass']
		print(username)
		print(password)
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect("/")	
		else:
			return render(request, "playerNotFound.html")

class DecryptPage(View):
	def get(self,request, url=""):
		components = str(url)
		context = {}
		print(url)
		#try:
		player = Player.objects.get(username=url)
		#except:
		#	return render(request, "playerNotFound.html")
		context["playerFound"] = player
		context["key1"] = "#"
		context["key2"] = "#"
		context["key3"] = "#"
		context["key4"] = "#"
		context["key5"] = "#"
		context["key6"] = "#"
		context["key7"] = "#"
		context["key8"] = "#"
		context["key9"] = "#"
		context["key10"] = "#"
		context["key11"] = "#"
		context["key12"] = "#"
		context["key13"] = "#"
		context["key14"] = "#"
		context["key15"] = "#"
		context["key16"] = "#"
		context["key17"] = "#"
		context["key18"] = "#"
		context["key19"] = "#"
		context["key20"] = "#"
		context["key21"] = "#"
		context["key22"] = "#"
		context["key23"] = "#"
		context["key24"] = "#"
		context["key25"] = "#"
		context["key26"] = "#"
		context["plain"] = player.cipherText
		context["encrypted"] = player.cipherText
		context["freq"] = freq(player.cipherText)
		context["member"] = request.user.username
		return render(request, "play.html", context)
		

	def post(self, request, url=""):
		components = str(url)
		context = {}
		for player in Player.objects.all():
			if url == player.username:
				context["playerFound"] = player
				key = ''
				keys = ["#"]*26
				for i in range (1,27):
					temp = request.POST.get("solution"+str(i))
					key += temp
					keys[i-1] = temp
				context["key1"] = keys[0]
				context["key2"] = keys[1]
				context["key3"] = keys[2]
				context["key4"] = keys[3]
				context["key5"] = keys[4]
				context["key6"] = keys[5]
				context["key7"] = keys[6]
				context["key8"] = keys[7]
				context["key9"] = keys[8]
				context["key10"] = keys[9]
				context["key11"] = keys[10]
				context["key12"] = keys[11]
				context["key13"] = keys[12]
				context["key14"] = keys[13]
				context["key15"] = keys[14]
				context["key16"] = keys[15]
				context["key17"] = keys[16]
				context["key18"] = keys[17]
				context["key19"] = keys[18]
				context["key20"] = keys[19]
				context["key21"] = keys[20]
				context["key22"] = keys[21]
				context["key23"] = keys[22]
				context["key24"] = keys[23]
				context["key25"] = keys[24]
				context["key26"] = keys[25]
				print(key)
				decr = decrypt(key, player.cipherText)
				context["plain"] = decr
				context["encrypted"] = player.cipherText
				context["freq"] = freq(player.cipherText)
				context["member"] = request.user.username
				if decr == player.plainText:
					request.user.member.score += 1
					request.user.member.save()
					return HttpResponseRedirect(url+"/win")			
				return render(request, "play.html", context)
		return render(request, "playerNotFound.html")

class SolvedPuzzle(View):
	def get(self, request, url=""):
		request.user.member.score += 1
		return render(request, "win.html")

class ProfilePage(View):
	def get(self, request, url=""):
		context = {}
		context["user"] = request.user
		return render(request, "profile.html", context)

	def post(self, request, url=""):
		request.user.member.name = request.POST.get("name")
		request.user.member.key = request.POST.get("key")
		request.user.member.plainText = request.POST.get("plain")
		request.user.member.save()
		context = {}
		context["user"] = request.user
		return render(request, "profile.html", context)

class HelpPage(View):
	def get(self, request):
		return render(request, "halp.html")
			


