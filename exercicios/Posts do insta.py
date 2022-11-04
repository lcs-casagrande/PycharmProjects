from datetime import datetime
import instaloader
L = instaloader.Instaloader()
L.login('lcs.casagrande','Lucas@2015')

posts = instaloader.Profile.from_username(L.context, 'lcs.casagrande').get_posts()

SINCE = datetime(2010,1,1)
UNTIL = datetime(2021,12,12)

for post in posts:
    if (post.date >=SINCE) and (post.date <= UNTIL):
        print(post.date)
        L.download_post(post, 'insta-post-dowloads')


