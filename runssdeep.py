import subprocess
import os

sign = "[2023/03/23 10:49:31] mod=mtu|cli=192.168.0.200/50317|srv=40.81.94.43/443|subj=srv|link=IPIP or SIT|raw_mtu=1480"

f = open('single_sign.txt', 'w')
f.write(sign)

stdout = subprocess.run(
    ['..\ssdeep-2.14.1\ssdeep', '-l', '.\p0f1.log', '>', 'output'], capture_output=True, shell=True).stdout.decode('utf-8')
ssdeep_result = ((open('output', 'r')).read()).splitlines()
print(stdout + "\n")
print("result:\n" + ssdeep_result[2].split(',')[0])
f.close()
os.remove('output')
