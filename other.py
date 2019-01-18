#coding:utf-8
rows = int(input('输入列数： '));


if(rows>100):
	print("不能超过100"); 
	exist();  #有BUIG

i = j = k = 1 #声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
#等腰直角三角形1
print("等腰直角三角形1");
for i in range(0, rows):
    for k in range(0, rows - i):
        print(" * ",); #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print ("\n");
 
#打印实心等边三角形
print("打印空心等边三角形，这里去掉if-else条件判断就是实心的");
for i in range(0, rows + 1):#变量i控制行数
    for j in range(0, rows - i):#(1,rows-i)
        print(" ",)
        j += 1
    for k in range(0, 2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:#因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print("*",)
                else:
                    print(" ",); #注意这里的","，一定不能省略，可以起到不换行的作用
            else:
               print("*",);
        else:
            print(" ",);
        k += 1
    print("\n");
    i += 1
 
#打印菱形
print("打印空心等菱形，这里去掉if-else条件判断就是实心的");
for i in range(rows):#变量i控制行数
    for j in range(rows - i):#(1,rows-i)
        print(" "),
        j += 1
    for k in range(2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2:
            print("*",);
        else:
            print(" ",);
        k += 1
    print("\n");
    i += 1
