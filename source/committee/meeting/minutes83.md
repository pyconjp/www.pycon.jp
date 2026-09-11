# 一般社団法人PyCon JP Association運営会議#83

* 日時: 2026年9月8日(火) 19:30-21:00
* 場所: マイクロソフト
* 参加者: <https://pyconjp-staff.connpass.com/event/399274/>
  * 理事: takanory, shimizukawa, maaya, jonas
  * オブザーバー: ike, peacock, terada, ryu22e, yoshi-tsukamo, sano, yamate

## PyCon JP

### PyCon JP 2025(takanory、低、報告)

* オープンの課題は以下の1つのみ
  * [HBI-669: 動画のサムネと説明欄の整備](https://pyconjp.atlassian.net/browse/HBI-669)

### PyCon JP 2026(sano、takanory、中、相談)

* イベントは無事終了
  * CoCチーム 特に連絡等はなかったので、集中期間も終えて解散済(sano
* 残件処理、会計処理を進めている
  * 作業会を実施中。企画書ドキュメントに成果物をまとめたりしている
  * [PyCon JP 2026 General Work Session 2026.9.9 - connpass](https://pyconjp-staff.connpass.com/event/405259/)
  * [PyCon JP 2026 General Work Session 2026.9.17 - connpass](https://pyconjp-staff.connpass.com/event/405260/)
* 会計は助成金込みでプラスマイナス0円になる見通し
  * [予算2026](https://docs.google.com/spreadsheets/d/1i66jFzOoQo_XX-V4f0RufSTaHnUi00JDEgNypUX0FcA/edit?gid=2098841222#gid=2098841222)
* 大きめ残件
  * [HRS-728: ホテル代と交通費の精算](https://pyconjp.atlassian.net/browse/HRS-728)
  * [HRS-817: PyCon JP 2026の決算](https://pyconjp.atlassian.net/browse/HRS-817)
    * 助成金申請
  * [HRS-825: 主催メンバー打ち上げ](https://pyconjp.atlassian.net/browse/HRS-825) (東京)
    * 広島でも実施予定
  * 写真公開
  * 録画公開
    * 既に限定公開アップロードで進行中です(sano
    * ↑どちらもJIRA作って進めてほしい(takanory
      * 会場チームでjira作成->チェック等を進めてもらいます(sano
  * [HRS-866: パンダスタジオから物損があったことに対して対応方法をまとめる](https://pyconjp.atlassian.net/browse/HRS-866?atlOrigin=eyJpIjoiZjQ3OGZkNTMxOWFlNDRmZWFjZTM0YjM5MWNmNjI4OWQiLCJwIjoiamlyYS1zbGFjay1pbnQifQ&issueKey=HRS-866&subProduct=jira-core)
    * 物損の連絡をもらって、状況確認中。賠償が必要なときに保険利用を考えてます
      [HRS-657: PyCon JP 2026の損害保険契約](https://pyconjp.atlassian.net/browse/HRS-657?search_id=cfccbdfe-13b7-4d15-82db-2eb62e64d98b&xpis=eyJicmlkZ2UiOiJxdWlja0ZpbmQiLCJpZCI6IjE3ODc5MTAxMzYyMDEiLCJzb3VyY2UiOiJqaXJhIn0%3D)
    * パンダスタジオからの連絡待ち(sano
    * 期日を決めて進めてほしい(takanory
      * 会計を締めたいのでいつまでも待てない
      * 期日を伝えて、いつまでに連絡くれ、等
  * 遠方支援の支払いが1件終わっていない(shimizukawa
    * 韓国の銀行送金がうまくいっていないため。最悪個人Wise/PayPal等を使って9/15までに終わらせます(shimizukawa

### PyCon JP 2027 (peacock、中、報告

* 共同座長3人(ikeda,peacock,sano)で隔週ミーティングを始めた
  * 進め方や立ち上げ方法を話し合っている
  * 体制やチーム構成も考え始めた
* 沼津市の助成金の申請の初段(全3回のうち)を9月中に出す必要がある
  * 大枠の収支計画書が必要なので作って提出予定
* 直近のTODO:
  * 沼津市の助成金申請の準備
  * JIRAプロジェクト作成(会計は別にする予定)
    * 会計プロジェクトはワークフローを固めて証跡が残るようにする予定
      * 方向性をまとめたらshimizukawaさんにレビュー依頼するといいのでは(takanory
    * 外部要求への対応か？（オブザーバー池
      * そうではない。会計理事として対応したほうがよいとの考え（清水川

## 一社運営関連

### 寺田が理事から離れる準備  (takanory、 中、報告)

* **TODO**: 進められていないため日程調整して作業会を実施する(shimizukawa

### 情報セキュリティ指針や情報レベルの定義  (terada、 中、報告)

* <https://pyconjp.atlassian.net/browse/ISSHA-3638>
* 定期的な作業会を通じて、適時対応中。
* Jiraの設定で苦戦していたが、一旦は運用できるレベルになっている。
  * JSMの権限が渡らない問題があるが、一旦保留。
* Jiraの新規ワークスペース「外部コラボレーション」を作ったがうまく運用が始められる。<https://pyconjp.atlassian.net/jira/core/projects/COLLAB>
  * PyCon mini Tokyo
  * PyCamp
* PyCon JP 2026中にオープンスペースを実施して今までの活動を報告した。
  * 告知ができて無くて参加者が少なかったが・・。
* 管理者（理事）には、パスワードマネージャーの利用を必須にしていきたい
* 今後
  * 1password運用の変更(PyCon JPイベント関係の保管庫をチーム単位に分ける)
    * PyCon JP 2026がほぼ終わっているので着手できそう(takanory
  * スクリプトで設定の定期確認
  * 新たな課題が無いかを見直す
    * 銀行の振り込みできるトークンを誰が持っているか問題など
* なにか運用上でトラブルや使いにくい点はあったか?(ike
  * Jira Service Managementの件は認識している(takanory
  * JIRAのAI機能がうまく使えない(sano

## 会計関連

### 2026年2月 決算(shimizukawa、低、共有)

* イベントチーム側でJIRAと証憑とかをどういう風に管理するといいか
  * <https://pyconjp.atlassian.net/browse/ISSHA-3881>
  * 7/中旬、Confluenceにまとめました(shimizukawa

## PyCamp、PyLadies関連

### PyCamp状況報告(ryu22e、低、報告)

* 運営メンバー: ryu22e、yamate、nishimoto、kobatomo
* [Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP](https://www.pycon.jp/support/bootcamp.html)
* 2026年9月以降の開催見込み
  * 長崎（現地スタッフ: 平山さん）
    * 平山さんはryu22eの同僚
    * 4月のオンライン相談会にも来てくれた
    * 佐世保で開催したいとのこと
    * 今のところ具体的な動きはなし
* PyCon JP 2026のブースではなにかあった?(takanory
  * 島根、長野、埼玉でやりたいという話はあった(yamate

### OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)

* 運営メンバー: yoshi-tsukamo
* 出展済み
  * [OSC島根](https://event.ospn.jp/osc2026-shimane/)
    * 2026/7/11(土)
    * 松江テルサ
    * eurahさん、sanoさんが参加
    * 松江在住の Shaon Alexさん(2026主催メンバー)は体調不良で不参加
  * [OSC京都](https://event.ospn.jp/osc2026-kyoto/)
    * 2026/8/1(土)
    * 京都リサーチパーク
    * takanoryさん、tazoeさんが参加
      * 当初セミナーは申し込みしなかったが空いている枠があったので講演させてもらえた
      * [エラーはともだち こわくないよ](https://event.ospn.jp/osc2026-kyoto/session/2320797)
* 出展検討中
  * [KOF2026](https://www.k-of.jp/2026/)
    * 2026/11/13(金),14(土)
    * 大阪南港ATC ITM棟
    * 協賛費: 50,000円(一口)
    * 予算は16万円ほど残っているので1名参加が可能な見込み
    * PyCon HKとかぶってるなぁ...(takanory
  * KOF以外にも他のOSCはあるが、どうか?(takanory
* チラシ作るとかはどうなってましたっけ?(takanory
  * 裏面簡略化などを考えている(yoshi-tsukamo

### PyLadies関係報告(maaya, 中, 報告)

* **PyLadies Caravan**
  * 次の開催地を探し中
    * 学生さん（大学、専門）ターゲット
    * または未開催/1回開催のみ地域
* **その他PyLadies**
  * PyCon JP 2026アクティビティ
    * Tokyoコミュニティブース採択済
      * Tシャツ6枚と缶バッチ1個売れました。ありがとうございました
    * 世界・国内PyLadies オーガナイザーが勢ぞろいであちこちでネットワーキング爆誕
  * PyLadies Shizuoka
    * 9/13（日）に#2 meetup Code&Connect（もくもく会）開催予定
  * PyLadies Fukuoka
    * 10/24（土）に #1 meetup 開催予定に向け、準備中
  * PyLaides Tokyo
    * 9/19 GTUG コラボ
    * 10/18 12th anniversary party
      * PyCon Taiwanとかぶってるなぁ...(takanory
      * こっちは男性参加できるよ
  * PyLadies Japan
    * 静岡・福岡・東京三拠点オフサイト中継忘年LT大会開催計画中
      * 男性が参加できるかは要議論

### PyCon JP TV(terada、低、報告)

* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* <https://www.youtube.com/user/PyConJP>
* Web <https://tv.pycon.jp/>
* 68回配信済み
  * [**#68: PyCon JP 2026振り返り - 2026-09-01**](https://tv.pycon.jp/episode/68.html)
  * [**#67: PyCon JP 2026の楽しみ方 - 2026-08-05**](https://tv.pycon.jp/episode/67.html)
  * [**#66: Python 3.15の新機能を試す - 2026-07-07**](https://tv.pycon.jp/episode/66.html)
* 次回は、10月6日（火）予定
  * Python 3.15 プロファイラーを試す(仮)
* 火曜日に変更した。しばらく様子見をするが、そんなに増えていないので再度変更するかも(terada
* ネタ募集中です(takanory
  * [開発系とイベント紹介系を軸に進めていくつもり](https://docs.google.com/spreadsheets/d/1N7QVU9uTcZeoHCrnzWw0LLZQ5lb82ocHopCbUO5biwo/edit#gid=0)
  * 特に技術ネタのアイデアが欲しい
    * サプライチェーンアタック対策（Takumi guardとか）どうですか(shimizukawa
    * 誰か開発者にインタビューとか?(takanory
    * PyCon JP 2027座長になにか(takanory
* 今年の地方遠征は未定
  * 静岡?

## コミュニティー支援

### PyCon US 2026 報告会支援(Maaya、低、報告)

* <https://pyconjp.atlassian.net/browse/ISSHA-3966>
* イベントブログ公開済み(takanory
  * [【PyCon US 2026 参加報告会】開催しました！会場とオンラインで盛り上がりました](https://pyconjp.blogspot.com/2026/07/pycon-us-2026.html)
* チケットクローズ済み

### イベントキャンセル補填の整備 (shimizukawa、中、共有)

* [ISSHA-3829: PyCon mini Shizuoka 2026 イベントキャンセル保険の検討](https://pyconjp.atlassian.net/browse/ISSHA-3829)
  * Yutaro Ikeda さんにとりまとめ完了✅️
    * [PyCon JP Associationによるイベント保険](https://docs.google.com/document/d/1AjX2MvFP85HMPSx8ojnvcwVegjTJHrdOfZyf5GLpnU8/edit?tab=t.0)
  * [www.pycon.jp](http://www.pycon.jp)で公開準備中🌀
  * ブログ準備中🌀
  * 予算を確保済みです(shimizukawa)
  * [(編集用) PyCon JP Associationによるイベント費用補填制度](https://docs.google.com/document/d/1a4CD6lCOe40zy8aMGK0Ys4dWq9A2a2BQ7HEluOs22AA/edit?tab=t.0#heading=h.mspair43fgjt)
  * 9/8 理事の承認待ち
    * 承認: shimizukawa, terada, maaya, yoshida, jonas
    * 承認待ち: takanory

## 海外コミュニティ連携

### PAO(PythonAsia)とのコラボイベント(tsutsui、高、報告)

* 12/12（土）に「PyCon mini Tokyo with PythonAsia conference」開催が決定した（[connpassイベントページ](https://pyconjp.connpass.com/event/404336/)）
  * まだ諸々が決まっていないので参加登録は10/01からにしている
* PyCon JP Blogでは告知済み <https://pyconjp.blogspot.com/2026/08/pycontokyo-with-pao.html>
* 現在運営メンバーはryu22e（副座長）とterada（座長）を除いて10名（うち3名が当日スタッフ）
  * スタッフ名簿（まだ作成中なので全員分書いていない）：[ PyCon mini Tokyo with PythonAsia conferenceスタッフ名簿](https://docs.google.com/spreadsheets/d/1yKDS9We4aLGWzf8_lkVDmzCFXF3jdhfXy4_j0gElwf8/edit?gid=0#gid=0)
* 撮影をやってくれる当日スタッフが来てくれるので、トークセッションの動画撮影はやれそう
  * ただ、撮影をやってくれる当日スタッフからは前日に会場に入って準備したいとの声があり、できるかどうかは要確認
* トーク数は日本語・英語それぞれ6つにする予定
  * タイムテーブルを作成中：[タイムテーブル案](https://docs.google.com/document/d/1sglzS20JfqZuE9RkYTzdhP0ma-LN8y1wWfP_Xod_FSk/edit?tab=t.0#heading=h.2hlob5s4yzks)
* このあと、どうやって広報していくかっていうのがきもかなって思った(takanory
  * PyCon JP  2026でイベント後半で広報戦略で色々やったので、そこからピックアップするとよいかも(takanory

### 海外イベント参加予定(terada、低、報告)

* 今後の主なイベント:
  * 10月 TW
    * 特典航空券は取っているが、どうするか決めてない(takanory
  * 11月 HK
    * 予定があえば行くかも(maaya

## その他

### ポリシー関連  (yoshida、 中、相談)

* PyCon JP 2026から「カンファレンス等における反社会的勢力排除まわりの運用方針の明文化」について、寺田が引き取り中
  * ポリシーや相談について、引き続きteradaがyoshidaに相談に乗ってほしい
  * 運用方針を考えたのでレビューして欲しい（再度のお願い）
  * <https://pyconjp.atlassian.net/browse/ISSHA-3926>
* TODO: 作業会の議題にしましょう(takanory

### PyCon JP共有インフラについて(yoshida、 低、報告)

* 遠方支援
  * AWS インスタンス, Sentry, Postmark をたてました(shimizukawa
  * Postmark $15/mo
  * AWS: $67/mo
  * Sentry: 無料
  * 8末に撤去予定
    * 9/8時点: まだ遠方支援がクローズしきっておらず、延長中

### CoC関連  (maaya、 低、なし)

* PyCon JP 2026 にてCoCチームとして対応
  * 今年の報告0件

###  **DUNS関係(terada、 低、相談)**

* <https://pyconjp.atlassian.net/browse/ISSHA-4018>
* DUNSに登録されている住所が古い
* 変更しますか?
* 作業会で実施刷る(takanory

## 次回

* 9月~11月は作業会をやりましょう
* 運営会議#84 <https://pyconjp-staff.connpass.com/event/406473/>
  * 2026年12月15日
  * 議題
    * PyCon JP 2027
