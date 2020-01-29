================================================
 2019年12月4日 一般社団法人PyCon JP 運営会議#33
================================================
:日時: 2019年12月04日(水) 19:00-21:00

  * https://pyconjp-staff.connpass.com/event/151884/
:場所: CMSコミュニケーションズ(御徒町)
:参加者:

  * 理事: 寺田、ヨナス、たかのり、吉田、清水川
  * オブザーバー: いなもり

    * PyCon JP: nishi(2020座長)、ueki(2020スタッフ)、nikkie(2019からスタッフ)、peacock(2020スタッフ)、Hirao(2019からスタッフ)、Emi Fukuta(2020スタッフ)、ainamori(2019, 2020スタッフ）
    * PyLadies: kanan, maaya
    * PyCamp: yoshi-tsukamo, kobatomo

.. contents:: アジェンダ
   :local:

課題のレビュー
==============
* `[一般社団法人PyCon JPの課題] 課題ナビゲーター - pycon.jp <https://pyconjp.atlassian.net/issues/?filter=11500&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20%3D%20%E4%B8%80%E8%88%AC%E7%A4%BE%E5%9B%A3%E6%B3%95%E4%BA%BA%20ORDER%20BY%20due%20ASC%2C%20updated%20ASC%2C%20component%20ASC>`_

PyCon JP
========

PyCon JP 2019の開催報告と残件など共有(yoshida)
----------------------------------------------
* 残タスク

  * 海外からのスポンサー入金待ちが1件ある、まもなく入金予定。
  * 会計とりまとめて会計事務所に行く(年明けの予定)
  * PayPalに2件の未払い請求が残っている。要確認(yoshida TODO)

    * PSF
    * Enthought

PyCon JP 2020 (nishi)
---------------------
* 日程: 2020年8月27日(木)29日(土)

  * 参考資料: https://drive.google.com/drive/folders/1j13gGPygkEg5bxRml7R4aW6_BrQrZFur
* 場所: 大田区産業プラザPiO
* 直近の進捗・完了事項

  * 立候補をうけ、副座長を斎藤さんが担当
  * 環境設定(JIRA, スタッフ応募フォーム, Slack, GoogleDrive)
  * スタッフ受付開始・活動開始・プレキックオフ
  * 企画ブレスト
  * 初期のチーム体制構築
* 直近の予定

  * キックオフ(12/5)・チーム組成
  * タイムライン検討
  * 企画案とりまとめ

    * 3日開催したいなどの意見有り

    * アイディアノート: https://docs.google.com/document/d/1KloaM0bNePM0ZQt9Jo2_d5Os4fHS9nt0WtrE2wuBlbc/edit#
  * スポンサーパッケージ企画
* 困っていること・懸念点

  * 経験者スタッフの参加がまだ少ない

    * 声がけは早めにしたほうがいい。(takanory, yoshida)
  * 招待講演を増やすことを考えているが、講演料を支払う形での依頼に際して、必要なことを調査(経理上の考慮点は #accounting で相談中)

    * 経理上の考慮と海外によってはVISAがあるので、早めに動いた方が良い(terada)
  * (かなり先)準備日が平日でスタッフが集まれるかどうか

【依頼】GitHubのpyconjp下に、noc用レポジトリを用意いただきたいです
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* イメージ: https://github.com/pyconjp/pycon2020-noc

  * 必要なら作ってください。(terada)
  * publicならご自由にどうぞ?(takanory)
  * **TODO:** jiraでGitHubのowner権限の依頼をする[nishi]
* 依頼元: NOCチーム
* 申請理由

  * NOC構築に必要な設定ファイルの保存・共有の為
* 申請の背景

  * NOCはwebサイト同様、多くの設定ファイルを扱う為、保存の場所が必要

    * これまではgoogle driveのPyConJP.YYYY のに入れている or 保存されていなかった

      * 個人ベースで保存している人は居る）
  * 従来はこれらの設定ファイルをGoogleドライブに置いていたが以下の理由により適格とは言い難い

    * NW機器、サーバ共に設定レビュー・および投入の際Google Driveからダウンロードするのは非常に手間が多く複雑

      * Googleドライブで迷子になって探せないことが頻発する
      * コメントを入れづらい
      * その為に .docxなんてことも

  * NOC-Tが扱うファイルはその特性上、不特定多数（チームメンバ）が編集・更新を行う為、バージョン管理が行える仕組みを有していることが好ましい。

    * githubは設定ファイル・インストール手順（ansible playbook等）を置く場として非常に好ましい
  * 昨今はVPS上にDocker deployすることも多いため、github に container registryが置けるとビルド時間の短縮が可能
* 導入により期待される効果

  * 知見の保存・継承
  * デプロイ時間の短縮（ansible git clone 等が可能な為
  * 議論の活性化(品質向上) pull request機能は編集を容易にする
* 懸念点

  * アクセス権の管理。ただし、これはGoogleドライブでもほぼ同様の問題が発生する。
  * 運用ルールの策定（主に容量の管理）

    * NW機器のファーム、Docker Image等を置くようになった場合、容量が急激に肥大化する。


【相談】CoCへの項目追記方法について
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 2020で使用するCoCに、文言の追記は可能でしょうか
* 今利用しているCoCは、一社やカンファレンス、その他活動で統一して利用しているもので、追記には議論や承認が必要なものなのでしょうか。それとも、2020用CoCとして独立なものを作成してよいものでしょうか。
* 追記を検討したい要素: 「敬意」(nikkieの発案)
* 背景 [nikkie]

  * 「セッションのレベルが低い」というSNSへの書き込みがあってスタッフ内で問題視されていたが、その発言には「敬意」という要素が欠けている
  * いいなと思った： https://portal.engineers-lt.info/guideline/

    | > 敬意を持った行動の徹底
    | > 特定の個人または団体に対する暴言や誹謗中傷など貶める発言を慎み、他者への攻撃的な言動を行わないように務めます

  * 登壇者と同じ産みの苦しみを味わっていない人間に軽い気持ちでネガティブな発言をしてほしくないという思いがあります
  * 「敬意」と「自由な議論」をうまくバランスを取る必要もある [nishi]
* コメント

  * (shimizukawa) CoC違反があった場合、退場してもらう等のアクションをとることも考えられるけれど、「セッションのレベルが低い」という発言があったら同様に対処する？

    * 強権発動につながるのは本意ではなく、書いたところで効果はあるのか
    * 手段は行動規範への記載だけでは無いのでは。「こう振る舞ってほしい」という説明するだけでもいいのでは(takanory)

  * 一社PyCon JPとしてのベースのCoCはあってもいいのでは。pycampとかの活動もあるし(terada)
  * CoCは2019でも変更の議論があったが変えなかった。イベントごとに変えてもよいとは思っている。CoCは掲載が必要なのでイベント公開時には必要。CoCが公開されているとスポンサー募集とかのためにサイトを作らなくていいので楽になる(yoshida)

    * PyCon JPの基本CoCはこれで、2020イベントでは追加でこれ、みたいな拡張可能な形にするのもよいのではないか(yoshida)
    * 大変そうだがよさそう(terada)

  * CoCに限った話ではないが、PyCon JPのイベントをやるときに「PyCon JPとしてこういう思いでやっています」ということを話す場所がイベントの最初に20分くらいあってもいいのではないか。人数が急激に増えているのでコミュニティ慣れしていない人もいる(maaya)

PyCon JP 2021
-------------
* https://pyconjp.atlassian.net/browse/ISSHA-1917
* 2021にPiOを使う場合は2020年の1月に申し込みする必要がある(yoshida)
* 2021年4月~2022年3月はPiOコンベンションホールが工事のために使用できない(yoshida)

  * 以降も他の部屋が工事になると思われる(terada)
* 全館とれないことと1.5年前に決定しないといけない悪条件のため、この段階でPiOに決定する必要はない(terada)

  * 同意(takanory, shimizukawa,jonas)
* TODO: 2月が始まったら2021年の方向性について議論を進めたい(terada)

  * 2月からでいいのでnishiの意見を聞きたい(takanory)

予算関係
========
* PyCon JP 2019イベント会計の締め

  * 吉田さんお願いします。
* 2019年度追加予定　・・なしで良いか？

  * 特になし
* 2020年度1月、2月で必要な仮予算

  * PyCamp Caravan 東京分(4万円)
  * Python Boot Camp 2回分(10万円)
  * PyLadies Caravan 1箇所分くらい(8万円）
  * PyLadies Okinawa託児 1回(3万円)
  * 弁護士への相談(10万円)
  * 合計35万円を決定とする。(terada)
  * カンファレンス準備にかかる費用は、カンファレンス予算内に組み込むものであれば、その都度相談すればOK(terada)
* 2019年度の決算処理

  * 清水川さんよろしくお願いします。(2月前半には確定して欲しい(terada))

pycamp状況報告(kobatomo)
========================
* `Python Boot Camp開催一覧 <https://docs.google.com/spreadsheets/d/1VjM7x6k6Cyk0323ZoAHY2lXMV6VyLrn_Bi8mnOiPMb4/edit#gid=0>`_
* `Python Boot Camp予算管理 <https://docs.google.com/spreadsheets/d/1Fcgck7fMl6JpqeEVS7j542LE39ibRmCi3UxzfWhcLuc/edit#gid=1116847018>`_
* 2019年は9回(藤枝、和歌山、福井、山形市、岐阜、沖縄、高知、群馬、福岡2nd)開催済み。
* 開催見込み: 12/7 熊本
* Pycamp予算進捗

  * 2019年12月3日時点 (福岡2nd、熊本 見込み)

    * 予算：510,000円
    * 実績：393,970円(福岡2nd、熊本 除く)
    * 予定：496,303円(福岡2nd、熊本 含む)
  * 詳細は以下スプレッドシートを参照。

    * https://docs.google.com/spreadsheets/d/1Fcgck7fMl6JpqeEVS7j542LE39ibRmCi3UxzfWhcLuc/edit#gid=1116847018
* 2020年 PyCamp 開催見込み：2/8  長崎開催

  * 3月以降の開催場所は見えていない状況
  * つつく都道府県はもうない感じ?(takanory)→あまりない感じ(kobatomo)
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

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamo)
------------------------------------------------
* `PyCamp Caravan実施一覧 <https://docs.google.com/spreadsheets/d/1aLKox2os-_qRUx_zY8o9LsJONFae_o-Rr_DhYwLHn6k/edit#gid=0>`_
* `PyCamp Caravan費用管理 <https://docs.google.com/spreadsheets/d/1aLKox2os-_qRUx_zY8o9LsJONFae_o-Rr_DhYwLHn6k/edit#gid=1381341604>`_
* 沖縄(takanory・yoshi-tsukamo)、北海道(takanory、ryu22e)、名古屋(yoshi-tsukamo)、京都(kobatomo)、島根(shimizukawa)、福岡(terada)に参加済み。
* 今年の出展はすべて終了しました
* 1年やってみての報告ブログを書く予定(yoshi-tsukamo)
* 予算800,000円に対し、807,029円(100.88%)

  * OSC協賛費: 200,000円(税込)
  * スタッフ派遣費: 532,353円(スタッフ手当含む)
  * 備品制作費: 50,710円(税込)
  * 備品送料: 23,966円(税込)
* 来年も継続していきたい

  * 来年度の年間スポンサーは4月スタート(4/1〜翌年3月末まで)
  * 2020/2/21(金)〜22(土)のOSC Tokyo/Springへ出展を計画中

    * 駒澤大学で開催
    * 1,000名規模のイベント
    * PyCampだけでなくPyCon JPの周知をしたい
    * 計2名の参加ができるよう追加予算をお願いしたいです
    * 予算申請 40,000円

      * 33,000円(スタッフ謝礼15,000+税 2名分)
      * 2,000円(交通費2名分、参考：東京-駒澤大学駅片道360円)
      * 5,000円(備品送料往復分 静岡-東京)
    * 関連チケット

      * https://pyconjp.atlassian.net/browse/ISSHA-1927
  * 名古屋、北海道、京都、島根、広島、福岡、KOFが現時点での出展候補
* 東京のOSC参加者にPyCon JPを知ってもらってスタッフとかProposalとかも知ってもらえて良いのでは(Hirao)

PyLadies関係報告(maaya)
=======================
* PyLadies Caravan進捗

  * 実施実績：5拠点済み　京都、沖縄、福岡、愛知、愛媛
  * 実施予定：2拠点調整・準備中　北海道、秋田、広島

    * 北海道　12/21（土）開催確定

      * 会場を借りる費用は3,000円程度の見込み
    * 秋田　実施調整中

      * 2020年2〜4月あたりを目処に日程調整予定
    * 広島　3/14（土）開催ほぼ確定

      * 広島caravan with WiDSとのコラボ予定
  * 予算消化率

    * https://docs.google.com/spreadsheets/d/1X-RA-wPS1crRaZDy4zj593f6-MoGcfniPC3vnxP1fAM/edit?usp=sharing
    * 12月末見込→ 43%（予算80万、実績34.6万）
* PyLadies Okinawa託児所

  * 実施実績：4回（予算計画時の予定回数は6回）
  * 託児予算消化率

    * https://docs.google.com/spreadsheets/d/1N7nw3D-3-PMzPgy8KAYibvf4vQBSnC1ERRwzGMt0Y4w/edit?usp=sharing
    * 12月末見込→ 50%（予算22.3万、実績11.1万）
* 来年度（2020年度）について

  * PyLadies Caravan

    * 継続して実施を希望（概算：5拠点、35万）
    * 未開催エリア（東北、北陸、中国）もしくは2nd要望地域での開催

      * 九州：熊本での開催要望もあり
      * 東海：愛知リージョン立ち上げ？も視野に入れた開催を検討
      * 四国：香川開催要望あり（現地スタッフも見つかっている）
      * 北海道：12月に間に合わなかったが、北海道大学と連携案
  * PyLadies Okinawa 託児所

    * 継続して実施を希望（概算：6回、20万）
    * 託児所設置における汎用メモははやく作ります（冬休みの宿題）
    * https://docs.google.com/document/d/15AQTwc_aErb7mjMHexotbNxFVtlcs1nS7yXuHHijvlg/edit?usp=sharing
  * その他PyLadies関連

    * PyLadies 日本リージョンのフォローの仕方検討

      * 1つはZoomのオンラインで運営を相談するのはとてもよかった(takanory)
      * イベントについてはサテライト(動画中継)とかをやるとどうかなと思った(takanory)
    * PyCon USに参加してPyLadies本家と連携したいな

pycon.jp OSサーバー移行(yoshida)
================================
* https://pyconjp.atlassian.net/browse/ISSHA-1894
* \*.pycon.jpのlet's encrypts20190612障害対応の記録 https://pyconjp.atlassian.net/browse/ISSHA-1669

  * 定期更新ができておらず3ヶ月毎(6月、9月)に障害となっている
  * 現在の証明書 https://pycon.jp/2018/
    * 2019/9/10-2019/12/9
* 過去のPyCon JPサイトを静的化 https://pyconjp.atlassian.net/browse/ISSHA-1632
* イベントスタッフから個人的に発注する方向で進める(yoshida)
* 主担当: yoshida

  * `2020以降のpycon.jpサイト要件案 <https://docs.google.com/document/d/1ukaLI4GzCsRvdlpzHqz6n2nPkoavn-mnzYAo63VAntA/edit>`_
  * https://pyconjp.atlassian.net/browse/ISSHA-1894
  * 上記要件をもう少し詰めて見積を @rmanzokuに依頼したい
  * 1月中に見積をもらいたい、２月の一社MTGでの2020予算に計上

ツールの活用・運用等
====================

Zapier有料版について (nishi)
----------------------------
* ZapierのStarter Plan(20枠・複数ステップ設定可能)を、PyCon JP 2020予算で申し込みました。
* 枠がまだ余っているので是非使って下さい。枠が埋まったら議論。

ZOOMアカウント(takanory)
------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-1923
* ビデオミーティングで利用する予定。振り込みしたので、TechSoupからの連絡待ち(takanory)

Google for Nonprofits(takanory)
-------------------------------
* https://pyconjp.atlassian.net/browse/ISSHA-1911
* https://pyconjp.atlassian.net/browse/ISSHA-1912
* Nonprofitsは取得済み。12/14(土)とかに作業してみる(takanory)

  * メールアドレスとか共有ドライブに移行とかやりたい(takanory)

コミュニティー支援
==================

イベント/コミュニティサポートプログラム(nishi)
----------------------------------------------
* 進捗・今後の予定

  * 主な部分を＠intelに引き継ぎました。nishiも引き続き担当。

Python地域交流オンライン座談会(intel)
-------------------------------------
* https://pyconjp.connpass.com/event/155287/
* 2019年11月28日第1回を開催
* 概要

  * 地域Pythonコミュニティの繋がりや交流をもっと深めていくための座談会
* 雜感

  * 参加は約15名程度。各地域のコミュニティーオーガナイザーが集いました。
  * 各地域オーガナイザーの相談の場になったところは非常に良いと思ったし、地方PyCon開催経験者が、未開催地方のPyCon mini 開催のアドバイスをして良いと感じました。
  * 事前議事録作成や当日の段取りをtakanoryさんにサポートしていただいたので、いい感じに第1回を開催することができた。
  * **定期開催していきたいのでまた1月下旬に第2回を開催したい**

地域PyCon等の支援について(takanory)
-----------------------------------
* PyCon mini Shizuoka 2020

  * https://shizuoka.pycon.jp/
  * 2020年2月29日(土)
  * Blogとドメインサポート
* PyCon Kyushu 2020 in Kumamoto

  * 2020年5月23日(土)
  * https://pyconjp.blogspot.com/2019/11/pycon-kyushu-2020.html
  * Blogとドメインサポート

APAC関連(terada)
----------------
* 2020はマレーシアに決定した

  * Target Location: Kuala Lumpur, Langkawi, Kota Kinabalu
  * Target Date: 18 - 19 July, 5 - 6 Sept 2020, 10 Oct - 11 Oct 2020
  * 詳細は未定。
  * 決定にあたり、タイからのプロポーザルを後で受け取ったが、マレーシアからの猛烈な反対がでて、タイのプロポーザルが撤回された。
  * ツアーやりたいが、PyCon JP 2020と近い時期になりそう(terada)
* イクバル氏(PyCon JP, PyCon MY立ち上げ)を中心に、以下が動いている

  * Beng Keat(PyCon Singapore立ち上げ)が引退をほのめかしている
  * 新たなコミュニケーション手段としてSlackを提案されたが、様々な意見が出た
  * 地域の代表者は1名にしたいという旨のやりとりがされている
    * teradaがやる。(terada)

コアスタッフ制度(takanory)
==========================
* https://pyconjp.atlassian.net/browse/ISSHA-1490
* 2020年本気出す(takanory)

法人名変更
==========
* 英語名称の変更

  * TODO: 2月に向けて準備を進める(jonas) https://pyconjp.atlassian.net/browse/ISSHA-1828
  * 行政書士さんとやりとりする(terada)
  * 英語名: PyCon JP Association
* 日本語名称の変更

  * 継続議論中

    * 一般社団法人PyCon JP Association はどうだろう。(terada)

      * 通称: PJA << 登記しない。
      * メールで書いたりするときに便利では。(terada)
      * 定着しないのでは？ (terada)
      * 通称は、別途議論する。
      * 一般社団法人PyCon JP Association で登記方向で社員総会に議案を出す。(terada)
  * 前回のMTG振り返り

    * 「一般社団法人PyCon JP」より「一般社団法人Python JP」とういう名前が一社の現在のミッションに合ってると思います。「一般社団法人PyConJP」＝「今年のPyConのスタッフリーダー」だと思う人に何人にも会いました。そうして一社はもPyCon以外の活動も色々サポートしているから、「一社＝PyCon」より「一社＝Python」と思われたいです。
    * 外から見ているとわからないという意見がある(yoshida)
    * 最終的には調整となると思う。名前を変えた場合外からどう見えるかということもある(shimizukawa)
    * -0: 変えるほどのメリットがあるのか?(terada)
    * -1: PyCon JPの名前はある方が外で話がしやすい(takanory)
    * +1: PJAとか通名はPyCon JP Associationだけにするはありでは(terada)

      * まぁ、ありかと(takanory)
      * よさそう(jonas, yoshida)
    * PJAと呼ぶのは、定款で定める必要はない(shimizukawa)
    * 呼び名は継続議論とする

その他
======
* サービス・リソースの管理(terada)

  * https://pyconjp.atlassian.net/browse/ISSHA-1896
  * 懸念はどれを誰が契約しているか不明になる(terada)
  * お金をどこから払っているかが不明になる(terada)
  * サービスの管理手法として1passwordいれる?(takanory)
  * **TODO**: まずは情報をとりまとめてほしい(terada→yoshida)
* 来年度に向けて、活動の定量的な評価指標を作れないか？(terada)

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
* 弁護士との契約について(terada) https://pyconjp.atlassian.net/browse/ISSHA-1470

  * スポンサーについてはPyCon JP側からの許諾書を提出することも考えた方が良いのではないか(terada)
  * 他のカンファレンスはどうしているのかなぁ(takanory)

    * JJUGでは契約のやりとりをして、間に合わないと終了している(maaya)
  * 金額を積んででも、弁護士に相談しても良いのでは無いか？ 例えば、20万円くらい(yoshida)
  * 日本語、英語で許諾書を作る (契約書ではなく) のはどうだろうか？(terada)
  * 10万円の予算で進める

    * (yoshida / terada で相談する)

次回ミーティング
================
* 日時: 2020年1月28日(火) 19:30から21:30

  * https://pyconjp-staff.connpass.com/event/xxxx
* 主な議事

  * 理事改選

