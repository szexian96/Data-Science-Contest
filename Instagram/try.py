target_profile = 'masakmasak_tokyo'

from instaloader import Instaloader, Profile
loader = Instaloader()
loader.login('j19048ss','Szexian960502')

profile = Profile.from_username(loader.context, target_profile)

num_followers = profile.followers
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0

for post in profile.get_posts():
    total_num_likes += post.likes
    total_num_comments += post.comments
    total_num_posts += 1


file = open("output.txt","w")
file.write(str(num_followers) + '\n')
file.write(str(total_num_likes)+'\n')
file.write(str(total_num_posts)+'\n')
file.close()