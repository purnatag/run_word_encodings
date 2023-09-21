import tlsh
sign2 = "[2023/03/23 12:19:34] mod=syn+ack|cli=192.168.0.200/50181|srv=198.252.206.25/443|subj=srv|os=???|dist=23|params=tos:0x0a|raw_sig=4:41+23:0:1460:mss*20,9:mss,sok,ts,nop,ws:df:0"
h1 = tlsh.hash(bytes(
    "[2023/03/23 10:49:31] mod=mtu|cli=192.168.0.200/50317|srv=40.81.94.43/443|subj=srv|link=IPIP or SIT|raw_mtu=1480", 'utf8'))
# h2 = tlsh.hash(bytes(
#    "[2023/03/23 10:49:31] mod=mtu|cli=192.168.0.200/50317|srv=40.81.94.43/443|subj=cli|link=IPIP or SIT|raw_mtu=1480", 'utf8'))
h2 = tlsh.hash(bytes(sign2, 'utf8'))
score = tlsh.diff(h1, h2)
print("The hashes are:\n", h1, "\n", h2, "\n")
print("Difference between the hashes:", score)

h3 = tlsh.Tlsh()
with open('p0f1.log', 'rb') as f:
    for buf in iter(lambda: f.read(512), b''):
        h3.update(buf)
    h3.final()
# this assertion is stating that the distance between a TLSH and itself must be zero
assert h3.diff(h3) == 0
score = h3.diff(h1)
print("file hash:", h3, "\n")
print("Difference between hash of the whole file vs a signature:", score)
