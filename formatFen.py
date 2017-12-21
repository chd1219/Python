import redis
import math

r=redis.StrictRedis(host='47.96.28.91', port=8641, db=0, password='jiao19890228')
w=redis.StrictRedis(host='localhost', port=8642, db=0, password='jiao19890228')
key = r.randomkey()
keys = r.keys()  
for key in keys:
    if w.exists(key):
        continue
    else:
        try:  
            infos = r.lrange(key,0,-1)
            str = ''  
            for info in infos:
                args = info.split(' ')
                size = len(args)       
                for i in range(size):
                    if args[i] == 'depth':
                        str += args[i+1]+','
                    if args[i] == 'score':
                        str += args[i+1]+','
                        break
                args = info.split(' pv ')
                str += args[1]+'|'
            w.lpush(key,str)
        except:
            print key+"error"

        

