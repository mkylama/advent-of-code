import requests
from datetime import datetime
from pprint import pprint as pp

session = 'SESSIONTOKEN HERE'

today = datetime.today()

r = requests.get('https://adventofcode.com/2021/day/{}/input'.format(today.strftime('%e').strip()), cookies={'session': session})

open('input/{}.txt'.format(today.strftime('%d').strip()), 'wb').write(r.content)