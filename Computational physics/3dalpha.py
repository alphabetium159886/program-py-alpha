from PIL import Image
import os

# 定义图片文件夹路径和导出路径
image_folder_path = r"C:\Users\toby1\Desktop\alpha"
export_path = r"C:\Users\toby1\Desktop\mygif.gif"

# 获取文件夹中所有图片文件的路径
image_paths = [os.path.join(image_folder_path, file_name) for file_name in os.listdir(image_folder_path) if file_name.endswith('.png')]

# 如果图片列表为空，打印错误提示并退出程序
if not image_paths:
    print("No image files found in the folder.")
    exit()

# 打开每张图片，存入一个列表中
images = [Image.open(image_path) for image_path in image_paths]

# 设置GIF的循环次数，0表示无限循环
loop_count = 0

# 如果只有一张图片，直接将该图片保存为 GIF
if len(images) == 1:
    images[0].save(export_path, format='GIF', save_all=True, duration=500, loop=loop_count)
else:
    # 将图片序列保存为 GIF 动画
    images[0].save(export_path, format='GIF', append_images=images[1:], save_all=True, duration=500, loop=loop_count)
