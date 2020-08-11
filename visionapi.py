# -*- coding:utf-8 -*-
import io # 파일을 읽고 쓰기위한 모듈
import os # os의 기능을 사용하기 위한 모듈

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
filenames = os.listdir('./img') # img 아래에 있는 이미지 파일 이름을 불러오기

if '.DS_Store' in filenames:
    filenames.remove('.DS_Store')

for filename in filenames:
    path = os.path.join('./img', filename)

    # Loads the image into memory
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    with io.open('./txt/'+filename[0:-4]+'.txt', "wt") as f:
        #print(u"{}".format(texts[0].description))
        lines = f.readlines()
        if lines == None:
            print('No text.')
            pass
        else:
            f.write(u"{}".format(texts[0].description))
'''
for filename in filenames:
    with io.open('./txt/'+filename[0:-4]+'.txt', "wt") as f:
        for line in f:
        #print(u"{}".format(texts[0].description))
            print(line)
'''