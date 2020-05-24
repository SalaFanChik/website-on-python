import vk_api
import json
import time
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import shutil
import sys
import os
import requests
from datetime import datetime
from config import swears


group = '184553679'
vk_session = vk_api.VkApi(token='925faf18494751f1ff19ccba9a7aed1b2190b02c360ebb9d5ff7f5f3f0b1124778fbc0bd67a83bf84eecb')
longpoll = VkBotLongPoll(vk_session, group)
vk = vk_session.get_api()



warn_count = 3 

def kickss():
	a = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	spisok = []
	for member in a:
		b = member['member_id']
		if b < 0:
			pass 
		else:
			spisok.append(b)
	for mem in spisok:
		usersget = vk.users.get(user_ids=int(mem))
		for userinfo in usersget:
			c = userinfo['first_name']
			cc = c.lower()
			try:
				if cc == kick:
					Vid = userinfo.get('id')
			except:
				vk.messages.send(chat_id=event.chat_id, message='Такого юзера в беседе',  random_id=random.randint(-2147483648, +2147483648))


	if Vid in spisok:
		vk.messages.removeChatUser(chat_id=event.chat_id, member_id=f'{Vid}')
	elif not Vid in spisok:
		vk.messages.send(chat_id=event.chat_id, message='Такого юзера в беседе',  random_id=random.randint(-2147483648, +2147483648))


def kicks():
	FirstGetMembers = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	spisokMembers = []
	for member in FirstGetMembers:
		b = member['member_id']
		if str(b).startswith('-'):
			pass 
		else:
			spisokMembers.append(b)
	if int(kick) in spisokMembers:
		vk.messages.removeChatUser(chat_id=event.chat_id, member_id=f'{kick}')
	elif not int(kick) in spisokMembers:
		vk.messages.send(chat_id=event.chat_id, message='Такого юзера в беседе',  random_id=random.randint(-2147483648, +2147483648))

def kicksss():
	ev = event.raw.get('object')
	evs = ev.get('reply_message')
	evt = evs.get('from_id')
	getmems = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	spisochek = []
	for man in getmems:
		b = man['member_id']
		if str(b).startswith('-'):
			pass 
		else:
			spisochek.append(b)
	if evt in spisochek:
		vk.messages.removeChatUser(chat_id=event.chat_id, member_id=f'{evt}')
	elif not evt in spisochek:
		vk.messages.send(chat_id=event.chat_id, message='Такого юзера в беседе',  random_id=random.randint(-2147483648, +2147483648))

def main():
	chat_id = event.chat_id
	blacklist = []
	users = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	for i in users:
		i['warn'] = 0
		a = i.get('is_admin')
		if a == True:
			i['role'] = 3
		else:
			i['role'] = 0

	chats = {
		'chat_id': chat_id,
		'blacklist': blacklist,
		'users': users,
	}


	

	
	try:

		data = json.load(open('persons.json'))

			

	except:
		data = []

	
	data.append(chats)

	with open('persons.json', 'w') as f:
		json.dump(data, f, sort_keys=False, skipkeys=False, indent=2, ensure_ascii=False)

	


def evcheck():
	mainEv = event.raw.get('object')
	try:
		secEv = mainEv.get('action')
		thirdEv = secEv.get('type')
		fourEv = secEv.get('member_id')
		if fourEv == -184553679:
			vk.messages.send(chat_id=event.chat_id, message=f"Привет. я чат бот чтобы начать пропишите '!update' ", random_id=random.randint(-2147483648, +2147483648))
		elif thirdEv == 'chat_invite_user':
			vk.messages.send(chat_id=event.chat_id, message=f'Привет', random_id=random.randint(-2147483648, +2147483648))
	except:
		'''try:
			checkingev = mainEv.get('text')
			lst = checkingev.split()
			for word in lst:
				if word in swears or checkingev in swears:
					info = json.load(open('persons.json'))
					for warning in info:
						chats_id = warning['chat_id']
						if chats_id == event.chat_id:
							warns = warning['users']
							for war in warns:
								wa = war['member_id']
								if wa == event.object.from_id:
									aw = war['warn']
									if aw < warn_count:
										vk.messages.removeChatUser(chat_id=event.chat_id, member_id=f'{wa}')
										vk.messages.send(chat_id=event.chat_id, message=f'&#128078; ты получил warn за слово {word} {aw}/{warn_count}', random_id=random.randint(-2147483648, +2147483648))		
									else:
										vk.messages.send(chat_id=event.chat_id, message=f'&#128078; ты получил warn за слово {word} {aw}/{warn_count}', random_id=random.randint(-2147483648, +2147483648))		
								
		except Exception as e:
			vk.messages.send(chat_id=2, message=f'{e}', random_id=random.randint(-2147483648, +2147483648))		'''
													
			
