with open('environment.env', 'r' ) as file :
    env = file.read().split('\n')
    CLIENT_ID           = env[0]
    CLIENT_SECRET       = env[1]
    NAVER_NEWS_QUERY_URL= env[2]
    GPT_KEY             = env[3]