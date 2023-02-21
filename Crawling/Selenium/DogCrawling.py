from selenium import webdriver
from selenium.webdriver.common.by import By ## 추가
import re
driver = webdriver.Chrome('chromedriver.exe')

baseurl = 'https://www.kkc.or.kr/megazine/megazine_02.html?page='
lasturl = '&key='

namelist = [] # 크롤링 해온 이름을 넣을 list
# linelist =[] # 크롤링 해온 Line01 클래스를 넣을 list
# line2list =[] # 크롤링 해온 Line02 클래스를 넣을 list
namedict ={} # json 저장을 위해 dict 하나 생성

for i in range(14):
    if i == 0:
        continue
    driver.get(baseurl+str(i)+lasturl) #url을 분석한 결과 baseurl과 lasturl 사이에 숫자만 바뀌면 페이지가 넘어감
    name=driver.find_elements(By.CLASS_NAME,"kind") # 견종 이름 가져오기

    for j in name:
        namelist.append(j.text) # 가져온 견종 이름 namelist에 넣기 # 몇번? -> name만큼

    '''
    line =driver.find_elements(By.CLASS_NAME,'line01')
    for i in line:
        linelist.append(i.text)
    ''' # line01이라는 class에 있는 데이터(text) 가져오기 # 무슨 데이터야? -> 강아지의 원산지

    '''
    line2 = driver.find_elements(By.CLASS_NAME,'line02')
    for i in line2:
        linelist2.append(i.text)
    ''' # line02라는 class에 있는 데이터(text) 가져오기 # 무슨 데이터야? -> 강아지의 체고, 체중, 운동량, 그룹 모두 담겨 있음 ;;;

    # print(namelist) # 중간중간 namelist가 점점 늘어나는 걸 확인하는 용


#print(namelist) # 위 for 문 안에 넣으면 for문이 끝날때마다 출력되나, 여기에다가 print를 쓰면 결과만 만옴
#print(linelist)
#print(linelist2)

## 리스트에서 특정 문자열 제거
namelist2 =[]

for i in namelist :
    text = re.sub('[A-Z(/s]','',i).strip()
    namelist2.append(text)
print(namelist2)

for i in range(len(namelist2)): # list 만큼 dict에
    namedict[i] = namelist2[i] # 넣어줌
print(namedict) # 그 dict가 제대로 됐는지 확인

import json
with open("dognames.json",'w', encoding='utf-8') as file :
    json.dump(namedict,file, indent='\t', ensure_ascii=False) # dict를 json으로 저장


