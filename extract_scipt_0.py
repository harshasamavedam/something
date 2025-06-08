from selenium import webdriver 
from selenium.webdriver.common.by import By as by 
import time
import re

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode

drive=webdriver.Chrome()
drive.get('https://wrogn.com/collections/view-all')
time.sleep(5)  # Wait for the page to load
drive.maximize_window()

start=0 
coun=0
objectdict={'product_name':[], 'product_price': [], 'product_image': []}
product_name=[]
product_price=[]   
product_image=[]

while True:
    print(drive.execute_script("return document.body.scrollHeight"))
    end=drive.execute_script("return document.body.scrollHeight")
    drive.execute_script(f"window.scrollTo({start}, {end-1000})")
    time.sleep(30)
    try:
        print("element in the site?")
        item=drive.find_elements(by.XPATH, '//*[@id="product-info"]/div/h3') 
        price=drive.find_elements(by.XPATH, '//*[@id="product-info"]/div/section/div/span[1]')
        print(len(price), len(item))
        # for each in price:
        #     print(each.text)
        # print(len(item), len(price))
        if len(item) == len(price):
            for i,pr in zip(item,price):
                objectdict['product_name'].append(i.text)
                objectdict['product_price'].append(pr.text)
                objectdict['product_image'].append(i.text+re.findall(r'\d+',pr.text)[0])
                product_name.append(i.text)
                product_price.append(pr.text)
                # print(pr.text)
                product_image.append(i.text+":"+re.findall(r'\d+',pr.text)[0])

    except Exception as e:
        print(f"Error occurred: {e}")
        break
    end1=drive.execute_script("return document.body.scrollHeight") 
    print(objectdict)
    print(product_image)
    if end==end1:
        break
print(objectdict.get('product_name'))






