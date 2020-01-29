================================================
 2020年1月28日 一般社団法人PyCon JP 運営会議#34
================================================
:日時: 2019年12月04日(水) 19:30-21:30

  * https://pyconjp-staff.connpass.com/event/158539/
:場所: CMSコミュニケーションズ(御徒町)
:参加者:

  * 理事: 寺田、ヨナス、たかのり、吉田、清水川
  * オブザーバー(12): peacock, ryu22e, wahho, yoshi-tsukamo, kanan, nishi, 福田, maaya, うえき, ainamori, nishi, kobatomo

.. contents:: アジェンダ
   :local:

課題のレビュー
==============
*   `一般社団法人PyCon JPの課題] 課題ナビゲーター <https://pyconjp.atlassian.net/issues/?filter=11500&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20%3D%20%E4%B8%80%E8%88%AC%E7%A4%BE%E5%9B%A3%E6%B3%95%E4%BA%BA%20ORDER%20BY%20due%20ASC%2C%20updated%20ASC%2C%20component%20ASC>`_

PyCon JP
========

PyCon JP 2019の開催報告と残件など共有(yoshida)
----------------------------------------------
* 残タスク

  * 海外からのスポンサー入金待ちが1件ある、まもなく入金された。
  * PayPalに2件の未払い請求が残っている。要確認　＜＜消したはず、再確認(yoshida)
  * 会計とりまとめて会計事務所に行く(年明けの予定)　予算関係にに記載済み(下記参照)
* PyCon JP 公式Blogで写真のリンク切れがある。(対応できればする)(yoshida)

  * https://pyconjp.blogspot.com/2019/10/pycon-jp-2019-10-kpt.html
  * JIRA作るなら一社のタスクにしてほしいかな(takanory)

PyCon JP 2020 (nishi)
---------------------
* 日程: 2020年8月27日(木)-29日(土) ※ 30(日)のSprint開催を検討中

  * 参考資料: https://drive.google.com/drive/folders/1j13gGPygkEg5bxRml7R4aW6_BrQrZFur
* 場所: 大田区産業プラザPiO
* 直近の進捗・完了事項

  * アイディア出し
  * チーム立ち上げ・始動開始(デザインチーム以外)
* 直近の予定

  * デザインチーム立ち上げ
  * スポンサーパッケージの確定(1月末に大枠確定、2末までにFix)

    * 3月頭に発表予定
  * Website立ち上げ: 2月前半に基本情報のみ公開予定
  * CfP準備: 2月くらいに出したい
  * キーノートの打診: 2月には確定させたい
* 困っていること・懸念点

  * デザインチームが手薄→ディレクションする人がいない

    * Blogで広く募集するのはどう?(takanory)

      * デザインディレクションに絞って募集してみる
  * 経験者スタッフの参加がまだ少ない→サポートみたいなのでも参加してほしい

    * nishiさんが一緒にやってほしい人に声をかけた方がいいと思う(takanory)
* 質問・その他コメント等

  * サービス管理・メアド管理シートは2020スタッフ全員が見れてもOKでしょうか。

    * Driveやファイルの権限整理の話が出ていたので確認しました。

      * いまいない人がずっと残っていることが不安ということと、定期的に整理するということが必要と思っている(terada)
    * 2020活動で使うものだけ抜き出したファイルを作ったほうがいい？

      * 2重管理になって大変だと思う(shimizukawa)
    * 性善説で、共有でいいんじゃないかなー(takanory)
  * Zoom導入で、お試し参加がリモートからもできるようになって便利。ホストキーが設定できるのも便利になりました。

PyCon JP 2021
-------------
* TODO: 2月が始まったら2021年の方向性について議論を進めたい(terada)

  * 2月からでいいのでnishiの意見を聞きたい(takanory)
