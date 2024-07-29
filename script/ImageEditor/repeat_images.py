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

import os, sys
from PIL import Image

################# CONFIG START #################

# 默认输出路径
output_path = './'

# 是否横向拼接
horizontal = False
# 默认拼接方向
#axis = 0|1

################# CONFIG END ###################


def join_images(img_path, repeat_times, output_path=None, horizontal=False):
    # 打开输入图片
    with Image.open(img_path).convert("RGBA") as img:
        width, height = img.size
        if horizontal:
            new_width = width * repeat_times
            new_height = height
        else:
            new_width = width
            new_height = height * repeat_times

        # 创建新的空白图像
        new_image = Image.new('RGBA', (new_width, new_height))

        # 拼接图片
        for i in range(repeat_times):
            if horizontal:
                new_image.paste(img, (i * width, 0))
            else:
                new_image.paste(img, (0, i * height))

        # 确定保存路径和文件名
        if output_path is None:
            output_dir = os.path.dirname(img_path)  # 默认输出图片路径
            output_filename = os.path.splitext(os.path.basename(img_path))[0] + '_拼接' + os.path.splitext(img_path)[1]
            output_path = os.path.join(output_dir, output_filename)
            output_dirname = os.path.dirname(output_path)
        # 检查输出路径是否存在
        elif not os.path.exists(output_dirname):
            sys.exit("输出路径不存在")

        # 保存结果图片
        new_image.save(output_path)
        print("图片拼接完成，已保存至：" + output_path)

if __name__ == '__main__':
    # 获取命令行参数
    if len(sys.argv) < 3:
        print("缺少参数！请参考下方命令格式：")
        print("python 脚本.py <图片路径> <重复次数> [输出路径] [横向 | 纵向(默认)：<true | false>]")
    else:
        img_path = sys.argv[1]
        if not os.path.isfile(img_path):
            sys.exit("目标图片不存在")

        # 检查重复次数是否为整数
        if not sys.argv[2].isdigit():
            sys.exit("重复次数不是正整数")
        else:
            repeat_times = int(sys.argv[2]) 
        # 判断拼接方向参数
        if len(sys.argv) > 3:
            if sys.argv[3].lower() in ['true', 'false']:
                horizontal = True if sys.argv[3].lower() == 'true' else False
            else:
                output_path = sys.argv[3]
        join_images(img_path, repeat_times, output_path, horizontal)