# !/usr/bin/env python
# -*- coding:gbk -*- 

# **************************************************************************
# * Copyright (c) 2024. All Rights Reserved
# **************************************************************************
# * @function OCR Demo, PaddleOCR ʵ��, windows ����
# * @author wqw547243068@163.com
# * @date 2024/12/07 17:00
# **************************************************************************

import sys
from paddleocr import PaddleOCR, draw_ocr

# Paddleocr supports Chinese, English, French, German, Korean and Japanese
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order


# file_name = "E:\ocr\data\���Ϲ�����\��Ӣ.jpg"
# file_name = "E:\ocr\data\���Ϲ�����\����.jpg"
# file_name = "E:\ocr\data\���Ϲ�����\����.jpg"
# file_name = "E:\ocr\data\���Ϲ�����\����.jpg"
# file_name = r"E:\ocr\data\hand\1.jpg"
file_name = r"E:\ocr\data\hand\3.jpg"
# file_name = r"E:\ocr\data\OCR_e2e_img\general_ocr_001.png"

# # ���Լ�� ���´���δ����ͨ��
# # pip install paddleclas
# import paddleclas
# lang_model = paddleclas.PaddleClas(model_name="language_classification")
# result = lang_model.predict(input_data=file_name)
# result = list(result)
# lang_type = result[0][0]['label_names'][0]
# print('��������Ϊ��',lang_type)


# ��ʼ��, �״�ִ�л��Զ�����ģ���ļ�
# ����ѡ��: ['ch', 'en', 'korean', 'japan', 'chinese_cht', 'ta', 'te', 'ka', 'latin', 'arabic', 'cyrillic', 'devanagari']
# ocr = PaddleOCR(use_angle_cls=True) # Ĭ��ch ����+Ӣ��
# ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
ocr = PaddleOCR(use_angle_cls=True, lang='ch')
# ocr = PaddleOCR(use_angle_cls=True, lang='japan') # ��֧��һ��ָ����������
# ocr = PaddleOCR(use_angle_cls=True, lang='ch', use_gpu=False, det=True, rec=True, cls=True)
# ָ����д��
# handwriting_ocr = PaddleOCR(use_angle_cls=True, use_gpu=False, det_model_dir='handwriting_det', rec_model_dir='handwriting_rec')

# ��ʼʶ�𣬴������ file_name �������ļ���+numpy, �� Image.open(img_path)
result = ocr.ocr(file_name, cls=True) # ���������
# result = ocr.ocr(file_name, det=False) # ÿ��itemֻ���ı����ݺ����Ŷ�
# result = ocr.ocr(file_name, cls=True, det=False) # ����Ҫ�ı���ÿ��itemֻ���ı����ݺ����Ŷ�
# result = ocr.ocr(file_name, cls=True, rec=False) # ����Ҫ�ı����ݣ�ÿ��itemֻ���ı���
# result = ocr.ocr(file_name, cls=True, rec=False, det=False) #  ��ִ�з��������, ���ط�����+���Ŷ�


print(f'{result=}')
# ��ʽ: [�ı���, [����, ���Ŷ�]]
# [[[24.0, 36.0], [304.0, 34.0], [304.0, 72.0], [24.0, 74.0]], ['����Ӫ��������', 0.964739]]
# [[[24.0, 80.0], [172.0, 80.0], [172.0, 104.0], [24.0, 104.0]], ['��Ʒ��Ϣ/����', 0.98069626]]
# [[[24.0, 109.0], [333.0, 109.0], [333.0, 136.0], [24.0, 136.0]], ['��45Ԫ/ÿ���100�����𶩣�', 0.9676722]]


for idx in range(len(result)):
    res = result[idx]
    if not res:
        continue
    for line in res:
        print(line)

if not result and not result[0]:
    print(f'���Ϊ��: {result}')
    sys.exit(1)

# draw result
from PIL import Image

result = result[0]
image = Image.open(file_name).convert('RGB')
boxes, txts, scores = [], [], []
for line in result:
    if not line:
        continue
    boxes.append(line[0])
    txts.append(line[1][0])
    scores.append(line[1][1])

im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
im_show.show('result.jpg')
