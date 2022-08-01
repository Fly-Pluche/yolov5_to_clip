# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val']
classes = ["cell"]  # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id,image_set):
    in_file = open(
        'D:/workspace/kaggle/HuBMAP/data_detect/annotations/%s.xml' %
        (image_id),
        encoding='UTF-8')
    out_file = open(
        'D:/workspace/kaggle/HuBMAP/data_detect/labels/%s/%s.txt' % (image_set,image_id),
        'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(
            str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')



if not os.path.exists('D:/workspace/kaggle/HuBMAP/data_detect/labels/'):
    os.makedirs('D:/workspace/kaggle/HuBMAP/data_detect/labels/')
wd = getcwd()
for image_set in sets:

    if not os.path.exists('D:/workspace/kaggle/HuBMAP/data_detect/labels/'+image_set):
        os.makedirs('D:/workspace/kaggle/HuBMAP/data_detect/labels/'+image_set)
    image_ids = open('D:/workspace/kaggle/HuBMAP/data_detect/%s.txt' %
                     (image_set)).read().strip().split()
    list_file = open(
        'D:/workspace/kaggle/HuBMAP/data_detect/whatever/%s.txt' % (image_set),
        'w')
    for image_id in image_ids:
        list_file.write(abs_path + '/paper_data/images/%s.jpg\n' % (image_id))
        convert_annotation(image_id,image_set)
    list_file.close()
