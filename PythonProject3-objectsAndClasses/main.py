# to import and use all fxns in the user.py file
#import user

#import class only from the user.py file
from user import User
from post import Post

app_user_one = User("ferdie@nn.com", "Acha Ferdie", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

#app_user_one.change_job_title("Senior site Reliability Engineer")
#app_user_one.get_user_info()

app_user_two = User("tekwe@gmail.com", "Tekwe smo", "pwd2", "Platform Engineer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()