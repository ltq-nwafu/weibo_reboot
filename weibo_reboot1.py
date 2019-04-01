import shlex
import webbrowser
import time
import subprocess
import sinaweibopy3


def main():
    """
    if you want to use this api,you should follow steps follows to operate.
    """

    try:
        # step 1 : sign a app in weibo and then define const app key,app secret,redirect_url
        APP_KEY = '4139690010'
        APP_SECRET = '4c3fb4a9b423c5cdeb0c0d9413e8b4a7'
        REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'

        # step 2 : get authorize url and code
        client = sinaweibopy3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
        url = client.get_authorize_url()
        # print(url)
        webbrowser.open_new(url)

        # step 3 : get Access Token
        # Copy the above address to the browser to run,
        # enter the account and password to authorize, the new URL contains code
        result = client.request_access_token(
            input("please input code : "))  # Enter the CODE obtained in the authorized address
        print(result)  # Save the access_token from here.

        # At this point, the access_token and expires_in should be saved,
        # because there is a validity period.
        # If you need to send the microblog multiple times in a short time,
        # you can use it repeatedly without having to acquire it every time.
        client.set_access_token(result.access_token, result.expires_in)

        # step 4 : using api by access_token
        '''
        in this step,the api name have to turn '/' in to '__'
        for example,statuses/public_timeline(this is a standard api name) have to turn into statuses__public_timeline
        '''

        # Obtain the UID of the authorized user
        # uid = client.get.account__get_uid()
        # print(uid)

        init_status = client.get.statuses__user_timeline()['statuses'][0]  # 获取用户最近微博

        while True:
            current_status = client.get.statuses__user_timeline()['statuses'][0]  # 获取用户最近微博
            current_text = current_status['text']
            current_id = current_status['id']
            # print(time.ctime(), current_text)

            if current_id != init_status['id'] and current_text:
                args = shlex.split(current_text)
                args.pop()
                subprocess.check_output(args, shell=False)

                if '-s' in args:
                    client.post.comments__create(id=current_id, comment='正在关机......')
                elif '-a' in args:
                    client.post.comments__create(id=current_id, comment='已取消关机......')

                init_status = current_status

            time.sleep(10)  # ip限制1000次/小时

    except ValueError:
        print('pyOauth2Error')


if __name__ == '__main__':
    main()
