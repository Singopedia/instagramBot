from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from datetime import date
import pickle

unfollow_them_in_days = 2
today = date.today ()
today_date = today.strftime ('%d')
today_final_date = int(today_date) + unfollow_them_in_days



class instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.driver = driver.Chrome()
        self.bot = webdriver.Chrome (
            executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    def set_window(self, w, h):
        bot = self.bot
        self.h = h
        self.w = w

        bot.set_window_size (w, h)



    def login(self):
        bot = self.bot
        bot.get ('https://www.instagram.com/accounts/login/')
        time.sleep (2)
        email = bot.find_element_by_name ('username').send_keys(self.username)
        password = bot.find_element_by_name ('password').send_keys(self.password + Keys.RETURN)
        time.sleep(4)


    def select_now(self):
        bot = self.bot
        bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        time.sleep(1)

    def search_hashtags(self, hashtags):
        bot = self.bot
        # self.hashtags = hashtags
        bot.get (f"https://www.instagram.com/explore/tags/{hashtags}")


    def OpenWindowtolike(self):
        bot = self.bot
        bot.find_element_by_class_name ('v1Nh3').click ()
        time.sleep(3)





    def followlike(self, amount):
        bot = self.bot
        self.amount = amount

        i = 1
        # pdb.set_trace()
        while i <= amount:
            time.sleep (1)

            # bot.find_element_by_class_name ('fr66n').click()
            # bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a')
            if bot.find_elements_by_xpath ("//div[contains(@class,'bY2yH')]//button[contains(@class,'')][contains(text(),'Following')]"):
                bot.find_element_by_class_name ('coreSpriteRightPaginationArrow').click ( )
                time.sleep (2)

            else:
                bot.find_element_by_xpath ("//div[contains(@class,'bY2yH')]//button[contains(@class,'')][contains(text(),'Follow')]").click () # or bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                bot.find_element_by_class_name ('coreSpriteRightPaginationArrow').click()

                time.sleep(1)


            i += 1


        waiting1 = today.strftime ('%d')
        waiting = int(waiting1)

        print ('All the Things are Done')
        time.sleep(1)
        print(f'Sir, We will be Unfollowing Them all in {unfollow_them_in_days} Days')
        pickle.dump (bot.get_cookies (), open ("cookies.pkl", "wb"))
        time.sleep(2)



        if waiting == today_final_date:

            cookies = pickle.load (open ("cookies.pkl", "rb"))
            for cookie in cookies:
                bot.add_cookie (cookie)


            print('Lets Unfollow Them Allll')

            def unfollow(amount):

                print("unfollowing NOW")
                bot = self.bot
                bot.get(f"https://www.instagram.com/{self.username}")
                bot.find_element_by_xpath('//li[3]//a[1]').click()

                time.sleep(2)

                z = 1

                while z <= amount:

                    if bot.find_elements_by_link_text("Following"):

                        bot.find_element_by_link_text('Following')[0].click()
                        time.sleep(1)
                        z += 1

                    else:
                        return

            unfollow(self.amount)
            bot.close()