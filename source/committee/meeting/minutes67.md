# 2024年6月4日(火) 一般社団法人PyCon JP Association運営会議#67

* 日時: 2024年6月4日(火) 19:30-21:30
* 場所: CMSコミュニケーションズ、Zoom
* 参加者 <https://pyconjp-staff.connpass.com/event/314135/>
  * 理事: takanory, yoshida, shimizukawa, terada, jonas, maaya
  * オブザーバー: peacock, yoshi-tsukamo, ryu22e, masashi kotera, kobatomo

```{contents}
:local: true
```

## PyCon JP

### PyCon APAC 2023(Selina、中、報告)

* スポンサー関連
  * **TODO**: BloomBergの入金確認。その後、2023チームとしてまとめ終わる(Selina
    * BloomBergはシルバー <https://2023-apac.pycon.jp/sponsor>
  * イベント決算blogの発表が遅くなる、会計事務所作業も必要(yoshida
    * 入金はされるはずなので、決算ブログは出せばいいのでは(terada, takanory
      * TODO: 決算Blog出す方向で会計事務所と進める(yoshida
      * 5/21に昨年分の協賛金の最後の振り込みがされたので、イベント決算について追記を羽藤会計事務所と調整しています。 
      * <https://pyconjp.atlassian.net/browse/USA-632>
        * 会計事務所より
        * 入金の約束が守られたことは喜ばしく、その点からは計上を行っておくべきだったと反省しております。
        * イベント収支の報告書の下の枠外にこの400,000円の収入を別記で「他、5月21日に2023年度分協賛収入400,000円あり」との記載しておいても宜しいかと考えます。
        * 注記表のような形で、そして来年の報告書では「うち400，000円は昨年度の協賛収入である」との記載を行うのも宜しいかと考えます。

#### その他

* **TODO**: アンケート報告ブログ(selina
  * JIRA <https://pyconjp.atlassian.net/browse/USA-634>
  * アンケート場所
    * 
    * おわってるのでは?? (peacock
    * <https://pyconjp.blogspot.com/2024/04/pycon-apac-2023.html>
* **TODO**: PSFへのイベントレポートを書く。内容はSelina。報告はjonas中心で進める(jonas
  * JIRA <https://pyconjp.atlassian.net/browse/USA-589>
  * 一部まとめたが、もう少し書くために時間が必要(selina

### PyCon JP 2024(takanory、中、報告)

* プロポーザル募集完了→レビュー中
* スポンサー募集は「ヤバい」状況は脱した
* 会計は見直しが必要そう
* 会場の使い方をそろそろFix?
* チケット発売の準備を進めている
* 今後の動き方
  * 6月13日(木)に全体作業会

### PyCon JP 2025

* <https://pyconjp.atlassian.net/issues/TAT-196>
* 会場はどうするか?
* そろそろ変えてもいいかという気もするが、同じ所でもよいかも(yoshida
* 東京以外は立候補があればやってもいいのではないか?(takanory
  * イメージはある? (terada
    * ある程度現地チームは必要だけど、いて立候補があれば可能そう? (takanory
  * 不安・懸念事項は?(terada
    * 参加者が集まるのか?
  * 規模が小さくなるのはありそうだが、地方開催にはネガティブではない(maaya
  * 実験としてやってみるのはアリでは(yoshida
    * RubyKaigi, YAPCがある
    * 単年で黒字を達成しなければいけない状況でもない
  * 一度体制も含めゼロベースでリセットしたい気持ちがある。やることも減らしたい(takanory
    * ソフトウェア的に変化する項目?
  * 東京から遠征する人の体力は厳しい
  * PyCon USみたいに「2年後はここでやります」宣言をするのは? (maaya
    * 2018, 2019みたいに翌年を発表できると準備しやすい(yoshida
    * やるなら、やれそうな地方コミュニティに直接聞くしかないかなあ(terada
  * バックアップでTOC有明を抑えておくのは? (terada
    * あんまりないかなあ。PiO? (takanory
      * 新しくない(yoshida
    * 他に選択肢があるかは2024会場チームに知見がありそう(peacock
    * **TODO**: 仮予約する(terada
* 会場も公募する? (shimizukawa
  * **TODO**: 某氏3名に声をかける(takanory

## 会計関連

### 2024年 予算(shimizukawa、中、相談)

* PyCon JP 2024の予算について、収入と支出を計画をたてた方がよいのでは(iqbal
  * 前回MTG
    * 収入と支出をまとめて予算をまとめる予定。4月後半にまとまるかなぁ(takanory
    * 変わる予定だが金額としてどのくらいかを予算として積んでおくとよいのでは無いか(terada
    * 予算規模としては「昨年同様規模」を考えていて収入35,000千円、支出30,000千円くらいかなぁ(takanory
      * 2024 会計チームとしては「純利益+500万円くらいを目標」で合意している(peacock
      * 良いと思います(terada
  * PyCon JP 2024の予算が固まりつつあるので、その内容を載せるのはどうか?(terada
    * 6月末くらい?(takanory
    * 了解です (shimizukawa
* [ISSHA-3084](https://pyconjp.atlassian.net/browse/ISSHA-3084) 遠方支援を一社事業に組み込むのかどうか(terada
  * 前回
    * 会計担当としてはやってもらえると助かる。大量の現金を持ちたくない(peacock
      * ただ、主催チームが窓口として参加者との間に立つのは仕方無いと思っている
    * PSFからのGrantが収入源として大きい。その申請もイベントチームでやっているが申請も一社で持つのか?(yoshida
      * これを一社として受けるのは筋ではないのでは(takanory
      * PSFは「Travel Grantのために使う」と明記して欲しくないらしい(jonas
    * PyCamp支援と一本化もするか?(takanory
      * この支援はイベント主催チームで決めている、という話ではない(terada
      * 継続して議論しましょう(takanory
      * ただユーザー体験としては一本化した方が良いはず(maaya
  * 全部運営チームに持っていくのは?(terada
    * なくはないと思う(takanory
    * PyCamp / PyLadies側をやめるのはどうか？(terada
      * やめたくないけど(terada
      * イベント側の募集フォームで吸収する? (takanory
        * イベント運営側の手数が変わってないのでは(terada
      * 事業としてやめるはない(shimizukawa
      * やめたくはない(maaya
    * 支援のPyCon JP 2024のチームにpyladies caravan、PyCampの誰かが入るのはどうか(maaya
    * あったほうがいいよね(yoshi-tsukamo
    * PSF / PyCon USは一緒の窓口だった(yoshida
      * 申し込みはPyLadiesだけど支払いは同じ(maaya
      * リストが中で共有されていると思われる(terada
    * 現金を持ち歩くことへのリスク
      * 一昨年・去年はyoshidaがほぼ一人でやっていたがイベントチームで継続的に可能なのか? (terada
      * 問題は海外。国内は事前にチェックで、事後に銀行振込でオンライン処理したい(takanory, shimizukawa
        * Wiseアカウントが開設できたら違う?
        * 楽になる。なくてもSWIFTが分かれば可能だが、確認が面倒(shimizukawa
        * PayPal送金だと海外に100万円/Day？month?の壁があった(yoshida
        * Wise推奨、ダメなら現金かなあ(takanory
          * Wiseでも100万/Day? の壁はありそう(shimizukawa
    * PyCamp / PyLadiesの本人確認は昨年どうしていた?(terada
      * 名札なり参加したことが確認できる写真なりと領収書を送付してもらって、後で銀行振込した(takanory
      * -> うまくやれば海外だけ処理すれば良くなりそう。がどこまで本人確認を厳格にやるのか考える必要がある(terada
    * 窓口一本化は進められる?(terada
      * PyCon JPの参加者管理チームとpycamp、pyladies caravanの運営メンバーで協議するところからだと思う(takanory
      * 最後の支払いはPyCon JP Associationが入る必要がある。Wise、PayPal等(terada
        * これは一社で可能な仕組みを考える必要がある(shimizukawa
        * **TODO** :イベントチームと7月にミーティングする方向で調整すすめる(shimizukawa
          * 関係者を集めて取りまとめます(shimizukawa
          * <https://pyconjp.atlassian.net/browse/ISSHA-3283>

## PyCamp、PyLadies関連

### PyCamp状況報告(ryu22e、低、報告)

* 運営メンバー: ryu22e、yamate、nishimoto、kobatomo
* [Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP](https://www.pycon.jp/support/bootcamp.html)
* 6月以降の開催状況
  * 福岡で3回目の開催に向けて会場の選定中（現地スタッフ: kuga, Sayaka）
    * 今の所具体的な動きはなし
    * SayakaさんSlack反応なし
  * 東京都八王子市で開催立候補あり（現地スタッフ: uniq）
    * 今の所具体的な動きはなし
    * 4/11 PyCamp相談会に参加申込あり→その後キャンセル
  * 6/15 札幌2nd(現地スタッフ: nakayoshix, コアスタッフ: kobatomo, 講師: ryu22e)
    * nakayoshixさんがイベントを中止したいといっている。6月4日(火) 20:00からMTG
    * がんばって参加者を集めて実現してほしい(terada
    * 1人でも実施してほしい。1人だからキャンセルみたいな前例を作りたくない(shimizukawa
    * タスクまきとるなりして進めてください(takanory
  * 6/22 愛知3rd(現地スタッフ: Ryo, Onur Boyar, コアスタッフ: yamate, 講師: takanory)
  * 6/29 山形3rd(現地スタッフ: kadowaki, コアスタッフ: ryu22e, 講師: shimizukawa)

### OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)

* 運営メンバー: yoshi-tsukamo
* 出展予定
  * 2024年6月29(土) 北海道
    * 札幌市産業振興センター
    * <https://www.sapporosansin.jp/>
    * たかのりさん参加予定
  * **TODO**: Blog書くぞ!!!(takanory
* 出展検討中
  * 2024年7月27日(土) 京都
    * 京都リサーチパーク
    * <https://www.krp.co.jp/access/>
    * 北海道の交通費が想定より安かったので京都に回すことができるかも
    * 予算が可能なら京都は結構集まるらしいのでありでは(takanory
    * 予算がOKならいいと思う(terada
* 備品購入予定
  * テーブルクロス、チラシ、ステッカー等を入れて送る際の箱を購入予定
  * →購入して領収書でshimizukawaに回す(yoshi-tsukamo
* Pythonステッカーが少なくなってきたので補充をお願いします
  * チケットください(takanory→yoshi-tsukamo→terada
  * 以前はPSFのBetsyさんにメールしたので、今のPSFスタッフに誰かメールしてステッカーを送ってもらう(yoshi-tsukamo

### PyLadies関係報告(maaya, 低, 報告)

* **PyLadies Caravan**
  * PyLadies Caravan 青森 5月11日開催済
    * 2名参加
    * 1回8万予算でとってたが超えたので次回以降も超えるようなら相談する
  * PyLadies Caravan in 北海道(室蘭・苫小牧) 11-12月くらいで開催調整中
    * 大学の先生と一緒にすすめます。高専ともコンタクト予定
      * 苫小牧高専のOGと繋がったので、なにか宣伝の依頼とか繋げられるかも....? (peacock
  * Caravan コミュニティカード品切れになったので再作成する
* PyLady Award ブログ公開待ち
  * <https://github.com/pyladies/pyladies/pull/664>
  * PyCon JP側ブログも頑張る

### PyCon JP TV(terada、低、報告)

* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* <https://www.youtube.com/user/PyConJP>
* Web <https://tv.pycon.jp/>
* 40回配信済み
  * [#39: 開発環境の整え方ライブデモ - 2024-04-05](https://tv.pycon.jp/episode/39.html)
  * [#40: JupyterLabで環境の整え方ライブデモ - 2024-05-02](https://tv.pycon.jp/episode/40.html)
* 次回は、6月7日（金）予定
  * [#41: PyCon US 2024報告会ライブ - 2023-06-07](https://tv.pycon.jp/episode/41.html)
* ネタ募集中です(takanory
  * [開発系とイベント紹介系を軸に進めていくつもり](https://docs.google.com/spreadsheets/d/1N7QVU9uTcZeoHCrnzWw0LLZQ5lb82ocHopCbUO5biwo/edit#gid=0)
* 宣伝方法の検討(terada 
  * 継続的にやることを重視し、広告はしばらくやらない方針

## コミュニティー支援

### PyCon JP地域開催サポートプログラム(terada、中、相談)

* 仕組み作りは進んでいない(terada

### 地域PyCon

* #regional-support チャンネルがPyCon JP Slackにできたよ(shimizukawa

#### PyCon mini 東海(shimizukawa、中、報告)

* PyCon mini 名古屋の開催に向けて動いている。
  * 相談: takanory / shimizukawa / terada が相談に乗っている
  * 担当: shimizukawa
* 5/11 東海向けに、100,000円の支援を決めた
  * <https://pyconjp.atlassian.net/browse/ISSHA-3267>
* 5/30 会場契約を行った 
  * <https://pyconjp.atlassian.net/browse/ISSHA-3268>
  * 契約の主体は一社PyCon JP Association
  * 2024年11月16日(土)、1日間。
* 6/4 会場への費用振込を行った（予定）
  * <https://pyconjp.atlassian.net/browse/ISSHA-3281>
  * 約25万円の全額を支払い、支援額との差額を開催後に東海から受領予定
* 11月早々に、イベント保険契約予定
  * 5,000円を想定

#### PyCon Kyushu 2024 in Kagoshima(terada、中、報告)

* 5月25日(土) 開催された
* [PyCon Kyushu](https://kyushu.pycon.jp/2024/)
* (terada) 100,000円でスポンサーした。
* 予定通り開催された
  * 100人以上の参加者
  * ブース設置し、PyCon JP / PyCamp他の宣伝をした。tsukamotoが中心にブース運営した
  * PyCampでは、宮崎、長崎の方々にアピールできた

#### PyCon mini Shizuoka (yoshi-tsukamoto、中、報告)

* サイト公開した <https://shizuoka.pycon.jp/2024/>
* 静岡市で8/31(土)開催。プロポーザル募集中
* Blogでイベントの告知をします
  * 是非どうぞ +1 (terada
* 有料イベントとして考えていたが、PyCon Kyusyuで話を聞いて無料化を検討している
  * 無料にするとメリット・デメリットがあるが、チームで決めてもらえればよいと思う(terada
    * 費用的な負担が増える
    * キャンセルが出る?
      * kyushuは結構キャンセル出なかった(terada
* 会場費等で10万円ほどの支援をしてもらえるとありがたいです
  * スタッフと相談してboardのほうにメールを送ります
  * PSFの[Regional Grant Program](https://www.python.org/psf/grants/)に申請をしてみてほしい(takanory
    * <https://www.python.org/psf/grants/>
    * 申請するノウハウがない。どうやって構築していくか(terada
      * PSF Discordでほぼ毎週Office hourをやっている。チャットで英語のやりとりが可能ならハードルは低いんじゃないかなぁ(takanory
      * イベントページとCoCページがあるなら大丈夫なんじゃないかな(terada
        * 東海チームと協力するとよさそう(takanory
    * PSFのアジア圏へのGrantに対するモチベーションは高いので、通るんじゃないかなぁ

## 海外コミュニティ連携

### APAC関連(terada、低、なし)

* Python Asia構想
  * PAO略称で、Euro Python Societyのようなもの
  * 10月の立ち上げに向けて動いているが、一社PyCon JP Associationとの関係は、PAOの方針が決まってから動き出すことになると思う。

### PyCon US 2024(terada、中、相談)

* PyCon APACとしてブースを作った
  * 多くの人にPRできたと思う
  * ブースに持っていくもの <https://pyconjp.atlassian.net/browse/ISSHA-3118>
  * 折り紙: 23,100円 <https://pyconjp.atlassian.net/browse/ISSHA-3183>
  * スタッフ用Tシャツ: 22,143円 <https://pyconjp.atlassian.net/browse/ISSHA-3180>
  * 2021で作ったマスクや、キットカットなどを持っていった。
    * 抹茶のキットカットはめっちゃ人気だったらしい(takanory
* ショートトーク（30秒）で、PyCon JP 2024の宣伝をyoshidaがした。
* 予算申請
  * 合計: 60,000円
  * だったので予算内で完了した。

### PyCon APAC 2024(terada、低、なし)

* インドネシアのDimaさんを中心に進んでいる
* 予算申請なし
* サイトが公開 <https://2024-apac.pycon.id/> されて進んでいる。
* ツアーをやるかどうか悩み中(terada
  * Suyama, maaya, teradaで進められればやる

### APACロゴ関係(terada、低、なし)

* 現在、ロゴキットを取りまとめ中。まもなく完了する。
* 予算申請なし

## その他

### 法務担当的立場  (terada、 低、報告)

* 弁護士費用
  * 予算申請: 400,000円
  * プライバシーポリシーの策定
  * 各種ガイドラインの策定
* 以下の策定を弁護士と進める
  * プライバシーポリシーの策定　（以前からタスクなっていたもの）
    * 完成した
    * 52,889円 <https://pyconjp.atlassian.net/browse/ISSHA-3266>
  * その他以下を進めている
    * プライバシーおよび個人情報の取り扱いに関してのガイドライン
    * カンファレンス会場におけるWiFi環境の提供のガイドライン
    * 問題が発生時の対応するフローを構築
  * ガイドラインは、公開するつもり
    * PyCon JP / RubyKaigi / その他
    * 外部も巻き込んで最小公倍数で作る？
	
## TODO

* [USA-632](https://pyconjp.atlassian.net/browse/USA-632) PyCon APAC 2023イベント収支表作成し、決算Blogを出す(yoshida
* [USA-589](https://pyconjp.atlassian.net/browse/USA-589) PyCon APAC 2023のPSFへのイベントレポートを書く(jonas
* [TAT-196](https://pyconjp.atlassian.net/browse/TAT-196) PyCon JP 2025の会場としてバックアップでTOC有明を仮予約する (terada
* [ISSHA-3286](https://pyconjp.atlassian.net/browse/ISSHA-3286) PyCon JP 2025の地方開催に興味があるか、地域コミュニティの人に声をかける(takanory
* [ISSHA-3283](https://pyconjp.atlassian.net/browse/ISSHA-3283) PyCon JP 2024の遠方支援の方式を相談を、PyCon JP 2024チーム、pycampチームと日程調整してすすめる(shimizukawa
* [ISSHA-3285](https://pyconjp.atlassian.net/browse/ISSHA-3285) PSFにPythonステッカーを送ってもらうよう依頼する(terada
* [ISSHA-3284](https://pyconjp.atlassian.net/browse/ISSHA-3284) Wiseの送金能力の調査(shimizukawa



## 次回

* 運営会議#68
  * <https://pyconjp-staff.connpass.com/event/321509/>
  * 8/22(木)
