from selenium import webdriver

brower = webdriver.PhantomJS()
brower.get('http://www.baidu.com')
print(brower.current_url)
