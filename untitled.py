def minpass(p):
	lower = [x for x in p if x.islower()]
	upper = [x for x in p if x.isupper()]
	num = [x for x in p if x.isdigit()]

	if (len(lower) > 0) and (len(upper) > 0) and (len(num)) > 0:
		return True
	else: 
		return False

def prating(p):
	schr = [".", "?", "!", "&", "#" ",", ";", ":", "-", "_", "*"]
	score = 0

	lower = len([x for x in p if x.islower()])
	upper = len([x for x in p if x.isupper()])
	num = len([x for x in p if x.isdigit()])
	sch = len([ch for ch in p if ch in schr])

	if lower > 0:
		score += 2
	if upper > 0:
		score += 2
	if num > 0:
		score +=3
	if sch > 0:
		score +=3
	return score

	

print minpass('29809285')
print minpass('29a09285')
print minpass('aaaaaaa')
print minpass('AAAAAAA')
print 
print minpass('popA23')
print minpass('29aB9285')

print prating('29809285')
print prating('29a09285')
print prating('aaaaaaa')
print prating('AAAAAAA')
print prating('popA23')
print prating('29aB9285')
print prating('123abcDE.G')
