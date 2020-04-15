from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://192.168.10.216/biz/user-login.html")
# driver.maximize_window()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("CD123456")
time.sleep(1)

driver.find_element_by_id("submit").click()
time.sleep(1)

#修改公司名称
driver.find_element_by_xpath('//a[@href="/biz/company/"]').click()
driver.find_element_by_xpath('//a[@href="/biz/company-view.html"]').click()
driver.find_element_by_id("editCompany").click()
time.sleep(1)
driver.switch_to.frame("iframe-triggerModal")
driver.find_element_by_xpath('//input[@id="name"]').clear()
driver.find_element_by_xpath('//input[@id="name"]').send_keys("丝路天地")
driver.find_element_by_xpath('//button[@id="submit"]').click()
time.sleep(3)

#创建部门
driver.find_element_by_xpath('//a[@href="/biz/dept-browse.html"]').click()
driver.find_element_by_xpath('//td[@class="w-300px"]/input[1]').clear()
driver.find_element_by_xpath('//td[@class="w-300px"]/input[1]').send_keys("部门1")
driver.find_element_by_xpath('//td[@class="w-300px"]/input[2]').clear()
driver.find_element_by_xpath('//td[@class="w-300px"]/input[2]').send_keys("部门2")
driver.find_element_by_xpath('//td[@class="w-300px"]/input[3]').clear()
driver.find_element_by_xpath('//td[@class="w-300px"]/input[3]').send_keys("部门3")
driver.find_element_by_xpath('//td[@class="w-300px"]/input[4]').clear()
driver.find_element_by_xpath('//td[@class="w-300px"]/input[4]').send_keys("部门4")
#driver.find_element_by_xpath('//table[@class="table table-form"]/tbody/tr[1]/td[2]/input[1]').send_keys("部门1")

driver.find_element_by_xpath('//button[@id="submit"]').click()
time.sleep(1)

#每个部门加入2个员工
driver.find_element_by_xpath('//a[@href="/biz/company-browse.html"]').click()
driver.find_element_by_xpath('//a[@href="/biz/user-batchCreate-0.html"]').click()
time.sleep(1)
driver.find_element_by_xpath('//a[@class="chosen-single"]').click()
driver.find_element_by_xpath('//li[@title="/部门1"]').click()

#批量添加
driver.find_element_by_xpath('//div[@id="dept0_chosen"]').click()
driver.find_element_by_xpath('//li[@title="/部门1"]').click()
driver.find_element_by_xpath('//div[@id="dept1_chosen"]').click()
driver.find_element_by_xpath('//div[@id="dept1_chosen"]/div/ul/li[@title="/部门1"]').click()

driver.find_element_by_xpath('//div[@id="dept2_chosen"]').click()
driver.find_element_by_xpath('//div[@id="dept2_chosen"]/div/ul/li[@title="/部门2"]').click()
driver.find_element_by_xpath('//div[@id="dept3_chosen"]').click()
driver.find_element_by_xpath('//div[@id="dept3_chosen"]/div/ul/li[@title="/部门2"]').click()

driver.find_element_by_xpath('//div[@id="dept4_chosen"]').click()
driver.find_element_by_xpath('//div[@id="dept4_chosen"]/div/ul/li[@title="/部门3"]').click()
driver.find_element_by_xpath('//div[@id="dept5_chosen"]').click()
driver.find_element_by_xpath('//div[@id="dept5_chosen"]/div/ul/li[@title="/部门3"]').click()

driver.find_element_by_xpath('//div[@id="dept6_chosen"]').click()
driver.find_element_by_xpath('//div[@id="dept6_chosen"]/div/ul/li[@title="/部门4"]').click()
driver.find_element_by_xpath('//div[@id="dept7_chosen"]').click()
driver.find_element_by_xpath('//div[@id="dept7_chosen"]/div/ul/li[@title="/部门4"]').click()

driver.find_element_by_xpath('//input[@id="account[0]"]').send_keys("yuangong1")
driver.find_element_by_xpath('//input[@id="account[1]"]').send_keys("yuangong2")
driver.find_element_by_xpath('//input[@id="account[2]"]').send_keys("yuangong3")
driver.find_element_by_xpath('//input[@id="account[3]"]').send_keys("yuangong4")
driver.find_element_by_xpath('//input[@id="account[4]"]').send_keys("yuangong5")
driver.find_element_by_xpath('//input[@id="account[5]"]').send_keys("yuangong6")
driver.find_element_by_xpath('//input[@id="account[6]"]').send_keys("yuangong7")
driver.find_element_by_xpath('//input[@id="account[7]"]').send_keys("yuangong8")

driver.find_element_by_xpath('//input[@id="realname[0]"]').send_keys("员工1")
driver.find_element_by_xpath('//input[@id="realname[1]"]').send_keys("员工2")
driver.find_element_by_xpath('//input[@id="realname[2]"]').send_keys("员工3")
driver.find_element_by_xpath('//input[@id="realname[3]"]').send_keys("员工4")
driver.find_element_by_xpath('//input[@id="realname[4]"]').send_keys("员工5")
driver.find_element_by_xpath('//input[@id="realname[5]"]').send_keys("员工6")
driver.find_element_by_xpath('//input[@id="realname[6]"]').send_keys("员工7")
driver.find_element_by_xpath('//input[@id="realname[7]"]').send_keys("员工8")

driver.find_element_by_xpath('//input[@id="password[0]"]').send_keys("Yg1123456")
driver.find_element_by_xpath('//input[@id="password[1]"]').send_keys("Yg2123456")
driver.find_element_by_xpath('//input[@id="password[2]"]').send_keys("Yg3123456")
driver.find_element_by_xpath('//input[@id="password[3]"]').send_keys("Yg4123456")
driver.find_element_by_xpath('//input[@id="password[4]"]').send_keys("Yg5123456")
driver.find_element_by_xpath('//input[@id="password[5]"]').send_keys("Yg6123456")
driver.find_element_by_xpath('//input[@id="password[6]"]').send_keys("Yg7123456")
driver.find_element_by_xpath('//input[@id="password[7]"]').send_keys("Yg8123456")

driver.find_element_by_xpath('//input[@placeholder="请输入您的系统登录密码"]').send_keys("CD123456")

