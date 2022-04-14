products = []
sum_p = 0
while True:
	name = input("請輸入商品名稱: ")
	if name == 'q':	# quit
		break
	price = input("請輸入商品價格: ")
	p = [name, price]
	products.append(p)
for p in products:
	print(p[0], ": ", p[1], "元")
	sum_p += int(p[1])
print("總共花了", sum_p, "元")