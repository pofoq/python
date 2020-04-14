# Task 2
TimeInSeconds = input("Enter Time in Seconds: ")

TimeInSeconds = int(TimeInSeconds)

hh = TimeInSeconds // 3600
nn = (TimeInSeconds % 3600) // 60
ss = (TimeInSeconds % 3600) % 60

if hh < 10:
    hh = '0{}'.format(hh);
if nn < 10:
    nn = '0{}'.format(nn);
if ss < 10:
    ss = '0{}'.format(ss);

print("{}:{}:{}".format(hh, nn, ss))

