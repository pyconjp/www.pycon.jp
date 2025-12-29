==============================================================
 2022年8月1日(月) 一般社団法人PyCon JP Association運営会議#54
==============================================================

* 日時: 2022年8月1日(月) 19:30-21:30

  * https://pyconjp-staff.connpass.com/event/248749/
* 場所: Zoom
* 参加者

  * 理事: terada, takanory, jonas, yoshida, shimizukawa
  * オブザーバー: kobatomo, maaya, yoshi-tsukamo, selina, peacock, nikkie, peacock, ryu22e


課題のレビュー
==============

* `PyCon JP Association(一社のみ) <https://pyconjp.atlassian.net/issues/?filter=11500>`_ の課題一覧
* `PyCon JP Association(一社以外) <https://pyconjp.atlassian.net/issues/?filter=15948&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20in%20(EMPTY%2C%20%22Pycamp%20Caravan%22%2C%20%22PyCon%20JP%20TV%22%2C%20%22Python%20Boot%20Camp%22)%20ORDER%20BY%20due%20ASC%2C%20component%20ASC%2C%20updated%20DESC>`_ の課題一覧

PyCon JP
========

PyCon JP 2022(selina、高、報告)
-------------------------------

予算について
~~~~~~~~~~~~
* `予算案2022 <https://docs.google.com/spreadsheets/u/2/d/1t4QvgPNbRVXkQXjrQiY7PodS96Kn4A53tlUdy8q8mGQ/edit#gid=1830081735>`__ 

.. list-table::
   :header-rows: 1

   * - 予算確度別収支
     - 支出
     - 収入
     - 収入 - 支出
   * - S(確定: 執行済・発注済)
     - 3,638,791
     - 0
     - -3,638,791
   * - S + A
     - 16,425,295
     - 22,330,000
     - 5,904,705
   * - S + A + B
     - 23,613,860
     - 26,290,000
     - 2,676,140
   * - S + A + B + C
     - 30,006,499
     - 28,560,000
     - -1,446,499

* 金額確定のものはSにしている。
* その他、内容によって、A〜Cのランク決めを調整済み

  * Cがパーティー食事ありの全部やる想定
  * パーティを行う際、パーティスポンサーを募る可能性あり。
* 先日MTG行い、チケット金額が決定した。

  * 通常: ¥12,000 * 想定500
  * ビジネス: ¥18,000 * 想定50
  * パトロン: ¥40,000 * 想定10
  * 学生: ¥2,000 * 想定50
  * オンラインのみ: ¥2,000 * 想定200
