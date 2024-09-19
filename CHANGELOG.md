# Changelog | 变更日志

这里是本项目文件的变更日志，不过由于本项目仓库并不是仅发布某个单独的发行版项目，所以与[通用变更日志](https://common-changelog.org)的规范会有所不同。

> [!IMPORTANT]
> 特殊规范：  
> 版本号前增加文件名作为标题： `日期 - 文件名 - 版本号`  
> 如果某一天进行了多次更新，且为同一类型，则合并至同一个二/三级标题下，其下属标题顺延增加。

## replace_content - [1.5.0](https://github.com/guobao2333/Python-HandyTool/commit/b0c2c76) - 2024-07-29
### Fixed | 修复

1. 修复文件夹拼写错误
   - `FileEditer` -> `FileEditor`
   - `ImageEditer` -> `ImageEditor`
2. 修复选择覆盖时`ctrl+c`退出出现的报错

### Changed | 变更

* 现在默认不显示详细输出信息
* 优化部分提示信息
* 缩减函数名
* 去除函数多余默认参数

### Added | 新增

+ 新增可选参数 `替换次数` 可用于指定在每个文件中的替换次数
+ 新增可选参数 `-e` or `--coding` 可用于指定编码
+ 新增可选参数 `-v` or `--verbose` 可用于显示详细输出信息

---
## 2024-07-27
### line_merger - [1.0.0](https://github.com/guobao2333/Python-HandyTool/commit/433b5bd)
#### New | 新脚本

+ 新增python脚本：[逐行合并内容](script/FileEditor/line_merger.py)  
  作用：将`文件2`中的内容逐行合并到`文件1`

### replace_content - [1.4.0](https://github.com/guobao2333/Python-HandyTool/commit/433b5bd)
#### Changed | 变更

* `path`现在是不可空的必选参数
* 优化部分代码逻辑
* 优化部分提示信息

---
## 2024-07-10 - replace_content - [1.3.0](https://github.com/guobao2333/Python-HandyTool/commit/4065ada)
### Added | 新增

+ 为不覆盖时新建的文件名称增加后缀配置
+ 为操作文件时新增编码格式配置

---
## 2024-05-11 - replace_content - [1.2.1](https://github.com/guobao2333/Python-HandyTool/commit/39497da)
### Changed | 变更

* **将仓库由 `python_handy-tool` 更名为 `Python-HandyTool`**

* 调整脚本部分提示内容
* 优化和完善文档

## 2024-05-08 - replace_content - [1.2.0](https://github.com/guobao2333/Python-HandyTool/commit/56cff86)
### Added | 新增

+ 新增`跳过匹配失败的文件`的功能

---
## 2024-04-21
### New | 新脚本

+ 新增python脚本：[合并图片](script/ImageEditor/overlay_images.py) overlay_images.py - [1.0.0](https://github.com/guobao2333/Python-HandyTool/commit/b929ef7)  
  作用：将`图片2`合并至`图片1`之上
+ 新增python脚本：[重复拼接图片](script/ImageEditor/repeat_images.py) repeat_images.py - [1.0.0](https://github.com/guobao2333/Python-HandyTool/commit/b929ef7)  
  作用：在同个方向上重复拼接图片

### Changed | 变更

* **调整存放所有脚本的目录为`script`**
* 优化和完善文档

## replace_content - [1.1.0](https://github.com/guobao2333/Python-HandyTool/commit/1e862b8)
### Fixed | 修复

1. 修复了批量操作文件时，**仅执行一次**的bug
2. 修复了批量操作文件时，错误传递`目录`参数用于操作文件的bug

### Changed | 变更

* 增加了一些注释
* 微调了提示信息

* 说明文档修改了亿点点措辞~
* 问题模板也修改了亿点点措辞~

### Added | 新增

* 新增变更日志
* 新增`.gitignore`文件

---
## 2024-04-19 - replace_content - [1.0.0](https://github.com/guobao2333/Python-HandyTool/commit/c0c63d5)
**创建了此项目仓库**👍🏻
### New | 新脚本

+ 新增python脚本：[批量替换文件内容](script/FileEditor/replace_content.py)  
  作用：可使用正则表达式替换文件内的指定内容

+ 新增许可证
+ 新增`README.md`说明文档
+ 新增`ISSUE_TEMPLATE`问题模板
