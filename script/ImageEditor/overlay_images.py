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
default_output_path = './'

# 输出文件名后缀
new_file_suffix = '_合并'

################# CONFIG END ###################


def overlay_images(img1_path, img2_path, output_path=None):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # 将图片2覆盖到图片1上
    img1.paste(img2, (0, 0), img2)

    # 使用默认路径
    if not output_path:
        # 获取图片1的文件名和后缀
        img1_filename = os.path.splitext(os.path.basename(img1_path))[0]
        img1_ext = os.path.splitext(os.path.basename(img1_path))[1]

        output_filename = f"{img1_filename}{new_file_suffix}{img1_ext}"
        img1_dir = os.path.dirname(img1_path)
        output_path = os.path.join(img1_dir, output_filename)
    img1.save(output_path)
    print("图片合并完成，已保存至：{output_path}")

img1_path = sys.argv[1]
img2_path = sys.argv[2]
output_path = default_output_path if not len(sys.argv) > 3 else sys.argv[3]

overlay_images(img1_path, img2_path, output_path)