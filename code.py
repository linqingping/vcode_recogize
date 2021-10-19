import re
import pytesseract
from PIL import Image
import tesserocr
# import base64
# from io import BytesIO
# from PIL import Image

class demo():

    def __init__(self, path):
        self.image = Image.open(path)
        self.image = self.image.convert('L')

    def test(self):
        threshold = 155
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        self.image = self.image.point(table, '1')
        self.img_array = self.image.load()
        width = self.image.size[0]
        height = self.image.size[1]
        for i in range(0, 1000):
            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    count = 0
                    if self.img_array[x, y] == self.img_array[x - 1, y + 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x, y + 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x + 1, y + 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x - 1, y]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x + 1, y]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x - 1, y - 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x, y - 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x + 1, y - 1]:
                        count += 1
                    if count <= 2 and count > 0:
                        self.img_array[x, y] = 1
        self.image.save('result.jpg')

demo('./myCodeNew.jpg').test()
code = pytesseract.image_to_string('result.jpg')
code = re.sub(' ','',code).strip()
print(code)

#验证码是base64
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
# }
# def getcode(currenttime):
#     url = 'http://localhost/jeecg-boot/sys/randomImage/'+str(currenttime)
#     code=''
#     while len(code)<4:
#         response = requests.get(url,headers=headers)
#         data=re.sub('data:image/jpg;base64,','',response.json()['result'])
#         image_data = base64.b64decode(data)
#         im = Image.open(BytesIO(image_data))
#         code = pytesseract.image_to_string(im)
#         code = re.sub(' ','',code).strip()
#         time.sleep(0.5)
#     return code