* ランチは含んでいる?(takanory

  * Yes(selina
  * パーティーを行う場合は、チケット代をあげるのはだめなのか?(takanory

    * パーティー券を別にするという考え方もある(selina
    * 同じチケット代金のままパーティーを含めるとかは無理にがんばらなくていいと思う(takanory

スポンサーについて
~~~~~~~~~~~~~~~~~~
* Diamond、Platinum、Gold、Silver一通り集まり一安心

  * `PyCon JP Blog: PyCon JP 2022 スポンサーシップ募集経過報告 <https://pyconjp.blogspot.com/2022/07/pyconjp2022-sponsorship-ja.html>`_
  * スポンサー企業の一覧は上記ブログを参照ください。
* ブースの数により、Goldスポンサーを調整する必要あり。
* コロナの関係でブース数に限りがあり、後半でお申し込みしたGoldスポンサーには事情を話してSilverに変更してもらう。
* 第一次申し込みしたGoldはブースありで確定。2次締め切り後は順次審査していく(yoshida

キーノートについて
~~~~~~~~~~~~~~~~~~
* 日本語：西内 啓さん（面談済み）
* 英語：Mark Shannonさん（メール回答済み）
* 特別出演案：デジタル大臣牧島かれんさん（調整中）
* 7月10日にトーク採択者会議を行い、下記の速報を出した

  * `PyCon JP Blog: PyCon JP 2022 トーク採択会議を行いました & トーク採択速報 <https://pyconjp.blogspot.com/2022/07/pyconjp2022-talk-adoption-bulletin-ja.html>`_
  * 今年は合計120本のプロポーザルが提出され、その中から45本を選出した。
  * 全体の採択率は37.5%
  * 言語別の内訳は日本語が40.26%(31/77本)、英語が32.56%(14/43本)

デザイン関連について
~~~~~~~~~~~~~~~~~~~~
* スタッフが配るステッカー類を事前に発注
* Tシャツ、冊子等の発注期限があるものを優先にスケジュール立てて進めている。
* 本番サイトはシステムチームと連携して進めている。
* 冊子はどのくらいのものを作る想定で、いまどのくらい進んでいる?(takanory

  * https://www.figma.com/file/bMJB2KMRwEiTf0Abz8hke4/PyCon-JP-2022-Booklet?node-id=0%3A1
  * 12ページくらいで台割りを決めている(yoshida
  * 結構大変なので、がんばらなくてもいいと思う。炎上しないといいですね(takanory

会場について
~~~~~~~~~~~~
* TOC有明コンベンションホール
* 8月26日(金)に再度下見に行く。

  * `PyCon JP 2022 会場下見#2 - connpass <https://pyconjp-staff.connpass.com/event/256373/>`_
* 開始まで3ヶ月を切っているので、キャンセルの時は要注意(キャンセルするということではなく)
* 9月14日はカンファレンスの1ヶ月前までなので、余裕を持って8月お盆過ぎまでにオフライン開催の決定を決める。（問題なければ開催）
* もしも、オフラインの開催が厳しそうだったら会場の一部キャンセルを行い、オンライン開催を行う。（配信場所は必要）
* 託児所→natsuさん担当で進めている。寺田さん署名等

  * https://pyconjp.atlassian.net/browse/ISSHA-2613
* 会場パーティ、食事など、natsuさん含め、コロナ状況を見ながら進めて行く。
* オフラインで開催されることを期待している。「こうなったらオフライン開催をやめる」ということをあらかじめ決めておくとよいのでは(terada

  * 例えば「緊急事態宣言が出たらやめる」とか?(takanory
  * 「緊急事態宣言が出たら議論する」程度でもよいのでは(terada
  * 宣言が出たら議論するでよいと思う(yoshida
* 登壇者が現地参加したくないとかの配慮はあるか?(nikkie

  * オンラインで発表できるようにする配慮は検討している(selina

オンラインの配信について
~~~~~~~~~~~~~~~~~~~~~~~~
* 基本は現地オフラインだが、遠方でもトークが見えるようにYoutube配信を行う。
* トーク採択者が諸事情で会場に来られない場合は、Zoomでの参加を行う。
* オンラインの参加チケットを販売するが、Youtubeで動画を視聴しつつ、質問に答える権利が付与されるものとする。

会場（NOC）について
~~~~~~~~~~~~~~~~~~~
* チームリーダーをPanakumaさんとし、Shinonomaryさんがサポートしながら進めている。
* 座長として、構成の仕組みはわからないのでお任せしている。経費などの予算が絡む場合は都度相談して進めて行くこととしています。

チーム編成について
~~~~~~~~~~~~~~~~~~
* そろそろ、現地会場案内チーム（のようなもの）はあった方が良いでしょうか。各チームのタスクはタスクを持っているので、デパートでいう1Fの案内係のようなチームです。

  * コンテンツチームとかで当日タスクがない人がやります(peacock
  * コンテンツチームは当日は司会進行とかで忙しいのではないか?(terada
  * 受付の近くには誰かはいてほしいと思う(takanory
  * ヘルプデスクのような感じはいてくれるとよさそう(terada

海外からのゲスト用ビザ取得(重要)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ビザ取得を希望している参加者？？からメールで問い合わせがきた
* 過去の手順書: 
* 2022年7月31日現在の状況

  * 観光等のビザ無し入国がほぼできない。
  * ビザ取得には、「招へい状」が必要
  * 招へい状には2種類あり、「身元保証なし」「身元保証あり」
  * 身元保証ありでないとビザ取得できないのではないかと思われる
  * ビザ申請には、「厚労省のERFS」も必要ではないか？＜結構面倒
  * `国際的な人の往来再開による新規入国のための査証（ビザ）の申請｜外務省 <https://www.mofa.go.jp/mofaj/ca/fna/page22_003381.html>`__

    * 6月15日に更新されたらしい(takanory
    * 入国者健康確認センター(ERFS)は変わってなさそう(takanory
* どのレベルの参加者に対してどのような対応を行うか？

  * キーノートなどの招待者

    * ↑ここは招待するでよさそう(terada
  * 一般スピーカー

    * ↑ここが議論のポイントでは(terada
  * スポンサーブース担当

    * ↑ここはスポンサー企業でまきとってほしい(takanory
  * 参加者

    * ↑ここは対象外(takanory
  * PyCon JPの場合は「（1）商用・就労等の目的の短期間（3か月以下）の滞在者」のパターンだと思う(takanory
* 今まではキーノートスピーカーには出していた(terada
* 行政書士に頼むのはありだと思う(terada
* 対象は最大14名(terada

  * 会社で呼べるなら会社の方で呼んでもらった方が楽(terada
* 一般スピーカー、キーノート、招待者はVISAの発行をサポートするで進めましょう(terada

  * 行動予定表を出さないといけない。先に飛行機とホテルを出さないといけない(terada
  * まずはスピーカーのリストを作って、日本の会社に依頼できる人は会社に依頼して、それから動く感じかなと(takanory
  * スピーカーの実績はGitHubなどで確認できるようにしてほしい(terada

その他
~~~~~~
* 次回の全体MTGは8月9日(火)20:00〜

  * `PyCon JP 2022 スタッフ全体MTG#8 - connpass <https://pyconjp-staff.connpass.com/event/256236/>`_
* 現地スタッフの案内準備を徐々に行う

PyCon JP 2021(nikkie、低、報告)
-------------------------------
* （7月着手となりましたが）残タスクなくなりました🙌

  * おつでした!!(takanory
* https://github.com/pyconjp/tasks-2021-planning/issues はアーカイブ済み

PyCon JP 2023(yoshida、低、報告)
--------------------------------
* TOC有明下記で仮押さえ済

  * ２０２３年１０月２６日（木）～２９日（日）
* **TODO**: キャンセル料、時期を確認する(yoshida
* PyCon JP 2023 座長募集(terada

  * PyCon JP 2022 開催1ヶ月前に実施するか？

    * TODO: 9月に座長募集する(terada)

PyCamp、PyLadies関連
====================

PyCamp状況報告(ryu22e、低、報告)
--------------------------------
* 運営メンバー: ryu22e、kobatomo
* `Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP <https://www.pycon.jp/support/bootcamp.html>`__
* 8月以降の開催予定

  * `佐賀（5月28日） <https://pyconjp.connpass.com/event/244411/>`__ →終了

    * 講師: shimizukawa
    * 現地スタッフ: malo21st, eguchi
    * 担当コアスタッフ: ryu22e
    * TA: 2名
    * 一般 10名、学生6名
  * `広島 2nd（7月9日） <https://pyconjp.connpass.com/event/248048/>`__ →終了

    * 講師: takanory
    * 現地スタッフ: isabisi1484, hiromizoshita
    * 担当コアスタッフ: kobatomo
    * TA: 6名
    * 一般 3名、学生9名
  * `静岡県沼津市（9月3日） <https://pyconjp.connpass.com/event/251468/>`__

    * 講師: arai
    * 現地スタッフ:hrs.sano645 , yoshi-tsukamo 
    * 担当コアスタッフ: ryu22e
  * 新潟2nd（9月17日）

    * 講師: terada
    * 現地スタッフ: wutali
    * 担当コアスタッ: kobatomo
* その他

  * ランディングページ、nikkieさんに作っていただきました！ nikkie++

    * https://github.com/pyconjp/pycamp.landing_page
    * GitHub PagesのCustom domainでpycamp-lp.pycon.jpの割当をお願いします

      * https://github.com/pyconjp/pycamp.landing_page/settings/pages
    * **TODO**: チケットでドメイン設定の依頼をください(takanory

      * チケット作りました(ryu22e)→ https://pyconjp.atlassian.net/browse/ISSHA-2640


OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)
------------------------------------------------------------
* 運営メンバー: yoshi-tsukamo
* 参加済み

  * 6月25(土) 北海道

    * Azumaさん＆Peacockさん参加予定
    * 2名とも体調不良によりキャンセルとなりました
  * 7月29(金)〜30(土) 京都

    * chiakiさんが参加
    * 17時からのLTでPyCon JP 2022の宣伝
* 今後の予定

  * 9月3日(土) ODC

    * LT枠で参加希望があればぜひ
    * PyCon JP 2022の宣伝などはどうか?(yoshi-tsukamo
  * 10月1日(土) 広島

    * Murakamiさんが参加希望出してくれています
  * 10月28(金)〜29(土) Fall

    * ミーティング枠で再びpycamp相談会やるのはどうでしょう？

      * 今年のpycamp関係者に入ってもらうなど
    * 10月29日は別件でNG(terada, takanory, shimizukawa
    * OK(ryu22e, kobatomo
    * araiさんにも打診するといいかも(takanory
  * 11月 福岡
  * 2023年1月 大阪
  * 2023年3月 Spring

PyLadies関係報告(maaya, 低, なし)
---------------------------------
* `ISSHA-1678 <https://pyconjp.atlassian.net/browse/ISSHA-1687>`__: 公開のタイミングを完全に見逃してしまっていてどうしようかなとなっています
* 8月6日 caravan 愛媛行ってきます。現在参加者5名(うれしい

  * `[オフライン] PyLadies Caravan in 愛媛 リターンズ! - connpass <https://pyladies-tokyo.connpass.com/event/251328/>`__
  * Python Boot Camp側での運営知見あれば教えてほしいです
  * コロナ関連でやっていることがあるので、共有お願いします(takanory→kobatomo, ryu22e

PyCon JP TV(takanory、低、報告)
-------------------------------
* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* https://www.youtube.com/user/PyConJP
* Web https://tv.pycon.jp/
* 6、7月配信済み

  * `#17: PyCon US 2022振り返り Part.2 - 2021-06-03 <https://tv.pycon.jp/episode/17.html>`_
  * `#18: ブラウザでPythonが動くPyScriptを解説 - 2022-07-01 <https://tv.pycon.jp/episode/18.html>`_
* 次回は8月5日(金)予定。内容は「EuroPython 2022振り返り」
* 機材購入、スタッフジャンパーの精算チケットを作成した

  * (担当者変わってなかったんで7/30にshimizukawaに回した(takanory
  * https://pyconjp.atlassian.net/browse/ISSHA-2635
  * https://pyconjp.atlassian.net/browse/ISSHA-2538
* ネタ募集中です(takanory

海外コミュニティ連携
====================

PSF AwardのBlogポスト(takanory、中、報告)
-----------------------------------------
* `ISSHA-2529 <https://pyconjp.atlassian.net/browse/ISSHA-2529>`_ PSFのAwardのBlog Post用写真を撮影して送った

  * インタビューは回答できなかった(Jonasだけ回答してくれた)
* 写真を送ってブログ公開された、わーい

  * `Python Software Foundation News: PyCon JP Association Awarded the PSF Community Service Award for Q4 2021 <https://pyfound.blogspot.com/2022/05/pycon-jp-association-awarded-psf.html>`_
  * `PyCon US 2022でCommunity Service Awardsを受賞してきました <https://pyconjp.blogspot.com/2022/06/pyconjp-win-awards.html>`__

Python商標問題(terada、低、報告)
--------------------------------
* PSFの弁護士のVanからメールで正式に解決したとの連絡を受け取った（2022年7月3日）


APAC関連(terada、高、相談)
--------------------------
* PyCon APAC 2022でPyCon JPオンライブースを出さないか？

  * 9月3日、4日
  * PyCon JP 2022ブースを出して「リモートで見てね」とかはありかなぁ(yoshida
  * COSCUP(台湾のOSCみたいなイベント)で発表した。PyCon Taiwan関係者がJPに参加したいと言っていた(yoshida
  * イベント紹介という意味では、ブースよりもLTとかの方がいいのではないか?(yoshida
  * PyCon JP Associationとしてはブースはごめんなさいする。LTとかならやりたいが...(terada
* TWチーム中心に、APAC内で、PSF memberになろう、さらに投票可能なメンバーになろうというキャンペーンを実施するらしい。

  * このミーティングに参加しているメンバーだとだいたいManaging Memberとかになって投票権を得られるはず(terada
  * `PSF Membership FAQ | Python Software Foundation <https://www.python.org/psf/membership/>`__
* APAC 2023にJPチームとして応募するか？ 

  * 今年は台湾。日本は前回2013年。(terada
  * PyCon APACだと何が違うか?

    * 言語はなるべく英語を中心にしてほしい(terada
    * トークの比率も英語を高めにしてほしい(2013は50%:50%だった)
  * 2023年段階で入国制限がどうなるかわからないので、現時点で手を上げにくい(takanory

    * 来年の座長を決めないと決まらないのでは(jonas
    * 募集の連絡がいつ来るか、そのときに状況が変わっているか...(takanory

APACロゴ関係(terada、低、なし)
------------------------------
* 進展なし

予算2022(terada、低、議論)
==========================
* `2020予算参考 <https://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=0>`__, `2021予算 <https://docs.google.com/spreadsheets/d/1iZOJ2avqr92xUCFGiwx3AtXYBfdXsAyhQr_DHz7QQWA/edit#gid=1331278426>`__
* 追加の予算申請は無いか？(terada)
* Python Boot Camp/PyLadies Caravan関係者の遠方支援はどうか?(takanory

  * PyCon JP 2022側では遠方支援を実施予定。主にはスピーカーのサポートとなると思われる(yoshida
  * 前回の実施ブログ

    * `Python Boot Camp & PyLadies Caravan 遠方参加者支援対象者募集のお知らせ <https://pyconjp.blogspot.com/2019/08/pycamp-and-pyledies-caravan-support.html>`__
    * `Python Boot Camp & PyLadies Caravan 遠方参加者支援実施レポート <https://pyconjp.blogspot.com/2019/10/pycamp-and-pyladies-caravan-support-report.html>`__
  * PyLadiesとしては支援によって沖縄から来れた人がいるのでありがたい(maaya
  * **TODO**: 予算案をまとめてSlack上で検討する(kobatomo
  * PyCon JP 2022のイベントチームとは独立して動く想定(takanory
* 招聘関連での行政書士への予算を組んでおくとよいと思う(takanory

  * **TODO**: 最大15名で行政書士の先生から見積もりをもらう(terata
  * 行政書士の人とのやりとりはする(yoshida

理事など(terada、中、議論)
==========================
* 法人設立から10年、理事が固定化されている
* 来年度に向けて何か検討すべき事項は無いか？
* `理事メンバーの履歴 — PyCon JP <https://www.pycon.jp/committee/board_history.html>`__
* 理事をもう一人は増やしたい(takanory

  * こういうことをやっていますという情報があると動きやすい(selina
  * 「議事録を読んで」だとわからないってことですよね(takanory
  * 仕事をストップしながらやらないといけないのかがわからない(selina
  * 動画を撮りますか?(terada
  * PyCon JPのイベントでやっている「公開ミーティング」がわかりやすい(selina
  * 「理事会の広報ができていない」と認識した(takanory
  * **TODO**: なにかやり方を考える(takanory

    * まずはブログかなぁ...(takanory
    * 質問を募集してそれに答えるとか(takanory

その他
======
* OSCはまだ現地開催を行われていない?(terada

  * Kyotoはハイブリッドで小規模現地開催だった(yoshida
  * 他に現地開催しているイベントってありますか?(terada
  * OSC新潟は現地開催を目指しているらしい(yoshida
* EuroPythonでのPyCon JPの紹介LTお疲れ様でした(terada

  * やりました!(takanory
* Python Charity Talks またやる?(takanory

  * 前回は2021年9月に実施(takanory
  * 狙いは「寄付」を募ること(takanory
  * PyCon JP 2022のアンカンファレンス? (peacock

    * 落選トーク? リジェクトコン
    * 前(3回目)はコミュニティ、その前2回は過去から再演
  * ハイブリッドはありかも? (takanory
  * 予算・スタッフが必要(terada

    * 予算規模は10万円くらい(takanory
  * やることと意義は全然ありだと思う。PyCon JP 2022直後じゃない方がいいのでは。時期としては年末とか年明けとか(maaya

    * 2月のイベントが少ない時期とか? (shimizukawa
    * やりたい++ (つつい
* PyCon JP 2022内のPyCon JP Associationの公開ミーティングの段取りをしたい(terada, takanory

  * 金曜日のランチタイムとかがよさそう(terada
  * **TODO**: 調整する(peacock

次回
====
* 運営会議#55

  * 2022年9月28日(水)
  * https://pyconjp-staff.connpass.com/event/256414/