def godmod():
	convuser = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	foradm = []
	for big in convuser:
		b = big['member_id']
		if b < 0:

			pass 
		else:
			foradm.append(b)
	
	if int(god) in foradm:
		vk.messages.send(chat_id=event.chat_id, message="Выдался +1 чтобы проверить напишите '!админы'",  random_id=random.randint(-2147483648, +2147483648))

		adm = json.load(open('persons.json'))
		for ads in adm:
			ss = ads['users']
			ass = ads['chat_id']
			chat_id = event.chat_id
			if ass == chat_id:
				for pull in ss:
					p = pull['member_id']
					sysd = pull['role']

					if p == int(god) and sysd < 3:
						pull['role'] += 1
					else:
						pass

			
		with open('persons.json', 'w') as f:
		    json.dump(adm, f, sort_keys=False, skipkeys=False, indent=2, ensure_ascii=False)
	
	elif not int(god) in foradm:
		vk.messages.send(chat_id=event.chat_id, message='Такого юзера в беседе',  random_id=random.randint(-2147483648, +2147483648))


def getadmins():
	amd = json.load(open('persons.json'))
	zoo = []
	for adms in amd:
		chat_id = adms['chat_id']
		if chat_id == event.chat_id:
			oooo = adms['users']
			for ooo in oooo:
				oo = ooo['member_id']
				o = ooo['role']
				sko = []
				if oo < 0:
					pass
				elif oo > 0:
					usersgetss = vk.users.get(user_ids=oo)
				
				for userinfo in usersgetss:
					c = userinfo['first_name']
				
				css = {
					c: o 
				}
				
				if o == 0:
					pass
				else:
					zoo.append(css)


		else:
			pass
	

	b = json.dumps(zoo, indent=1, ensure_ascii=False)
	vk.messages.send(chat_id=event.chat_id, message=f'Все админы:{b}',  random_id=random.randint(-2147483648, +2147483648))
		

def modgod():
	ve = event.raw.get('object')
	sve = ve.get('reply_message')
	tve = sve.get('from_id')
	smemget = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	spisoksec = []
	for nam in smemget:
		b = nam['member_id']
		if b < 0:
			pass 
		else:
			spisoksec.append(b)
	
	if tve in spisoksec:
		vk.messages.send(chat_id=event.chat_id, message='успешно добавил',  random_id=random.randint(-2147483648, +2147483648))
		admtree = json.load(open('persons.json'))
		for adssec in admtree:
			sssec = adssec['users']
			saa = adssec['chat_id']
			chatik_id = event.chat_id
			if saa == chatik_id:
				for lupp in sssec:
					wee = lupp['member_id']
					ssys = lupp['role']

					if wee == tve and ssys < 3:
						lupp['role'] += 1
					else:
						pass
		with open('persons.json', 'w') as f:
		    json.dump(admtree, f, sort_keys=False, skipkeys=False, indent=2, ensure_ascii=False)
		
	elif not tve in spisoksec:
		vk.messages.send(chat_id=event.chat_id, message='возникла проблема отпишитесь админу',  random_id=random.randint(-2147483648, +2147483648))

def modban():
	FirstGetMembers = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	spisokMembers = []
	for member in FirstGetMembers:
		b = member['member_id']
		if b < 0:
			pass 
		else:
			spisokMembers.append(b)
	if int(kick) in spisokMembers:
		try:
			vk.messages.removeChatUser(chat_id=event.chat_id, member_id=f'{kick}')
			aban = json.load(open('persons.json'))
			for bani in aban:
				fban = bani['chat_id']
				chid = event.chat_id
				if fban == chid:
					bang = bani['blacklist']
					bang.append(kick)
				else:
					pass

			with open('persons.json', 'w') as f:
			    json.dump(aban, f, sort_keys=False, skipkeys=False, indent=2, ensure_ascii=False)
				
		except Exception as e:
			vk.messages.send(chat_id=event.chat_id, message=f'предлогаю убрать его из админов [id{kick}|АААА]',  random_id=random.randint(-2147483648, +2147483648))




	elif not int(kick) in spisokMembers:
		vk.messages.send(chat_id=event.chat_id, message='Такого юзера в беседе',  random_id=random.randint(-2147483648, +2147483648))




