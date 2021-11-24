import os
from dotenv import load_dotenv
from instapy import InstaPy
from instapy import smart_run

# carregar arquivo .env
load_dotenv()

# variaveis de ambiente .env
email       = os.getenv('EMAIL')
password    = os.getenv('PASSWORD')

# inciando uma sessão
session     = InstaPy(username=email, password=password)

with smart_run(session):
    session.set_do_follow(enabled= True, percentage= 100)
    session.set_do_like(enabled= True, percentage= 100)

    session.like_by_tags(['decorarcasa'], amount=5)

    # comments = ['Linda decoração']
    # session.set_do_comment(enabled= True, percentage=95)
    # session.set_comments(comments, media='Photo')
    session.join_pods()