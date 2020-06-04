'''
coding=utf-8
'''
from PIL import Image
# img=Image.open('G:/siamfc tc数据集/tc_Airport_ce/0001.jpg')
# img.show()
# print('图像的格式是：',img.format)
# print('图像的大小是：',img.size)
# print('图像（100，100）处的像素位：',img.getpixel((100,100)))

# img1=Image.open('G:/siamfc tc数据集/tc_Airport_ce/0001.jpg').convert(mode='RGB')
# img2=Image.new('RGB',img1.size,'red')
# #img2.show()
# Image.blend(img2,img1,alpha=0.5).show()

##按像素缩放图像
img1=Image.open('G:/siamfc tc数据集/tc_Airport_ce/0001.jpg')
# img1.show()
# #将每个像素都扩大2倍
# Image.eval(img1,lambda x:x*2).show()

##按尺寸进行缩放
# img2=img1.copy()
# print(img2.size)
# img1.show()
# img2.thumbnail((600,360))
# img2.show()