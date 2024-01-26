from modules import preparation as prep

data = prep.prepare_file()
for idx in data:
    print(idx, "\t", data[idx])
