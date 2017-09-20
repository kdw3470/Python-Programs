import urllib.request

url = "http://www.newsis.com/view/?id=NISX20170915_0000097186&cID=10101&pID=10100"


f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')
Start = data.find('니콜라스')
End = data.find('키우고 있다')



print(data[Start:End])










