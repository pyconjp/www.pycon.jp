===============================================================
 2020年9月25日(金) 一般社団法人PyCon JP Association運営会議#41
===============================================================

* 日時: 2020年9月25日(金) 19:30-21:30

  * https://pyconjp-staff.connpass.com/event/181858/
* 場所: Zoom
* 理事: terada, takanory, jonas, yoshida, shimizukawa
* オブザーバー: ryu22e, nishi, yoshi-tsukamo, maaya, peacock, kobatomo, kanan, iqbal

.. contents:: 目次
   :local:

課題のレビュー
==============
* `一般社団法人PyCon JPの課題 <https://pyconjp.atlassian.net/issues/?filter=11500&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20%3D%20%E4%B8%80%E8%88%AC%E7%A4%BE%E5%9B%A3%E6%B3%95%E4%BA%BA%20ORDER%20BY%20due%20ASC%2C%20updated%20ASC%2C%20component%20ASC>`_

PyCon JP
========

PyCon JP 2020 (nishi、中、報告)
-------------------------------
* PyCon JP 2020開催完了

  * 大きな事故等もなく無事終了。

  * みなさん、ご協力ありがとうございましたm(_ _)m
  * カンファレンス(8/28-29)参加者に関する情報

    * Zoom参加権[connpassチケット等]数: **631**

      * 一般参加者、スピーカー、スタッフ、スポンサー提供チケット等
    * YouTube Live 2日間ユニーク視聴者数: **2,988**

      * YouTube Analyticsによる値
      * 集計期間は、2020/8/27 17:00JST - 8/29 16:59JST

        * 集計単位の基準タイムゾーンが公開されていないがおそらくPSTのようなので(少なくともJSTではない)、JST換算では上記の期間での集計となる
      * ※YouTube Analyticsによるchannel全体の集計値(各日/各動画のユニーク視聴者数の合算ではなく、両日該当期間設定した際のchannel全体ユニーク視聴者数(2日視聴した人も1人とカウント))。
    * その他集計情報 [外部非公開資料]

      * https://docs.google.com/spreadsheets/d/1GMhuDpdXN4kIeyUd7ZByohFi-3GheOpJXM75mhPGCno/edit#gid=0
* 収支見込

  * 結果的には200万円近くの黒字が出る見込み
  * 予算・収支シート(確度S+Aの値が最終値に近い): https://docs.google.com/spreadsheets/d/1s2mzwGCuVosBkfg7xF_MEtxuFal_D0Q1qc7c8fj410g/edit#gid=650187930
* 会期後タスクの状況

  * 各チーム残タスク

    * [完了] 残タスク確認会
    * プレゼント企画の商品発送系タスク
  * [完了] 各チーム・全体振り返り(KPT整理・共有)

    * KPT: https://docs.google.com/spreadsheets/d/1zyAM2KruTaHacmywD-seX0ASQV_BMIVgE4lYbfRrt1w/edit#gid=584506076
    * 要点

      * 初のオンラインカンファレンスをなんとか準備し、無事開催できたことが良かった
      * **個人への負荷が非常に高かった**。特定個人への依存が高く、組織的なフォローアップが弱かった。

        * 新規参加スタッフがいくつかの主要なタスクを担当し、またリーダーロールでも活躍
        * 経験者スタッフが、チーム間をまたぐ視点を持ち、タスクを拾ったり、ほかスタッフをサポートしたり活躍
      * (ある時点でできそうであっても)スタッフリソースは安定しないと考えられるので、2021以降はその時のスタッフの意向に関わらず、専門性の高い各タスクを外注することを前提として動くことを強く推奨

        * 強く推奨: 各デザイン、Website制作、配信関連(2020も外注)
        * 予算に見合う方法を模索: スポンサー対応、問い合わせ対応
        * 英語
      * スタッフの「やりたいこと」を制限してでも、「**開催スコープの拡大阻止・途中での縮小化**」を行う必要があることを強く認識
    * 全体振り返り開催をもって、PyCon JP 2020の全体活動は終了
  * カンファレンス以外(Sprint/Tutorial/YouthCoderWorkshop)の参加者・視聴者情報の集計
  * ナレッジ整理・マニュアル整備

    * 情報集約先を議論中
    * Confluence濃厚(既存の情報も移植)
  * 会計担当(@ds110)タスク → ds110が対応不可とのことで、後任分担中

    * 残支払い対応
    * 残入金確認対応
    * 予算/PL表の最終化
    * 立替精算(nishiに集約済み)
    * (年末頃以降)収支情報の整理・公開
