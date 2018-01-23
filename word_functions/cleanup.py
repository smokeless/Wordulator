'''clean up stuff i pulled from web'''
s = ''
with open('homonyms.py', 'r') as e:
    s = e.read()
s = s.split()
s = dict(zip(s[::2], s[1::2]))
for k, v in s.items():
    print("'"+k+"'" + ':' + "'"+v+"'" + ',')
