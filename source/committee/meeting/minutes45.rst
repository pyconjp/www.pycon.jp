===============================================================
 2021年3月18日(木) 一般社団法人PyCon JP Association運営会議#45
===============================================================

* 日時: 2021年3月18日(木) 

  * https://pyconjp-staff.connpass.com/event/205668/
* 場所: CMSコミュニケーションズ、Zoom
* 理事: terada, takanory, jonas, shimizukawa, yoshida
* オブザーバー: ryu22e, nikkie, yoshi-tsukamo, kanan, maaya, peacock, kobatomo, nishi


課題のレビュー
==============
* `一般社団法人PyCon JPの課題 <https://pyconjp.atlassian.net/issues/?filter=11500&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20%3D%20%E4%B8%80%E8%88%AC%E7%A4%BE%E5%9B%A3%E6%B3%95%E4%BA%BA%20ORDER%20BY%20due%20ASC%2C%20updated%20ASC%2C%20component%20ASC>`_

PyCon JP
========

PyCon JP 2020 (nishi、低、報告)
-------------------------------
* 全活動完了していますので、Association運営会議のトピック掲示も今回が最後で大丈夫です。
* 完了事項

  * PyCon JP 2020収支とりまとめ・収支報告Blog公開
  * 旧マニュアル上で更新されていた会計に関する情報を、Confluenceへ移植
* 今後の予定

  * PyCon JP 2020の特定タスクはすべて完了
  * 継続活動として、Confluenceへの情報追加・更新
