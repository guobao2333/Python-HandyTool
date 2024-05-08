################# LICENCE START ################
#    Copyright 2024 @shiguobaona (https://github.com/guobao2333)

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
################# LICENCE END ##################

import os,re,sys,argparse,inquirer

################# CONFIG START #################

# 不覆盖时创建的新文件名后缀
new_file_suffix = '_new' #file_new.txt

# 是否默认覆盖文件
overwrite_default = False #默认False

# 是否提示覆盖文件
# 如果为False，则在命令行未给参数时提示
overwrite_prompt = True #默认True

# 默认替换次数
#暂未开发，请等待后续更新
#overwrite_count = 0 #默认0为全部替换

################# CONFIG END ###################


def replace_content_in_file(file, match_content, replace_content, use_regex=False, overwrite=overwrite_default):
    # 以只读模式操作，防止异常导致原始文件损坏
    with open(file, 'r') as f:
        content = f.read()

    # 使用正则表达式进行匹配和替换
    if use_regex:
        result = re.sub(match_content, replace_content, content)
    else:
        result = content.replace(match_content, replace_content)

    if result == content:
        print(f"\033[33m未匹配到目标内容。\033[0m已跳过此文件：{file}")
    else:

        content = result

        #dir_name = os.path.dirname(file)
        #file_name = os.path.basename(file)

        # 覆盖操作
        if not overwrite:
            # 不覆盖创建新文件
            file_name_without_ext, ext = os.path.splitext(file)
            new_file = f"{file_name_without_ext}{new_file_suffix}{ext}"
            with open(new_file, 'w') as f:
                f.write(content)
            print(f"\033[32m修改完成！\033[0m新文件已保存到：{new_file}")
        else:
            # 直接覆盖
            with open(file, 'w') as f:
                f.write(content)
            print(f"\033[32m修改完成！\033[0m文件路径：{file}")


def replace_content_in_dir(dir, match_content, replace_content, regex=False, overwrite=overwrite_default):
    # 批量操作目录下的所有文件
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            replace_content_in_file(file_path, match_content, replace_content, regex, overwrite)

# 命令行参数解析
parser = argparse.ArgumentParser(description='替换指定目录下的所有文件或单独某个文件中的指定内容。')
parser.add_argument('path', metavar='目录 | 文件', type=str, nargs='?', default='./', help='要替换的目录或文件的路径，如果未提供目录(不推荐)，则默认为当前目录')
parser.add_argument('match_content', metavar='<匹配内容>', type=str, help='要匹配的内容，开启正则表达式需使用引号包裹，否则可能会导致您的命令行出现异常(并非我的代码问题)')
parser.add_argument('replace_content', metavar='<替换内容>', type=str, help='替换后的内容，由于"$"符号在python中存在其他用途，其原本功能应改用"\\"符号代替')
parser.add_argument('-r', '--regex', action='store_true', help='使用正则表达式进行匹配(默认不使用)')
parser.add_argument('-o', '--overwrite', action='store_true', help='覆盖旧文件而不是创建新文件(默认不覆盖)')

args = parser.parse_args()
overwrite = args.overwrite
path = args.path

# 判断路径存在
if not os.path.exists(path):
    sys.exit(f"\033[91m\033[1m错误\033[0m：此路径\033[1m不存在\033[0m：\033[33m\"{path}\"\033[0m")

# 判断绝对路径
if not os.path.isabs(path):
    path = os.path.join(os.getcwd(), path)
    #print(f"绝对路径：{path}")

# 提示是否覆盖旧文件
if overwrite_prompt:
    if not args.overwrite:
        overwrite_question = [inquirer.List('overwrite', message="\033[33m是否覆盖旧文件？\033[0m", choices=[('是', True), ('否', False)], default=False)]
        overwrite_answer = inquirer.prompt(overwrite_question)
        overwrite = overwrite_answer['overwrite']

# 判断文件操作方式
if os.path.isfile(path):
    replace_content_in_file(path, args.match_content, args.replace_content, args.regex, overwrite)
else:
    replace_content_in_dir(path, args.match_content, args.replace_content, args.regex, overwrite)

