import tlsh

sign1 = "[2023/03/23 10:49:31] mod=mtu|cli=192.168.0.200/50317|srv=40.81.94.43/443|subj=srv|link=IPIP or SIT|raw_mtu=1480"
sign2 = "[2023/03/23 10:49:31] mod=mtu|cli=192.168.0.200/50317|srv=40.82.94.43/443|subj=srv|link=IPIP or SIT|raw_mtu=1480"
sign3 = "[2023/03/23 12:19:34] mod=syn+ack|cli=192.168.0.200/50181|srv=198.252.206.25/443|subj=srv|os=???|dist=23|params=tos:0x0a|raw_sig=4:41+23:0:1460:mss*20,9:mss,sok,ts,nop,ws:df:0"

h1 = tlsh.hash(bytes(sign1, 'utf8'))
h2 = tlsh.hash(bytes(sign2, 'utf8'))
h3 = tlsh.hash(bytes(sign3, 'utf8'))

score1 = tlsh.diff(h1, h2)
score2 = tlsh.diff(h1, h3)

print(f"The hashes are:\n {h1} \n {h2} \n {h3}")
print("Difference between the hashes with 1 change:", score1)
print("Difference between the hashes with multiple changes:", score2)

h4 = tlsh.Tlsh()
with open('p0f1.log', 'rb') as f:
    for buf in iter(lambda: f.read(512), b''):
        h4.update(buf)
    h4.final()
# this assertion is stating that the distance between a TLSH and itself must be zero
assert h4.diff(h4) == 0
score = h4.diff(h1)
print("file hash:", h4, "\n")
print("Difference between hash of the whole file vs a signature:", score)