def banmod():
	ev = event.raw.get('object')
	evs = ev.get('reply_message')
	evt = evs.get('from_id')
	getmems = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
	spisochek = []
	for man in getmems:
		b = man['member_id']
		if str(b).startswith('-'):
			pass 
		else:
			spisochek.append(b)
	if evt in spisochek:
		try:
			vk.messages.removeChatUser(chat_id=event.chat_id, member_id=f'{evt}')
			aban = json.load(open('persons.json'))
			for bani in aban:
				fban = bani['chat_id']
				chid = event.chat_id
				if fban == chid:
					bang = bani['blacklist']
					bang.append(evt)
				else:
					pass

			with open('persons.json', 'w') as f:
			    json.dump(aban, f, sort_keys=False, skipkeys=False, indent=2, ensure_ascii=False)
				
		except Exception as e:
			vk.messages.send(chat_id=event.chat_id, message=f'предлогаю убрать его из админов [id{evt}|АААА]',  random_id=random.randint(-2147483648, +2147483648))


	elif not evt in spisochek:
		vk.messages.send(chat_id=event.chat_id, message='Такого юзера в беседе',  random_id=random.randint(-2147483648, +2147483648))




for event in longpoll.listen():
	evcheck()
	if event.type == VkBotEventType.MESSAGE_NEW and event.obj['text']:
		msg = event.object.text.lower()
		if msg == 'привет':
			vk.messages.send(chat_id=event.chat_id, message=f'О', random_id=random.randint(-2147483648, +2147483648))
		elif msg == '!update':
			main()
		elif msg == 'пинг':
			vk.messages.send(chat_id=event.chat_id, message='ПОНГ(пока только так потом сделаю)', random_id=random.randint(-2147483648, +2147483648))
		elif '+адм' in msg:
			try:
				god = msg.replace("+адм ", "").split('|')[0].replace("[id", "")
				godmod()
			except:
				modgod()
		elif '-адм' in msg:
			try:
				god = msg.replace("+адм ", "").split('|')[0].replace("[id", "")
				ungodmod()
			except:
				unmodgod()


		elif msg == '!админы':
			getadmins()
			'''admcheck = json.load(open('persons.json'))
			for q in admcheck:
				z = q['chat_id']
				zq = q['users']
				if z == event.chat_id:
					for i in zq:
						zqs = i['member_id']
						if zqs == event.user_id:
							zqss = zq['role']
							if zqss > 0:
								getadmins()
							else:
								vk.messages.send(chat_id=event.chat_id, message='доступа к команде нету',  random_id=random.randint(-2147483648, +2147483648))'''

		
		elif '!кик' in msg:
			amdsec = json.load(open('persons.json'))
			kick = msg.replace("!кик ", "").split('|')[0].replace("[id", "")
			if msg == '!кик':
				kicksss()
				banmod()
			else:
				try:
					if kick.isdigit():
						kicks()
						modban()
					elif not kick.isdigit():
						kickss()
					elif msg == '!кик':
						kicksss()

				except Exception as e:
					vk.messages.send(chat_id=event.chat_id, message=f'Такого юзера в беседе нет, если есть отпишитесь админу {e}',  random_id=random.randint(-2147483648, +2147483648))
					vk.messages.send(chat_id=2, message=f'Хозяин тут ошибка {e}',  random_id=random.randint(-2147483648, +2147483648))


		elif '!бан' in msg:
			amdsec = json.load(open('persons.json'))
			kick = msg.replace("!бан ", "").split('|')[0].replace("[id", "")
			if msg == '!бан':
				banmod()
			else:
				try:
					if kick.isdigit():
						modban()

					else:
						pass

				except Exception as e:
					vk.messages.send(chat_id=event.chat_id, message=f'Такого юзера в беседе нет, если есть отпишитесь админу {e}',  random_id=random.randint(-2147483648, +2147483648))
					vk.messages.send(chat_id=2, message=f'Хозяин тут ошибка {e}',  random_id=random.randint(-2147483648, +2147483648))


		
'''
GetInfo = vk.groups.getLongPollServer(group_id=group, v=5.8)
key = GetInfo.get('key')
server = GetInfo.get('server')
ts = GetInfo.get('ts')'''


'''while True:
	r = requests.get(f'{server}?act=a_check&key={key}&ts={ts}&wait=3').json()

	if r.get('failed') is not None:
		key = api.groups.getLongPollServer(group_id=group_id, v=5.8)['key']
	if ts != r.get('ts') and r.get('updates'):

		if r.get('updates')[0]['type'] == 'message_new':

				msg = r.get('updates')[0]['object']['text']
				peer_id = r.get('updates')[0]['object']['peer_id']
				vId = r.get('updates')[0]['object']['from_id']
				time = r.get('updates')[0]['object']['date']
				ttime = datetime.now().timestamp()'''