import urllib.request, urllib.parse, urllib.error

urlrequest = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in urlrequest:
    print(line.decode().strip())
