from InstagramFollowBot import instabot
import time
import random

#Write Down Your Preffered Hashtags.

hashtagze = ["pubggaming", "pubg", 'arcadepubg', 'pubgmontage', 'pubgmemes', 'pubgstory', 'starchallenge', 'cradles', 'meme', 'funnypubg', 'mememaker']
random_hashtagze = random.choice(hashtagze)


insta = instabot("", '') #Add Username and Add Password Respectively


insta.set_window(210, 708)

insta.login()



insta.select_now()

insta.search_hashtags(random_hashtagze)

insta.OpenWindowtolike()
insta.followlike(3)

