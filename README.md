# www.pycon.jp

[![Documentation Status](https://readthedocs.org/projects/wwwpyconjp/badge/?version=latest)](http://www.pycon.jp/?badge=latest)
                
- GitHub: https://github.com/pyconjp/www.pycon.jp
- URL: http://www.pycon.jp/ or https://www.pycon.jp/
- URL(RTD): http://wwwpyconjp.readthedocs.org/

## build

```
$ git clone https://github.com/pyconjp/www.pycon.jp.git
$ cd www.pycon.jp
$ virtualenv env
$ . env/bin/activate
(env)$ pip install -r requirements.txt
(env)$ make html
(env)$ open _build/html/index.html
```