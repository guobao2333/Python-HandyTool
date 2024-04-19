import os
import re
import sys
import argparse
import inquirer


# 不覆盖时创建的新文件名后缀
new_file_suffix = '_new' #file_new.txt

# 是否默认覆盖文件
overwrite_default = False #默认False

# 是否提示覆盖文件
# 如果为False，则在命令行未给参数时提示
overwrite_prompt = True #默认True

# 默认替换次数
#暂未继续开发，请等待后续更新

def replace_content_in_file(file, match_content, replace_content, use_regex=False, overwrite=overwrite_default):
    # 打开文件并读取内容
    with open(file, 'r') as f:
        content = f.read()

    # 使用正则表达式进行匹配和替换
    if use_regex:
        content = re.sub(match_content, replace_content, content)
    else:
        content = content.replace(match_content, replace_content)

    #dir_name = os.path.dirname(file)
    #file_name = os.path.basename(file)
    
    # 覆盖操作
    if not overwrite:
        # 不覆盖创建新文件
        file_name_without_ext, ext = os.path.splitext(file)
        new_file = f"{file_name_without_ext}{new_file_suffix}{ext}"
        with open(new_file, 'w') as f:
            f.write(content)
        sys.exit(f"修改完成！新文件已保存到：{new_file}")
    else:
        # 直接覆盖
        with open(file, 'w') as f:
            f.write(content)

    sys.exit(f"修改完成！")

def replace_content_in_dir(dir, match_content, replace_content, regex=False, overwrite=overwrite_default):
    # 遍历指定目录下的所有文件
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            replace_content_in_file(dir, match_content, replace_content, regex, overwrite)

# 命令行参数解析
parser = argparse.ArgumentParser(description='替换指定目录下的所有文件或单独某个文件中的指定内容。')
parser.add_argument('path', metavar='目录|文件', type=str, nargs='?', default='./', help='要替换的目录或文件的路径，默认为当前目录')
parser.add_argument('match_content', metavar='匹配内容', type=str, help='要匹配的内容，使用正则表达式时需使用引号')
parser.add_argument('replace_content', metavar='替换内容', type=str, help='替换后的内容，由于$符号存在其他用途，应改用\\')
parser.add_argument('-r', '--regex', action='store_true', help='使用正则表达式进行匹配(默认不使用)')
parser.add_argument('-o', '--overwrite', action='store_true', help='覆盖旧文件而不是创建新文件(默认不覆盖)')

args = parser.parse_args()
overwrite = args.overwrite
path = args.path

# 判断路径存在
if not os.path.exists(path):
    sys.exit(f"\033[91m\033[1m错误\033[0m：此路径：\033[33m\"{path}\"\033[0m 不存在！")

# 判断绝对路径
if not os.path.isabs(path):
    path = os.path.join(os.getcwd(), path)
    #print(f"绝对路径：{path}")

# 提示是否覆盖旧文件
if overwrite_prompt:
    if not args.overwrite:
        overwrite_question = [inquirer.List('overwrite', message="是否覆盖旧文件？", choices=[('是', True), ('否', False)], default=False)]
        overwrite_answer = inquirer.prompt(overwrite_question)
        overwrite = overwrite_answer['overwrite']

if os.path.isfile(path):
    replace_content_in_file(path, args.match_content, args.replace_content, args.regex, overwrite)
else:
    replace_content_in_dir(path, args.match_content, args.replace_content, args.regex, overwrite)
