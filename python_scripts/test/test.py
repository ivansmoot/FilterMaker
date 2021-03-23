import hashlib

m1 = hashlib.md5()
m1.update('../main/template.data')
print(m1.hexdigest())
