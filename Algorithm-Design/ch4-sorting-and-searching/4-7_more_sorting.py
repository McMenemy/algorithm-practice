#a) sort checks with a nlogn algorithm by name. then go through bills bsearching the checks by last name to see if present. the runtime is nlogn + klogn where k is the string length which can be assumed constant so runtime is O nlogn

#b) iterate through once by publisher counting for each publisher (n time)

#c) without using a hash the quickest way is to sort by name then iterate through once increaseing the distinct counter everytime the name changes which is nlogn + n or O nlogn
