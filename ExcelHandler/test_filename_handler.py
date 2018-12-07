# -*- coding:utf-8 -*-
"""
测试文件，对一个文件夹里照片的名字的批量修改
"""
import os


def rename_img(class_img_dir):
    """
    对学生图片进行重命名
    参数class_img_dir:对应的班级的照片文件夹
    :return: None
    """
    img_name_list = []
    img_postfix = '.jpg'  # 图片后缀
    if os.path.exists(class_img_dir):
        if os.path.isdir(class_img_dir):
            dir_list = os.listdir(class_img_dir)
            if len(dir_list) > 0:
                print(dir_list)
                img_dir = class_img_dir + '/' + dir_list[0]
                student_img_name_list = os.listdir(img_dir)
                if len(student_img_name_list) > 0:
                    # print(student_img_name_list.sort())
                    # 图片名字构建成字典，存入列表，根据时间戳排序
                    for name in student_img_name_list:
                        split_list = name.split('_')
                        img_time = split_list[-1]
                        img_time = img_time.split('.')[0]
                        if len(img_time) < 17:
                            i = 17 - len(img_time)
                            for x in range(i):
                                img_time = img_time + '0'
                        print(img_time)
                        img_dict = dict(img_name=name, img_time=img_time)
                        img_name_list.append(img_dict)

                    # print(len(img_name_list))
                    # print(len(set(img_name_list)))
                    # 排序
                    img_name_list.sort(key=lambda s: s['img_time'])
                    print(img_name_list)
                    # 返回排序后的列表，和文件夹路径，图片格式
                    return img_name_list, img_dir, img_postfix
                    # # 修改文件文件名
                    # count = 0
                    #
                    # for x in range(3):
                    #     file_url = img_dir + img_name_list[count]['img_name']
                    #     os.rename(file_url, '学号-' + str(x) + '.jpg')

                else:
                    print('%s 文件夹为空' % img_dir)
                    return None
            else:
                print('%s 文件夹为空' % class_img_dir)
                return None
        else:
            print('%s 不是个文件夹' % class_img_dir)
            return None
    else:
        print('%s 改文件夹不存在' % class_img_dir)
        return None


if __name__ == "__main__":
    print(rename_img('1601░р'))
    print('ok')


