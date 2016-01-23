# www.pycon.jp

- GitHub: https://github.com/pyconjp/www.pycon.jp
- URL: http://www.pycon.jp/
- URL(RTD): http://wwwpyconjp.readthedocs.org/

## build

```
$ git clone https://github.com/pyconjp/www.pycon.jp.git
$ virtualenv env
$ . env/bin/activate
(env)$ pip install -r requirements.txt
(env)$ make html
(env)$ open _build/html/index.html
```