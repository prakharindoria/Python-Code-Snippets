t=input("Type a  string")
s=t.lower()
alll="abcdefghijklmnopqrstuvwxyz1234567890"
for c in alll:
    d={c:s.count(c) for c in s}
dt=sorted(d.items(), key=lambda x: x[1], reverse=True)
for k,v in dt.items():
    print(k,":",v)
