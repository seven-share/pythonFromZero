ls list 展示目录下的文件
pwd print work directory 展示工作文件夹
cd change director 切换目录
mkdir make directory 新建目录
touch 如果文件不存在，新建该文件
注意：是文件还是文件夹
rm remove 删除文件
clear 清除终端命令行
command --help 查找某个命令的帮助
man command 查找命令手册，man是manual手册的缩写
	空格是查看下一页
	回车是查看下一行
	b是查看上一屏 back
	p是查看下一屏和空格效果一样 forward
	q退出手册 quit
tab键可根据已打入的字母自动补全，如果有重复，再按一次tab键，会有提示
按上下光标键可选择之前的命令
.代表当前文件夹
..代表上一级目录
绝对路径：从/开始
相对路径：前面没有/
在同一目录下，文件和文件夹都不可以重名

ls
	创建文件如果第一个字符是.，这表示创建隐藏文件
	ls -a 则会展示所有文件，包括隐藏文件
	-l 查看文件详细信息
	配合-l加上-h可显示文件大小
	可使用-lha，这样一起使用
	搜索使用通配符，方便搜索
		×代表任意数量的字符
		？代表一个字符
		[]选择中括号里的任意一个匹配即可
			例子：[1-4]可选择1-4中任意一个数字匹配
cd
	cd 或cd ~ 跳转到/home/用户文件
	cd .保持当前目录不变
	cd ..跳转到上一级目录
	cd -在最近两次工作目录之间跳转
touch
	创建文件，如果已经存在，则会改变末次文件修改时间
mkdir
	连续创建多个目录：mkdir -p a/b/c/d.....
rm
	rm -f ..强制删除
	rm -r ..reculsive强制删除
	rm 也可以使用通配符选择文件，同搜索
tree
	tree直接回车查看所在文件夹内的文件树
	tree 文件夹名 查看该文件夹内的文件树
	tree -d 只显示目录
cp	cp 源文件位置 目标位置
	cp -i 源文件 目标文件 如果文件名字一样，一般会直接覆盖，如果用-i则会有提示是否覆盖（推荐）
	复制到目标位置，如果加上文件名，则复制过来后会同时改名字
	cp -r 这样才能复制目录，同样可以改名字（因为不能重复，所以必须改名字）
mv	mv 源文件 目标文件位置（如果有重名会直接覆盖）文件名和目录均可
	mv -i 如果有重名，则会有是否覆盖的提示（推荐）
cat	cat 文件名	在终端打开该文件，查看 concatenate，连锁，并置
	cat -b 除去空行，标出所有行号
	cat -n 标出所有行号
more	more 文件名	在终端查看该文件，more会分页查看，每次只显示一页面（页面多的时候，推荐）
grep	grep 搜索部分 所搜索的文件
	grep -n 会显示行号	-v不显示搜索部分
	-i 忽略大小写 如果搜索内容中间有空格，则用双引号包裹起来
	模式查找 grep ^文本，搜索文本在行首，grep 文本$ 行尾的搜索
echo	会输出内容
	echo 内容 >位置 如果没有，则会直接该创建位置的文件
重定向	>将原本在终端显示的内容，写入到>指定的位置，会覆盖原有文件内容
	>>追加到指定位置
管道	将一个命令的输出结果作为另一个命令的输入
	使用|连接两个命令即可

远程管理常用命令
关机或重启	
	shutdown 选项 时间
	shutdown 默认一分钟后关机
	shutdown -c 取消关机
	shutdown now 直接关机
	shutdown 20：36
	shutdown +10 十分钟之后关机
	shutdown -r now 现在重启
	（推荐，作为服务器，一般都是重启，不会关机）
ifconfig
	查看配置信息，包括本机ip
	interface
ping ip地址 检查是否连接到该ip地址，可以输入域名参数
ip地址的别名是域名，通过端口号可以找到该机算计的某个应用程序
ssh secret shell
	ssh [-p port] user@remote，port端口号默认是22,登录到ssh
	user为用户名，remote为远程机器的地址，可以使ip或域名或别名
	使用exit退出登录
	windows中只能使用xshell进行远程登录
	使用ssh首次远程，会在本地机的用户目录下.ssh文件夹下生成配置信息
	使用别名配置远程电脑
	ssh 别名 即可连接
	~/.ssh/config 在这个文件下添加如下代码
	Host 别名
		HostName ip地址
		User 用户名
		Port 端口号
scp secret copy
	scp -P port 0.1.py user@remote：desktop/0.1py
	或scp -P port user@remote：desktop/0.1py 0.1py
	将远程机复制到本机，或将本机复制到远程机，均可
	使用-r才可以复制文件夹
	windows下使用ftp，进行文件交换fileZille，因为是使用ftp，所以端口号是21



