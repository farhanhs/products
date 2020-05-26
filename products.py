import os


products = []
if os.path.isfile('products.csv')
 print('check')
    with open('products.csv','r',encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue #將項目主題這行跳過
       name,price = line.strip().split(',') #切割後面寫入的檔案變成二維清單
       products.append([name,price])
else 
    print("error file")
while True:
    name = input('商品名稱')
    if name == 'q':
        break
    price = input('價格')
    price = int(price)
    p = [name,price]
    products.append(p)
print(products)

for p in products:
    print(p[0],'的價格是',p[1])

with open('products.csv','w',encoding='utf-8') as f:
    f.write('商品,價格\n')  #csv use"," to divide items
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n")