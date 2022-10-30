import datetime
x=datetime.datetime.now()
print(x)
print('%a',x.strftime('%a')) # day in sort
print('%A',x.strftime('%A')) # day full form
print('%b',x.strftime('%b')) # month name
print('%B',x.strftime('%B')) # month full form
print('%d',x.strftime('%d')) # date in sort 
print('%D',x.strftime('%D')) # date in full form
print('%f',x.strftime('%f')) # micro seconds
print('%F',x.strftime('%F')) # full date without time
print('%h',x.strftime('%h')) # month name in sort 
print('%H',x.strftime('%H')) # Time hour 24hrs format
print('%j',x.strftime('%j')) # shows seconds
print('%m',x.strftime('%m')) # month in neumeric form 
print('%M',x.strftime('%M')) # minute of current hour
print('%S',x.strftime('%S')) # shows second 
print('%U',x.strftime('%U')) # shows week of the year
print('%p',x.strftime('%p')) # shows AM/PM
print('%Y',x.strftime('%Y')) # shows year
print('%w',x.strftime('%w')) # weekdays #