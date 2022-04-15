import os	# operating system
file_exist = False
# 讀檔
def read_file(address='ledger.csv'):
	products = []
	if os.path.isfile(address):
		file_exist = True
		with open(address, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue	# 跳到下次迴圈
				if 'Total' in line:
					continue	# 跳到下次迴圈
				name, price = line.strip().split(',')
				products.append([name, price])
	else:
		print('找不到舊帳本,本次輸入會生成新檔')
	return products
	
# user輸入
def user_input(old_data):
	while True:
		name = input("請輸入商品名稱: ")
		if name == 'q':	# quit
			break
		price = input("請輸入商品價格: ")
		p = [name, price]
		old_data.append(p)
	return old_data

# 印出帳本
def print_all(data):
	sum_p = 0
	for p in data:
		print(p[0], "的價格是: ", p[1], "元")
		sum_p += int(p[1])
	print("總共花了", sum_p, "元")
	return sum_p

# 存檔
def write_file(new_data, total, address='ledger.csv'):
	with open(address, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')	# 欄位名稱
		for p in new_data:
			f.write(p[0] + ',' + p[1] + '\n')
		f.write('Total,' + str(total))

# Main
def main():
	ledger = read_file()
	ledger = user_input(ledger)
	total_price = print_all(ledger)
	write_file(ledger, total_price)

if __name__ == '__main__':
	main()