# www.pycon.jp

[![Documentation Status](https://readthedocs.org/projects/wwwpyconjp/badge/?version=latest)](http://www.pycon.jp/?badge=latest)
                
- GitHub: https://github.com/pyconjp/www.pycon.jp
- URL: http://www.pycon.jp/ or https://www.pycon.jp/
- URL(RTD): http://wwwpyconjp.readthedocs.org/

## ビルド環境準備

Ubuntu環境でのフォントインストール
```
$ sudo apt update
$ sudo apt install fonts-noto-cjk
$ rm -rf ~/.cache/matplotlib
```

## build

```
$ git clone https://github.com/pyconjp/www.pycon.jp.git
$ cd www.pycon.jp
$ python3.12 -m venv env
$ . env/bin/activate
(env)$ pip install -r requirements.txt
(env)$ make html
(env)$ open _build/html/index.html
```
