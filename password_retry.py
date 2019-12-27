password = 'a123456'
i = 3 #剩下三次機會
while True:
	pwd = input('請輸入密碼:') #要用新變數pwd
	if pwd == password: #最好輸入password而非a123456
		print('登入成功!')
		break #逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤！還有', i, '次機會')
		if i == 0:
			print('超過登入次數3次，請過十分鐘重試')
			break