* `旧ドライブ <https://drive.google.com/drive/folders/0BzmtypRXAd8zZDZhOWJkNWQtMDNjOC00NjQ1LWI0YzYtZDU3NzY1NTY5NDM3>`_ の `2020フォルダ <https://drive.google.com/drive/folders/1yCt6uroZ-9-6ZUBm2m959fecEdA6GBvH>`_ 削除できます (nikkie

  * 削除した(3/18 takanory
  * 2021でも参照したいアンケートフォームは、PDFにして共有ドライブ 2020下に移動済み（`ここ <https://drive.google.com/drive/folders/1iCvK6RXEPGkTtk4qjvJmcr5yKfBHB4sC>`_）
* #2020 のチャンネルは残っている(nikkie

  * 全然残しておいていいと思う(terada
  * +1 (takanory

PyCon JP 2021(nikkie、高、報告)
-------------------------------
* ここまでの動きの共有 (中、報告、nikkie)

  * 目標: 3月末にティザー公開、スポンサープランやプロポーザル募集を告知する
  * 直近の様子: https://pyconjp.blogspot.com/2021/03/pyconjp-2021-03-staff-mtg.html （読む時間30秒）

    * #committee で不定期にしていた共有は公開できることに気づき、スタッフ応募につなげるためにブログに書いてみました（継続予定）
* 今後の見通しについて共有 (中、報告、nikkie)

  * ☀️ ティザー公開はできそう（すでに動き出しており、人も集まっている）
  * ☁️ スポンサーやプロポーザルは、3月末では「こういう感じで動きます」という告知が現実的（4月中に募集開始）

    * 「メインで進めていきたい」という立候補いまだなし
    * タスクが大きいからでは？ → nikkieの方でタスクをバラす
    * nikkieタスク手を出しすぎ問題はある
  * タスクの割り振り難しいところはあると思っている。過去の紹介をすると2011~2013は似た感じで全体で相談してってやっていた。規模が大きくなってまわらなくなってきた。2014~2016はチームのリーダー/副座長で責任を分担していた。2017年からはその中間という感じ(terada
  * 2017からはチーム制をゆるめにやってみた。スポンサーとかはやりたがる人がいない。どうしようもなければ吉田、寺田とかに入ってもらうのはありだと思う(yoshida
  * 2020にワンマンでコンテンツチームをやりすぎたので、お願いできる候補がいないということを思い出した。2020でリーダーやっていた人に声を掛けるのはありだと思う(nikkie
  * 「nikkieがやりやすいように」と発言。それだけを考えるのはよくないと思っている。トータルでどうなったらよくなるかを考えるのもいると思う(takanory
  * 自分はまわりの目を見て、気を使いすぎてやっていたなと思った(terada
  * この🌥の感じの気持ちを、スタッフに共有してもいいかな?と思った(takanory
  * 経験者とかをうまく「ここやってよ」って言うのはあり。遠慮なく言ってください。2016年に会場チームをまとめてほしい、と言われてやったのはよかった。(terada
* 予算の決め方について相談 (高、相談、nikkie)

  * 支出の総額💰が決めがたい → どう決めるべきか、これまでの経験から意見をください

    * 項目確度Dが多くあり、現在のスタッフの人数でできる範囲を考えるとやらない（nikkieとしてはこれで割り切りたいが、予算はこのあと大きく変更できないので悩んでいる）
    * 今後スタッフの人数が増える可能性はある。こなせる量が増えてやれるかもしれない。ただしやろうとすると、支出が増えてしまう
  * 案：幅をもたせて決める

    * イメージ：300万〜700万（現地併催したり、やることを増やすと結構膨らむ見立て）
    * 余った額をPSFに寄付
    * 寄付はあらかじめ公表しておく（Django Congress JPにならう）
  * ほかに案があれば教えてください

    * 当初は「これくらいならスポンサー収入が入るのでは」と思って決めていた。思い切って「PyCon JPにはこれだけの価値があるんだ」と金額を決めたときもある。スポンサーが集まらなくて苦労したこともある(terada
    * バランスをとるというよりは、価値ベース(terada
    * 最低これだけ集まるでしょ+参加費で賄えることをやっていた(takanory
    * 以前は会場、食事などで支出が読めていた(terada
    * 2016年までは会場費がかかっていなかった(terada
    * 参加費10,000円から8,000円を返す。スポンサー費用で他のことをまかなう感じでやっていた(terada
    * スポンサープランは価値ベースで決めるといいのではというのが1案(terada
    * 参加費はコスト(食事、ノベルティ、パーティー)をベースに考えていたと思う(terada
    * 利益があまり大きく出るとよくないかなと思っている(nikkie
    * 一般社団法人はプールできる。余剰金を他の施策に使っている。毎年プラスマイナスゼロだとお金が足りないので、10年とかではプラスである必要がある。単年度では赤字でも困らない(terada
    * 2021の難しいところで、ハイブリッド開催かどうかが決められていない。予算を両方作らないといけないところが難しい。その上で経験者もいないので予算を作るのがとても困難な状況(yoshida
    * 早めに「予算、スポンサー」などの話をする会を別途やりたい(takanory

      * 参加候補: shimizukawa, terada, yoshida, takanory
      * 現役のスタッフ一部
      * 調整さん作る（来週あたりで調整） @nikkie
    * 2020は支出の総額を積み上げで決めた。それに対して必要な収入を決めた。価値ベースは単価であって、何枠は決められないかなと思った(nishi

      * 2020の予算組み、スポンサープラン設計では。。。(nishi

        * 予算組の支出総額はどうやって決めたか -> スタッフからの申告の積み上げ
        * スポンサープラン単価はどう決めたか -> 価値ベース(いくらくらいの価値が提供できると考えているか・類似カンファレンスの特典内容別広告単価を参考)
        * スポンサープラン枠数をどう決めたか -> 支出積み上げとのバランスと、各単価に対する直感的な申込数
* その他共有事項 (中、共有、nikkie） 読むだけで済ませる予定

  * yoshidaさんに作ってもらった https://twitter.com/pyconjapan アカウントを運用していく

    * 準備の様子を発信して、スタッフ増につなげたい
  * eurieを「Close Account」します（JIRA不要）

    * #committee で都度共有予定

      * 都度の共有は不要です(takanory
    * 関連 https://pyconjp.atlassian.net/browse/ISSHA-2318

PyCamp、PyLadies関連
====================

Pycamp状況報告(ryu22e、低、報告)
--------------------------------
* 運営メンバー: ryu22e、kobatomo
* 3月以降の活動状況

  * 現在開催が決まっているのは以下のイベント（前回の報告と同じ）

    * 5月29日山口開催予定

      * 現地スタッフ: KeisukeSawaさん
      * 講師: shimizukawa
      * 担当コアスタッフ: kobatomo
    * 鎌倉市開催予定日はまだ未定
* Python Boot Camp オンライン相談会（担当: kobatomo）

  * 4月15日（木）20:30〜22:00開催予定
  * connpassイベントページ: https://pyconjp.connpass.com/event/207631/

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、低、報告)
------------------------------------------------------------
* 運営メンバー: yoshi-tsukamo
* OSCは今年夏までオンライン開催を継続する方針との連絡あり

  * 5月29日(土) 名古屋（6/5予定から変更）
  * 6月26日(土) 北海道
  * 7月下旬〜8月 京都
  * 8月末 ODCオンライン
* 3月6日「OSCオンラインSpring」に参加しました

  * https://event.ospn.jp/osc2021-online-spring/session/274261
  * nikkieさんと稲森さんが講師として発表
  * `YouTube Liveのアーカイブで公開 <https://www.youtube.com/watch?v=kiVvos1utfU>`_
  * どうでしたか?価値があった、なかった。どう思った?(terada

    * やり方が違うので、視点の違う話が聞けて良かった。テーマとか変えていく予定なので、オンラインに向いていると思う。オンラインだと同じ人がいろんな場所に見に来る可能性があるので(yoshi-tsukamo
    * 発表した側としては、つつがなくできた(nikkie
    * 聴衆がいないと発表がやりにくいよね(shimizukawa
    * 顔出しお願いします、チャットで反応ください、とか言うと多少反応があった。スタッフ募集の効果はまだあがっていない(nikkie

PyLadies関係報告(maaya, 低, なし)
---------------------------------
* 運営メンバー: maaya, kanan
* PyLadies各リージョン状況

  * kyoto/okinawa 活動停止中
* PyLadies Caravanもコロナが落ち着くまで休止

  * 秋：企画再始動開始(秋田とか)
  * 2022年1月くらい：PyLadies Caravan再始動（願望)
* オンラインで1回くらい座談会とかやるかも?これから考える(maaya
* pycampにPyLadies Tokyoのスタッフが行くっていうのはメリットが大きいと思った。長崎のときにkamekoさんが行ったのはよかったなと思った(terada

  * そもそもpycampが動き出さないとって感じかな(takanory
  * 山口が決まっているので、動き出してもいいのかも(terada

PyCon JP TV(takanory、中、議論)
===============================
* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* Web https://tv.pycon.jp/
* YouTubeライブで月1くらいでやっていくつもり
* 2月5日(金)に1回目を配信 https://www.youtube.com/watch?v=LOyoOa6wODA

  * 知ってる人のコメントが多かったが、少し新しい人からもコメントがあった
* 3月4日(木) に2回目を配信 https://www.youtube.com/watch?v=xdgNNP8j4gY
* #3 4月2日(金), #4 5月7日(金) 予定
* 活動についてどうですか?(terada

  * めっちゃおもしろいです(shimizukawa
  * 毎月第1金曜日という感じ?(maaya

    * その予定です(takanory
    * 第1金曜日は遊びにいかないようにします(maaya
  * 結構気づくと終わっている。まわりにうまく知らせていくのが必要かなと思っている(yoshida

    * PyCon JP TVのカレンダーを作りました(takanory
    * https://calendar.google.com/calendar/u/0/embed?src=tv@pycon.jp&ctz=Asia/Tokyo&mode=AGENDA
    * 順次やっていきます(terada
  * PyCon JP 2021の情報は順次告知していこうと思っている(terada
* 経費の予算化をしたい (terada)

  * イニシャル(初期費用)

    * 多くの機材は個人の持ち出し。(terada)
    * 三脚やマイクスタンド、ケーブルなど、持ち運びコストが高く、購入コストが低いものは購入したい。 (terada)
    * 予算として、65,000円を計上したい。

      * https://docs.google.com/spreadsheets/d/13JP0ecnixpfNyyTS74nRglfAMrWfPwiIWqnmLIJIK9k/edit?pli=1#gid=1275653170
    * ステッカー、カード、郵送費: 15,000円

      * お便りコーナーでお便りを読んだ人にプレゼントする
  * ランニング

    * オンライン懇親会費用を計上したい。1回10,000円
    * 懇親会の対象者は、パーソナリティー2名程度、スタッフ2名程度、ゲスト1名程度
    * 具体的な項目

      * ピザ 5,000円
      * 飲み物 5,000円
  * 年で合計20万円の予算申請

コミュニティー支援
==================

Python地域交流オンライン座談会(takanory、低、なし)
--------------------------------------------------
* 一旦中止

地域PyCon等の支援について(takanory、低、なし)
---------------------------------------------
* PyCon mini Shizuokaが開催準備を進めてるっぽい(takanory
* PyCon Kyushuも準備をはじめているっぽい(terada

海外コミュニティ連携
====================

Python商標問題(terada、低、報告)
--------------------------------
* 進展なし

Python Charity Talks in Japan 2012.02(takanory、中、報告)
---------------------------------------------------------
* 2月20日(土)開催済

  * https://pyconjp.connpass.com/event/199787/
* 890,000円をPSFに送金予定

  * https://pyconjp.atlassian.net/browse/ISSHA-2306
* connpassへ資料掲載、報告Blog、プレゼント送付など完了
* また気が向いたらやる感じ(takanory

  * とはいえ、8月ターゲットだと5月くらいには動き出さないといけないなー(takanory
  * 私としてはやりたいけど、すぐ次ってなっちゃってちょっと疲れないかなーって思った(takanory
  * 終わってからアンカンファレンス的にやってもいいのでは(peacock
* PyCon JP Associationのお金を使っているので、予算化の必要がある(terada
* 年何回やるのか?(shimizukawa

  * 最大2回だと思う(takanory
  * 12月、6月みたいにずらすといいのでは(shimizukawa

APAC関連(terada、低、なし)
--------------------------
* 進展なし

APAC・JPロゴ関係(terada、低、なし)
----------------------------------
* なし

予算2021(terada、高、議論)
==========================
* `2020予算参考 <https://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=0>`_, `2021予算 <ttps://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=1331278426>`_
* 仮予算を以下の通り決定済み

  * Python Boot Camp: 5万
  * Python Charity Talks: 10万円
  * 月次費用(会計事務所、Flickr、行政書士): 50万円
  * (スポンサー契約書、COC)弁護士相談費用: 40万円　2020年予算からの持ち越し
  * 他
* 決定: 

  * 2月末までの仮予算として、120万円を計上する
  * PyCon JP TVの3月の懇親会費1万円
* 予算案

  * PyCon JP 2021: 0円
  * Python Boot Camp: 30万円
  * Python Boot Camp Caravan: スポンサー20万円+30万円

    * OSCで効果が減っている感じがするが、スポンサー費用そのままでどうするかを一緒に考えたい(terada
    * OSCにはお世話になっているので恩返しはしたい(terada
    * OSCに出ていない人が発表する場としてあるのはありがたい(terada
    * 別でLUG、BUGの集合とかで人が集まった。各コミュニティでOSCに来てくださいって言っていた(yoshida
    * OSCに参加する人を各コミュニティで連れてくる(yoshida
    * OSC側の気持ちはわかるが、スポンサー費用を払ってそこを力を入れてがんばる意味はあるのかという疑問がある。新しいつながりとかが薄い(terada
  * PyLadies Caravan: 8万+4万円でpycamp派遣(terada)
  * PyCon JP TV: 20万円
  * Python Charity Talks: 20万円(10万円 x 2)
  * 予備予算: 50万円
  * システム費: 86,000円

    * Flickr, さくら, AWS, Zoom Meeting
  * 合計: 3,316,000円
* 予算案について

  * AWSの費用が入ってなさそう(takanory

    * 金額はかなり少ない(shimizukawa, yoshida
    * 月100円、年1200円のため、念のため、5000円計上しておく
  * その他

    * Flickr 7000円、さくらDNS 4000円
  * 追加収入は今年ないと考えられるので、追加予算をたてにくい。そのため、予備の予算を50万円くらい持ちたい(terada

    * 賛成(takanory
    * 異論なし(shimizukawa, yoshida, jonas
    * 収入が減っているが、予算をどう考えるか?(terada
  * 予算をうまく使えていないのではないか、という議論が過去にあった(terada
  * しかし、収入が減って先行きが見えない中で2021年や今後の予算をどうするか考えてほしい(terada
  * PyCon JP AssociationはPyCon JPのイベント活動を継続するための組織、が大前提なので、PyCon関連に興味がありそうな人たちをつなぎとめるための活動に予算を使うのはありだと思う。いまこそ必要であればやった方がいい(shimizukawa
  * しみずかわさんが言った考えもあると思う(jonas
  * しみずかわさん意見と同意。いいアイデアがあればお金を積極的に使いたいが、アイデア不足(yoshida
  * PyCon JP Associationが日本のPython界隈のためになにかやっている。と見えるような活動にお金は使いたい。とはいえ、どうやってもそんなにお金を使えないと思っている。pycamp、pycamp-caravanの予算が減るので(takanory
  * すべてがオンラインになった状況でお金を使うところが少ない(jonas
  * こんな時代なので積極的にお金を使っていっていいと思う。お金が減りにくい。施策としてPyCon JP TVとか新しいことに挑戦すること。新しいアイデアが思いついたらやりたい。がんばって探していきたい(terada
  * PyCon JPの継続が大事。PyCon JPの継続にあたってお金が必要なことがないか。PyCon JP Associationの予算でなにかするとかもあるかもしれない。(terada
  * PyCon JPは毎年スタッフが足りない問題を聞いている。お金を使ってアウトソースするのはどうか?Webサイトの制作、デザインとか(jonas

    * 以前Webサイトや冊子などをアウトソースしたことはある。yoshida座長が事務局のアウトソースをしようとしたが、指示をするのが難しかった認識(terada
    * Scala Matsuriみたいにうまくまわっているところもある(yoshida
    * 法人の予算でWebサイトのフレームワーク改修を行ったこともある(terada
    * Webのアウトソースは、最近は必要なタイミングでできている認識(yoshida
  * PyCon APACがリアル開催の可能性がある。そこに補助を出すとか?(yoshida

    * アイデアとしてはありだが、目的をどうするか(terada

その他
======

PyCon JP Twitterについて(yoshida、低、報告)
-------------------------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-2210
* pyconjapanアカウントを作成したので上記はCloseで良い認識
* https://twitter.com/pyconjapan
* アカウント情報など詳細はサービス管理シートに記載しています。
* https://docs.google.com/spreadsheets/d/1YiqErBDdp5QWfTlfDmxc6Vi696b_NGFJKzuyM-v6PDM/edit#gid=0
* 年次イベントの広報に使用したい

  * ティザーサイトへの掲載

    * nikkieから担当者に共有済み（`Slack <https://pyconjp.slack.com/archives/C01M5K8JKKN/p1616070213020100>`_）
  * Pyconjpのblogの連携を設定したい

    * ノ nikkie（2020も設定したのでやります）→ https://github.com/pyconjp/tasks-2021-planning/issues/56 で設定済み
  * 理事関係者のフォローとRTをお願いしたい。

弁護士との契約について(yoshida、低、なし)
-----------------------------------------
* 

Zoomライセンス見直し(takanory、中、相談)
----------------------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-2227
* すすめたい。ライセンスが必要な人を教えてほしい(takanory
* 2,200円 x 人数 

  * https://www.techsoupjapan.org/node/3522
  * 6,234円 / 年っぽい
* PyCon JP Associationが1つ(terada
* Python Boot Campで1つ(ryu22e or kobatomoあたり
* PyCon JP 2021は座長+チームリーダー分 > PyCon JP 2021予算で？
* アカウントは pycon.jp ドメインのメアドで運用したい

2021年の活動(takanory、中、議論)
--------------------------------
* とりあえずPyCon JP TVをやっていく
* 他なにか思いついたら
* 高校生以下だけの発表イベント、女性だけの発表イベントとかできないかな(takanory

  * https://pyconjp.slack.com/archives/C024JGVAU/p1615111029133200
  * 目的: 発表のためのハードルを下げたい、PyCon JPとかのスピーカー予備軍を増やしたい
  * オンラインイベントをやりたいってこと?(terada

    * まずはオンラインでやるのかなと思っている。広く発表してほしいからオンラインがいいのかなと思っている(takanory
  * 発表者が高校生だけ、参加者も高校生だけ?(jonas

    * 参加者高校生だけは集まらないから、参加者は誰でもありかなと思っているが、考えたい(takanory
  * 高校生の一緒にやってくれる人がほしいと思っている(takanory

    * PyCon JP 2021スタッフやっている人にN高関連の人がいる(peacock
  * 女性側の方は疑問があって、PyLadiesで発表している人は外で発表するのが怖くてPyLadiesでした。参加者が女性だから発表したって人もいると思う。イベントのたてつけは検討が必要(maaya

    * すごくわかる。(takanory
    * 私も(jonas
    * 顔出ししないとかはどうかな?(takanory
    * そこではない。発表してみなよ、という後押しがほしい(maaya
  * 予算はかけないということでよい?(terada

    * Zoomがあればよいので、OK(takanory
* 思いついたらアイデアを出してほしい(terada

次回
====
* 運営会議#46

  * https://pyconjp-staff.connpass.com/event/208036/
  * 2021年5月13日(木) 19:30-


