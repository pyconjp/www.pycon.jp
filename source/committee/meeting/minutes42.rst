===============================================================
 2020年11月25日(水) 一般社団法人PyCon JP Association運営会議#42
===============================================================

* 日時: 2020年11月25日(水) 19:30-21:30

  * https://pyconjp-staff.connpass.com/event/190301/
* 場所: CMSコミュニケーションズ、Zoom
* 理事: terada, takanori, jonas, shimizukawa, yoshida
* オブザーバー: peacock, yoshi-tsukamo, ryu22e, nikkie, nishi, kanan, maaya,kobatomo


課題のレビュー
==============
* `一般社団法人PyCon JPの課題 <https://pyconjp.atlassian.net/issues/?filter=11500&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20%3D%20%E4%B8%80%E8%88%AC%E7%A4%BE%E5%9B%A3%E6%B3%95%E4%BA%BA%20ORDER%20BY%20due%20ASC%2C%20updated%20ASC%2C%20component%20ASC>`_

PyCon JP 2020 (nishi、低、報告)
-------------------------------
* 残タスクの状況

  * Tシャツ発送

    * 国内完了 @peacock/@yoshida
    * COVID-19関係で送付できなかった海外の一部は諦め
  * ジャパンネット銀行トークンカードの返却

    * nikkieに手渡しする
  * 旧ドライブ(2020)の削除

    * @ds110のファイル移動作業待ち
    * フォームはダウンロードできないので、作成者本人の移動が必要。
  * ナレッジ集約(11月末目処)
    * Confluenceでとりまとめ

      * https://pyconjp.atlassian.net/wiki/x/c4CpM
      * 今は公開されていないけど、まだ設定していないだけ?(takanory
      * まだ設定していない。これから設定予定(nishi
  * 会計担当(@ds110)タスク → ds110が対応不可とのことで、nishiが実施

    * 立替精算(nishiに集約済み) 依頼済み
    * (年末頃以降)収支情報の整理・公開

      * 会計事務所から集計データをもらってから着手(年始以降)

PyCon JP 2021(terada、高、報告)
-------------------------------
* nikkieさんから座長の立候補があり、全会一致で決定済み 🎉
* Blogでの報告済み

  * `PyCon JP Blog: PyCon JP 2021 座長決定 <https://pyconjp.blogspot.com/2020/10/pyconjp-2021-chair.html>`_
* ここまでの動きの共有 (低、報告、nikkie)

  * 10月〜11月は2020のナレッジ集約を優先した形になった
  * Confluenceでnishiさんから座長が最初にやること引き継ぎ済み
* 今後の動きの相談 (高、相談、nikkie)

  * 今週・来週（〜12/6）でスタッフ募集を始められるように動く
  * まずどんな形態でやるか、考えたい人だけで始めたい（スタッフ経験者or過去参加者前提）

    * オンライン
    * 併催（オンライン + オフライン）
  * 他のオンラインカンファレンスを参考に、2020より盛り上がれる・一体感を感じられる形を模索したい
  * 次回一社の運営会議で相談できるようにいくつか案をまとめる考え
* 2021のSlackって作った?(nishi

  * 昨日そっと作った(nikkie
  * チャンネル作ったことを 2020 スタッフに伝えて、入ってもらうとよさそう(nishi

PyCon JP 2022のPiO予約
----------------------
* https://pyconjp.atlassian.net/browse/ISSHA-2226

  * 必要ならメール回答:令和４年度ＰⅰＯ特別予約希望調査について
  * 令和3（2021）年１月22日（金）まで
* 現状なにも決まっていないので申し込めないかなー(terada, takanory
* 「申し込めないという連絡をする」でよいと思う(shimizukawa
* いつ申し込めるようになるかは考える必要があるか。オフラインイベントに積極的に切り替えるのはいつか?(shimizukawa

  * 都度話すしかなさそう(terada, takanory
* **TODO**: 連絡する(yoshida

PyCamp、PyLadies関連
====================

Pycamp状況報告(ryu22e、低、報告)
--------------------------------
* 11月以降の開催場所状況

  * 2021年1月16日 鎌倉で開催予定

    * 講師: 新井さん
    * Connpassイベントページ: https://pyconjp.connpass.com/event/191650/
* 「Python Boot Campその後」ブログの進捗状況(@ryu22e)

  * 以下は公開済み

    * 第3回 すごい広島 with Python

      * https://pyconjp.blogspot.com/2020/09/after-pycamp-sugoi-hiroshima-with-python.html
    * 第4回 Shonan.py

      * https://pyconjp.blogspot.com/2020/11/after-pycamp-shonan-py.html.html
  * 以下はレビュー中

    * Shingen.py（回答をもらっている中ではこれがラスト）
  * 以下のコミュニティには回答をもらっていないが、再度お願いしてみる。1週間ぐらい待って返答がなければ諦める。回答してくれたコミュニティの記事を書いたらこの企画は完了にする予定。

    * 和歌山 Python もくもく会: @ottidododo
    * PyCon Kyushu: @kiyota
    * PyEhime: @kazweda
    * Udon.py: @kobatomo
    * 大阪Pythonの会 @akira_taniguchi
  * Python Boot Campのページとかでまとめて、リンクとかするとよさそう(takanory

    * **TODO**: 検討して進める(ryu22e
* 9/29(火) 20:30 - Python Boot Camp オンライン相談会 2回目を開催した。(@kobatomo)

  * https://pyconjp.connpass.com/event/188776/
  * 今回は、OST(Open Space Technology)形式で進めます。 `mural <https://www.mural.co/>`_ を使って話のネタを当日決める。という実験をした
  * いい感じで話ができた(takanory, ryu22e

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、低、報告)
------------------------------------------------------------
* スライド置き場 https://github.com/pyconjp/slides/
* 最近の活動

  * OSC Fallオンライン(10/24)

    * セミナーとミーティング(講師：たかのり)
    * Python Boot CampやPyLadies Caravanの概要説明（塚本）
  * 11票くらいでトップだった(terada

    * OSCへの貢献みたいな効果はあったのではないか?(terada
* 今後の活動

  * OSC 福岡オンライン(11/28)

    * セミナーとミーティング(講師：寺田)
* OSC大阪オンラインの受付が開始(2021/1/30)

  * 大阪参加していないから出たいって感じ?(terada
  * オンラインなので参加したい(yoshi-tsukamoto
  * 参加した効果がわかりにくい。OSC全体の参加者も減っている(terada
  * 2021年度のOSC出展の予算をどうするかも議論することになると思う(terada
* OSC浜名湖(静岡)の開催検討中

  * 普段小規模なところ、さらにオンラインになりそう。出展するかは要検討
* また来年のネタを考えないとなー(takanory

  * 2021年4月あたりから新しいネタにしたい感じ(takanory

PyLadies関係報告(maaya, 低, 報告)
---------------------------------
* 年内のCaravanツアーは断念。冬を超えてから状況見て判断
* オンラインでやるならJapanでなんかイベントやればよいか？という話はでているものの、各リージョン運営に現在その体力がなく立ち消え気味

コミュニティー支援
==================

イベント/コミュニティサポートプログラム(takanory、低、なし)
-----------------------------------------------------------
* とくになし

Python地域交流オンライン座談会(takanory、低、報告)
--------------------------------------------------
* 10月23日(金)に静岡の佐野さん発案で「のみpy」実施済。

  * https://pyconjp.connpass.com/event/188778/
  * takanory参加予定だったが、体調不良で欠席
  * 結構盛り上がった。ふだん交流がない人とも話ができた。またやろうって感じだった(ryu22e
  * 言い出しっぺ佐野さんのブログ

    * `Python地域コミュニティ飲み会の「のみPy（仮）」を開催しました #pyconjp <https://hr-sano.net/blog/2020/11/08/nomipy_no1/>`_
  * 2021年になったらまた開催するかな?

地域PyCon等の支援について(takanory、低、報告)
---------------------------------------------
* PyCon mini Hiroshima

  * https://hiroshima.pycon.jp/2020/
  * 日付: 10月10日(土)
  * 会場: オンライン
  * 開催済
* SciPy Japan

  * https://www.scipyjapan.scipy.org/
  * 日付: 10月30日(金)~11月2日(月)
  * 会場: オンライン
  * 開催済
  * サポートは連絡がなかったので未実施

海外コミュニティ連携
====================

Python商標問題(terada、低、報告)
--------------------------------
* 進展なし。

PSFへの寄付イベント(terada、中、報告)
-------------------------------------
* PSFへ楽天銀行から振込済み。楽天銀行も比較的に安い（2000円）で振り込めた。
* PSFからニュースレターで報告をしてもらえることになっている。
* 上記のニュースレターが出たら、最終報告やスポンサーへのお礼を行う。
* またやりたい気持ちはある(takanory
* 省力化したいので、スポンサー対応は減らす。LTもなし or LTリハーサルなし(takanory

  * 寄付はするけど金額は減るかな(takanory
* 時期的には早くて来年2月とか(takanory
* 見る側としては楽しみ(yoshi-tsukamo
* 再演で安定したトークがあった。PyCon JP 2020の前に実施してノウハウがない中でいい練習になった(yoshida

  * PyCon JP 2020とmini Hiroshimaのネタから選べると思っている(takanory
* ハイブリッドを少人数でやってみるとか?(terada

APAC関連(terada、高、相談)
--------------------------
* PyCon APAC 2021の開催地立候補が2箇所あり
* https://pyconjp.atlassian.net/browse/ISSHA-2224

  * マレーシア・コタキナバル
  * タイ・バンコク
* 11月19日にプロポーザル読み合わせ会を行った

  * https://docs.google.com/document/d/186RPa8N9_igTmeDrs2QiRuiCpC9Qc-wJBzzs29iX8sA/edit
* どっちとも決めかねている(yoshida
* オンラインはどっちでも変わらない。オフラインだったらタイがよさそう。初のPyCon Thailandでもちゃんとしていた。マレーシアはクオリティが上がらない。Proposalも気合い入っている(jonas
* マレーシアに+0って感じです。今年開催予定がオンラインになってしまったので、かわいそうだなっていう感じです(takanory

  * 同じ意見です。オフラインにならないだろうなと思っている(shimizukawa
* 主催者の実績の点でタイの方が実行可能性が高いと感じた。タイは6月に実施していたのを、COVID-19対策で11月にしているので、よく考えられている。一方takanoryの意見にも同意する部分はある。マレーシアでオフラインのイベントをやってもらうのも一つだと思っている。タイに+1(terada
* 「タイ」で決定(terada
* **TODO**: 11月27日までに日本からの投票を行う。寺田が投票システムへのアカウントをもらっている

APAC・JPロゴ関係(terada、低、相談)
----------------------------------
* 進展なし

APACブース in US PyCon(terada、中、報告)
----------------------------------------
* ロゴデザイン費用を、採択されたデザイナーの意向で2020のAPAC（マレーシアチーム）に寄付を行った。

その他
======

PyCon JP Twitterについて(takanory、高、議論)
--------------------------------------------
* 現在凍結されている

  * https://pyconjp.atlassian.net/browse/ISSHA-2210
* スパムアカウント認定されてしまったのが原因(takanory
* 一発アウトなので、さすがに凍結解除されないってことはないんじゃないのかなー(takanory

  * Twitterとやりとりする窓口はあるの?(terada
  * メールで連絡する窓口はある(yoshida
  * 日本の窓口に問い合わせるのがいいんじゃないかなぁ(takanory
  * 原因を聞いてダメって言われたら諦める?(terada
  * **TODO**: 巻き取って進める(terada
* Twitter IDでログインしているアカウントが使えなくなっている(takanory

  * Connpass, papercallくらい?そこまで影響はなさそう(yoshida
  * connpassに入れないとなにが困る?(shimizukawa)
* 凍結解除は望みが薄い認識→新アカウントを作りたい (nikkie)

  * 2021スタッフ募集など告知を始めていきたい
  * スタッフが動き出すと、Twitter IDログインが軒並み使えないのが不便（例：connpass）

Zoomアカウントについて(takanory、中、議論)
------------------------------------------
* Zoomの現在使用しているライセンスは人に紐付いているので、貸し借りとかするのはNGっぽい
* Zoom Roomsで契約して、PyCon JPの会議室をみんなで利用するという形式の方が適切っぽい

  * 参考: `ZoomミーティングとZoom Roomsの違いを教えてください。 <https://zoom-support.nissho-ele.co.jp/hc/ja/articles/360037518372-Zoom%E3%83%9F%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%A8Zoom-Rooms%E3%81%AE%E9%81%95%E3%81%84%E3%82%92%E6%95%99%E3%81%88%E3%81%A6%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84>`_
* 料金は「25,200円/年/ユーザ」→「63,600円/年/会議室」
* ただ、実際の会議室がないので、どういう運用になるのかは要調査(Googleカレンダーと連携できそう?)
* 問い合わせたが方が早そう?
* **TODO**: チケット作ってやります(takanory

  * https://pyconjp.atlassian.net/browse/ISSHA-2227

運営メンバー制度(takanory、低、報告)
------------------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-1490
* 運営メンバーのページを公開した

  * https://www.pycon.jp/committee/members.html
* 運営メンバー募集のBlogを公開したら終了

弁護士との契約について(yoshida、低、なし)
-----------------------------------------
* 報告なし

法人名変更(terada、 中、報告)
-----------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-2091
* 銀行名の変更手続き中。書類の発送を終えた。
* 書類が戻ってきた。印鑑変更の手続きを行う。

pycon.jp OSサーバー移行(yoshida、中、報告)
------------------------------------------
* `20201115pycon.jpサイト移行MTG <https://docs.google.com/document/d/1P8UaMO7Z6DaKKn6ii6_5oFIJahNg7mq-RUOh7ai1f-0/edit#>`_

  * 11/1 サーバ移行完了
  * `origin.pycon.jpログイン方法 <https://docs.google.com/document/d/1a982l0dYJVP731Mn7Dl8hBNrm83IicJ3Q7lXBF33a4k/edit>`_

    * 理事はログインできることを確認してください
    * Terada / terapyonでログインできた。
  * 12月以降の作業を有償で満足さんに依頼するか、一社)PyCon JP Associationに相談

11月の作業内容
~~~~~~~~~~~~~~
* pycon.jpサイトのサーバシャットダウン

  * VPSの停止
  * done(11/1)
* ドキュメント

  * botの運用手順書
* Bugfix

  * https://pyconjp.atlassian.net/browse/ISSHA-2223
* AWSの金額Bot

  * 着手予定(rmanzoku)
* バックアップの手順を作成

  * botのDB (sqlite)

    * 日次でs3に上げる？ 
  * google等のパスワードのクレデンシャル情報

    * ansible vaultで暗号化してgithub保存
* vaultのパスワード更新(rmanzoku)

12月?
~~~~~
* 問題無ければさくらVPS解約?

  * ストレージ費用だけかかっている？
* 今回移行したawsの内容をドキュメント、レクチャー欲しい

  * ここまで実施してもらう(terada, takanory
  * レクチャー会を設定して今後の方針もそこで(TODO yoshida)

    * Takanoy,shimizukawa,yoshida,rmanzoku(MUST)
* vaultのパスワード:理事に共有する(yoshida)
* ドキュメント

  * バックアップリストア手順書
  * 再構築手順書
* 12月以降の作業を満足さんに依頼するか、一社)PyCon JP Associationに相談

  * githubやgoogleアカウントの管理などもあり

2020年の活動(takanory、低、議論)
--------------------------------
* Pythonを広めるためになにができるんだろう(takanory

  * Python Charity Talks的なことをまたやる(terada
  * オンラインチュートリアル(terada
  * LT大会(shimizukawa

    * 準備が大変じゃないものがいい(shimizukawa
  * PyCon JP知らない人につながりたい(takanory

    * 勉強したい人にリーチする感じ(terada
    * チャンネルが大事なのでは(shimizukawa
    * start python clubとかはその層にリーチできている感じがする(takanory
* 2021年に向けてどういう活動ができそうか(terada

  * PyCon JPじゃなくてもいいけど、毎月pythonのニュースを流すとか?(terada

    * Ref: Chrome/Web Frontの動向 https://mozaic.fm
  * 面白そうだが、結構コストはかかりそう(takanory
* やるとしてもスモールスタートではじめる感じかなー(shimizukawa

サービス・リソースの管理(yoshida、低、なし)
-------------------------------------------
* 

次回
====
* 作業日

  * 2020年12月18日(金)
  * https://pyconjp-staff.connpass.com/event/197217/
* 運営会議#43:

  * 2021年1月8日(金) 
  * https://pyconjp-staff.connpass.com/event/197218/
  * PyCon JP 2021の相談
  * 理事交代
  * 2021年度仮予算
  * 2021年の施策
* 運営会議#44 + 社員総会

  * 2021年2月24(水)
  * https://pyconjp-staff.connpass.com/event/197219/

TODO
====
* `ISSHA-2226 <https://pyconjp.atlassian.net/browse/ISSHA-2226>`_ PiOに予約しないことを連絡する(yoshida)
* `ISSHA-2228 <https://pyconjp.atlassian.net/browse/ISSHA-2228>`_ Python Boot Campその後をまとめたページを作成する(ryu22e)
* `ISSHA-2224 <https://pyconjp.atlassian.net/browse/ISSHA-2224>`_ PyCon APACの開催地の投票を行う(terada)
* `ISSHA-2210 <https://pyconjp.atlassian.net/browse/ISSHA-2210>`_ Twitter凍結解除ができないか問い合わせる(terada)
* `ISSHA-2227 <https://pyconjp.atlassian.net/browse/ISSHA-2227>`_ Zoomアカウントについて問い合わせ、適切なライセンスに変更する(takanory)
* `ISSHA-2231 <https://pyconjp.atlassian.net/browse/ISSHA-2231>`_ 移行したpycon.jpについてのレクチャー会を行う(yoshida)

