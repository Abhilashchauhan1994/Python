# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = '<yourUsername>'
insta_password = '<yourpassword>'

comments=[ 
    {'mandatory_words': ["mehandi", "hena","make up"], 
     'comments': [":thumbsup:",
        "incredible :open_mouth:",
        ":raised_hands: Yes!",
        "Good Work keep it up"]},
    ]
comments = [
        ]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  #session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(["makeup"], amount=10)

  # Joining Engagement Pods
  #session.set_do_comment(enabled=True, percentage=35)
  #session.set_comments(comments)
  #session.join_pods(topic='', engagement_mode='no_comments')