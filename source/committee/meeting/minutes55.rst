===============================================================
 2022年9月28日(水) 一般社団法人PyCon JP Association運営会議#55
===============================================================

* 日時: 2022年9月28日(水) 19:30-22:20

  * https://pyconjp-staff.connpass.com/event/256414/
* 場所: Zoom
* 参加者

  * 理事: terada, takanory, jonas, yoshida, shimizukawa
  * オブザーバー: selina, maaya, yoshi-tsukamo, ryu22e, sano, kobatomo, peacock

.. contents:: 目次
   :local:

課題のレビュー
==============

* `PyCon JP Association(一社のみ) <https://pyconjp.atlassian.net/issues/?filter=11500>`_ の課題一覧
* `PyCon JP Association(一社以外) <https://pyconjp.atlassian.net/issues/?filter=15948&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20in%20(EMPTY%2C%20%22Pycamp%20Caravan%22%2C%20%22PyCon%20JP%20TV%22%2C%20%22Python%20Boot%20Camp%22)%20ORDER%20BY%20due%20ASC%2C%20component%20ASC%2C%20updated%20DESC>`_ の課題一覧

PyCon JP
========

PyCon JP 2022(selina、高、報告)
-------------------------------

現地にて開催します！（1ヶ月前発表）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* コロナ関連が気になっていたが決行！


予算について
~~~~~~~~~~~~

* S+A+B+Cを見ると赤字になっているのでご相談。
* 原因は収入源をチケット販売に頼っていたため。（チケットは開催前まで販売しているので、赤字金額はPR等をして押さえたい。）


.. csv-table::
   :header: 予算確度別収支, 支出, 収入, 収入 - 支出

   S(確定: 執行済・発注済), "7,301,859", "21,082,000", "13,780,141"
   S + A, "19,318,003", "21,082,000", "1,763,997"
   S + A + B, "22,702,438", "22,247,000", "-455,438"
   S + A + B + C, "25,634,648", "22,932,000", "-2,702,648"

