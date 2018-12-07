# -*- coding:utf-8 -*-
"""
根据Excel表修改对应的文件夹中学生照片名
"""
import os
import xlrd
import traceback


def read_excel(excel_file):
    """
    读取某个班级学生信息Excel
    :param excel_file: 某班级学生信息Excel
    :return: student_list 存储有照片的学生的ID
    """
    try:
        # 打开excel文件
        workbook = xlrd.open_workbook(excel_file)
        # 获取到sheet1
        sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
        student_list = []
        for i in range(sheet1.nrows):
            if i == 0:
                continue
            student_id = sheet1.cell(i, 0).value  # 获取学生学号
            has_img = sheet1.cell(i, 4).value  # 如果==0表示，没有照片，跳过该学生
            # print('是否有照片=', has_img)
            if has_img == '':
                student_list.append(student_id)
        return student_list
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return None


def get_img_info(class_img_dir):
    """
    对学生图片进行重命名
    参数class_img_dir:对应的班级的照片文件夹
    :return: None
    """
    try:
        img_name_list = []
        img_postfix = '.jpg'  # 图片后缀
        if os.path.exists(class_img_dir):
            if os.path.isdir(class_img_dir):
                dir_list = os.listdir(class_img_dir)
                if len(dir_list) > 0:
                    # print(dir_list)
                    img_dir = class_img_dir + '/' + dir_list[0]  # img_dir = ╚¤─ъ╝╢/1601░р/2018-09-28
                    student_img_name_list = os.listdir(img_dir)
                    if len(student_img_name_list) > 0:
                        # print(student_img_name_list.sort())
                        # 图片名字构建成字典，存入列表，根据时间戳排序
                        for name in student_img_name_list:
                            split_list = name.split('_')
                            img_time = split_list[-1]
                            img_postfix = '.' + img_time.split('.')[-1]
                            img_time = img_time.split('.')[0]
                            if len(img_time) < 17:
                                i = 17 - len(img_time)
                                for x in range(i):
                                    img_time = img_time + '0'
                            # print(img_time)
                            img_dict = dict(img_name=name, img_time=img_time)
                            img_name_list.append(img_dict)

                        # print(len(img_name_list))
                        # print(len(set(img_name_list)))
                        # 排序
                        img_name_list.sort(key=lambda s: s['img_time'])
                        # print(img_name_list)
                        # 返回排序后的列表，和文件夹路径，图片格式
                        return img_name_list, img_dir, img_postfix
                    else:
                        print('%s 文件夹为空' % img_dir)
                        return None, None, None
                else:
                    print('%s 文件夹为空' % class_img_dir)
                    return None, None, None
            else:
                print('%s 不是个文件夹' % class_img_dir)
                return None, None, None
        else:
            print('%s 改文件夹不存在' % class_img_dir)
            return None, None, None
    except Exception as e:
        print(e)
        print(traceback.format_exc())


def rename_img(student_list, img_name_list, img_dir, img_postfix):
    """
    学生图片重命名,每个学生有三张照片。命名方式：学号_1.jpg
    :param student_list: 存储有照片的学生的ID
    :param img_name_list: 排序后的学生照片的列表
    :param img_dir: 图片文件夹
    :param img_postfix: 图片的格式
    :return:
    """
    count = 0
    try:
        if not all((student_list, img_name_list, img_dir, img_postfix)):
            print('参数不完整错误')
        if len(student_list) * 3 != len(img_name_list):
            print('学生照片数量不正确，有照片的学生个数=%d,照片数=%d，%s' % (len(student_list), len(img_name_list), img_dir))
        else:
            # print('当前工作目录， ', os.getcwd())
            current_work_dir = os.getcwd()
            names_dir = img_dir.split('/')
            os.chdir(current_work_dir + '\\' + '\\'.join(names_dir))
            for student_id in student_list:
                for x in range(1, 4):
                    # file_url = img_dir + '/' + img_name_list[count]['img_name']
                    # print('原文件名= ', img_name_list[count]['img_name'])
                    # print('要修改成的名字= ', str(int(student_id)) + '_' + str(x) + img_postfix)
                    os.rename(img_name_list[count]['img_name'], str(int(student_id)) + '_' + str(x) + img_postfix)
                    count += 1
            # # 切换工作空间修改重命名OK的班级
            # os.chdir(current_work_dir + '\\' + names_dir[0])
            # os.rename(names_dir[0], names_dir[0] + '-OK')
            # 切换回原来工作空间
            os.chdir(current_work_dir)
            # print('当前工作空间', os.getcwd())

    except Exception as e:
        print(e)
        print(traceback.format_exc())


def dir_handler(excel_dir, image_dir):
    """
    获取相应的Excel文件和与之对应的照片文件夹
    :param excel_dir:
    :param image_dir:
    :return: 返回Excel和对应的照片的路径
    """
    try:
        excel_img_url_list = []
        excel_list = os.listdir(excel_dir)
        image_dir_list = os.listdir(image_dir)
        if len(image_dir_list) == 0:
            raise '%s 空文件' % image_dir
        if len(excel_list):
            for excel_name in excel_list:
                find_dir_str = excel_name[:4]
                for image_dir_name in image_dir_list:  # 有与花名册对应的照片文件夹才存入列表
                    if image_dir_name.startswith(find_dir_str):
                        excel_img_url_list.append((excel_name, image_dir_name))  # 存入列表
        else:
            raise '%s 空文件' % excel_dir
        return excel_img_url_list
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return None


if __name__ == "__main__":
    # 只需要修改文件夹名
    excel_dir = '16╝╢╗и├√▓с'  # 存放班级学生信息的Excel文件夹
    image_dir = '╚¤─ъ╝╢'  # 存放班级学生照片的文件夹

    excel_img_url_list = dir_handler(excel_dir, image_dir)
    # print(excel_img_url_list)
    for excel_img_url in excel_img_url_list:
        try:
            excel_file = './' + excel_dir + '/' + excel_img_url[0]
            student_list = read_excel(excel_file)
            class_img_dir = './' + image_dir + '/' + excel_img_url[1]
            img_name_list, img_dir, img_postfix = get_img_info(class_img_dir)
            if not all((student_list, img_name_list, img_dir, img_postfix)):
                continue
            rename_img(student_list, img_name_list, img_dir, img_postfix)
        except Exception as e:
            print(e)









