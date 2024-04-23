# Changelog | 变更日志

这里是本项目文件的变更日志，不过由于本项目仓库并不是仅发布某个单独的发行版项目，所以与[通用变更日志](https://common-changelog.org)的规范会有所不同。

> [!IMPORTANT]
> 特殊规范：
> 版本号前增加文件名作为标题： `文件名 - 版本号 - 日期`
> 如果变更不涉及某一脚本，则以： `仓库更新 - 日期` 为标题。
> 如果某一天进行了多次更新，且为同一类型，则合并至同一个二级标题下。

## repeat_images.py - [0.1.0](https://github.com/guobao2333/python_handy-tool/commit/b929ef7) - 2024-04-21

* 新增python脚本：[重复拼接图片](script/ImageEditer/repeat_images.py)

## overlay_images.py - [0.1.0](https://github.com/guobao2333/python_handy-tool/commit/b929ef7) - 2024-04-21

* 新增python脚本：[合并图片](script/ImageEditer/overlay_images.py)

## 仓库更新 - 2024-04-21

### Changed | 变更

* **调整存放所有脚本的目录为`script`**

* 优化和完善文档

## replace_content - [1.1.0](https://github.com/guobao2333/python_handy-tool/commit/1e862b8) - 2024-04-21

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

## replace_content - [1.0.0](https://github.com/guobao2333/python_handy-tool/commit/c0c63d5) - 2024-04-19

**创建了此项目仓库**👍🏻

### Added | 新增

* 新增python脚本：[批量替换文件内容](script/FileEditer/replace_content.py)
  > 因完成度较高，故为正式发布版v1.0.0。

* 新增许可证
* 新增`README.md`说明文档
* 新增`ISSUE_TEMPLATE`问题模板
