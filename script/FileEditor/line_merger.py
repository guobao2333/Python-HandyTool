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

import os,argparse

def is_valid_path(parser, arg, file_or_folder=None):
	if file_or_folder == 'file':
		if not os.path.isfile(arg):
			parser.error(f"文件不存在：'{arg}'")
	elif file_or_folder == 'folder':
		if not os.path.isdir(arg):
			parser.error(f"目录无效：'{arg}'")
	else:
		if not os.path.exists(arg):
			parser.error(f"路径无效：'{arg}'")
	return arg

def merge_files(file1, file2, output, direction):
	f1_n = os.path.basename(file1)
	f2_n = os.path.basename(file2)
	with open(file1, 'r') as f1, open(output, 'w') as f3:
		with open(file2, 'r') as f2:
			if direction == 'left':
				print(f"合并方向：{f2_n} + {f1_n}")
				for line1, line2 in zip(f1, f2):
					merged_line = line2.rstrip('\n') + line1
					f3.write(merged_line)
			elif direction == 'right':
				print(f"合并方向：{f1_n} + {f2_n}")
				for line1, line2 in zip(f1, f2):
					merged_line = line1.rstrip('\n') + line2
					f3.write(merged_line)
		path = os.path.abspath(output)
		print(f"合并完成！已保存到：{path}")

parser = argparse.ArgumentParser(description='将 file2 中的内容逐行合并到 file1 并输出到新文件。')
parser.add_argument('file1', type=lambda x: is_valid_path(parser, x, 'file'), help='文件1的路径')
parser.add_argument('file2', type=lambda x: is_valid_path(parser, x, 'file'), help='文件2的路径')
parser.add_argument('output', help='合并后的文件保存路径')
parser.add_argument('-d', '--direction', choices=['left', 'right'], default='right', help='合并方向（左或右）默认为右（将file2的内容放到file1后面）')

args = parser.parse_args()

merge_files(args.file1, args.file2, args.output, args.direction)
