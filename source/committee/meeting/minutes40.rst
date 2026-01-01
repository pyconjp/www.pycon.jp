==============================================================
 2020年7月3日(金) 一般社団法人PyCon JP Association運営会議#40
==============================================================

* 日時: 2020年7月3日(金) 19:30-21:30

  * https://pyconjp-staff.connpass.com/event/175764/
* 場所: Zoom
* 理事: terada, takanory, yoshida, jonas, shimizukawa
* オブザーバー:  peacock, Akira Inamori, ryu22e, yoshi-tsukamo, maaya, kanan, nishi, kobatomo, takasaki


課題のレビュー
==============
* `一般社団法人PyCon JPの課題 <https://pyconjp.atlassian.net/issues/?filter=11500&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20%3D%20%E4%B8%80%E8%88%AC%E7%A4%BE%E5%9B%A3%E6%B3%95%E4%BA%BA%20ORDER%20BY%20due%20ASC%2C%20updated%20ASC%2C%20component%20ASC>`_

PyCon JP
========

PyCon JP 2020 (nishi, 中, 報告/相談)
------------------------------------
* 報告

  * 申し込み出足が遅かったものの、スポンサー売上が目標値を越え、黒字着地できる見込み。
  * トーク採択95%完了　速報Blog公開済み

    * 1件、審議中のもの有り
  * 配信構成・チケット価格

    * Zoom(質疑応答可) 一般500円/day予定, パトロン3万円/2日

      * 有料にする理由は、冷やかし登録で本当に利用した人に権利が行き渡らないことを防ぐため
      * 質問: 1日だけ参加の人に、適切にZoomのURLをどう渡すのか?(takanory)

        * connpassは1つ。紳士的にやってもらう予定(yoshida
        * 分けなくていいんじゃないと思うが?(takanory, terada

          * nikkeeの強い希望
        * Zoomの上限が1,000名で考えているので、片方の日のキーノートが入れないとかを懸念して、分ける(yoshida
    * Youtube live 無料(connpass無し)

      * 機械フィルタされたtwitterコメントが画面に流れる予定
  * イベント構成

    * カンファレンス配信トラック: 5トラック + 本部配信 + 各スポンサーブース予定
    * チュートリアル: 8/30(日)
    * 検討中

      * Online Sprint 8/26-30
      * コミュニティブース(難しいかも)

        *  miroのような共有ボード空間を用意することを検討中
  * webサイト更新(少し遅れ気味)

    * 7月後半くらいに公開目標(nishi
  * PyCharityTalksのクロージング(17:30-18:00で待機)で3分程度告知(スライド追加済み)

    * 日時
    * キーノート紹介
    * 面白いから！来てね！
  * データ取り扱い不具合

    * proposalレビュー用にまとめたexcelファイルをGitHubにpushしてしまった
    * Forkされたら残ってしまう

      * Forkはなかったが、Cloneされたかはわからない
      * Private repositoryにする
      * 該当者30人を特定して、連絡する
      * 対策用のSlack channelを作る
      * https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository
  * 質疑応答

    * 無理をしなくていいと思う。オンラインならではのところに集中した方がいいのでは(terada

      * どうしてもやりたいスタッフがいるのでそこで進めてもらっている(nishi
      * 逆算してスケジュール考えないとやりきれないと思う(takanory

        * 諦めるラインも見えていないと厳しい。(takanory
      * オンラインなのでできるだけスコープを小さくした方がよい(jonas
* 相談

  * パネルディスカッション(スポンサーPR用企画)

    * Slackで相談している件(モデレーター等)

      * https://pyconjp.slack.com/archives/C024JGVAU/p1593431391452200
    * @yoshida, @hanaiが中心に取りまとめる予定
  * 行動規範

    * PyCon JPのCoCを掲示することに加えて、オンライン開催に向けて2020用の行動規範も追加掲示する用意する予定。

      * 内容: https://docs.google.com/document/d/15IoSF5OeCsSW-an_o-DwvMoxUHv7trSYYXO3rzXOOEE/edit
    * 既存のPyCon JP のCoCに手を加えないという確認をしましたが、以下の一文に注釈を加える予定

      * もしあなたがハラスメントに遭った場合、他の人がハラスメントに遭っている場合、あるいは他に気になることがあった時は、すぐに会議スタッフの誰かに連絡していただくようお願いします。会議スタッフは会議のブランドを付けたTシャツを着ています。
        * 2020はTシャツを来たスタッフがいないため、スタッフへのコンタクト方法を追記予定
    * 質疑応答

      * CoC自体をオンラインに向けて更新する効果があるの?補足情報なのでは(takanory
      * 連絡先についても行動規範の外の情報として、連絡先をオープニングで言うとかでよいと思う(takanory

        * ガイドラインとするのがたしかによいと思う(nishi
      * 厳しめに書いているが、なにか恐れがあるのか?(terada

        * 心配している(nishi
        * 現地でやっているときに「写真を撮らないでください」って言っているように感じる。個人のBlogに載せる写真が撮れない(shimizukawa
* 相談(terada)

  * `ISSHA-2133 <https://pyconjp.atlassian.net/browse/ISSHA-2133>`_
  * PyCon JP 2020 (オンライン)中に一般社団法人PyCon JP Associationとして何を行うか？
  * 案

    * 公開型運営ミーティング
    * クロージングでの活動報告
    * イベント開催相談窓口(ブースイメージ) ←優先度低
  * 意見

    * 内容的にはOK(yoshida
    * pycharityの報告はクロージングだよねー(shimizukawa
    * 上2つだけでいいと思う(takanory、jonas
    * 公開型運営ミーティングをどこでやるか?(jonas

      * Zoomかなとは思うけど...(takanory
      * タイムテーブルで空いているところに入れてほしい(takanory, terada
    * 2つで「公開型運営ミーティング」「クロージングでの活動報告」決まり

PyCon JP 2021(terada、中、議論)
-------------------------------
* TFT(有明) 2021年11月に借りる予定で進めてきたが、定員の50％で使って欲しいということで言われた。
* キャンセル料が発生する契約となることだったので、リスクが大きいので、キャンセルした
* いずれも、JTBが窓口になっている
* 別の場所が確保できないかをJTBが調査してもらっている
* いつどうやって進めるか?(terada)

  * 小さい規模で会場を押さえに行く?(terada

    * この方向性を個人的には模索したい(takanory
  * 地方会場?(terada

    * これは厳しいのでは。東京から地方に行けないリスク(shimizukawa, takaory
  * オンライン?(terada

    * オンラインやりたくないけどオンラインがリスクが低い(jonas
  * PyCon JP 2020後(9月中旬)に議論をはじめるがよいのでは(takanory

    * +1(yoshida
    * 今年のカンファレンス見てから考えましょう(jonas
  * 2020のスタッフ的には「オンライン」がやむなし。という意見が多かった(nishi

PyCon JP 2021以降の座長の募集時期(terada、 中、相談)
----------------------------------------------------
* 今後の方向性が決まっていないので、しばらく保留したい。(変更なし)
* 場所決めを始める前に座長の募集を開始してほしい(yoshida
* どういう風に募集をかけるかってのが難しい(takanory
* 募集自体は早くした方がいいと思う。会場決めに来期の座長が入っていた方がいいと思う(nishi

  * 公募だが実際には関係者しか申し込めないので、どうなるかわからない状態で募集をかけてよいのではないか(nishi
* 2019のときに、早くに募集してnishiさん立候補したと思う?(terada

  * 現役スタッフはイベントが終わるまでには考えられないが、イベント終了後でもあまり変わらないのではないか(nishi
  * 早くに募集してもあまり変わらないのではないか?締め切りがあることが一つのきっかけになると思う(nishi
  * どっちにしても応募がないのであれば、早く募集しちゃっていいのではないか(shimizukawa
* 早くに募集しても効果がないのではないか?(terada
* 2021について方向性も全く決まっていないので座長募集を保留したい(terada

  * 上記の方針だと8月には募集は行わないことになる(terada
  * 作業コストがそこまでかかるわけじゃないので「8月1日~20日まで」みたいに一度募集してもよいのでは(takanory

    * +1(yoshida, shimizukawa
  * **TODO**: 募集の段取りを進める(terada

PyCamp、PyLadies関連
====================

Pycamp状況報告(ryu22e、低、報告)
--------------------------------
* 2020年 PyCamp 開催

  * 7月以降の開催場所状況

    * 今のところ開催が決定している地域はない。
    * 埼玉県行田市は開催予定はあるが、時期は未定。
    * 佐賀の江口さんが現地スタッフとして立候補した（現地スタッフ受け入れ手続きは完了）
* 2020年 PyCamp開催以外の取り組み

  * 過去回から生まれたPythonコミュニティの主催者にインタビュー（担当: ryu22e）

    * JIRAチケット: https://pyconjp.atlassian.net/browse/ISSHA-2103
    * あまり時間が取れなくてまだ記事を公開できていません…（ryu22e）

      * 以下のコミュニティには回答してもらったので、順次記事にして公開予定。（ryu22e）
      * 飛騨高山Pythonの会/山腰
      * 岡山Python勉強会/山手
      * すごい広島 with Python/西本
      * Shonan.py/大貫
      * Shingen.py/高木
      * 先に上の5コミュニティの記事を公開してから他に声かけでもいいのでは(takanory
  * オンラインでのPyCamp説明会開催（担当: kobatomo）

    * IRAチケット: https://pyconjp.atlassian.net/browse/ISSHA-2060
    * 6/24(水) に第1回目を開催しました。(https://pyconjp.connpass.com/event/177517/)

      * 参加者計：8名。
      * 佐賀県より現地スタッフの応募があったことが成果。

        * つながり作っておくことが大事。

      * ブログを書いて完了する。(7/9までに完了予定)
      * 次回は9月を予定。
    * 素晴らしい試みだと思います(terada
* 10月以降くらいから動き出せるかなぁ(kobatomo

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、低、報告)
------------------------------------------------------------
* 会場都合などでオンライン開催に変更が相次いでいる
* `PyCamp Caravan 2020年度計画案 <https://docs.google.com/document/d/1ksRsxgh2tkqBlSFkmV7B8Mdu4Hxdqhk9B4kovX3I1ik/edit#heading=h.llb8ldfd7mio>`_
* 最近の出展

  * 名古屋(5/30) →オンライン名古屋として開催

    * ブース出展とLTを実施(yoshi-tsukamo)

      * Zoomによるオンラインブースは思った以上に人が来ない
      * 北海道に出展予定の人が偵察に来ていた
  * 北海道(6/27) → オンライン開催

    * 新ネタ🍣: セミナー「Python開発環境の整え方」(takanory)
    * ミーティング

      * ブース展示の代わりに時間を決めて実施
      * セミナーの質疑応答など
      * LT予定が時間の関係で実施できず次回以降に
* 2回やってみてどうか?(terada

  * ブースは難しい(yoshi-tsukamoto
  * Python boot campの新しい地域の候補を探しているが、どうか?(terada
  * セミナーをやってみてどうか?(terada

    * とくに、普通という感じ(takanory
  * 実施についての準備、発表などのコストがそこまでかかっていないので、継続でよいのではないか(takanory
  * OSCを盛り上げるためのコンテンツ出しとして協力していく感じ(terada
* 現時点での2020年出展予定

  * 京都(8/28〜29)→**PyCon JP 2020と同じ日程**

    * セミナーだけなら出れなくもないかも(頑張らなくてもいいけど)(takanory
    * connpassで重複登録しようって話をしている(yoshida
  * 島根(時期未定)
  * 福岡(9〜11月)
  * 広島(9〜11月)
  * 関西オープンフォーラム(時期未定: 秋頃)

    * 今年はパスでいいかなぁ(takanory

PyLadies関係報告(maaya, 低, 報告)
---------------------------------
* 秋ごろを狙ってPyLadies Caravan 秋田の話をそろそろ進めてみるつもり
* PyLadies JapanのTシャツが在庫余ってるので、ネットで販売するスキームを作る予定
* PyLadies Japan各リージョンのモチベーションが下がって来てるのどうしようかな

  * 時間を確保するのが難しくなっている人が多い(maaya
* Tokyoだけでもいっぱいいっぱいの状況(maaya

  * 落ち着いたら地方も手伝いたい(maaya

コミュニティー支援
==================

イベント/コミュニティサポートプログラム(takanory、低、なし)
-----------------------------------------------------------
* 報告なし

Python地域交流オンライン座談会(takanory、低、なし)
--------------------------------------------------
* そろそろやろうかな

地域PyCon等の支援について(takanory、中、報告)
---------------------------------------------
* PyCon Kyushu

  * 6月24日 実行委員会 https://pycon-kyushu.connpass.com/event/180288/
  * 議事録によるといったん中止らしい
  * https://docs.google.com/document/d/1STXbRtMGSU5x4ywNR4W3pZydqjKbMqLzLtC9J1mwacc/edit#heading=h.1mj748f6cv9k
* PyCon mini Hiroshima

  * 10月10日開催に向けて進んでいるもよう
  * 7月3日 運営ミーティング https://pycon-hiroshima.connpass.com/event/181398/
* SciPy Japan

  * https://www.scipyjapan.scipy.org/
  * トーク、レビュアー募集などBlogでの宣伝協力する予定

海外コミュニティ連携
====================

PSFへの寄付イベント(terada、中、報告)
-------------------------------------
* https://pyconjp.connpass.com/event/177586/
* 明日(7月4日)にオンラインで開催する
* 予定の130万円以上の寄付ができる見込み
* 手数料や振込金額は、PyCon JP Associationの出費となる

  * 詳細は、別途報告する

APAC関連(terada、低、報告)
--------------------------
* 元PyCon JP 理事のイクバルさんがPSFの理事に立候補しました

  * しかし残念ながら落選になりました

APACブース in US PyCon(terada、中、相談)
----------------------------------------
* ロゴ作成費が未精算

  * ロゴデザインコンペ　3万円　(決定済み)
  * ロゴなどのデザイン決定版作成　・・5万円　(今回の提案・**決済したい**)

    * ロゴのブラッシュアップ、ロゴマニュアル作成
  * OK(takanory, yoshida
  * **TODO**: kinofumiさんから請求書をもらって、処理する(terada
  * **TODO**: ロゴデザインの3万円は「APACに寄付してほしい」とのこと。すすめる(terada
* 完成版のロゴなどをとりままとめて、Driveに置く(寺田のタスク)

その他
======

運営メンバー制度(takanory、低、報告)
------------------------------------
* Python Charity Talks in Japan終わったら本気出す

各地のイベント中止に対して(terada、低、なし)
--------------------------------------------
* TODO: やっていない

  * ブログで「メールとかSlackで相談してね」とアピールする(takanory)
  * USのサポートイベントのこともからめてもいいかも(yoshida)

弁護士との契約について(yoshida、低、なし)
-----------------------------------------
* Yoshidaに任せている
* 状況把握していない(terada)
* イベント側や一社のPyCon JP 2020のスタッフで打ち合わせを行う予定(yoshida

Read the Docsの有料メッセージ(Jonas、低、相談)
----------------------------------------------
* RTDから：

  I think the best thing to do here is to simply just opt your projects into skipping advertising. We understand that conferences are in a particularly difficult place right now and while we appreciate any support, we'd rather we don't take away any budget from more important community expenses. \
  If you'd still like to make a one-time donation, that is still possible using our general donation form:
  https://readthedocs.org/sustainability/
  I've gone ahead and marked those projects to skip advertising. If something still doesn't look right, or there were more projects you were hoping to alter, let me know!
* 一社のプロジェクトは広告なしになりました。
* 寄付は今回はしなくてよいのでは(jonas

  * pycharityで頑張ったし、今回はいいのでは(takanory

法人名変更(terada、 中、報告)
-----------------------------
* 銀行口座の名称変更が終わっていない。
* 来週から進める。(terada)
* 銀行口座の名称が変わると、振り込み時に影響があるのではないか?(yoshida

  * 口座番号が同じで名前も近いので大丈夫だとは思うが...(terada
  * スポンサーへの請求書はすでに出してある。7月末から振り込みがくる(yoshida
  * **TODO**: 9末を超えてから銀行の名称変更をする(teraeda

pycon.jp OSサーバー移行(yoshida、中、報告)
------------------------------------------
* manzokuに作業を進めてもらっている(yoshida
* 静的コンテンツは大体めどが付いた。DNSの移行をこれから行う(yoshida
* これからアプリ(bot等)の移行がはじまる(yoshida

  * 了解(takanory

2020年の活動(takanory、中、議論)
--------------------------------
* Python Charity Talks in Japanはイベントとしてできてよかった(takanory

  * オンライン半日集金イベントとして、半年に一回くらいできるのでは?(terada
  * チームを作らないと無理そう(takanory

    * 運営メンバーとして誰か専任で入ってくれるとよさそう(takanory
  * 定期的に運営費を集めたり、スポンサーとの窓口と継続的につながったり、参加者ともつながったりとかがあるとよいと思う(terada
* リモートイベントの運営ノウハウ的なのを共有したい気もする(takanory

  * オンラインイベントとしてやりたい(takanory
  * **TODO**: 8月頭くらい目標で実施するかー(takanory
* 小さいものでいいからオフラインの活動ができないかとも思っている(takanory
* オンラインのpython boot campはないよね?(terada

  * ない。やるとしたら別のコンテンツだと思う(takanory

サービス・リソースの管理(yoshida、低、なし)
-------------------------------------------
* 順次やりたいが手が回っていない。
* yoshidaさんに任せたい。

次回
====
* 8月28日(金) 昼に公開型ミーティング
* 9月9日(水) 作業日
* 9月25日(金) 運営会議#41 https://pyconjp-staff.connpass.com/event/181858/
