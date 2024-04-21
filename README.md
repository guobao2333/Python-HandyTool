# Python Handy Tool
- 我自己使用python语言编写的一些方便的小工具

[![Common Changelog](https://common-changelog.org/badge.svg)](https://common-changelog.org)
### 方便的py小工具
虽然说好像我实现的这些功能可能已经有人做了，甚至已经封装成了一个库，可能比我的更好用，但我的本意只是为了丰富自己的编程技术，也就是俗话说的写着玩(:

不过完全没有关系，我花了大量时间写的工具，本来只为满足我自己的一点小小目的，结果后面写上头了😂就花了亿点点把细节扣了扣，然后放上来开源给大家玩玩~

# Change Log | 更新日志

## replace_content - [1.1.0](script/FileEditer/replace_content.py) - 2024-04-21
### Fixed | 修复
1. 修复了批量操作文件时，**仅执行一次**的bug
2. 修复了批量操作文件时，错误传递`目录`参数用于操作文件的bug

> 仅展示最新一个脚本变更版本，更多版本细节请[查看变更日志](CHANGELOG.md)

# Usage | 使用
由于我使用Linux系统，所以不知道在macOS和Windows上表现如何……好吧你只需要安装python环境，还有pip用于安装依赖库。
> 由于部分系统/包管理器安装的python可能不会自带pip，所以还需要额外安装，并且可能还需要设置系统环境变量。_**这并不是本项目关注的重点，所以请自行解决。**_

相关注释我已经在源码中写的很清楚了，感兴趣自行翻阅。

## Install Runtime Environment | 安装运行环境
### Linux
- Ubuntu/Debian
```Shell
sudo apt install python3
```
or
```
sudo apt-get install python3
```

- Android Termux
```Shell
pkg install python3
pkg install python-pip
```

- CentOS
```Shell
sudo yum install python3
```

### Other OS | 其他系统
请自行使用Google、Bing、Baidu、yandex等搜索引擎寻找答案

## Check Installed | 验证安装
```shell
python3 --version
pip help
```

如果到这里没有报错，并输出了版本号的话，
恭喜你！已经安装成功了，享受代码吧！

# Discussions | 讨论
暂未完善~

# Contribute | 贡献
1. 点击上方`fork`仓库后，修改或添加你的代码
2. 点击`Pull requests`创建新的拉取请求后填写你应该填写的信息。
3. 接下来请等待代码审查，如果审查结束将会合并代码。

如果合并完成，恭喜你🎉你完成了对本项目的贡献！我们由衷的感谢为每个开源项目做出贡献的人，无论贡献多少。

# License | 许可证
[Apache-2.0 license](./LICENSE)
