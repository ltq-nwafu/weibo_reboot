import shlex
import time
import subprocess
import requests


def run():
    """
    if you want to use this api,you should follow steps follows to operate.
    """

    try:

        ACCESS_TOKEN = '2.00TrgCYCiTiJWEe9567ae00e4mwgqB'
        USER_URL = 'https://api.weibo.com/2/statuses/user_timeline.json'
        COMMENT_URL = 'https://api.weibo.com/2/comments/create.json'

        params1 = {
            'access_token': ACCESS_TOKEN
        }

        init_status = requests.get(url=USER_URL, params=params1).json()['statuses'][0]  # 获取用户最近微博
        # print(init_status)

        while True:
            current_status = requests.get(url=USER_URL, params=params1).json()['statuses'][0]  # 获取用户最近微博
            # print(current_status)
            current_text = current_status['text']
            current_id = current_status['id']
            # print(time.ctime(), current_text)

            if current_id != init_status['id'] and current_text:
                # print("将执行的命令：", current_text)
                args = shlex.split(current_text)
                args.pop()
                subprocess.check_output(args, shell=False)

                tmp1 = '正在关机......'
                tmp2 = '已取消关机......'
                params2 = {
                    'access_token': ACCESS_TOKEN,
                    'id': current_id,
                    'comment': tmp1
                }
                params3 = {
                    'access_token': ACCESS_TOKEN,
                    'id': current_id,
                    'comment': tmp2
                }
                # if '-s' in args:
                #     requests.post(url=COMMENT_URL, params=params1, id=current_id, comment='正在关机......')
                # elif '-a' in args:
                #     requests.post(url=COMMENT_URL, params=params1, id=current_id, comment='已取消关机......')
                if '-s' in args:
                    requests.post(url=COMMENT_URL, data=params2)
                    # print('已经关机!')
                elif '-a' in args:
                    requests.post(url=COMMENT_URL, data=params3)
                    # print('已经取消!')

                init_status = current_status

            time.sleep(10)  # ip限制1000次/小时

    except ValueError:
        print('pyOauth2Error')


if __name__ == '__main__':
    run()
