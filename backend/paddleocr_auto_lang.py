
import langid

sen = [
    '����, fdsfd nfdsfd ',
    'fdsfd ����, nfdsfd ',
    '��õļ���, fdsfd nfdsfd ',
    '�� 534 ���� ',
    'TK BAA BAD! 292.4 ������?. BX LRA} mW. ',
    'BOARDING PASS ���� FLIGHT ���� DATE ��λ CLASS  ��� SERIAL NO.  ��λ�� ��SEAT ����. MU 2379 03DEC    ��    035      <Ŀ�ĵ� T0   ʼ���� FROM [3       =         +'
]
for s in sen:
    tmp = langid.classify(s)
    print(s[:5], tmp)


# ���Լ�� ���´���δ����ͨ��
# pip install paddleclas
import paddleclas

# file_name = "E:\ocr\data\���Ϲ�����\��Ӣ.jpg"
# file_name = "E:\ocr\data\���Ϲ�����\����.jpg"
# file_name = "E:\ocr\data\���Ϲ�����\����.jpg"
# file_name = "E:\ocr\data\���Ϲ�����\����.jpg"
# file_name = r"E:\ocr\data\hand\1.jpg"
file_name = r"E:\ocr\data\hand\3.jpg"
# file_name = r"E:\ocr\data\OCR_e2e_img\general_ocr_001.png"

lang_model = paddleclas.PaddleClas(model_name="language_classification")
result = lang_model.predict(input_data=file_name)
result = list(result)
lang_type = result[0][0]['label_names'][0]
print('��������Ϊ��',lang_type)

# RuntimeError: (NotFound) Cannot open file C:\Users\wqw/.paddleclas/inference_model\PULC\language_classification, please confirm whether the file is normal.
#   [Hint: Expected static_cast<bool>(fin.is_open()) == true, but received static_cast<bool>(fin.is_open()):0 != true:1.] (at ..\paddle\fluid\inference\api\analysis_predictor.cc:2577)