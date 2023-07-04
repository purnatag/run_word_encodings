import floret


# train vectors
model = floret.train_unsupervised(
    "p0f1.log",
    model="cbow",
    mode="fasttext",
    hashCount=2,
    bucket=50000,
    minn=3,
    maxn=6,
)

# query vector
model.get_word_vector("broccoli")

# save full model
model.save_model("vectors_ft.bin")

# export standard word-only vector table
model.save_vectors("vectors_ft.vec")

# export floret vector table
model.save_floret_vectors("vectors_ft.floret")