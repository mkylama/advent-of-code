import requests
from datetime import datetime

session = ''

today = datetime.today()

r = requests.get('https://adventofcode.com/2019/day/{}/input'.format(today.strftime('%e').strip()), cookies={'session': session})

open('input/{}.txt'.format(today.strftime('%d').strip()), 'wb').write(r.content)