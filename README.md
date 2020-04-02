# Slackbot

## Features

1. You can execute linux command from Slack.

```
@(BOTNAME) ///(Linux command)
```
Bot reply excute results.

![image](https://user-images.githubusercontent.com/44022415/78248900-6dd46880-7528-11ea-9ad3-2cd53adad85e.png)

## Setup

1. Install module

```sh
pip3 install -r requirements.txt
```

2. Set TOKENs

Set TOKENs to this file.

```sh
vim keys-example.py
```

Change file name 'keys-example.py' to 'keys.py'

```sh
mv keys-exapmle.py keys.py
```

3. Run slackbot

```sh
python3 run.py
```


## Autostart

```sh
mv Slackbot.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable Slackbot.service
systemctl status Slackbot.service
```

If you can see `active(running)`, it is working.
