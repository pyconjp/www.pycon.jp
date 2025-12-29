================================================================
 2021年12月16日(木) 一般社団法人PyCon JP Association運営会議#49
================================================================

* 日時: 2021年12月16日(木) 19:30-21:30

  * https://pyconjp-staff.connpass.com/event/227273/
* 場所: Zoom
* 理事: terada, takanory, jonas, yoshida, shimizukawa
* オブザーバー: maaya, peacock, ryu22e, nikkie, yoshi-tsukamo


課題のレビュー
==============
- `PyCon JP Association(一社のみ) <https://pyconjp.atlassian.net/issues/?filter=11500>`__ の課題一覧
- `PyCon JP Association(一社以外) <https://pyconjp.atlassian.net/issues/?filter=15948>`__ の課題一覧

PyCon JP
========

PyCon JP 2021(nikkie、高、報告)
-------------------------------
* 優先度比較的高そうなのは会計
* 会期後作業進捗(低)

  * 会期前は毎週mtgしていましたが、会期後はmtgはなく、ほそぼそとやっています
  * 会計：いくつか残っているようなので、このmtgの裏で確認します

    * スポンサー入金は先日完了
    * 使途不明金にならなければよい(terada
    * 例えば、今回食事出さないので、精算のために現金立替て予定 (yoshida

      * この作業が遅れてしまったのであきらめることも検討
    * 11月までのスタッフ清算(建て替え)を作業中(吉田)
    * インド宛の関税清算が１月請求見込み
    * 2月にイベント報告予定
  * カンファレンスレポート：スタッフで書き上げ、次は技評さんに送付です
  * FlickrアップロードDONE(peacock

    * https://www.flickr.com/photos/pyconjp/albums
  * YouTubeへトーク動画アーカイブ公開DONE(peacock

    * 個人的な質問ですが、LTの動画は公開されないんですか?(takanory

      * https://discord.com/channels/876812133571129344/898469795576573992/908676010667548692 で案内した同意フォームに期日までに回答があったスピーカーのみ切り出して公開しました
      * 回答があったのは1本 https://www.youtube.com/watch?v=_LuLs8H1gJc
      * スタッフからLTスピーカーにメンションしていないので、ミスコミュニケーションになってしまったと見ています (nikkie

        * まったく気づいてませんでした。11月12日にメンションなしのメッセージなので、ほとんどの人は気づいていないだけだと思います(takanory
    * 同意をとりたい理由はなにか?(terada

      * Youtubeの場合は同意が必須という認識(shimizukawa
    * 動画を切るのは大変なので、1本でまとめて出せばよいのでは(terada

      * 動画を分割しなくてよいと思う(takanory
    * 全部を公開するか一部を公開するかで進めればよいのでは(terada
    * **TODO:** 対象者全員にメンション飛ばして、全員からYESと回答があれば全部つなげて公開。1人でも未回答だったら公開しない(nikkie
* 他に残件はなにがありますか?(takanory

  * https://github.com/pyconjp/tasks-2021-planning/issues
  * discordのアーカイブ処理
  * 業者にお礼
  * ナレッジベース整備
  * Website静的化・インフラリソース削除

PyCon JP 2022座長募集(terada、高、相談)
---------------------------------------
* 立候補者はいるが決めていない
* ヒアリングなどを行って、次のステップへ行きたい
* https://pyconjp.atlassian.net/browse/ISSHA-2404

PyCamp、PyLadies関連
====================

PyCamp状況報告(ryu22e、低、報告)
--------------------------------
* 運営メンバー: ryu22e、kobatomo
* 2021年12月4日(土) PyCamp山口 開催済み。リブートDone.（山口初開催）

  * 参加者：6名、TA：3名、現地スタッフ：1名、講師：1名
  * https://pyconjp.connpass.com/event/205993/
* 次の地域は未定。
* 過去開催した地域の現地スタッフの方に声がけして2回目開催を進める予定。

  * PyCamp活動していることを広めていく。
* 現地スタッフ応募者増えています。

  * 広島（2回目、溝下さん）、新潟（3回目、藤原さん）
  * 積極的にやっていく?(terada

    * そのつもり(ryu22e
  * 2月とかがあるのなら仮予算が必要となる(terada

    * 1回分の仮予算を申請しておくとよいのでは(terada
    * 可能性はある(ryu22e
* 久しぶりのpycampどうでしたか?(terada

  * 段取りは大丈夫だった(shimizukawa
  * コロナ対策で準備が大変そうだった。消毒、名簿等の作業コストがかかる(shimizukawa
  * コロナ禍での開催にこぎつけるまで、山口県のステージなど新型コロナの状況情報を毎月監視するのが大変。現地スタッフがウォッチしてくれてよかった(shimizukawa
  * 現地では特に問題なく進められた(shimzukawa
* 今後の開催の難易度とかはどうか?(terada

  * 現地スタッフが立候補してくれれば問題なく進められそう(ryu22e
  * 今回は現地スタッフが東京在住で、広報などが少し難しかった(shimizukawa

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)
------------------------------------------------------------
* 運営メンバー: yoshi-tsukamo
* OSCは今年度オンラインで毎月開催の予定

  * 10月22日(金)〜23日(土) Fall(東京)

    * 23(土)10:00〜
    * セミナー: ryu22e, yoshi-tsukamo
  * 11月20日(土) 福岡

    * 15:00〜
    * セミナー: nikkie, murakami
  * 1月29日(土) 大阪

    * murakami, yoshi-tsukamo
    * 時間未定
  * 3月11日(金)〜12日(土) Spring(東京)

    * murakamiさんが立候補
* セミナーとは別のミーティング枠を使ってpycamp相談会をやってみても良いかも？ というアイデアを思いつきました

  * ちゃんとアナウンスができれば効果はありそう(terada
  * OSCに既存で来ている人だと常連に固まっているので、PyCon JP Association側でも宣伝をする必要がある(yoshida
  * 宣伝をちゃんとやると効果がでそうではないか(terada
  * やってみましょう。いいと思います(takanory、shimizukawa
  * PyCon JP 2021でやってみたが、Twitter/Facebook広告とか打ってみてもいいかもね(yoshida
* 発表の記録を更新してもらってありがとうございます(takanory

  * https://github.com/pyconjp/slides/
* OSCの契約は4月~3月なので仮予算としての検討は不要。来年度どうするか検討したい。振り返りをしたい(terada

  * 2月末に予算の会議があるので、そこで決められるとわかりやすい(terada
  * 可能なら2月中に話したいなー(takanory
  * **TODO**: 日程調整から考える(yoshi-tsukamo

PyLadies関係報告(maaya, 低, なし)
---------------------------------
* そろそろ復活させたい気持ちがあるので運営チーム相談を再開します

  * わいわい(takanory
* PyLadiesに参加している人で兵庫の人がいる。兵庫でCaravanをやってほしいなと言われている。兵庫から再開しようかな(maaya
* PyCon JP Associationの会計年度は12月末まで、2022年1、2月の仮予算を立てる予定。予算が必要であれば先に知りたい(terada

  * 1月はない。2月はありえるが3月開催でもありえる(maaya
  * やっても2月までで1回開催できるかどうかという感じか?(terada
  * その認識であっている(maaya
* US PyCon 2022にポスター出さないの?(terada

  * 出したいが余力がない。PyLadiesチームに相談する(maaya

PyCon JP TV(takanory、低、報告)
-------------------------------
* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* https://www.youtube.com/user/PyConJP
* Web https://tv.pycon.jp/
* 月一で継続配信している。ネタ絶賛募集中
* 年内? あまり調子が良くなかった機材の代わりを購入申請予定(peacock

  * モバイルディスプレイ(20k - 25kくらい
  * HDMIスプリッター ( - 5kくらい?
  * 予算のあまりがあるので買えるなら年内に買っちゃいたい(takanory
* (3月以降)来年度予算をどれくらい申請するか悩み中(peacock

  * オーディオミキサー(30k)、マイク(10k * 2)?
* 仮予算では懇親会だけを申請すればよさそう(takanory, terada

コミュニティー支援
==================

地域PyCon等の支援について(takanory、中、報告)
---------------------------------------------
* PyCon mini Shizuoka

  * https://shizuoka.pycon.jp/
  * 2021年11月20日(土)
  * 開催済み
* PyCon Kyushu

  * https://kyushu.pycon.jp/2022/
  * 2022年01月22日(土)
  * ブログ等
  * connpassの集客はどう?(shimizukawa

    * 一般がまだまだって感じ(takanory
    * 近場の人たちにどうアピールするか?(takanory

海外コミュニティ連携
====================

Python商標問題(terada、低、なし)
--------------------------------
* 特に無し

Python Charity Talks in Japan 2021.09(kobatomo、中、報告)
---------------------------------------------------------
* 寺田）450,000円送金した

  * https://pyconjp.blogspot.com/2021/11/pycharity-donations-have-been-sent.html.html
* 清水川）会計をまとめた
* 次回の予定は未定(terada

APAC関連(terada、中、報告)
--------------------------
* https://th.pycon.org/ PyCon APAC 2021が終わった
* オンラインで開催された
* 2022は台湾で開催予定

APAC・JPロゴ関係(terada、低、なし)
----------------------------------
* 特に無し

会計(清水川、中
===============
* 年度末（12月末）なので、決算に向けてまとめ進めます

  * `ISSHA-2452 <https://pyconjp.atlassian.net/browse/ISSHA-2452>`_ 2021支払調書作成
  * `ISSHA-2453 <https://pyconjp.atlassian.net/browse/ISSHA-2453>`_ 2021決算
* 12月

  * 清水川）マイナンバー確認
  * 会計事務所）支払い調書の送付
* 1月早々

  * 会計事務所）会計、科目整理
* 2月頭

  * 決算書作成
* 2月下旬

  * 総会での決算承認
  * 決算書公開

予算2022(terada、高、議論)
==========================
* `2020予算参考 <https://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=0>`_, `2021予算 <https://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=1331278426>`_
* 2022年1月2月の仮予算
* 必要経費は仮予算を組む必要がある

:羽藤会計事務所へ: 310,000円
:塩野行政書士へ: 50,000円
:システム利用料: 50,000円 (AWS, Zoom等)
:Python Boot Camp: 100,000円
:PyLadies Caravan: 100,000円
:PyCon JP TV 懇親会費(2回分): 20,000円
:予備費: 70,000円
:合計: 700,000円

* 仮予算は上記で決定(terada

その他
======

Zoomライセンス見直し(takanory、低、報告)
----------------------------------------
* そろそろ本気出す(takanory

次回
====
* 運営会議#50

  * 2022年1月26日(水) 19:30-
  * https://pyconjp-staff.connpass.com/event/234334/
