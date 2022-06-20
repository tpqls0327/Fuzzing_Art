# 그림닷컴 전체 그림 이미지 크롤링
from ast import excepthandler
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
 
baseUrl = 'https://gurim.com/search-all/?p_sort=1&p_style=0&p_subject=0&p_price=0&p_size_wh=1&p_size=0&p_shape=0&p_color=0&p_num='
tailUrl = '&put-sorting='

n=0
for i in range(1,287):
    url = baseUrl + str(i) + tailUrl
    html = urlopen(url)
    soup = bs(html, "html.parser")
    img = soup.find_all('img')
    for j in img:
        try:
            j.attrs['data-original']
            tmp_url = j.attrs['data-original']
            try:
                with urlopen(tmp_url) as f:
                    print(j.attrs['data-original'])
                    with open('./images/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
                        img = f.read()
                        h.write(img)
                        n+=1
                    
            except:
                continue
        except:
            continue
print("step1 done!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
