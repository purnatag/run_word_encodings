import floret
import numpy as np

# train vectors
model = floret.train_unsupervised(
    "p0f1.log",
    model="cbow",
    mode="floret",
    hashCount=2,
    bucket=50000,
    minn=3,
    maxn=6,
)
sign1 = "[2023/03/23 10:49:31] mod=mtu|cli=192.168.0.200/50317|srv=40.81.94.43/443|subj=srv|link=IPIP or SIT|raw_mtu=1480"
sign2 = "[2023/03/23 10:49:31] mod=mtu|cli=192.168.0.200/50317|srv=40.82.94.43/443|subj=srv|link=IPIP or SIT|raw_mtu=1480"
sign3 = "[2023/03/23 12:19:34] mod=syn+ack|cli=192.168.0.200/50181|srv=198.252.206.25/443|subj=srv|os=???|dist=23|params=tos:0x0a|raw_sig=4:41+23:0:1460:mss*20,9:mss,sok,ts,nop,ws:df:0"
# query vector
# print(model.get_word_vector("broccoli"))

array1 = model.get_word_vector(sign1)
array2 = model.get_word_vector(sign2)
array3 = model.get_word_vector(sign3)

diff1 = np.setdiff1d(array1, array2)
diff2 = np.setdiff1d(array1, array3)

print(
    f"Diff for a single change:\n {diff1} \n Diff for multiple changes:\n {diff2}")

# save full model
model.save_model("vectors_ft.bin")

# export standard word-only vector table
model.save_vectors("vectors_ft.vec")

# export floret vector table
model.save_floret_vectors("vectors_ft.floret")
