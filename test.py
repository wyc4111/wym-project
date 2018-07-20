'''
Created on 2018Äê7ÔÂ10ÈÕ

@author: youming
'''
# coding=utf-8

from selenium.webdriver import Remote
from time import ctime,sleep
import threading
import multiprocessing
from selenium import webdriver
from threading import Thread

def test_baidu(host,browser):
    print('start:%s' %ctime())
    print(host,browser)
    dc={'browserName':browser}
    dr=webdriver.Remote(command_executor=host,
                        desired_capabilities=dc
                        )
    dr.get("http://www.baidu.com")
    dr.find_element_by_css_selector("#kw").send_keys(browser)
    dr.find_element_by_css_selector("#su").click()
    sleep(2)
    dr.get_screenshot_as_file('D:\\workspace\\remote\\0712.png')
    sleep(2)
    dr.quit()
if __name__=='__main__':
    lists={"http://127.0.0.1:4444/wd/hub":"chrome",
#           "http://127.0.0.1:8888/wd/hub":"firefox",
           "http://192.168.100.182:9999/wd/hub":"firefox",
           }
    threads=[]
    files=range(len(lists))
    for host,browser in lists.items():
        t=Thread(target=test_baidu,args=(host,browser))   
        threads.append(t)
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join() 
    print("end:%s"%ctime())
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
