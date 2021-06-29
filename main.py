from PIL import ImageFont, ImageDraw, Image
import textwrap
from bs4 import BeautifulSoup
import requests

#appear as a browser to reddit to avoid detection
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url='https://www.reddit.com/r/coronavirus/top?=day'
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')
titles = []
links = []
for item in soup.select('.Post'):
  try:
    print('----------------------------------------')
    print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
    titles.append(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
    print(item.select('._10wC0aXnrUKfdJ4Ssz-o14 a[href]')[0]['href'])
    links.append(item.select('._10wC0aXnrUKfdJ4Ssz-o14 a[href]')[0]['href'])
  except IndexError:
    print('nope')
    titles = titles[:-1]
  # except Exception as err:
  #   exception_type = type(err).__name__
  #   print(exception_type)

image_name = 0
for item in titles:
  image_name += 1
  image = Image.open('test.png')
  draw = ImageDraw.Draw(image)
  body = item
  increase_font = 0
  if len(body.split()) > 8:
    increase_font = 15
  else:
    increase_font = 0
  # txt = textwrap.wrap(content, width=40)
  fontsize = 1  # starting font size
  w = textwrap.TextWrapper(width=30,break_long_words=False,replace_whitespace=False, fix_sentence_endings=True)
  body = '\n'.join(w.wrap(body))
  # textwrap.fill(txt, width=40)
  W, H = image.size

  # portion of image width you want text width to be
  blank = Image.new('RGB',(581, 512))


  font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", fontsize)
  # print(image.size)
  # print(blank.size)

  while (font.getsize(body)[0] < blank.size[0]) and (font.getsize(body)[1] < blank.size[1]):
      # iterate until the text size is just larger than the criteria
      fontsize += 1
      font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", fontsize)

  # optionally de-increment to be sure it is less than criteria
  fontsize -= 1
  font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", (fontsize+increase_font))

  w, h = draw.textsize(body, font=font)

  # print('final font size',fontsize)
  draw.text(((W-w)/2,(H-h)/2), (body), font=font, fill="black") # put the text on the image
  image.save('images/' + str(image_name) + '.png') # save it

  #GUI IDEAS:
  #start, stop button
  #view images
  #input instagram login
  #