import random

transport_time = 2

print 'Shop: Job'

for i in range(30):
	print 'Job: job{}'.format(i)
	print 'RGB: {};{};{}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	print 'Release: 0'
	print 'Due: 0'
	print 'Weight: 1'
	print 'Oper: Magazyn -> Korowanie;{};A'.format(transport_time)
	print 'Oper: Korowanie;{};A'.format(max(round(random.normalvariate(30, 9)), 0))
	print 'Oper: Korowanie -> Belki;{};A'.format(transport_time)
	print 'Oper: Belki;{};A'.format(max(round(random.normalvariate(10, 3)), 0))

	if random.random() < 0.18:
		print 'Oper: Belki -> Magazyn;{};A'.format(transport_time)
	else:
		print 'Oper: Belki -> Deski;{};A'.format(transport_time)
		print 'Oper: Deski;{};A'.format(max(round(random.normalvariate(20, 6)), 0))
		print 'Oper: Deski -> Magazyn;{};A'.format(transport_time)
