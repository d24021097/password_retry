password = 'a123456'
i = 3 #剩下三次機會
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼:') #要用新變數pwd
	if pwd == password: #最好輸入password而非a123456
		print('登入成功!')
		break #逃出迴圈
	else:
		print('密碼錯誤！')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('密碼錯誤三次,帳號被鎖住')