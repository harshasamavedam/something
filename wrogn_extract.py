from selenium import webdriver 
from selenium.webdriver.common.by import By as by 
import time
import re
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime as dt
from selenium.webdriver.support.ui import WebDriverWait as WAIT
import openpyxl


name=("wrogn_products"+str(dt.now().date()))
raw_data=pd.DataFrame()

# import py
def wrogn_extract_raw():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode

    drive=webdriver.Chrome(options=options)
    drive.get('https://wrogn.com/collections/view-all')
    time.sleep(5)  # Wait for the page to load
    drive.maximize_window()

    start=0
    coun=0
    objectdict={'product_name':[], 'product_price': [], 'product_image': [],'offer_price':[],'Date':[]}
    product_name=[]
    product_price=[]   
    product_image=[]

    def expect(text):
        if(len(text)>0):
            return re.findall(r'\d+',text)[0]
        else:
            return "0"
    cn=0
    while True :
        print(drive.execute_script("return document.body.scrollHeight"))
        end=drive.execute_script("return document.body.scrollHeight")
        drive.execute_script(f"window.scrollTo({start}, {end-1000})")
        WAIT(drive,30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
        )
        try:
            print("element in the site?")
            item=drive.find_elements(by.XPATH, '//*[@id="product-info"]/div/h3') 
            price=drive.find_elements(by.XPATH, '//*[@id="product-info"]/div/section/div/span[1]')
            off_by=drive.find_elements(by.XPATH, '//*[@id="product-info"]/div/section/div/span[3]')
            print(len(price), len(item))
            # for each in price:
            #     print(each.text)
            # print(len(item), len(price))
            if len(item) == len(price):
                for i,pr,ofe in zip(item,price,off_by):
                    if i.text+re.findall(r'\d+',pr.text)[0] not in objectdict['product_image']:
                        objectdict['product_name'].append(i.text)
                        objectdict['product_price'].append(pr.text)
                        objectdict['offer_price'].append(expect(ofe.text))
                        objectdict['product_image'].append(i.text+re.findall(r'\d+',pr.text)[0])
                        objectdict['Date'].append(dt.now().date())
                        product_name.append(i.text)
                        product_price.append(pr.text)
                        # print(pr.text)
                        product_image.append(i.text+":"+re.findall(r'\d+',pr.text)[0])
                    else:
                        print("product already exists")

        except Exception as e:
            print(f"Error occurred: {e}")
            break
        end1=drive.execute_script("return document.body.scrollHeight") 
        print(objectdict)
        print(product_image)
        if end==end1:
            break
        # break 
        cn+=1


    df=pd.DataFrame(objectdict)
    # print(df)
    print(f'no_of_itterations happend {cn}')
    print(f"product extraction_done creating connection to data base at {time.ctime()}")
    return df
    # try:
    #     engine = create_engine("mysql+pymysql://my_user:my_password@localhost:3306/my_database")
    #     print("connection_estrablisehed")
    #     df.to_sql('wrogn_products',con=engine,if_exists='append',index=False)
    #     print("data inserted into the database")   
    # except Exception as e:
    #     print(e)
    
   
def price_range_det(x):
    if x>0 and x<500:
        return '0-499'
    elif x>=500 and x<700:
        return '500-699'
    elif x>=700 and x<1000:
        return '700-999'
    elif x>=1000 and x<1500:
        return '1000-1499' 
    elif x>=1500 and x<2000:
        return '1500-1999'
    elif x>=2000 and x<3000:
        return '2000-2999'
    elif x>=3000 and x<5000:
        return '3000-4999'
    elif x>=5000 and x<10000:
        return '5000-9999'
    elif x>=10000:
        return '10000+'


def raw_to_gold(df):
    print("raw data to gold data conversion started")
    try:
        df['color']=df['product_name'].str.split("|").apply(lambda x:x[1] if len(x[1:])>0 else 'no_color')
        df['type']=df['product_name'].str.split("|").apply(lambda x:x[0] if len(x)>0 else 'no_type')
        df['product_styp']=df['type'].str.split(" ").apply(lambda x: x[-1] if len(x[-1])>0 else (x[-2] if len(x)>0 and len(x[-2])>0 else 'unappor') )
        df['price']=df['product_price'].apply(lambda x: re.findall(r'\d+', x.replace(',',""))[0] if len(re.findall(r'\d+', x))>0 else '0').astype(int)
        df['price_range']=df['price'].apply(lambda x:price_range_det(x) if x>0 else'no_price_detected') 
        print("raw data to gold data conversion done")
        return df.copy()
        
    except Exception as e:
        print(e)

        if __name__ == "__main__":
            raw_data=wrogn_extract_raw()
            gold_data=raw_to_gold(raw_data)
