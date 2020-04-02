#!/usr/bin/python3
# coding: utf-8

from slackbot.bot import respond_to     # メンションされて反応する
from slackbot.bot import listen_to      # メンションなしで反応
from slackbot.bot import default_reply  #どれにも当てはまらない場合 

import keys
import subprocess
import requests
import json

def exec_linux_cmd(cmd):
    res = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    res = res.stdout
    return res.decode("utf-8")

############slack api###########
url = "https://slack.com/api/chat.postMessage"
data = {
        "token": keys.API_TOKEN,
        "channel" : keys.CHANNEL_TOKEN,
        "text" : "default",
        "as_user": "true"
    }
################################

# @hogehoge ///ifconfig
# => @hogehoge が ifconfig を実行して，その結果を投げる
@respond_to("^///")
def test_ls(message):
    try:
        cmd = message.body["text"][3:]
        message.reply("run command:  " + cmd)
        data["text"] = "```" + exec_linux_cmd(cmd) + "```"
        requests.post(url, data=data)
        #message.reply(data)
    except:
        message.reply("Error.")

#  メンションテスト
@respond_to('test_mention')
def mention_func(message):
    message.reply('メンションされた') # メンション

# cpuとかの温度を投げる(メンション不要)
@listen_to('sensors')
def mention_all(message):
    data["text"] = "```" + exec_linux_cmd('sensors') + "```"
    requests.post(url, data=data)