* 早めに場所探しをはじめたい(yoshida)

  * yoshidaとNOCのたけださん(=わっほー)が動きたいという話をしている(yoshida)
  * 先送りし2月から議論を開始する(terada)

    * 次年度の理事が決まってからすすめる(terada)
  * 調査を始めるとかであれば今から動いてもいいと思うけど(takanory)
  * `台東館 <https://www.sanbo.metro.tokyo.jp/taito/>`_ の予約説明会がはじまる。大田区の設備を作っているが、そろそろ情報を集め始めた方がいいのでは(yoshida)

    * 昨年のように調査したがPiOの予約となった。先にどういうイベントにするかの方針を先に決めた方がよいのではないか。地方開催などもある。(terada)
    * 急ぐのであれば方向性を決める会議を先にやったほうがいい(terada)
  * 調査というのが、設備をリストアップしてWebから情報集めるとかであれば、全然進めていていいのでは(takanory)

    * 近い規模で開催できそうな会場がどういうのがあるのかをリストアップして、いつ頃から予約できるかを集めようと思っている(yoshida)

      * であればよいのでは(takanory)
      * 使われなくなる可能性もあるので、そこは認識しておいてね(terada)

        * JIRA作ってスプレッドシート貼って埋めてく感じですかねー(takanory)
  * 2020年の4月には人数と予算が決まっていて施設のリストアップができているとうれしい(わっほー)

    * 4月は結構きびしい(terada)
    * これが本当に必要なら議論を先にする必要がある(terada)
    * PyCon JP 2020は2019年6月に確定した。NOCの下見として4月に必要なのかはまだピンときていない。6月には決まっている必要があると思っている。(yoshida)
    * 6月末決定だと予約のための下見に期間が厳しい。候補が多いと下見が困る。まったく新しい会場が多いと下見の期間がとれないため、2、3カ所くらいが妥当(わっほー)

予算関係
========
* PyCon JP 2019イベント会計の締め

  * rmanzokuから羽藤会計事務所に依頼中

    * https://pyconjp.atlassian.net/browse/WYI-390
  * 下記の対応がおそらく必要(2/2めど)

    * 2019年度の一社・PyCon JPイベントの会計で、チケットのない（わからない）資金移動、入出金について、分かる範囲で記載お願いします。

      * https://docs.google.com/spreadsheets/d/1nGudKUWSa9pigm8CVVue_Hn2pDCjan31/edit#gid=1336430564
* 2019年度の決算処理

  * 2月前半にまとめる予定(shimizukawa)
