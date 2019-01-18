#!/usr/bin/env python3 
#!/usr/bin/python
#coding=utf-8

import sys;

print('hello,world');print('test'); 
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"];

#多个引号
word = 'word';
sentence = "一句话"
paragraph = """第一句话
第二句话
第三句话
完整的段落""";

one = 1;
two = 2;
three = 3;

#多行语句 使用\将语句分多行进行显示
total = one+\
        two+\
		three;
	
#3种Python注释方式
	
#1.我是单行注释

'''
2.多行注释，使用'
'''

"""
3.多行注释使用 "
"""

#等待用户输入
#input("按下 enter 键退出，其他任意键显示...\n");

x = "runoob";
sys.stdout.write(x+"\n"+"write测试");

x = "a";
y = "b";

#换行输出
print ("\n",x);
print (y);
#不换行输出
print (x,y),

flag = 3+2==5;
if flag:
	print('是的')
	print('的确是的')
else :
	print('不是')
	print('的确不是的')

#申明变量
q,w,e = 1,2,3;

var1 =1 ;
var2 = 2;
del var1;
#print(var1)

#字符串操作
vars = "我是字符串1234567890";
print('获取的字符串中文部分:',vars[0:5]);
print(vars * 2)
print(vars + "2")

#列表和元数组
list = [1,2,3,4,5];
tuple = (1,"2",list);
list[0] = 100;
#tuple[0] = 100; #不允许更新元数组

#字典
dict = {};
dict["one"] = "this is one";
dict[2] = "this is two"; 
dict2 = {"name":"张三","age":"24岁"};

#打印 列表  元数组  字典(是无序的)
print('字典:',dict);
print('列表',list);
print('元数组',tuple);

#数据的转换
inta = 188;
print("转换188为十六进制:",hex(inta));
print("转换188为八进制:",oct(inta));

#Python算数运算符
#+ - * / % **（返回x的y次幂）  //取整除 返回商的整数部分(向下取整)
print(2**3);
print(9//2);

#Python比较运算符 == !=(是否相等) <>(对象是否相等) < <= > >=
a  =3;
b = "3";

if a != b:
	print("a!=b")
# elif a <> b:
	  # print("a<>b"); # 语法不支持了
else:
	print('不知道了');
 
#Python位运算符
pa = 60; #0011 1100
pb = 13; #0000 1101
pc = 0;

rc = pa & pb;
print(rc)
rc = pa | pb;
rc = pa ^ pb;
rc = pa << 2;
rc = pa >> 2;

a = 10;
b = 20;

#逻辑运算符
if a and b :
	print("AND true");
else :
	print(" AND false");
	
if a or b :
	print("OR true");
else :
	print(" OR false");
	
if not(a or b) :
	print("NOT true");
else :
	print("NOT false");
	
#Python成员运算符
list = [1,2,3,4,5];
if(5 in list) :
	print('5成员存在');
else :
	print('5不在成员中');

if(50  not in list) :
	print('50不在成员存在');
else :
	print('50在成员中');
	
a = 188;
b = 188;

if( a is b ):
	print('a,b有相同的标识');
else:
	print('a,b没有相同的标识');
	
if( id(a) == id(y) ):
	print('a,b有相同的标识(id)');
else:
	print('a,b没有相同的标识(id)');

#追星while

numbers = [12,37,5,42,8,3];
event = [];
odd = [];
while(  len(numbers) > 0):
	number = numbers.pop();
	if(number % 2 == 0):
		event.append(number);
	else:
		odd.append(number);

print(event,"|-|",odd);

#continue 和 break
i =1;
while i<10:
	i+=1;
	if(i == 10):
		print('结束continue，break');
		break;
	
	if i % 2 > 0:
		continue;
	else:
		print("输出;",i);  

#无限循环可以使用 ctr + c 终止

while (False):
	print("执行主体");
else:
	print('while也存在else');

#如果只有一条执行语句可以直接在while后面书写
#while(flag):print("一句话直接写");

#Python执行 for in 循环
  
fruits = ["banana","apple","mango"];

for  fruit in fruits:
	print('当前的水果:'+fruit);

for index in range(len(fruits)):
	print("当前的水果通过索引:",fruits[index]);
 

for num in range(10,20):
	for i in range(2,num):
		if num % i == 0:
			j = num/i;
			print("%d等于%d*%d"%(num,i,j));
			break;
	else:
		print(num,"是一个质数");

















