* 収入として現在の実績、今後このくらい販売できるだろう、売り切れた場合の3段階の収入の予算が立てられると思う。それをみないとどこまでの赤字になるのかを見えてこない(terada

  * 参加者が少ないと支出が少ないものもある。とはいえ、そこまで細かく見なくても良いと考えている(terada
  * ここの収入は「いま売れている金額」が入っている(yoshida
  * 過去の例だと「人数が増えると収入も増えて支出も増えている」イメージ。予算として固定費と変動費があるのでは(shimizukawa
  * ランチが今は500なので300などには減らせそう。とはいえ、それで50万円くらい減らせる(seliina
  * 会場費の割に人数が入れられない、コロナ対策などで固定費が増えている(yoshida
  * 無駄な物は減らしてほしい(terada
  * 労力としてはPRにさいてほしい(shimizukawa
  * フード系の支出は実際に集まる人数にあわせて、調整してほしい(takanory

    * 調整には動いている(selina
* 収支のマイナスはどこまで許容できるか？

  * 仮に「許容できない」となった場合、なにか対策を話したりしているなら知りたい(shimizukawa
  * 気になっているのは、責任はどこまで取る必要があるか？(selina
  * 金額的な責任を負わせるつもりはありません(terada
  * もしチケットが全部売れたら黒字になる？(sano
  * （なるはず、という話）
* チケット販売の伸び悩みについて
  * 予算の問題だけではないと思うが、これをどう考えるか(terada
  * 来場者が少ないことに対して、スポンサーが不満に感じないか？(terada

    * スポンサー募集に、例年の人数を書いていて、その人数を期待して活動していると思う(terada
    * （来場者を増やす施策の話）

      * 事務局では検討していて **Twitter/FB広告** などを打っている(yoshida
      * それは販売を増やす努力として良いと思います(terada
      * スタンプラリー企画など、**スポンサーへの誘導を強化** しようとしている(yoshida
      * Python関係 **コミュニティー主催者に依頼** して、PyCon JPへの参加を促す施策などを進めている(selina
      * スタンプラリー参加でTシャツをもらえる、というPRをしようと考えている(selina
      * **スポンサー、スピーカーへの宣伝協力依頼** (terada **(優先度4)**
      * **メディアへの協力依頼**

        * 歩き方記事は技評さん打診済み(peacock)
        * 開催前のレポートを書いたりしていた(ryu22e
        * CodeZine近藤さん(優先度3)
      * X日までに参加してくれたらなにかプレゼントをあげる(takanory
      * 一度チケット枚数を減らす(terada **(優先度2)**

        * アナウンスも同時にする。戻すかもしれない匂わせも必要
        * 理由づけはできる。発注する数が読めないため(terada
        * プレゼントよりはこっちの方がいいのでは無いか(iqbal
      * 一日だけのチケットを出す(terada

        * すでに買った人がいるので微妙(peacock
        * 1日だけど理解して買っている人がいるので微妙(takanory
      * ユーザーの分類

        * 買い控えている人→チケット枚数を減らす。N日までに買ってくれ
        * 伝わっていない→メディア対策
      * Twitterで「connpassページが分かりづらい」との声があった。

        * ->案内文の見直しが必要そう
    * （スポンサーに対する施策の話）

      * スポンサーに対してどのくらい来場者数の話をしているか？(terada
      * 今このくらいの参加者、必要になるグッズ数の予測、もっと参加者増やすようなblog書いて欲しい、といった連絡など
      * （今日事務局メンバーは参加していないが）そこまでの行動はしていないと思う(yoshida
      * ぶっちゃけて話した方が良いと思う(takanory

        * 現状こうです、がんばってます、でもダメかも知れません(takanory
        * 期待値を早めに下げておいたほうがいい（takanory
      * スポンサーはPyCon JP 2022を開催する一緒のチームなので、現状共有とか対策を打つとかを一緒にやる関係性を作った方がいい(shimizukawa
    * オンラインでスポンサーとミーティングを持って現状を共有したい。スポンサー担当経験者にも同席してほしい(selina

      * 現在のスタッフの人たちはどういう意見か(terada
      * スポンサーへの現状共有は早めにした方がいいと思う。PR協力依頼もいいアイデアだと思う(jonas
      * 次のアクション

        * 誰が、なにを、どうするのか
        * **プラン1: Slackで早急にメッセージを出す(優先度1)**
        * **プラン2: オンラインで相談会を開催(優先度1)**

          * 同席可能: terada, takanory
          * 2、3、枠を作って、参加側スポンサーが選べると良いと思う(takanory
          * スポンサーからの案、意見がでたときにその場で応答できるように、イベントの実務担当者が同席してほしい(takanory
        * 主担当: selina

          * アナウンス文章とかのレビューサポートは理事等みんなでやりましょう
    * チケット伸び悩みは来場者も残念に思うのでは(takanory

      * 他の人との交流が減ることで、参加者、スピーカーが残念に感じるのではないか？そういう人たちにも協力してもらえる流れを作れないと厳しいと思う(takanory
      * 来場者を増やす施策としてそれも含めて話しましょう(terada
* 金額確定のものはSにしている。
* チケット販売中

  * ランチ及びコーヒー（ソフトドリンク含む）を含んでいる。
  * https://pyconjp.connpass.com/event/255827/
  * パトロン: ¥40,000 * 想定15 (9/28現在：15)
  * ビジネス: ¥18,000 * 想定150 (9/28現在：47)
  * 通常: ¥12,000 * 想定400 (9/28現在：109)
  * 学生: ¥2,000 * 想定50 (9/28現在：16)
  * オンラインのみ: ¥2,000 * 想定100 (9/28現在：67)
* パーティー（別チケット）5000円

  * https://pyconjp.connpass.com/event/261187/

キーノートについて
~~~~~~~~~~~~~~~~~~
* 日本語：西内 啓さん（15日登壇、現地公演）
* 英語：Mark Shannonさん（14日登壇、残念ながらリモート出演）
* 特別出演案も出ていたが、プログラムの調整も難しいので今年は断念

その他
~~~~~~
* 次回の全体MTGは特になし。都度Zoom等を用いて集まる予定。
* 現地スタッフの案内準備中。下記の通り、説明会を行う。
* **カンファレンス前事前顔合わせ** （当日スタッフ会兼務）

  * 10月11日(火) 18:00〜
  * ここで最終的な調整を行う。
  * **何か気になる点があれば、10日までに連絡がほしいです。(selina)**

PyCon JP Associationの公開ミーティング(takanory、中、報告)
----------------------------------------------------------
* https://2022.pycon.jp/timetable
* 10月14日(金)の11:45-12:45で開催
* **TODO**: 資料作成、告知

PyCon JP 2023(yoshida、低、報告)
--------------------------------
* TOC有明下記で仮押さえ済

  * ２０２３年１０月２６日（木）～２９日（日）
* **TODO**: キャンセル料、時期を確認する(yoshida
* PyCon JP 2023 座長募集(terada

  * PyCon JP 2022 開催1ヶ月前に実施するか？

    * 9月に座長募集する-> Blogを執筆した(terada

会計
====

消費税インボイス制度の申請(terada、中、議論)
--------------------------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-2607
* 申請するか、しないか、を議論したい
* 2022年中に、申請する場合は手続きを完了させる必要がある

予算2022(terada、低、議論)
--------------------------
* `2020予算参考 <https://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=0>`_、`2021予算 <https://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=1331278426>`_
* 追加の予算申請は無いか？(terada)

  * 受け付けない方針
* Python Boot Camp/PyLadies Caravan関係者の遠方支援
* 招聘関連での行政書士への予算を組んだ


PyCamp、PyLadies関連
====================

PyCamp状況報告(ryu22e、低、報告)
--------------------------------
* 運営メンバー: ryu22e、kobatomo
* `Python Boot Camp(初心者向けPythonチュートリアル) <https://www.pycon.jp/support/bootcamp.html>`_
* 9月以降の開催状況

  * `静岡県沼津市（9月3日） <https://pyconjp.connpass.com/event/251468/>`_ →終了

    * 講師: arai
    * 現地スタッフ:hrs.sano645 , yoshi-tsukamo
    * 担当コアスタッフ: ryu22e
  * `新潟2nd（9月17日） <https://pyconjp.connpass.com/event/255600/>`_ →終了

    * 講師: terada
    * 現地スタッフ: wutali
    * 担当コアスタッフ: kobatomo
  * 香川2nd（11月19日）

    * 講師: takanory
    * 現地スタッフ: yanotoyko1
    * 担当コアスタッフ:kobatomo
  * 福岡で3回目の開催に向けて会場の選定中（現地スタッフ: kuga）
* その他

  * https://pyconjp.atlassian.net/browse/ISSHA-2641

    * PyCon JP 2022の遠方者支援の予算確保OKいただく。
  * https://pyconjp.atlassian.net/browse/ISSHA-2654

    * 遠方者支援の活動を進めています
    * 9/22 時点 3 名の応募
    * 9/29 まで延長して募集を募ります。
  * https://pyconjp.atlassian.net/browse/ISSHA-2673

    * Tシャツ追加作成をはじめた。内容はまとめたのでuniqさんにデザインまとめてもらっている→その後発注

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)
------------------------------------------------------------
* 運営メンバー: yoshi-tsukamo
* 参加済み

  * 9月3日(土) ODC

    * セミナー: Iosif, yoshi-tsukamo
    * LT: seigot
    * Pycamp沼津と同じ日だったのでセミナーでpycampの様子を生配信 https://youtu.be/PtaPJPxCipo?t=1355
* 今後の予定

  * 10月1日(土) 広島

    * ~~Murakamiさんが参加希望出してくれています~~
    * 会社の都合でセミナー参加が不可となってしまい参加断念
  * 10月28(金)〜29(土) Fall

    * ミーティング枠でpycamp相談会を予定
    * 10/29(土) 13:00〜
  * 11月26日(土) 福岡

    * PyCon JP 2022スタッフも余裕が出てくる頃だと思うので参加者募集
  * 2023年1月 大阪
  * 2023年3月 Spring

PyLadies関係報告(maaya, 低, なし)
---------------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-1687: 公開のタイミングを完全に見逃してしまっていてどうしようかなとなっています
* 8月6日 caravan 愛媛行ってきました

  * 直前で愛媛コロナ感染者数最多更新のニュースが出たことをきっかけにcancelが相次ぎ、結果2名の参加者に向けての開催となりました

    * しょうがないですねー(takanory
  * ペアプロ形式で開催
* 11月19日に愛知開催を予定しているが、現在参加者ナシの状態

  * https://pyladies-tokyo.connpass.com/event/260718/
  * このまま参加者が1人もいないようならリスケも検討
* Python Boot Camp in 新潟2ndで女性がいたので、Caravanのことは伝えた(terada

  * PyLadiesのSlackにはいるので、手を上げてくれるのを待っている(maaya

PyCon JP TV(takanory、低、報告)
-------------------------------
* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* https://www.youtube.com/user/PyConJP
* Web https://tv.pycon.jp/
* 第19回(8月)、第20回(10月)配信済み

  * `#19: EuroPython 2022振り返り - 2022-08-05 <https://tv.pycon.jp/episode/19.html>`_
  * `#20: PyCon JP 2022の楽しみ方 - 2022-09-02 <https://tv.pycon.jp/episode/20.html>`_
* 次回は10月7日(金)予定。内容は「Python 3.11の新機能を試す」

  * https://tv.pycon.jp/episode/21.html
* ネタ募集中です(takanory

コミュニティー支援
==================

地域PyCon等の支援について(takanory、低、なし)
---------------------------------------------
* PyCon miniの件ではないのですが静岡コミュニティから質問があります(yoshi-tsukamo
* コミュニティーのある人から質問があった(sano

  * MS,Google等の非営利団体向けの支援制度を使えるなら使ってみたい
  * PyCon JP Associationから支援してもらうことは可能か
  * コミュニティーをPyCon JP Associationの支部団体とすることで、非営利団体支援制度に申し込めるか
* 支部団体を作るか、について

  * 相当なディスカッションが必要。支部の定義、役割から決めないといけない(terada
* 支援について

  * PyCon JP Association自体が行っている支援としては、物品の貸し出しなどいくつか施策がある
  * しかし、Zoomライセンスの貸し出しは禁止されているためNGなど、第三者が提供するライセンス物を支援に含めることは非常に難しい
  * Google,MS,AWSといったものは今のところ扱っていないし、分かっていない
* 大前提として

  * コミュニティーの声は、どのようなものでも聞きたい。是非色々相談してほしい。支部の件も、それがどういうメリットがあるかよく説明してほしい。門前払いしたい訳では無い(terada
  * とはいえ、タダ乗りするような話には関わるつもりはない(terada
  * 自分で調べてみても、どうしようかな、という感じだったので、相談できて良かった(sano

海外コミュニティ連携
====================

APAC関連(terada、高、相談)
--------------------------
* Asia Python Society

  * アジア地区のPyConやPythonのコミュニティの集まり？？
  * 目的

    * PyCon APACイベントを統一的に管理、運営できる団体を作りたい

      * 現地はロジスティック関係をメインにやるのはいい
    * PSFから見れていないし、知ろうとしていないし、知るすべも無い

      * ダイバーシティー的にもアジアとの意識の違いもある
      * PSFが遠い存在となっている
      * 組織として意見が言いやすい
  * 状況

    * イクバルさんがAPAC MLに提案して意見を募集中
  * いくつか課題・疑問がある(terada

    * どうやって組織を実現するのか

      * あるといいと思うが、うまくいかないのであれば組織がない方が良い(terada
    * どうやって運営していくのか

      * どの国にたてるのがいいのか?(jonas
      * よさそうとなってから、どこで設立するかは考えようと思っている(iqbal
    * JP などのリージョンコミュニティーとどう関係性を作るのか
  * イクバルさんが提案している
  * PyCon JP 2022のときにも話ができるとよさそう(terada
  * 考え方としては分かります(takanory
  * EuroPython Societyも参考にして同じ失敗をしないように考えている(iqbal
* 今後APACにJPチームとして応募するか？

  * 2023については、まだ各国から応募がない(iqbal
  * やっていいと思っている(selina
  * やること自体は大きく変わらないが、英語が増える(terada
  * 日本でやっていいと思うが、やっていない国(インドネシア、香港等)でやりたい国があればそちらにまかせたい(jonas
  * 2022年11月に決めたいが、今のままだとAPACの開催の消極的で心配(iqbal

APACロゴ関係(terada、低、なし)
------------------------------
* 進展なし

理事など(terada、中、議論)
==========================
* 法人設立から10年、理事が固定化されている
* 来年度に向けて何か検討すべき事項は無いか？
* `理事メンバーの履歴 <https://www.pycon.jp/committee/board_history.html>`_
* 理事をもう一人は増やしたい(takanory

  * https://pyconjp.atlassian.net/browse/ISSHA-2648
  * こういうことをやっていますという情報があると動きやすい(selina
  * 「議事録を読んで」だとわからないってことですよね(takanory
  * 仕事をストップしながらやらないといけないのかがわからない(selina
  * 動画を撮りますか?(terada
  * PyCon JPのイベントでやっている「公開ミーティング」がわかりやすい(selina
  * 「理事会の広報ができていない」と認識した(takanory
  * **TODO**: なにかやり方を考える(takanory

    * まずはブログかなぁ...(takanory
    * 質問を募集してそれに答えるとか(takanory
  * **PyCon JP TVで30分程度の番組を収録公開** したいなと思っている(terada

その他
======

* 1PasswordのOpen Source Projects用のサポートプログラムがあるらしい(takanory

  * `1Password for Open Source Projectsの申請をした | Web Scratch <https://efcl.info/2022/09/23/1password-teams-open-source/>`_
  * EuroPython Societyが通ってるっぽいので、いけそう?
  * https://github.com/1Password/1password-teams-open-source#europython-society
  * 一同）賛成
* PyCon JP 2022前日(10月13日(木))の東京案内(iqbal

  * 海外からの来場者をもてなす企画。参加人数、時間は未定(terada
  * スピーカーで1名リアクションがあった(peacock
  * 13日(木)の夜は飲みに行く?(takanory
  * 13日(木)午後は予定がある。場所の提案とかは可能(terada
  * 調整可能かも(takanory
  * フィリピンではカンファレンスの次の日にバンを借りて自然を見に行った(iqbal
  * 予算はあるのか?(iqbal
  * 予算はない。一般社団法人PyCon JP Associationで組むかどうか(terada
  * 予算としてはpycamp/pyladiesの予算が使えていないので、組み替えは可能と思う(takanory
  * 都内なら電車で動くくらいなのでいいのでは。現地の手段で移動するのも面白い(jonas
  * 予算化はやめましょう(terada
  * PyCon JP 2022中に声かけをして、イベント終了後に行くのがよいのではないか?(iqbal
  * 11月16日(日)はスプリントとかぶっている(jonas
  * 13日来日で動ける人は少ない。17日(月)観光して帰る人はそこそこいる。(yoshida
  * 日曜日はNGだが、開催は日曜、月曜の方がよいのではないか(iqbal
  * 月曜なら体力があれば行きたい(selina
  * 決めたいこと

    * スタッフが動くのは止めた方がよい（詰め込み過ぎ）(terada

      * Iqbal, takanory
    * 木曜夜か、日曜月曜か

      * 木曜夜の飲み会を開催
      * 木曜午後観光する？

        * 案: 浅草ランチ～ `水上バス <https://www.suijobus.co.jp/cruise/asakusa/>`_ でお台場着、有明近辺で飲み会
* Jira以外のIssue管理ツール(Iqbal

  * 自社ツールがあるので、興味があれば提供できます(Iqbal
  * （次回以降のMTGで改めて）

次回
====
* PyCon JP 2022内での公開ミーティング

  * 2022年10月14日(金) 11:45-12:45
  * https://2022.pycon.jp/timetable
* 運営会議#56

  * 2022年11月17日(木) 19:30-21:30
  * https://pyconjp-staff.connpass.com/event/261842/