* 2020年度1月、2月で必要な仮予算の再確認 (terada)

  * 以下が決定済み

    * PyCamp Caravan 東京分(4万円)
    * Python Boot Camp 2回分(10万円)
    * PyLadies Caravan 1箇所分くらい(8万円）
    * PyLadies Okinawa託児 1回(3万円)
    * 弁護士への相談(10万円)
    * 合計35万円を決定とする。(terada)
  * US PyConへのAPACブース出展に伴う製作物(詳細下部) (terada)

    * 金額は、20万円くらい？？ (未定)

      * 最初にやるところがお金を出して、あとにつなげる価値もあると思う(terada)
      * Shimizukawa、ヨナス、yoshida賛成
      * 合計金額のうちわけはどんな感じ?(maaya)

        * テーブルクロス: 3万円
        * ステッカー: 1万円
        * バナー: 5万円
        * Tシャツ: 2万円
  * PyCon mini Shizuoka 2020へのスポンサー費: 30,000円

pycamp状況報告(ryu22e)
======================
* `Python Boot Camp開催一覧 <https://docs.google.com/spreadsheets/d/1VjM7x6k6Cyk0323ZoAHY2lXMV6VyLrn_Bi8mnOiPMb4/edit#gid=0>`_
* `Python Boot Camp予算管理 <https://docs.google.com/spreadsheets/d/1Fcgck7fMl6JpqeEVS7j542LE39ibRmCi3UxzfWhcLuc/edit#gid=1116847018.`_
* 2019年は10回(藤枝、和歌山、福井、山形市、岐阜、沖縄、高知、群馬、福岡2nd、熊本2nd)開催済した。
* PyCamp2019予算実績

  * 2020年1月23日時点 

    * 予算：510,000円
    * 実績：495,542円
  * 詳細は以下スプレッドシートを参照。

    * https://docs.google.com/spreadsheets/d/1Fcgck7fMl6JpqeEVS7j542LE39ibRmCi3UxzfWhcLuc/edit#gid=1116847018
* PyCamp2019のふりかえりを1/31に行い、今後の活動方針を決める。
* 2020年 PyCamp 開催

  * 2/8  長崎 (https://pyconjp.connpass.com/event/158803/)
  * 3/14 福島県郡山市 (https://pyconjp.connpass.com/event/159583/)
  * 4月以降の開催場所状況

    * 埼玉県行田市で現地スタッフ立候補あり。4月・5月予定
* 2020年度 PyCamp 予算申請

  * 関連チケット

    * https://pyconjp.atlassian.net/browse/ISSHA-1926
  * 525,000円

    * 内訳
    * PyCamp開催 10回予定	：500,000円 (50,000円 * 10地域 )
    * ポスターセッション		：    5,000円
    * ステッカー追加製作		：  10,000円
    * T-シャツ追加製作		：  10,000円
  * 参考

    * 2019年の1開催あたりの平均支出：¥47,005
  * 過去の予算はどうだったか?

    * 2018は予算60万円で実績40万円
    * 2019は予算40万円で足りなくて追加予算で50万円にした

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamo)
------------------------------------------------
* `PyCamp Caravan実施一覧 <https://docs.google.com/spreadsheets/d/1aLKox2os-_qRUx_zY8o9LsJONFae_o-Rr_DhYwLHn6k/edit#gid=0>`_
* `PyCamp Caravan費用管理 <https://docs.google.com/spreadsheets/d/1aLKox2os-_qRUx_zY8o9LsJONFae_o-Rr_DhYwLHn6k/edit#gid=1381341604>`_
* 2020年の活動計画

  * `PyCamp Caravan 2020年度計画案 <https://docs.google.com/document/d/1ksRsxgh2tkqBlSFkmV7B8Mdu4Hxdqhk9B4kovX3I1ik/edit#heading=h.llb8ldfd7mio>`_
  * 現時点での2020年出展予定

    * 2/21(金)〜22(土)のOSC Tokyo/Springへの出展決定

      * 会場: 駒澤大学
      * 21日(takanory・セミナー実施)、22日(terada)
      * PyCon JPの周知も目的なのでサポートしてくれる方歓迎です

        * PyCon JPとのコラボどうしようか?(takanory)
        * **TODO**: peacockとやりとりする(takanory)
    * 名古屋(5/16)
    * 北海道(6/27)
    * 京都(8/21〜22)
    * 島根(時期未定)
    * 福岡(9〜11月)
    * 広島(9〜11月)
    * 関西オープンフォーラム(時期未定)
  * 予算案

    * 800,000円

      * OSCスポンサー協賛金: 200,000円(前年と同じ場合)
      * KOF: 50,000円（一口につき）
      * 交通費・宿泊費は2019年と同じ条件と仮定
      * テーブルクロス刷新、チラシ増刷等の備品
* PyCamp島根に来ていた愛媛の人と2月に打合せ予定(terada)
* **TODO**: 今年のセミナーのネタを考える必要がある(yoshi-tsukamo)

  * 2月以降に検討(yoshi-tsukamo)
  * Pythonの環境ネタとか?venvとか。これからはじめる人向け(yoshida)

PyLadies関係報告(maaya)
=======================
* PyLadies Caravan進捗

  * 北海道　12/21（土）開催完了

    * 6人
    * Slackにも参加してくれている
    * コミュニティができあがったわけではないが、学生も多かったのでこれからだと思う。
  * 秋田　実施調整中

    * 手をあげてくれてた方が音信不通になったので先行き不明
  * 広島　3/14（土）開催確定

    * WiDSとのコラボ
    * 現地スタッフOK・会場調整中
* 今年度（2020年度) について

  * PyLadies Caravan

    * 継続して実施を希望（概算：5拠点、35万）
    * 未開催エリア（東北、北陸、中国）もしくは2nd要望地域での開催

      * 2ndは前回から発展していないエリアを中心に別プログラムでの開催を検討予定
  * PyLadies Okinawa 託児所

    * 継続して実施を希望（概算：6回、20万）
    * https://docs.google.com/document/d/15AQTwc_aErb7mjMHexotbNxFVtlcs1nS7yXuHHijvlg/edit?usp=sharing
  * その他PyLadies関連

    * PyLadies 日本リージョンのフォローの仕方検討
    * PyLadies本家と各チャプターとの連携が緩やかに開始

      * PyCon US posterがacceptされたので、現地で交流をする予定

pycon.jp OSサーバー移行(yoshida)
================================
* https://pyconjp.atlassian.net/browse/ISSHA-1894
* \*.pycon.jpのlet's encrypt20190612障害対応の記録 https://pyconjp.atlassian.net/browse/ISSHA-1669

  * 定期更新ができておらず3ヶ月毎(6月、9月)に障害となっている

    * 現在の証明書 https://pycon.jp/2018/

      * 2020/2/27まで
      * あと数日様子見
* 過去のPyCon JPサイトを静的化 https://pyconjp.atlassian.net/browse/ISSHA-1632
* イベントスタッフから個人的に発注する方向で進める(yoshida)
* 主担当: yoshida

  * `2020以降のpycon.jpサイト要件案 <https://docs.google.com/document/d/1ukaLI4GzCsRvdlpzHqz6n2nPkoavn-mnzYAo63VAntA/edit>`_
  * https://pyconjp.atlassian.net/browse/ISSHA-1894
  * 上記要件をもう少し詰めて見積を @rmanzokuに依頼したい
  * 1月中に見積をもらいたい、２月の一社MTGでの2020予算に計上

    * manzokuさんに月額で10H月10万程度3ヶ月or半年更新という予算案
    * １社のMTGで予算について検討
    * 移行のターゲットとしては竹または梅がよさそう、いきなり松は要件漏れがあるのでは。
    * 1/28の１社MTGで　Go/NoGO判断
    * 松、竹、梅等詳細については下記参照
    * https://docs.google.com/document/d/1ukaLI4GzCsRvdlpzHqz6n2nPkoavn-mnzYAo63VAntA/edit#
  * 金額

    * 金額の正当性をどう決めるかの議論が必要(terada)
    * 10万円/10Hで個人で仕事として受けるのは問題ない(takanory, terada, ヨナス)
    * 作業量が見えない(terada)

      * 竹案で作業がどれくらいあって、合計何時間とかのリストがほしい。実際に作業して増減する分にはしょうがない(takanory)
      * **TODO:** 作業を進める前提で幅のある予算案を作って申請してもらう(terada)
  * 技術

    * もう1人くらい入った方がいいのか?(terada)

      * AWSに詳しくないので構成についてはわかっていない(yoshida)
      * maaya, teradaは相談には乗れそう

ツールの活用・運用等
====================

ZOOMアカウント(takanory)
------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-1923
* 利用開始している。終了(takanory)

Google for Nonprofits(takanory)
-------------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-1911
* https://pyconjp.atlassian.net/browse/ISSHA-1912
* Google for Nonprofits, GSuite for Nonprofitsは取得済み。(takanory)
* PyCon JP、一社PyCon JPフォルダの共有フォルダを作成した(takanory)

  * https://drive.google.com/drive/u/2/folders/0AB4V-gRXzKWgUk9PVA
  * https://drive.google.com/drive/u/2/folders/0AKLhHa9lUV2NUk9PVA
  * TODO: ファイルをガッと移行する会をやりたい(takanory)
  * 2/3に作業(https://pyconjp-staff.connpass.com/event/164418/)
  * GSuite for Nonprofitsが権利としてあるので、使いたいサービスあったら使いましょう(takanory)
  * ファイルを移動するとリンク切れが発生すると思う(takanory)

    * 外部公開しているGoogle form 注意 (nishi)

Flickr
------
* Flickrのクレジットカードが切れている。(yoshida)

  * チケットをshimizukawaにまわした(yoshida)
  * https://pyconjp.atlassian.net/browse/ISSHA-2006

コミュニティー支援
==================

イベント/コミュニティサポートプログラム(intel)
----------------------------------------------
* 進捗・今後の予定

  * @intel 側で時期的な問題あって、一旦コミュニティ支援活動をnishiが引き継ぐ形に(忙しさが落ち着いたらまた引き継ぎ直します。
  * 予定としては3月末から4月にかけて復帰する予定です・・・
* [イベント支援] PyCon Kyushu 2020 Kumamotoの申込への対応 (intel)

  * https://pyconjp.atlassian.net/browse/ISSHA-1982
  * 上記件があって、対応できてない状態です。対応できていない件についてはintelからkiyotaさん宛に連絡します
  * takanoryが巻き取る(takanory)
* ピザ支援 (terada)

  * 受付フォームが機能していない
  * まかびにTwitterでDしたが返事がない、ただのしかばねのようだ(takanory)
  * **TODO**: フォームを作り直して貼り直すしかない(takanory)

    * Googleフォームの連絡先をグループとかにできないかなー。GSuiteになっていい感じにできないか(terada)

Python地域交流オンライン座談会(intel)
-------------------------------------
* https://pyconjp.connpass.com/event/155287/
* 2019年11月28日第1回を開催
* 概要

  * https://pyconjp.connpass.com/event/155287/
  * 地域Pythonコミュニティの繋がりや交流をもっと深めていくための座談会
* 雜感

  * **定期開催していきたいのでまた1月下旬に第2回を開催したい**
  * 上記事情あって、一旦はストップ(or どなたかに一旦準備を引き継いでいただけるのであれば第2回の開催をお願いしたいです)。
  * Blogは1/29に公開する(takanory)
  * **TODO**: コアスタッフを募集する(takanory)

地域PyCon等の支援について(takanory)
-----------------------------------
* PyCon mini Shizuoka 2020

  * https://shizuoka.pycon.jp/
  * 2020年2月29日(土)
  * Blogとドメインサポート
  * 30,000円の支援依頼がきた

    * https://pyconjp.atlassian.net/browse/ISSHA-1999
  * 金額と用途がOKか?(terada)

    * 理事全員賛成
  * 用途が変わったときに付け替えてOKか?(terada)

    * 用途と領収書を確認する or スポンサー費として渡すという2つの考えがある(terada)

      * スポンサー費でいいと思う: ヨナス、takanory、shimizukawa、yoshida、terada
    * 前者の場合は会計としては監査する必要がある(shimizukawa)
  * https://www.pycon.jp/support/community.html

    * **TODO**: ここに書いてある内容とは合っていないので、会計報告は不要なので行を削除するとかした方がよさそう(terada)
* PyCon Kyushu 2020 in Kumamoto

  * 2020年5月23日(土)
  * https://kyushu.pycon.jp/2020/
  * Blogとドメインサポート

APAC関連(terada)
----------------
* 2020はマレーシアに決定した

  * 場所: コタキナバル
  * 日付: 9月19日、20日
  * 詳細は未定。
  * ツアーやりたいが、PyCon JP 2020と近い時期になりそう(terada)
* イクバル氏(PyCon JP, PyCon MY立ち上げ)を中心に、以下が動いている

  * イクバル氏による徐々に進めている

APACブース in US PyCon
~~~~~~~~~~~~~~~~~~~~~~
* https://pyconjp.atlassian.net/browse/ISSHA-1890
* US PyCon (4月中旬・アメリカ ピッツバーグ) https://us.pycon.org/
* コミュニティブースとしてAPACブースを出すことが決定
* 1/18 イクバル、たかのり、寺田で認識あわせMTG実施

  * https://docs.google.com/document/d/1WqShFLf-VrsDg0G2KBB-K3EzlDzocBhL4rtiwHH_0mQ/edit#
* 1/24 Younggunと認識あわせ実施(iqbal, terada, takanory)
* `ISSHA-2000 US PyConブースの実施内容を英語でまとめる <https://pyconjp.atlassian.net/browse/ISSHA-2000>`_
* `ISSHA-2001 US PyConのブース実施内容をYounggunとMTGで共有する <https://pyconjp.atlassian.net/browse/ISSHA-2001>`_
* `ISSHA-2002 US PyConブース用にイベントロゴを作成する <https://pyconjp.atlassian.net/browse/ISSHA-2002>`_
* 製作物は、PyCon JPの予算で進める→今日の会議で合意済み

コアスタッフ制度(takanory)
==========================
* https://pyconjp.atlassian.net/browse/ISSHA-1490
* ざっとまとめた

  * 月に5時間以上 PyCon JPのための活動ができる人にフォームで申し込んでもらう
  * 氏名、メールアドレス等を申し込んでもらう
  * どの活動がやりたいかを選んでもらう
  *  Python Boot Camp, Pycamp caravan, 地域イベントサポート, PyLadies caravan?, その他(自由記入)
  * 内部で審査(する?)→OKだったらSlackに招待
  * 名簿に記入してWebサイトに掲載する
* @pycon.jpのメアドがとれるとか(yoshida)
* 大枠としてはいいと思う。それぞれなにやっているか予備知識がない人がイメージできるような情報があるとよい(ryu22e)
* ありがたい仕組みだと思う。やりたい人が入ってくるので枠組みとして良いと思う(kobatomo)
* 概ね同意。活動を選ぶというか、活動をやるときにこういう人が向いている。とかがあるといいかも。求人情報みたいなものがあるといいと思う(maaya)
* 内容はよいと思う。できればやってみたい。一つだけ選ぶ感じ?(kanan)
* 申し込みフォームを作るときに「意気込み」を書けるようにするとよいと思う(maaya)
* フォームの内容とか細かいところはやりながら進めていきましょう(terada)
* 審査するかどうか?(terada)

  * 審査はするってして、実はしないくらいかなー(takanory)
  * 連絡が付かない。(takanory)
  * ネットで炎上している人とかはぶくとか(maaya)
  * 実績がXカ月ないと名簿からは削除になりそう(takanory)
  * 理事から反対がなければOKって程度にしておこう(terada)

法人名変更
==========
* 英語名称、日本語名称の変更

  * TODO: 2月に向けて準備を進める(jonas) https://pyconjp.atlassian.net/browse/ISSHA-1957
  * 行政書士さんとやりとりする(terada)　(済み)
  * 英語名: PyCon JP Association
  * 日本語名: 一般社団法人PyCon JP Association
* 社員(4人)への事前説明

  * 事前に丁寧に説明する必要があると思う。(terada)

その他
======
* サービス・リソースの管理(terada)

  * https://pyconjp.atlassian.net/browse/ISSHA-1896
  * 継続中
  * **TODO**: まずは情報をとりまとめてほしい(terada→yoshida)
* 来年度に向けて、活動の定量的な評価指標を作れないか？(terada)

  * 継続中

    * 目的: 今後の予算の使い方、どういう方向性に向かっていくかを内外に共有するため(terada)
      * 指標があって数字だけが一人歩きすることは懸念している(takanory)
    * PyCon JPスポンサー、参加者

      * 海外からの参加者数
      * 関東以外からの参加者数
    * Python Boot Camp回数、参加者数
    * PyCamp Caravan回数、あとなんだろ?
    * PyLadies Caravan回数、参加者数
    * 地方コミュニティの立ち上がり数
    * 海外での発表者の増加
  * **TODO:** タスクにする。時間を作って資料にまとめて社員総会で提示する(terada)
* 弁護士との契約について(terada) [ISSHA-1470](https://pyconjp.atlassian.net/browse/ISSHA-1470)

  * 継続中

    * スポンサーについてはPyCon JP側からの許諾書を提出することも考えた方が良いのではないか(terada)
    * 他のカンファレンスはどうしているのかなぁ(takanory)

      * JJUGでは契約のやりとりをして、間に合わないと終了している(maaya)
    * 金額を積んででも、弁護士に相談しても良いのでは無いか？ 例えば、20万円くらい(yoshida)
    * 日本語、英語で許諾書を作る (契約書ではなく) のはどうだろうか？(terada)
    * 10万円の予算で進める

      * (yoshida / terada で相談する)

次回ミーティング
================
* 日時: 2020年2月26日(水) 19:30から21:30

  * https://pyconjp-staff.connpass.com/event/165073/
* 主な議事

  * 社員総会(30min)
  * 理事改選(15min)
  * 運営会議

    * 予算、方針など大枠の話

TODO
====
* `[ISSHA-2008] OSC 2020 Tokyo SpringでPyCon JPブースをPyCon JP 2020チームとどうするか決める <https://pyconjp.atlassian.net/browse/ISSHA-2008>`_ (takanory, peacock)
* `[ISSHA-2009] PyCamp Caravanの2020のセミナーのネタを決める <https://pyconjp.atlassian.net/browse/ISSHA-2009>`_ (yoshi-tsukamo)
* `[ISSHA-2010] ピザ支援フォームを作り直す <https://pyconjp.atlassian.net/browse/ISSHA-2010>`_ (takanory)
* `[ISSHA-2011] 「支援コミュニティにお願いすること」の見直し <https://pyconjp.atlassian.net/browse/ISSHA-2011>`_ (terada)
* `[ISSHA-2012] 一社としての活動の定量的な指標をまとめる <https://pyconjp.atlassian.net/browse/ISSHA-2012>`_ (terada)
* `[ISSHA-2013] 2020の理事募集を実施 <https://pyconjp.atlassian.net/browse/ISSHA-2013>`_ (terada)
