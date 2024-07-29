################# LICENCE START ################
#    Copyright 2024 shiguobaona(https://github.com/guobao2333)

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

# 读取和写入时使用的编码
read_encoding = 'utf-8' #默认utf-8
write_encoding = 'utf-8' #默认utf-8

# 默认覆盖文件
overwrite_default = False #默认False

# 提示是否覆盖
# 如果为False，则在命令行未提供-o参数时提示
overwrite_prompt = True #默认True

# 不覆盖时为新创建的文件添加文件名后缀
new_file_suffix = '_new' #file_new.txt

# 默认替换次数
replace_count = 0 #默认0为全部替换

################# CONFIG END ###################


def in_file(file, match_content, replace_content, use_regex=False, overwrite=overwrite_default, replace_count=None):
    global match_num
    global no_match_num
    # 读取文件
    with open(file, 'r', encoding=read_encoding, errors='ignore') as f:
        #try:
        content = f.read()
        #except UnicodeDecodeError:
            #sys.exit(f"\033[31m编码错误\033[0m：你的文件与默认编码'{read_encoding}'不一致，请检查你的文件编码！\n  可以使用\033[33m-e '编码'\033[0m 参数指定编码。\n\n使用 '-h' 参数获得更多帮助。")
        # 狗屎编码判断😡💢有一个字符不是这个编码就要报错，我就草🤬这下只能忽略了……啊？unicode？哦那没事了……

    # 使用正则表达式进行匹配和替换
    if use_regex:
        result = re.sub(match_content, replace_content, content, count=replace_count)
    else:
        result = content.replace(match_content, replace_content, replace_count)

    if result == content:
        if verbose:
            print(f"\033[33m未匹配到目标内容。\033[0m已跳过此文件：{file}")
        else:
            no_match_num += 1
    else:
        content = result

        # 覆盖操作
        if not overwrite:
            # 不覆盖创建新文件
            file_name_without_ext, ext = os.path.splitext(file)
            new_file = f"{file_name_without_ext}{new_file_suffix}{ext}"
            with open(new_file, 'w', encoding=write_encoding, errors='ignore') as f:
                f.write(content)
            if verbose:
                print(f"\033[32m替换完成！\033[0m新文件已保存到：{new_file}")
            else:
                match_num += 1
        else:
            # 直接覆盖
            with open(file, 'w', encoding=write_encoding, errors='ignore') as f:
                f.write(content)
            if verbose:
                print(f"\033[32m替换完成！\033[0m已替换的文件路径：{file}")
            else:
                match_num += 1


def in_dir(dir, match_content, replace_content, regex, overwrite, replace_count):
    # 批量操作目录下的所有文件
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            in_file(file_path, match_content, replace_content, regex, overwrite, replace_count)
    if not verbose:
        print(f"\033[32m已替换文件数\033[0m：{match_num}")
        print(f"\033[33m未匹配文件数\033[0m：{no_match_num}")


# 命令行参数解析
parser = argparse.ArgumentParser(description='替换指定文件或目录下的所有文件中的指定内容。')
parser.add_argument('path', metavar='目录|文件', type=str, help='要替换的目录或文件的路径')
parser.add_argument('match_content', metavar='匹配内容', type=str, help='要匹配的内容。开启正则表达式需使用引号包裹，否则可能会导致您的命令行出现异常')
parser.add_argument('replace_content', metavar='替换内容', type=str, help="替换后的内容。建议使用引号包裹，匹配组应使用'\\x'代替原生正则的'$x'")
parser.add_argument('replace_count', metavar='替换次数', nargs = '?', type=int, help='匹配内容在一个文件中的替换次数')
parser.add_argument('-r', '--regex', action='store_true', help='在匹配内容中使用正则表达式进行匹配')
parser.add_argument('-o', '--overwrite', action='store_true', help='直接覆盖旧文件而不是新建文件且不会提示')
parser.add_argument('-v', '--verbose', action='store_true', help='输出冗长的详细提示信息')
parser.add_argument('-e', '--encoding', action='store', help='改变读写文件的编码格式（默认UTF-8）')

args = parser.parse_args()
overwrite = args.overwrite
path = args.path
encoding = args.encoding
match_content = rf"{args.match_content}"
replace_content = rf"{args.replace_content}"

if args.replace_count != None:
    replace_count = args.replace_count

if encoding:
    # 哎呀懒得分了，自己改前面配置分开设置
    read_encoding = encoding
    write_encoding = encoding

# 输出详细信息
if args.verbose:
    verbose = True
else:
    # 狗屎自增需要初始化😡💢
    verbose = False
    match_num = 0
    no_match_num = 0

# 判断路径存在
if not os.path.exists(path):
    sys.exit(f"\033[91m\033[1mERR:\033[0m 此路径\033[1m不存在\033[0m：\033[33m\"{path}\"\033[0m")
# 使用绝对路径
if not os.path.isabs(path):
    path = os.path.abspath(path)
#print(f"绝对路径：{path}")

# 提示是否覆盖旧文件
if overwrite_prompt:
    if not args.overwrite:
        overwrite_question = [inquirer.List('overwrite', message="\033[33m是否覆盖旧文件而不是创建新文件？\033[0m", choices=[('是\033[31m(危险)\033[0m', True), ('否', False)], default=False)]
        overwrite_answer = inquirer.prompt(overwrite_question)
        try:
            overwrite = overwrite_answer['overwrite']
        except TypeError:
            sys.exit()


# 判断文件操作方式
replace_fn = in_file if os.path.isfile(path) else in_dir
replace_fn(path, match_content, replace_content, args.regex, overwrite, replace_count)
