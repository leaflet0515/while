while True:
	print('輸入指令: 1 , 2 , 3 , 離開請輸入q')
	mode = input('請輸入遊戲模式: ')
	if mode == 'q':
		print('離開遊戲')
		break
	elif mode == '1':
		print('啟動模式一')
	elif mode == '2':
		print('啟動模式二')
	elif mode == '3':
		print('啟動模式三')
	else:
		print('請重新輸入指令')
