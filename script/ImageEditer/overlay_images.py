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

import os, sys
from PIL import Image

################# CONFIG START #################

# 默认输出路径
default_output_path = './'

# 输出文件名后缀
new_file_suffix = '_合并'

################# CONFIG END ###################


def overlay_images(image1_path, image2_path, output_path=None):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # 将图片2覆盖到图片1上
    image1.paste(image2, (0, 0), image2)

    # 使用默认路径
    if not output_path:
        # 获取图片1的文件名和后缀
        image1_filename = os.path.splitext(os.path.basename(image1_path))[0]
        image1_ext = os.path.splitext(os.path.basename(image1_path))[1]

        output_filename = f"{image1_filename}{new_file_suffix}{image1_ext}"
        image1_dir = os.path.dirname(image1_path)
        output_path = os.path.join(image1_dir, output_filename)
    image1.save(output_path)
    print("图片合并完成，已保存至：{output_path}")

image1_path = sys.argv[1]
image2_path = sys.argv[2]
output_path = default_output_path if not len(sys.argv) > 3 else sys.argv[3]

overlay_images(image1_path, image2_path, output_path)