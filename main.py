from instascrape import *
profile = Profile('https://www.instagram.com/tamarailievaa/')
profile.scrape()
recents = profile.get_recent_posts()
user_photos = [post for post in recents if not post.is_video]
for post in user_photos: 
    fname = post.upload_date.strftime("%Y-%m-%d %Hh%Mm")
    post.download(f"{fname}.png")