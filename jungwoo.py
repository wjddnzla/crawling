'''
from selenium import webdriver
driver1=webdriver.Chrome()
driver1.get("https://www.amazon.com")

driver2=webdriver.Chrome()
driver2.get("https://www.youtube.com")

driver1.back()
driver1.forward()
driver1.close()

driver2.maximize_window()
driver2.minimize_window()
driver2.set_window_size(500,300)
driver2.set_window_position(0,0)


u=["https://youtube.com","https://fedex.com","https://tesco.com"]
d=[]

for i in range(len(u)):
    driver=webdriver.Chrome()
    d.append(driver)
    d[i].get(u[i])

import time
driver2.set_window_size(500,300)
for i in range(5):
    driver2.set_window_position(i*100,i*100)
    time.sleep(1)

w=1920/2
h=1080/2
pos=[(0,0),(w,0),(0,h),(w,h)]
d=[]
u=["https://youtube.com","https://fedex.com","https://tesco.com","https://netflix.com"]
for i in range(4):
    driver=webdriver.Chrome()
    d.append(driver)
    d[i].set_window_size(w,h)
    d[i].set_window_position(pos[i][0],pos[i][1])
    d[i].get(u[i])

'''

#피자아저씨 URL 따서 프로필 작성
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)

driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")
p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element('xpath',p)
e.click()

import time
time.sleep(2)
x='//*[@id="id_firstName"]'
e=driver.find_element('xpath',x)
e.send_keys("Jungwoo")

x='//*[@id="id_lastName"]'
e=driver.find_element('xpath',x)
e.send_keys("Kim")

x='//*[@id="id_gender_0"]'
e=driver.find_element('xpath',x)
e.click()

x='//*[@id="id_username"]'
e=driver.find_element('xpath',x)
e.send_keys("qazwsxedcrfvtgbyhn")

x='//*[@id="id_password"]'
e=driver.find_element('xpath',x)
e.send_keys("wjddnsmstjdrhdgksek100")

x='//*[@id="id_state"]/option[3]'
e=driver.find_element('xpath',x)
e.click()
#e.send_keys("Texas")

x='//*[@id="id_fee"]/option[4]'
e=driver.find_element('xpath',x)
e.click()
#e.send_keys("$200:Platinum")

x='//*[@id="id_date"]'
e=driver.find_element('xpath',x)
e.send_keys("10/02/9999")

time.sleep(2)

x='/html/body/form/div/input'
e=driver.find_element('xpath',x)
e.click()
'''


#브롤스타즈 깔기
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)

driver.get("https://play.google.com/store/games?hl=ko-KR")
p='//*[@id="kO001e"]/header/nav/div/div[1]/button/i'
e=driver.find_element('xpath',p)
e.click()

import time
time.sleep(1)

p='//*[@id="kO001e"]/header/nav/c-wiz/div/div/label/input'
e=driver.find_element('xpath',p)
e.send_keys("브롤스타즈")

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)
driver.get("https://www.youtube.com")

p='//input[@id="search"]'
e=driver.find_element('xpath',p)
e.send_keys("you and me")

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)

import time
time.sleep(2)

p1='//a[@id="thumbnail"]'
elements=driver.find_elements('xpath',p1)
time.sleep(2)
print(elements[2].get_attribute('href'))
time.sleep(2)
driver.get(elements[2].get_attribute('href'))
'''

#미미미누, chilli, 스모크(유튜브)
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW

import time

driver=webdriver.Chrome(service=serv)
driver.get("https://www.youtube.com")
qwerty=['미미미누','chilli','스모크']
for i in range(len(qwerty)):
    driver.get("https://www.youtube.com")
    p='//input[@id="search"]'
    e=driver.find_element('xpath',p)
    time.sleep(2)
    e.send_keys(qwerty[i])
    from selenium.webdriver.common.keys import Keys
    e.send_keys(Keys.RETURN)
    time.sleep(2)
'''

#'샤프' 검색 (당근)
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

serv=Service()
serv.creation_flags=CREATE_NO_WINDOW

import time

driver=webdriver.Chrome(service=serv)
driver.get("https://www.daangn.com/")
time.sleep(2)

p='//*[@id="gnb-root"]/div/div/div/div/span[1]/form/input'
e=driver.find_element('xpath',p)
e.send_keys('샤프')
time.sleep(2)
from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN
'''


#포맷팅
'''
name='정우'
print(f'나는 {name}야. 잘 지내자')
'''


# 학교종이

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

serv=Service()
serv.creation_flags=CREATE_NO_WINDOW

import time


driver=webdriver.Chrome(service=serv)
driver.get("https://schoolbell-e.com/ko/main/home")
time.sleep(2)
p='/html/body/schoolbelle-root/div/app-gate/app-gate-home/div[1]/div[3]/div[1]/div/button[1]/p'
e=driver.find_element('xpath',p)
e.click()
time.sleep(3)
p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div[1]/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.send_keys('010-9250-4131')
p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div/input'
e=driver.find_element('xpath',p)
e.send_keys('8080')
p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[3]/button'
e=driver.find_element('xpath',p)
e.click()
time.sleep(2)
p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[1]/div/div[1]/div/div[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(3)

info=[]
for i in range(10):
    temp=[ ]
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div[4]/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/extended-letter-metadata/p/span'
    e=driver.find_element('xpath',p)
    temp.append(e.text)
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div[3]/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    temp.append(e.text)
    info.append(temp)
for i in range(10):
    print(info[i][0].replace('발행 ',''), ":", info[i][1])
'''    
file=open('학교종이.txt','w')
file.close()
'''
