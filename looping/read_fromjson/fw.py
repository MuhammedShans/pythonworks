from json import load
# open(path,node,encoding)
path="C:/Users/abhij/Desktop/python_work/looping/read_fromjson/data.json"

with open(path) as f:
    records=load(f)
#for f in records:
# print(f.get("name"))    

fw_names=[f.get("name") for f in records]

print(fw_names)

top_fw=max(records,key= lambda d:d.get("rating"))

print(top_fw)

# frontend framework names
