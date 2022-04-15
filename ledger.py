import os	# operating system
products = []
sum_p = 0
if os.path.isfile('ledger.csv'):
	# 讀檔
	with open('ledger.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue	# 跳到下次迴圈
			if 'Total' in line:
				continue	# 跳到下次迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('找不到舊帳本,本次輸入會生成新檔')
	
# user輸入
while True:
	name = input("請輸入商品名稱: ")
	if name == 'q':	# quit
		break
	price = input("請輸入商品價格: ")
	p = [name, price]
	products.append(p)

# 印出帳本
for p in products:
	print(p[0], "的價格是: ", p[1], "元")
	sum_p += int(p[1])
print("總共花了", sum_p, "元")

# 存檔
with open('ledger.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')	# 欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
	f.write('Total,' + str(sum_p))