用户和权限
	读 r 写w 执行x（excute）
	组：可真对组组设置不同权限，然后将不同用户加入不同权限的组中
	ls -l显示详细的文件列表
		最前面，d代表文件夹，-代表文件，后面的三个一组，共三组，，代表rwx读写执行，-代表不能
		分别对应后面的拥有者，组，和其他人
		中间有一列数字，硬链接数：代表该文件有多少方式可以到达
改变用户权限
	chmod change the mode
		chmod +/-rwx 文件名|目录名
超级用户root
	sudo substitude user do，使用另一个身份，默认是root
	负责系统维护和管理，具有所有访问权限
组的管理，需要使用sudo
	groupadd 组名 ，添加组
	groupdel 组名 ，删除组
	cat /etc/group ，查看etc配置文件夹下的group文件，确认是否添加或删除组
	chgrp -R 组名  文件或目录 ，-R是递归修改文件/目录
	实际应用中，会对组设置权限，再将用户加入该组
新建用户
	useradd -m -g 组名 用户名
		-m 自动添加用户目录
		-g 归属与哪个组，如果不写，会创建一个和用户名相同的组
	passwd 用户名	，和useradd组合使用，为用户设置密码，注意passwd，没有wd中间没字母
	userdel -r 用户名 ，删除用户和用户的文件，如果创建用户时忘了创建用户文件夹，最简单的方法是删除重建
	cat /etc/passwd|grep 用户名 ,查找该用户是否存在
查看用户信息
	id 用户名 ，	查看用户信息，用户id，组id，组名
	whoami ，	我是谁，就是目前登录的本用户
	who ，	因为是多用户，who是查找登录的所有用户，远程登录
将用户添加到组
	每个用户有主组和附加组
	创建用户时使用的-g创建的是主组
	sudo usermod -G sudo 用户名
		-G是添加到附加组，上面是使用sudo权限，将用户添加到sudo组
	注：添加的用户没有sudo权限，因为使用的-g。只有添加到sudo组中，才能有sudo权限
 	更改用户登录的shell，新加的用户一般是dash shell，dash效率一般
		sudo usermod -s /bin/bash 用户名
whitch 命令名 ，whitch是查看该命令执行程序在哪
	/bin（binary）是二进制执行文件，主要用于具体应用
	/sbin（system binary）系统管理员专用二进制代码，主要用于系统管理
	/user/bin后期安装的软件
	/user/sbin超级用户的管理程序
su -用户名	切换到该用户
	su 不接用户名则会切换到root
	exit则会退回到上一个用户，直到退出shell

修改文件权限
	chown 修改拥有者 chown 用户名 文件名|目录名
	chgrp 修改组	chgrp -R 组名 文件名|目录名
	chmod 修改文件权限
	chmod +/-rwx 文件名|目录名


查看终端时间
	date	返回当天
	cal	返回当月 calendar -y会返回一年的日历
查看磁盘
	df -h	disk free 显示磁盘剩余空间
	du -h	disk usage 显示目录下文件大小
	-h人性化显示
查看进程
	ps aux	进程查询process status 
		默认只显示本终端启动的程序		
		a：显示终端所有进程，包括其他用户进程
		u：显示进程详细状态
		x：显示不是控制终端的进程
	top	按从高到低显示进程，cpu，内存较高的上面
		实时监控，按q退出
	kill [-9] pid	结束进程，需要先ps查询pid,-9为强制结束
查找文件
	find [路径] -name "条件" 不指定路径，则查找本路径，条件使用通配符，同之前
软链接	类似windows快捷方式
	ln -s 被连接的源文件路径 软链接名
	源文件路径使用绝对路径，如果使用相对路径，则在移动软链接后软件接会失效，-s必不可少，软
	如果源文件被删除，则软连接失效
	如果没有使用-s则是硬链接，硬链接：在删除源文件后，仍然有效
打包/解包
	tar -cvf 打包文件名.tar 被打包的文件名或路径（被打包的文件是多个，用空格隔开）
	tar -xvf 打包文件.tar [-C 目标路径] 注意是大写的c
	-c打包，-x解压缩，-v显示归档详细过程，显示进度，-f指定压缩文件名
	以上为打包解包，并未压缩
压缩/解压缩 文件名后缀.tar.gz
	tar -zcvf 打包文件名.tar.gz 被打包的文件名或路径
	tar -zxvf 打包文件名
	压缩文件后缀 .tar.bz2
	tar -jcvf，将前面加上-j

安装/卸载软件apt advance packaging tool
	sudo apt install 软件包
	sudo apt remove 软件名
	sudo apt upgrade 更新已经安装的包
	
	





























