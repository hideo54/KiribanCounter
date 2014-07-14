キリ番カウンター(KiribanCounter)
===============

##概要
きりの良いツイート数になるときに自動でつぶやいてくれるbotです。

具体的には、100の倍数ツイートになるとき、もしくはツイート数がゾロ目になるときにつぶやいてくれます。

ただし、ツイート数が一桁の時には、ゾロ目判断は無効。毎回つぶやかれてしまうからです。

また、ツイート数が "99…9" の時も、ゾロ目判断は無効。その直後に100の倍数ツイートがくるためです。

##バージョン
ver 2.0.1

##動作環境
Python 2系がインストールされたPC

###動作確認済み環境
Python 2.7.5 on OS X 10.9.4 (2014/7/14)

##動かし方
1. ソースコード内の"consumer_key", "consumer_secret", "access_token", "access_token_secret" にそれぞれ自分の鍵を設定。

2. crontabなどで1分毎に動かすなどしてください。

##連絡先
Twitter… [@hideo54](https://www.twitter.com/hideo54)
Email… hideo54.pub@gmail.com
