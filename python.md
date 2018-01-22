python
ubantu部分
	解释型语言，跨平台，每个平台安装不同的解释器即可
	编译型语言，因为要编译后在执行，所以快，但不跨平台
终端	打python默认是2.x解释，不支持中文
	打python3，使用python3解释器，支持中文
	例：python3 xxx.py
终端打python或python3进入python交互式终端
exit（）或按ctrl+d退出

ipython 是一个可以自动补全的交互式终端

重置pycharm
	关闭pycharm，终端运行rm -r ~/.pyCharmxxx.xx
	.pyCharmxxx.xx是其配置信息，在家目录下，用ls -la可以查到，删除即可重置
	再次打开pycharm即可


语法部分：
	//为地板除，向下取整，如果两个都是int，则求出来的仍然是int，且取整
	如果有一个是float，则结果是float
	0b代表是二进制，0o代表8机制，0x代表16进制
	bin（），可以实现其他进制向2进制转换
	oct（），可以实现其他进制向8进制转换
	int（），可以实现其他进制向10进制转换
	hex（），可以实现其他进制向16进制转换

	ord（'w'）,将字符转为ASCII码	

	布尔值，True，Flase，都必须首字母大写

	输出多行文字，例子:单双引号均可
	'''
	fdsa
	fdsaf
	'''
	加上反斜杠可以点击回车换行
	r'fjsadkk/nfdsaf',前面加多了一个r，R也可
	原始字符串，所见即所得，无转义效果

	字符串运算
		'fdsa'+'fdsaf'
		'fsafdsa'*3,会输出三遍
		'hello'[0],会输出h
		'hello'[-1],会输出o，倒数第一个
		'hello world'[0:5],截取hello，注意o的序号是4
		'hello'[0:11],会全部取出，大于最后一个字母的序数
		'hello'[0:],为空，会取到最后
		'hello'[：4],这样会从首字母开始取


	列表，list
		['dsaf',1,3,True][0]，取出第一个，且仅为内容
		['dsaf',1,3,True][0:2],会取出列表内容，形式为列表，一个也是
		[fsdaj,fasdf,fsa]+[fdsaf,fas],会合并列表
		[s,s]*3,会输出[s,s,s,s,s,s],会重复内容3次
	元组，tuple
		（1,2，'fsdaf'）,和列表使用方法类似
		（1），（'jdsa'），都不是元组，分别是int和str
		（1，），（'fasd',）,才是元组，（）代表空元组
		[1],['fsa'],会被认为是list
	str，list，tuple均为序列
		3 in [1,2,3,4],判断3是否在序列中，返回True或False
		not in，用法相反
		len（[1,2,3,4]）,返回序列长度
		len（“fdsadfasd fdsa”）
		max（[1,2,3,4]），max（[fdsaafadsf]）输出最大值
		min（）输出最小值
		ord（'w'）,将字符转为ASCII码

	集合，set，无序
		{1,2,3,4}，不能使用{1,2,3,}[5],因为是无序
		{1,2,3，7,1,2}，里面重复数字会被消除
		len（{1,2,3，7}），计算长度
		2 in {1,2,3,4}，同上
		{1,2,3，4}-{1}，会剔除1，求差集
		{1,2,3}&{3}，求交集
		{1,2,3}|{1,3,4}，求并集{1,2,3,4}，并会剔除重复部分
		定义空集合方法，s=set（），若用s={}，s为dict类型
	字典，dict
		{key：value，key：value.....}
		{key1：value，key2：value.....}[key1]
		key不能重复，后者会覆盖前者
		key必须是不可变得类型

	值类型：int，str，tuple（不可改变）
	引用类型：list，set，dict（可改变）
	理解：不可改变，是每次赋值都会重新开辟新位置
			可改变，是每次复制，都会在原来位置上改变该值，变量赋值可传递
	id（变量），显示变量储存地址


	运算符
		算数运算符
			+，-，*，/，//，%，**（2**4即2的四次方）
		赋值运算符
			=，+=，-=，/=,//=,%=,**=
		比较运算符
			==，！=，>,<,>=,<=
		逻辑运算符
			and，or，not，not>and>or,优先级
		成员运算符
			in，not in
		身份运算符
			is，is not（判断位置id是否相同）
		小例子：{1,2,3}，{2,1,3}
			集合没有顺序，所以{1,2,3}=={2,1,3}返回True
			is返回False，因为储存id不同
			（1,2,3），（2,1,3）
			元组有顺序，所以都为Flase
		位运算，变成二进制后的运算
			$,|,~,^,<<左移一位,>>右移一位
	input（） 获取键盘输入
	pass,暂时占位
	条件控制
		if Ture：
			。。。
		else：
			。。。
		注意缩进形式
		if True:
			...
		elif Flase
			...
		elif True
			...
		注意嵌套级别
	a or b，可以返回a，b中为真的值
	循环控制
		while 条件：
			。。。。
		else:

		用来循环，遍历
		for target_list in express_list:
			...
		else：
			。。。在for执行完毕后执行

		执行10次
		range（0,10）函数会生成0到9的序列，0开始，结束点是10，不包括10
		range（0,10,2），第三个参数是步长
		切片第三个参数a[1:10:10],第三个也是步长
		print（。。。，end='|'）,end默认是'\n'
		for x in range（0,10）：
			print（）

		历遍key	for k in emp.keys():
             
		历遍值	for v in emp.values():
                         
		历遍key和值	for v,k in emp.items():



	包
		文件夹里面包含__init__.py才能成为一个包
		执行包内文件时，会首先自动运行__init__.py
	包里面的文件称为模块
		导入模块
			import 包名字.文件名	[as 自己气的名字]
		不能直接导入模块中的方法名
			包名字.文件名.方法名
		from 模块 import 方法名或变量名字,第二个变量名，第三个变量名
		form 模块 import *，将方法变量全部导入（不推荐）
			在导入文件头部加入，__all__=['变量名','变量名',模块名也可以]
			仅会导入__all__中的
		form 包 import 模块（不常见）

		两个模块最好不要相互引入
		import引入后等于直接把代码放入，会被执行，同时improt两次，并不会被执行两次
		from 。。。 import 变量名或变量
		会导入该变量或方法，同时会执行导入模块

		相对引用和绝对引用
			绝对引用：从顶级包，层层寻找引入
			相对引用：.代表本层，..代表上一层，...上上层
				相对引用不能超过自己的顶级包引入
			入口文件，必须使用绝对导入，因为__name__在入口文件是__main__,无法使用相对查找
		

		dir（），查看相关文件内的变量和方法
		模块内置变量
		__name__,包.文件名
		__package__，所属包
		__file__，文件路径
		__doc__,头部注释

		注意如果是执行或入口文件，则不属于任何包，name变为__main__,文件路径为何当前目录对比的，文件路径

		python -m 文件名	在模块所在文件夹内，执行，使用命名空间.的方法，会被当作模块运行
	


	函数
		自带函数
			round（数字，保留几位），同时会四舍五入
		自定义函数
			def funcname(parameter_list)
				pass
			如果函数没有return，则返回None
			可直接返回多个值，用多个逗号隔开即可，会自动成为tuple（不推荐）
			直接按相对应的逗号形式，接收返回值
			a,b,c=funcname();
			a,b,c=1,2,3;
			d=1,2,3,用的时候，会自动成为tuple
			解包，a,b,c=d
			同时python是从头到尾执行，函数定义必须在调用上面
		函数的参数
			必须参数：必须传递进来的函数
			关键字参数
				def (x,y):
					pass
				调用时
				def (y=1,x=2)
				可以自由传入参数，不用按原本顺序传入
			默认参数
				def (name,age=18,address="fdsa"):
					pass
				如果跳过一个默认参数，则后面需要指定
				def（name，address="sdfa"）
			可变参数
				def （*param）
				*的意思是解包和生成闭包
				例子
					def （1,2,3）
						参数会成为元组（1,2,3）
					如果已经是元组传入的话，可以先用解包
					a=（1,2,3）
					def （*a）
				注意def的可变参数和默认参数的传参
				函数内解包
					def （*param）：
						for i in param：
				字典可变参数传参
					def funcname(**param):
						for key,value in param.items():
							这样会获取到字典的key和value
							**这样可以传入不限个数的字典，可以理解为生成字典
							a={'a'='A',b='B'}
							本来就是字典可以用**解包再传入def （**a）
				可变参数可以什么都不传

	作用域
		函数内部是局部作用域，for，if均无块级作用域
		全局变量，global
			先定义，后使用
				global c
				c=2

	变量小写，用下划线连接
	面向对象，对象名，首字母大写并且使用驼峰法
		类只负责描述，并不执行内部方法
		class Student（）：
			name=''
			age=''
			def funcname（self）：	注意括号里，必须加上self
				self.name
				self.age	调用全部变量的的时候需要使用self.变量名
				pass
	实例化
		student=Student()	没有new，直接等于即可
	构造函数
		def __init__(self，[mingzi,age]);
			pass
		实例化时，构造函数会自动执行，也可以调用__init__(),很少用
		构造函数不能return，除了None
		传入参数student(xiaoming,13),传入参数不用包括self
		def __init__(self，[mingzi,age]);
			self.name=mingzi
			self.age=age
				调用类变量，赋值需要使用self
				如果没有，仅为局部变量
		变量
			类变量，实例变量
			访问类变量的时候，使用类名.类变量名
							或self.__class__.类变量名
			类变量在多次实例化过程中，并不会被重新生成，会被延续
		类或变量.__dict__,该变量会显示出内部方法和变量

		类方法
			@classmethod	增加此装饰器，确定为是类方法，用来操作类变量
			def fuctname(cls):		cls必须有
				pass

			调用方法	类名.funcname
						对象名.function 也可以，但是不推荐
		静态方法（不推荐）
			@staticmethod		没有强制传参数
			def funcname():
				pass

			对象和类均可使用静态方法，用 . 即可
	公开或私有
		在变量或方法名前加__，则被认为是私有
		其他的被认为是公开
		前后都加上__,则会被认为是公开的，例子__init__
		私有__score，其实储存的时候被改了名字，_类名__score
		所以，外部可以使用修改后的名字进行访问（不推荐）
	继承
		class 子类名（父类名）：
			调用父类方法(推荐)
				super（子类名，self）.函数名（）
			调用父类__init__
				super（子类名，self）.__init__()
			直接调用父类方法(不推荐)
				父类名.方法名（），注意因为没有实例化，需要自己传参时，写上self
			pass


	正则表达式，针对字符串
		python自带的查找
			a.index('school')
				查找a中是否含有school，没有则返回-1，有返回索引值
			school in a，有返回True，无False

		import re
		re.findall('正则表达式'，被匹配的字符串)
			返回列表[],每次匹配都会插入一次，没有则为空
		\d 表示0-9，\D字母
		a[bc]f,中间是b或c	a，f是定界，[]里是或的关系		[^bc]，^为取反，不取bc
		[c-f],匹配c到f		[0-9]匹配0到9，[^0-9],匹配非数字
		\w，数字或字符，即[A-Za-z0-9_]，包括下划线
		\W,非数字或字符，包括&，空格，换行，制表符等	注意&%$等特殊符号
		\s,空白字符，空格，换行，制表符等
		\S,非空白字符
		.匹配除换行的所有字符

		数量词
			[a-z]{3},三个字符一组的字符
			[a-z]{3，6},3到6个字符一组，倾向贪婪，即6个字符
			[a-z]{3，6}?,	非贪婪，优先3个一组
			python{1，2}，n出现1到2次均可，python{1-2}？非贪婪，1次优先
			python*，n出现0次或无限多次
			python+，n出现一次或无限多次		最后一个字母
			python？，n出现0次，或一次，	pythonn，也会被选中，但是会被截取pyhton
		界限匹配
			^\d{4,8}$	从头到尾，有4到8为数字
			^从头开始匹配，&从末尾看，匹配
			例子100000001
				用000匹配，有两个000,000
				^000匹配，从开始匹配，是000，因为开始是1，所以返回为空
				000$，从末尾匹配，是000，但检验的末尾是001，所以返回为空
		组匹配
				python{3}，三个n去匹配
				（python）{3}，python三个为一组，去匹配
		匹配模式
			re.findall('正则表达式'，被匹配的字符串,re.I|re.S)
			re.I,忽略匹配大小写
			re.S,改变.的行为，匹配换行
			上面的竖线是且
			返回列表，内容是搜索到的匹配值

			re.sub('正则表达式','替换的字符'，'被匹配的字符串'，[count]，[匹配模式])
				count:0为全部替换，1为值替换第一个，2类推
			str.replace('原本字符'，'替换字符')
			re.sub函数中，替换的字符串位置可以传入一个处理函数
			将传入一个查找结果对象
			span（6,8），match='匹配结果'
			span为初始和结束的位置，用value.group()获取到match的值
			def convert（value）：
				value.group
			
			和findall不同
			re.match('正则表达式','替换的字符'，匹配模式)，从首字母进行匹配，如果找到，返回对象
			span（6,8），match='匹配结果'
			span为初始和结束的位置，用value.group()获取到match的值
			re.search('正则表达式','替换的字符'，匹配模式)，搜索整个字符串，直到找到第一个，返回结果同上

			r=re.search('life(.*)python',字符串)
			r.group(1)可以获取到（）内部匹配的内容,	group(2)获取到第二个匹配的内容
			r.group（0）则是全部内容，包括life和后面的python
			如果是group（0,1,2），会返回元组，内容同上
			group（），则会返回出了全部内容外的匹配

			r=re.findall('life(.*)python',字符串)
			较为简单，会直接返回（）内部内容，以列表的形式


	JSON	是字符串
		反序列化
			import json
			json_str='{"name":"qiyue","age":18}'	json内部必须都是双引号，同时，字符串都要带双引号
			student=json.loads()
			返回结果是dict类型
			'[{"name":"qiyue","age":18},{"name":"qiyue","age":18}]'
			json.loads()后，会变成列表，里面包裹着dict
		序列化
			json.dumps()


	枚举，内部值因为是常量，所以最好大写
		from enum import Enum
		class funcname（Eum）：
			YELLOW=1
			GREEN=2
		
		和类的不同
		print（funcname.YELLOW）,枚举会原样打印，不会输出数值
		funcname.YELLOW.value,可以获取到值
		funcname.YELLOW.name,可以打印出枚举名字，YELLOW
		枚举类型不能在外部被改变，同时内部不能重复定义变量
		print（funcname['YELLOW']）	通过枚举名称获取
			打印出funcname.YELLOW		枚举类型

		for v in funcname：
			pass
			可以历遍所有枚举类型
				v是funcname.YELLOW

		枚举类型可以比较是否相等，但不能比大小，例子：funcname.YELLOW==funcname.GREEN
		只能在本枚举内部比相等，两个枚举中的枚举类型比较都会返回Flase

		枚举类型数值，可以相等，但是第二个相当于别名，print时，仍打印第一个名字
		数值相等时，for历遍时，第二个别名不会被打印出来
		如果想打印出来
		for v in funcname.__member__.items():
			值重复的别名也会被打印出来
		funcname（value）会返回相对应的枚举类型funcname.YELLOW

		枚举类型Enum，IntEnum，unique
		IntEnum，值只能是int
		from enum import unique
		@unique	里面的值不允许相同
		class funcname（Enum）：
			pass

	闭包
		def funcname1（）:
			a=25
			def funcname2(x):
				return a*x
			return funcname2
		上面整个函数是一个闭包
		闭包保存了内部函数和函数定义时的环境变量
		闭包返回的函数.__closure__,该属性标示闭包保存的函数和环境变量
			在闭包中，nonlocal，声明不是局部变量
			def factory(pos):
				def go(step):
					nonlocal pos		如果没有这一行，pos会被认为是先使用后定义，会被认为是错的
					new_pos=pos+step		因为读到pos，会在内部环境搜索，发现有pos，但在后面，于是被认为是错的
					pos=new_pos				只有加上nonlocal pos，才表明pos是外部变量
					return new_pos			闭包在使用过程中，外部变量会被保存下来
				return go
			travel=factory(1)
			travel(2)
			travel(3)
	python 三元表达式
		x if x>y else y

	map对象
		map（执行函数名，列表或元组）
		列表中每个数，都执行那个函数

	匿名函数，lambda表达式
		lambda	x,y : x+y
			冒号后面会自动返回，同时后面内容只能是表达式，不能是个代码块
		lambda x,y:a=x+y
			后面不是表达式，会返回错误
		
		调用方式（不推荐这个调用方法）
		f=lambda x,y : x+y
		f（x,y）

	结合map进行使用
		r=map(lambda x,y : x+y,list_x,list_y)
	后面list_x和list_y分别对应前面应该传入的参数x，y
	如果有一个列表长度不一，以短的为准，多余的将不会被使用
	r是一个map对象，list（r）之后，才会变成列表


	reduce	直接返回结果
		from functool import reduce
		list_x=[1,2,3,4,5]
		r=reduce(lambda x,y:x+y,list_x)
		print(r)
		x,y两个参数，第一次取前两个值，结果会被当作下一次的x，y为第三个，以此类推
		reduce（执行函数或函数名，列表，[初始值]）
	filter	过滤，返回对象，需要用list格式化
	filter(lambda x:True if x==1 else False,序列)
	第一个函数需要返回真假，如果为真则保留，如果为假，则删除


	装饰器
		定义方法
		def decorator(func):
			def wrapper(*arg,**kw):
				pass
			func(*arg,**kw)
			return wrapper 
		*arg,普通参数，个数不限，（元组）
		**kw，关键字参数，个数不限，（字典）

		使用
		在对应函数前
		@decorator


	爬虫
		明确目的
		找到数据对应的网页
		分析页面的结构，找到数据所在页面标签的位置

		模拟请求，向服务器发送这个请求，获取到服务器返回的HTMl
		用正则表达式，获取所需数据