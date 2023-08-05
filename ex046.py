from time import sleep
import emoji
print ('Irá começar a estoura de fogos em:')
for c in range (10, -1, -1):
    print (c)
    sleep (0.5)
print(emoji.emojize('BOOMMM!! :boom:', language='alias'))