* 質疑応答

  * スポンサーの反応どうですか?(たかのり

    * スポンサーしてよかったという声はあった。ブースへの集客は工夫の余地がありそう。ブースのツアーはよかったとのこと。(nishi
  * スタッフの2021への継続の意識とかどうですか?(takanory

    * 振り返り会で「2021も自分がスタッフとして参加する」という視点で発言してくれている人が30%~40%くらいいた感じ(nishi
  * Python Charity Talks in Japanのtipsで活かせたものありましたか?(kobatomo

    * Zoom Webinarでkumagaiさんの知見を活用した(peacock
  * コンテンツとかデザイン、システムの負荷が高かった。外注できるものは外注したいし、1人の負荷を減らすことを強く感じた(peacock

    * これはオンラインイベントとはあまり変わらなそうだが(takanory
    * スタッフ活動がオンラインだったこと、経験者が少なかったこと、コロナ関連で経験スタッフが捕まえられなかったとかが原因として考えられる(nishi
    * 2021開催に向けては、スタッフのフルオンラインは多少はゆるくなりそう(takanory
    * 逆にオンラインなので、地方のスタッフもフラットでよかった(nishi
  * Confluenceであれなんであれ、ぜひまとめてほしい(terada

    * 情報を公開してほしい(takanory

PyCon JP 2021(terada、高、相談)
-------------------------------
* 座長への立候補者がいたが、terada、jonasでヒアリングした。スタッフ経験などがほぼなく、立候補を取り下げてもらった
* 引き続き2021の座長募集のディスカッションを行う。
* 一番いいのは今年のメインどころのスタッフから「立候補or nishiからの強い推薦」があること(takanory
* 次回運営会議まで待って、立候補がないときに次の方策を考える?(terada

  * 開催しない、座長経験者が座長をするとか?(terada
  * 3月末くらいには日程が決まっていてほしいので、年内は座長の募集をして、出なかったら調整でよいと思う(yoshida
* 一旦募集締め切られて候補者がいなかったが、立候補者があったら先着順?(nishi

  * nishiさんが推薦する人で2020のスタッフなのであれば、基本的に通るはず(takanory
* 地方開催について

  * https://pyconjp.atlassian.net/browse/ISSHA-2092
  * 2021の地方開催をPyCon JP Associationから声を掛けるのはないかなと思っています(takanory
  * 東京でも地方でも開催できる、という状況になったときに地方での開催を打診する方がよいのではないか(terada
  * リスクを理解した上で、立候補、開催してくれるならありがたいし、支援はする(shimizukawa

PyCon JP 2021以降の座長の募集時期(terada)
-----------------------------------------
* **TODO**: 募集の段取りを進める(terada

PyCamp、PyLadies関連
====================

Pycamp状況報告(ryu22e、低、報告)
--------------------------------
* 7月以降の開催場所状況

  * 今のところ開催が決定している地域はない。
  * 9月 神奈川県鎌倉市から現地スタッフ立候補者2名あり（平原さん・樋口さん）
* 「Python Boot Campその後」ブログの進捗状況(@ryu22e)

  * 第１回(飛騨高山Pythonの会)公開: https://pyconjp.blogspot.com/2020/06/after-pycamp-hidatakayama-python-kai.html
  * 第２回(岡山Python勉強会)公開: https://pyconjp.blogspot.com/2020/08/after-pycamp-okayama-python-benkyokai.html
  * 今月・来月に以下も公開予定

    * すごい広島 with Python
    * Shonan.py
    * Shingen.py
* 9/29(火） 20:30 - Python Boot Camp オンライン相談会 2回目を開催するよー。(@kobatomo)

  * https://pyconjp.connpass.com/event/188776/
  * 今回は、OST(Open Space Technology)形式で進めます。mural(https://www.mural.co/)使って話のネタを当日決める。という実験をします。

OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、低、報告)
------------------------------------------------------------
* 最近の活動

  * OSC 広島オンライン(9/19)

    * セミナーとミーティング(講師：清水川)
    * ミーティングへの参加者が1人しかいなかったので、pycampの紹介をして、質問をもらって答えたりした(shimizukawa
* 今後の活動

  * OSC Fallオンライン(10/24)

    * セミナーとミーティング(講師：たかのり)
  * OSC 福岡オンライン(11/28)

    * セミナーとミーティング(講師：寺田)
* 来年1月のOSC大阪まで予約していた会場をキャンセルしたと聞いたので、最低でもそこまではオンラインでの開催となる見込みです

PyLadies関係報告(maaya, 低, 報告)
---------------------------------
* PyLadies Japan チャリTシャツオンライン販売開始しました

  * https://fril.jp/shop/10f1aa16b6adee42de1f23eb7d44737f
  * ラクマを選んだ経緯とかチームでの販売フローなど色々知見があるのでどこかでブログにしようと思っています
* 年内のCaravanツアーは断念。冬を超えてから状況見て判断

コミュニティー支援
==================

イベント/コミュニティサポートプログラム(takanory、低、なし)
-----------------------------------------------------------
* とくになし

Python地域交流オンライン座談会(takanory、低、報告)
--------------------------------------------------
* 10月23日(金)に静岡の佐野さん発案で「のみpy」をやることになった

  * https://pyconjp.connpass.com/event/188778/

地域PyCon等の支援について(takanory、中、報告)
---------------------------------------------
* PyCon mini Hiroshima

  * https://hiroshima.pycon.jp/2020/
  * 日付: 10月10日(土)
  * 会場: オンライン
  * サブドメイン以外はとくにサポート依頼はなさそう
  * Blogで宣伝とかぜひしてほしい(たかのり
* SciPy Japan

  * https://www.scipyjapan.scipy.org/
  * 日付: 10月30日(金)~11月2日(月)
  * 会場: オンライン
  * トーク、レビュアー募集などBlogでの宣伝協力する予定

    * そういえば、とくに連絡が無いなぁ

海外コミュニティ連携
====================

Python商標問題(terada、中、報告)
--------------------------------
* PSFのEwaさんから連絡があり、顧問弁護士と各種進めているとのこと
* TMチームのMarcは、PyCon JP Associationとの連携や何か進めることが有るのではないかと確認を進めている

PSFへの寄付イベント(terada、中、相談)
-------------------------------------
* https://pyconjp.connpass.com/event/177586/
* 振込用の口座申請中。手続きが面倒で進められていない
* 別の方法で振り込むか、口座申請を頑張るか考えたい。

  * ジャパンネット銀行または楽天銀行からであれば、手数料は多くなる。Go Remitは手数料が安いが手続きが大変。(てらだ
  * 楽な方でいいと思います(しみずかわ、たかのり

APAC関連(terada、低、報告)
--------------------------
* 9月12日から20日(土日 x 2回)で、APACオンラインが開催された。

  * https://pycon.my/pycon-apac-2020-event-calendar/
* PyCon APACのチームとしてJapanでも宣伝とかはあまり手伝えていない(てらだ
* PyCon APACのJamesから依頼があり、PyCon JP 2020の報告ビデオを作成した。PyCon APAC開催中に幕間で再生してもらった

  * ビデオ作成 https://pyconjp.atlassian.net/browse/ISSHA-2169

    * https://www.youtube.com/watch?v=5fZs3JG7eN4
  * 支払い https://pyconjp.atlassian.net/browse/ISSHA-2170

    * ビデオ作成に10万円の予算を使った
* APAC2021の開催地募集を開始した。いまだに立候補地なし

  * マレーシアは立候補しているが、追加の項目が出ていない(Iqbal
  * 現地開催できそうならマレーシアに開催してほしい(てらだ、たかのり

APAC・JPロゴ関係(terada、中、相談)
----------------------------------
* PSFでトレードマークチームがボランティアを募って動き始めた。
* イクバルさんが活動を始めている
* APACやJPロゴはPSFの規定違反になるかもしれない。

  * https://drive.google.com/drive/u/0/folders/1qkKy6dcljPQNxBaRgFmiC8NhTdzmhCFo
* イクバルさんとして、知ってしまい、動いている以上、何かしらの動きをしたいがどうしたほうが良いか相談したいとのこと。
* PyCon ID 2019のロゴはグレー、PyCon APACのロゴはアウト(iqbal

  * https://twitter.com/pyconapac
* ものを作っていないのであればロゴを変えてほしい(iqbal
* 形をそのままにして色を変更するのはOK(iqbal

  * PyCon JP 2020はOK
  * 一般社団法人PyCon JP Associationは多分OK
  * https://www.python.org/psf/trademarks/#derived-logos
* PyCon Indonesia 2019(サメとワニ)、PyCon Thailandはグレーだと思う
* **TODO**: PyCon JP Associationのロゴについて問い合わせる(terada
* 今後のPyCon JPロゴの扱いについて、周知が必要そう(iqbal、terada

  * PyCon miniイベントを支援する条件として「CoCとロゴの扱いの準拠」を入れるとよいのでは(iqbal
  * **TODO**: 継続議論する(てらだ

APACブース in US PyCon(terada、中、報告)
----------------------------------------
* **TODO**: ロゴデザインの3万円は「APACに寄付してほしい」とのこと。すすめる(terada

  * マレーシアに寄付する

その他
======

運営メンバー制度(takanory、低、報告)
------------------------------------
* いい加減本気出す

各地のイベント中止に対して(terada、低、なし)
--------------------------------------------
*

弁護士との契約について(yoshida、低、なし)
-----------------------------------------
*

法人名変更(terada、 中、報告)
-----------------------------
* **TODO**: 9末を超えてから銀行の名称変更をする(teraeda

pycon.jp OSサーバー移行(yoshida、中、報告)
------------------------------------------
* タスクの確認する

2020年の活動(takanory、中、議論)
--------------------------------
* リモートイベントの運営ノウハウ的なのを共有したい気もする(takanory

  * オンラインイベントとしてやりたい(takanory
  * 8月3日実施済み https://pyconjp.connpass.com/event/182075/
* Pythonを広めるためになにができるんだろう(takanory

  * Python Charity Talks的なことをまたやる(terada
  * オンラインチュートリアル(terada
  * LT大会(shimizukawa

    * 準備が大変じゃないものがいい(shimizukawa
  * PyCon JP知らない人につながりたい(takanory

    * 勉強したい人にリーチする感じ(terada
    * チャンネルが大事なのでは(shimizukawa
    * start python clubとかはその層にリーチできている感じがする(takanory

サービス・リソースの管理(yoshida、低、なし)
-------------------------------------------
*

次回
====
* 作業日: 10月15日(木) 19:00-21:00

  * https://pyconjp-staff.connpass.com/event/190302/
* 運営会議#42: 11月25日(水) 19:30-21:30

  * https://pyconjp-staff.connpass.com/event/190301/

TODO
====
* `ISSHA-2176 <https://pyconjp.atlassian.net/browse/ISSHA-2176>`_ PyCon JP Associationのロゴについてレギュレーション違反がないかPSFに問い合わせる(jonas
* `ISSHA-2175 <https://pyconjp.atlassian.net/browse/ISSHA-2175>`_ PyCon APACロゴの制作費30,000円をマレーシアに寄付する(terada
* `ISSHA-2093 <https://pyconjp.atlassian.net/browse/ISSHA-2093>`_ 法人名が変わったので、9末を超えてから銀行の名称変更をする(terada

