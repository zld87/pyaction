import re
import random, time
import sys

Nameage = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)
print(names)
ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1
print(ageDict)

c = "a1a1"
num = re.match(r"^(.)(\d+)\1\2$", c)
print(num.groups()[0])

ds = "s dfsfda1232fsda dfa3232dsffsdf"
se = re.search("^s dfsf", ds)
print(se.group())
ws = re.match(r".+?\bdf\B", ds)
print(ws.group())

ss = r"\tdf\t"
print(ss)


value = time.time()
value = format(value, '.0f')
print(type(value))
o = random.choice(["a1", "a2", "a3", "a4"])
print(type(o))

zzz = '''
\n我是短\n发短发\t地方范德萨7887898*&^**\n
'''

zld = re.sub("发短发", '778', zzz)
print(zld)
print(zzz.lstrip())

#re.search()

c = 0.8 % 2
d = format(c, ".2f")

print(d)

a8 = "  dfs1ewe "
print(a8.rsplit("w"))

print(sys.argv)

a = "1234"

print(re.match(r'(\d+)', a))
a=[{"zhou":"123", 'Database':"123"},{"liu":"456","Database":"456"}]
dbs = [x['Database'] for x in a]
print(dbs)
