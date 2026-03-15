# 2026年3月9日(月) 一般社団法人PyCon JP Association運営会議#80

* 日時: 2026年3月9日(月) 19:30-21:00
* 場所: HENNGE、Zoom
* 参加者 <https://pyconjp-staff.connpass.com/event/386163/>
  * 理事: takanory, shimizukawa, jonas, maaya, yoshida
  * オブザーバー: terada, ike, ryu22e, takubo, kanan, yoshi-tsukamo, taku

## PyCon JP

### PyCon JP 2025(peacock、低、報告)

* 残タスクの確認を行い、進めている(peacock
* クリティカルな残件はない認識(peacock
* 決算をまとめた中で、2025の会計報告が出ていないことが気になっている(shimizukawa
  * draft作成中、公開予定(peacock

### PyCon JP 2026(sano、takanory、中、報告)

* 会場
  * 広島国際会議場
* 会場利用申請
  * 2026年8月20日(木) 午後から準備、ヒマワリ（2025スポンサーブース）のみ18時から
  * 2026年8月21日(金)、22日(土) 全館
  * 2026年8月23日(日) 会議運営事務室、ヒマワリ
* PyCon JP 2026のJIRAスペースを作った
  * [ISSHA-3768: PyCon JP 2026用JIRAの準備](https://pyconjp.atlassian.net/browse/ISSHA-3768)
    * 今は共同座長のみが使用している、今後主催メンバーが使用していく予定
* 企画書作成
  * 以下のシートの各行の内容を企画書としてまとめている
  * [PyCon JP 2026でやりたいこと、やらないこと、維持するとこ](https://docs.google.com/spreadsheets/d/1nvjmebcVOhvXQWcK4V29Qu3mRijRhjQLhEHhJdpBmlE/edit?gid=0#gid=0)
  * [HRS-16: 企画書の作成サポートするAIの運用を行う](https://pyconjp.atlassian.net/browse/HRS-16)
  * GeminiのGem便利
  * [PyCon JP 2026企画書](docs.google.com/document/d/15aUxh6iFGJEwihojonmmOtBFyy2Yk5cLPpMn6Mg9oCA/edit?tab=t.0)
* TODO: 主催メンバー[`pycon.jp`](http://pycon.jp)のGoogleアカウント発行の準備中。JIRA、1Passwordなども発行予定。あわせてチーム分けなどを進める予定
  * オンボーディングのミーティングを3/11(水)、17(火)、26(木)に実施予定。そこから徐々にチームとして動き始める感じかなー
* 質疑応答
  * チーム分けできたら遠方支援の話をはじめたい(maaya
    * そうですね(takanory

### PyCon JPの一般社団法人とイベントチームの役割分担について(terada、低、報告

* 進んでいないので、進めていきます (terada
* <https://pyconjp.atlassian.net/browse/ISSHA-3844>

## 一社運営関連

### 寺田が理事から離れる準備  (takanory、 中、報告)

* [ISSHA-3691: 寺田さんが理事から離れることに伴い登記先などを調査して方針を決める](https://pyconjp.atlassian.net/browse/ISSHA-3691)
* takanory, yoshida, shimizukawa で調査してミーティングで情報共有をしている
* バーチャルオフィスを使用する方向→[バーチャルオフィス1](https://virtualoffice1.jp/)に決定
  * [ISSHA-3797: バーチャルオフィス1申し込み](https://pyconjp.atlassian.net/browse/ISSHA-3797)
* 荷物はトランクルームを使う想定→[minikura（ミニクラ](https://minikura.com/)に決定
  * [ISSHA-3804: トランクルームの確定と契約](https://pyconjp.atlassian.net/browse/ISSHA-3804)
* 検討事項
  * 郵便物の転送はするよね?(terada
  * 最後に残った物品の廃棄の段取りも必要(takanory

### 情報セキュリティ指針や情報レベルの定義  (terada、 中、報告)

* <https://pyconjp.atlassian.net/browse/ISSHA-3638>
* 松山さんという専門家に業務委託をして、一緒に月2回ペースでMTGを実施して進めている
* Ikeさんにも参加いただき、現在は、teradaとtakanoryも入って3名で対応している
* 最初の対策方針案を理事で合意した。
  * [情報セキュリティ対策のための方針](https://docs.google.com/document/d/1qjlORbB3kt4nyyoIK9CA23N4zAXBYhBRXG96l8_dKvE/edit?tab=t.0#heading=h.8n1tqv9kmmjt)
  * 具体的な作業（対策など）を進めていく予定
  * 対策を行うことでリスクが減ると考えていて、脅威シナリオも順調にリスクが下がっている
* Google Workspaceのアカウント作成を進めている (takanory
  * 理事、運営メンバーは[pycon.jp](http://pycon.jp)アカウントでのGoogleドライブアクセスに切り替わっている(takanory
  * **TODO**: PyCon JP 2026主催メンバーはこれから(takanory
* Slackの管理者への2FAを依頼した (terada
  * 完了した
* Jiraのセキュリティ設定やドメイン認証などを実施しようとしている (terada
  * 難しくて困っているが、Ebiharaさん（元主催メンバー）にサポートをしてもらう予定
* 情報セキュリティやアカウント管理に関する講習会を準備している (Ike
* Ian、Iqbalが[`pycon.jp`](http://pycon.jp)ドメインのメールアドレスを持っている。使っていないのであれば停止するが、どうする?(terada
  * 1年くらい転送して欲しい。(iqbal
  * すでに転送している。メールアドレスとしては使っていない。アカウント停止でOK(ian
    * **TODO**: アカウントを停止する(terada
* 理事が1名になる。誰かこの件を担当している理事がtakanoryの他にもう1名ほしい(terada
  * 片手間で良ければ入ります(maaya

## 会計関連

### 2026年 決算(shimizukawa、低、共有)

* ✅️[ISSHA-3809: 2025年 決算](https://pyconjp.atlassian.net/browse/ISSHA-3809)
  * 2/26 社員総会にて、決算報告および承認
* 今後のメモ
  * イベントチーム側でJIRAと証憑とかをどういう風に管理するといいか、先にルールを確認したい(takanory
    * 銀行にログインしてJIRAチケット番号を書くとか(shimizukawa
  * **TODO**: やり方はちょっと整理したい。イベントチームでお金が動き始める段階で、どういうルールだと運用しやすいか相談したい(takanory
    * 今回の決算で突き合わせに困ったところをメモっておきます(shimizukawa
    * 3/9 チケット作りました <https://pyconjp.atlassian.net/browse/ISSHA-3881>

### 2026年予算(takanory、高、議論)

* 経緯
  * 2025本予算 [https://www.pycon.jp/committee/meeting/minutes73.html#id2](https://www.pycon.jp/committee/meeting/minutes73.html#id2)
  * 2026仮予算 [https://www.pycon.jp/committee/meeting/minutes77.html#takanory](https://www.pycon.jp/committee/meeting/minutes77.html#takanory)
* [予算申請](https://docs.google.com/spreadsheets/d/10mcr1LZ7EgUnum5gwVyzS2h2jYegogqrxCQmmMwIIzQ/edit?gid=1871292783#gid=1871292783)の**シートにまとめましょう**(takanory

| カテゴリ   | 項目                                                                                                                        | 金額         | 小計         | 備考                                                                                                                                                                                      |
| ------ | ------------------------------------------------------------------------------------------------------------------------- | ----------: | ----------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 事務経費   |                                                                                                                           |            | ¥1,359,060 |                                                                                                                                                                                         |
|        | 行政書士（総会）                                                                                                                  | ¥155,000   |            | 2026年の総会の行政書士の費用。事務所移転があるため去年より高くなっている                                                                                                                                                  |
|        | 情報セキュリティ指針コンサル                                                                                                            | ¥100,000   |            | 昨年の半額でいけると思う。2025は15万円(ISSHA-3821)                                                                                                                                                      |
|        | 会計事務所                                                                                                                     | ¥968,000   |            |                                                                                                                                                                                         |
|        | 事務所移転経費                                                                                                                   | ¥100,000   |            | ゴミ廃棄費用、他、念の為多めに積んでおく                                                                                                                                                                    |
|        | トランクルーム                                                                                                                   | ¥20,000    |            | [minikura - ラージBOX 38x45x68 1箱 + 送料 8440円<br>](https://docs.google.com/spreadsheets/d/1ERZmAFT_I58sHJJDg1S1veJwSo2ox2cGqrLquwJWqp4/edit?gid=0#gid=0&range=G5:K5)初年度なので2倍積んでおきたい         |
|        | バーチャルオフィス1                                                                                                                | ¥16,060    |            | ISSHA-3797:入会金・月額料金1年分:16,060円                                                                                                                                                          |
| システム費用 |                                                                                                                           |            | ¥284,000   |                                                                                                                                                                                         |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3453)[さくらインターネット ドメイン年次更新](https://pyconjp.atlassian.net/browse/ISSHA-3453) | ¥4,000     |            | 例年通り                                                                                                                                                                                    |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3121)[AWS](https://pyconjp.atlassian.net/browse/ISSHA-3121)                 | ¥60,000    |            | 例年通り                                                                                                                                                                                    |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3383)[Flickr](https://pyconjp.atlassian.net/browse/ISSHA-3383)              | ¥15,000    |            | 例年通り                                                                                                                                                                                    |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3503)[Zoom Meeting](https://pyconjp.atlassian.net/browse/ISSHA-3503)        | ¥30,000    |            | 例年通り                                                                                                                                                                                    |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3123)[Freee](https://pyconjp.atlassian.net/browse/ISSHA-3123)               | ¥60,000    |            | 2025: ポイント充当前で52000円、ポイント充当9000円想定                                                                                                                                                      |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3122)[ZAPIER](https://pyconjp.atlassian.net/browse/ISSHA-3122)              | ¥40,000    |            | 例年通り                                                                                                                                                                                    |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3354)[dlvr.it](https://pyconjp.atlassian.net/browse/ISSHA-3354)             | ¥20,000    |            | 例年通り                                                                                                                                                                                    |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3581)[X](https://pyconjp.atlassian.net/browse/ISSHA-3581)                   | ¥5,000     |            | 例年通り、X Basicの年間(広告用)                                                                                                                                                                    |
|        | PayForex                                                                                                                  | ¥50,000    |            | 旅費支援の送金手数料 2000円(SWIFT) \* 25件 = 50,000円 相当。<br>2025年は、インドの送金は700円未満だが、事前送金テストで2回ずつ手数料がかかった。                                                                                            |
| 税金     |                                                                                                                           |            | ¥370,000   |                                                                                                                                                                                         |
|        | [](https://pyconjp.atlassian.net/browse/ISSHA-3254)[法人税](https://pyconjp.atlassian.net/browse/ISSHA-3254)                 | ¥70,000    |            |                                                                                                                                                                                         |
|        | [消費税](https://pyconjp.atlassian.net/browse/ISSHA-2056) 2025                                                               | ¥300,000   |            | 2025は赤字で0（むしろ還付）                                                                                                                                                                        |
| その他    |                                                                                                                           |            | ¥640,000   |                                                                                                                                                                                         |
|        | PyCon JP 地域開催サポ                                                                                                           | ¥200,000   |            | PyCon mini等の開催に使用。10万x2回<br>ピザ支援（1名x1500円上限）                                                                                                                                            |
|        | PyCon JP 地域開催 中止補填                                                                                                        | ¥300,000   |            | 確率的には使われない想定、発生確率は10%未満。1回分は積んでおく                                                                                                                                                       |
|        | PAO Silver sponsor                                                                                                        | ¥110,000   |            | 600Euro                                                                                                                                                                                 |
|        | 海外イベント参加お土産                                                                                                               | ¥30,000    |            | 3000円\*10回                                                                                                                                                                              |
| 主催事業   |                                                                                                                           |            | ¥1,852,000 |                                                                                                                                                                                         |
|        | PyCon JP 2026                                                                                                             | ¥0         |            | イベント単体でトントンを目指す(takanory                                                                                                                                                                |
|        | PyLadies Caravan                                                                                                          | ¥410,000   |            | +100,000円<br><br>PyLadies Caravanイベント：40万<br>\* 1開催10万（交通費8万、宿泊費1.5万、会場費0.5万）×4回分<br>　　※2026/02 1回開催済み（@福岡）<br>\* ステッカー：1万                                                              |
|        | PyLadies TA／講師派遣                                                                                                          | ¥100,000   |            | ±0円<br><br>PyCampTA参加または国内PyLadiesイベントへの講師派遣：10万<br>\* 1回5万（交通費3.5万、宿泊費1.5万）×2回分                                                                                                        |
|        | PyCamp                                                                                                                    | ¥482,000   |            | 開催：40万円 ( 8万円/1箇所)<br>ステッカー、Tシャツ : 2万円<br>広報 : 62,000円(Xの広告)<br>参考：<br>2022年: 5回 31万/38万円<br>2023年: 4回 25万/50万円<br>2024年: 4回 32万/42万円<br>2025年: 2回+ポスター印刷代 20万円/49万円<br>今年の開催見込み: 長崎、山口 |
|        | PyCamp Caravan                                                                                                            | ¥660,000   |            | \-20,000円<br><br>\* 協賛費: 210,000円<br>\* 出展: 420,000円<br>\* 香川、名古屋、島根、京都、KOF(予定)<br>\* 備品: 30,000円<br>\* チラシ、テーブルクロス(新規制作、既存クリーニング)                                                      |
|        | PyCon JP TV                                                                                                               | ¥200,000   |            | 昨年同様に10万円に加えて、地方からのライブ放送で10万円(交通費)を加えたい                                                                                                                                                 |
|        | PyCon JP イベント 遠方支援                                                                                                        | ¥0         |            | 2025年実績: 国内 43万円, 海外 286万円<br>（PyCon JP 2026 イベント内で検討するため、一社予算では0）                                                                                                                      |
|        | PyCamp / PyLadies 遠方支援                                                                                                    | ¥0         |            | 2025年実績: PyCamp 33.3万円, PyLadies 3.3万円<br><br>PyLadies 4万 x 5名: 20万円<br>Pycamp 4万 x 10名: 40万円<br>→これもPyCon JP イベント側に回してもよさそう                                                                 |
| 合計     |                                                                                                                           | ¥4,505,060 | ¥4,505,060 |                                                                                                                                                                                         |

* 議論
  * PyCon JP の遠方支援の予算項目がない(takanory)
    * PyLadies / PyCampの遠方支援だけではなく、PyCon JP全体の旅費支援も予算に含めてもいいのでは？(takanory)
    * PyCon JPの旅費支援を一社で持つと支援者の選定もAssociation側にゆだねるべきになるので微妙では？(terada)
      * 1人あたりの金額上限を下げて運営するかもしれないので予算減などについては検討できる(takanory)
      * スポンサー費獲得モチベーションとの連動性が気になる(shimizukawa)
        * とはいえ収入の見通しが立ったら追加予算検討も可能なため、連動を気にしすぎる必要はないかもしれない (shimizukawa
      * [PyCon JP 2026企画書](https://docs.google.com/document/d/15aUxh6iFGJEwihojonmmOtBFyy2Yk5cLPpMn6Mg9oCA/edit?tab=t.rmog8ephj6is#heading=h.5l8ibx9dqeli)
    * 今日のMTGだけで一社予算にもたせるかイベント予算を組むかを決められるものではなさそう。
      * EuroPythonでは対象者が国内か国外かを分けずに500EUR (takanory
      * 一社予算でもつ場合、支援金額の設計を一社で行えるというメリットはある(terada
      * 今後議論していきたい
  * PyLadies Caravan は昨年1名実績のため5名予算、PyCampは昨年実績に基づき10名予算をつける(1名上限4万)
    * この項目もPyCon JP全体の旅費支援にいれてもらうことはできないのか(jonas)
    * イベント側としてもまとめられるならまとめてもいいのでは(takanory)
      * 混乱してる参加者も過去多かった(yoshida)
    * 現在上限金額がPyCon JP旅費支援とPyLadies/PyCamp旅費支援で異なっているので、まとめられるのであればよいのでは(maaya)
    * PyCon JP 2026の予算として一つにまとめていく。まとめ方や運営方法は後日相談とする
  * 地域イベント開催サポート費が計上されていない(jonas)
    * 忘れていたので計上する

## PyCamp、PyLadies関連

### PyCamp状況報告(ryu22e、低、報告)

* 運営メンバー: ryu22e、yamate、nishimoto、kobatomo
* [Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP](https://www.pycon.jp/support/bootcamp.html)
* 2026年3月以降の開催見込み
  * 長崎（現地スタッフ: 平山さん）
    * 平山さんはryu22eの同僚
    * 4月のオンライン相談会にも来てくれた
    * 佐世保で開催したいとのこと
    * 今のところ具体的な動きはなし
  * 山口県周南市（しゅうなんし）（現地スタッフ: 中嶋さん）
    * 現地スタッフ受け入れ手続き進行中
    * 今仕事が忙しいので、2026年3月末から動ける見込みとのこと
* 山梨でやってみたい方がいるかも(takanory)

### OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)

* 運営メンバー: yoshi-tsukamo
* 出展済み
  * [OSC2026 東京春](https://event.ospn.jp/osc2026-spring/)
    * 2026/2/27(金)・28(土) 東京春
    * 駒澤大学
    * 28土曜日のみの参加
    * たかのりさん、塚本が参加しました
* 出展申し込み済み（期限が3/9までだったため）
  * [OSC2026 香川](https://event.ospn.jp/osc2026-kagawa/)
    * 2026/4/18(土)
    * e－とぴあ・かがわ
    * 西本さん参加予定
* 名古屋・島根が続きます

### PyLadies関係報告(maaya, 中, 報告)

* **PyLadies Caravan**
  * PyLadies Caravan in 福岡 2nd
    * 2月28日開催済
    * 参加者：12名 (参加率100％でした)
    * テーマ：データ加工＆Web可視化(Streamlit）
    * 参加者間でPyLadies Fukuoka立ち上げの動きあり
  * 金沢大学の学生さんからcaravanやりたい旨お問い合わせあり
    * 大学入試関係で冬は大学が使えない＆雪で大学にたどり着けないとのことなので春に開催の方向で調整中
      * Python文法初級 + Numpyハンズオン(仮)
    * PyCon JP 2025 でリアルご挨拶済み
  * PyLadies Caravan in 静岡の参加者からもPyLadies Shizuoka立ち上げの動き
    * PyLadiesへ支部申請中（承認待ち）
    * ロゴ作成済
    * 現在やりたいこと等検討中
* **その他PyLadies**
  * 4月に東京で入学式やります

### PyCon JP TV(terada、低、報告)

* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* <https://www.youtube.com/user/PyConJP>
* Web <https://tv.pycon.jp/>
* 60回配信済み
  * [#60: Pythonistaに聞く2025重大ニュースと2026の展望 - 2026-01-09](https://tv.pycon.jp/episode/60.html)
* 次回は、3月13日（金）予定
  * PyCon JP 2026 共同座長座談会
* 現在、月初の金曜日に実施しているが、火曜日などに変更する可能性を模索中
* ネタ募集中です(takanory
  * [開発系とイベント紹介系を軸に進めていくつもり](https://docs.google.com/spreadsheets/d/1N7QVU9uTcZeoHCrnzWw0LLZQ5lb82ocHopCbUO5biwo/edit#gid=0)
  * 特に技術ネタのアイデアが欲しい
* 2026予算規模
  * 2025と同等を希望。厳しいようなら地方遠征をなくすのはあり。(terada

## コミュニティー支援

### PyCon mini 東海 2025（shimizukawa、低、報告）

* [ISSHA-3534](https://pyconjp.atlassian.net/browse/ISSHA-3534)
* 開催報告blog:
  * 1/6 開催報告blog ✅️ [PyCon mini 東海 2025を開催しました！](https://pyconjp.blogspot.com/2026/01/pycon-mini-2025.html)
  * 2/6 会計報告blog: ✅️[PyCon mini 東海 2025 決算報告＆アンケート結果報告](https://pyconjp.blogspot.com/2026/02/pycon-mini-2025.html)
  * クローズ！🎉

### SciPyDataJapan2026 広報支援（shimizukawa、低、報告）

* [ISSHA-3665](https://pyconjp.atlassian.net/browse/ISSHA-3665)  （理事で合意し手続きを進行中）
* <https://scipydata.connpass.com/event/364718/>
* 日程: 2026年1月24日(土)
* 会場: 御茶ノ水ソラシティ
* Blog: アカウント付与済み、作成済み✅️
* メディア告知: 済み✅️
* 開催: 1/24 済み✅️
* 開催報告blog 未🌀

### PyCon mini Shizuoka 2026（shimizukawa、中、報告）

* [ISSHA-3813: PyCon mini Shizuoka 2026 支援（親チケット）](https://pyconjp.atlassian.net/browse/ISSHA-3813)
* <https://pycon-shizu.connpass.com/event/372943/>
* 日程: 2026年2月21日(土)
  * 無事に開催できました、ご支援ありがとうございました！(yoshi-tsukamo)
* 会場: 静岡市 コ・クリエーションスペース
* 支援
  * [ISSHA-3831: PyCon mini Shizuoka 2026 スポンサー 支払い](https://pyconjp.atlassian.net/browse/ISSHA-3831)済み✅️
  * [ISSHA-3829: PyCon mini Shizuoka 2026 イベントキャンセル保険の検討](https://pyconjp.atlassian.net/browse/ISSHA-3829)済み✅️
  * [ISSHA-3830: PyCon mini Shizuoka 2026 ピザ支援](https://pyconjp.atlassian.net/browse/ISSHA-3830)未🌀
  * ブログをこの後作成予定(yoshi-tsukamo)
    * ぜひ3月13日までに(terada)
      * 昨年 [PyCon mini Shizuoka 2024 continueを開催しました](https://pyconjp.blogspot.com/2025/03/pycon-mini-shizuoka-2024-continue-report.html)

### イベントキャンセル補填の整備 (shimizukawa、中、共有)

* [ISSHA-3829: PyCon mini Shizuoka 2026 イベントキャンセル保険の検討](https://pyconjp.atlassian.net/browse/ISSHA-3829)
  * Yutaro Ikeda さんにとりまとめ完了✅️
    * [PyCon JP Associationによるイベント保険](https://docs.google.com/document/d/1AjX2MvFP85HMPSx8ojnvcwVegjTJHrdOfZyf5GLpnU8/edit?tab=t.0)
  * [www.pycon.jp](http://www.pycon.jp)で公開準備中🌀
  * ブログ準備中🌀
  * 次回、予算を確保してから公開します(shimizukawa)

## 海外コミュニティ連携

### PAO(PythonAsia)関連(terada、低、報告)

* PyCon JPとして、PAOの年間Silverスポンサー(600Euro)になる。（2026年度予算が決まった）
* Jiraチケットを[teradaが]作って、誰かを担当者にする。
* JPからPAOへの支援として、年間スポンサーになることになった。

### 海外イベント参加予定

* この後は、PythonAsia(Philippines) / PyCon US / SG / Euroと続く
* 日本からスタッフのみなさんへのお土産が持って行くという動きが、アジア内で多く見かけるようになり一般化してきている。
  * 【決定】来年度は初期から予算を決めて3000円*10回とか実施する
    * 1回目は仮予算として3000円が決定している。
  * TODO: 予算申請する。(terada
    * 3万円

## その他

### PyCon JP共有インフラについて(yoshida、 中、報告)

* OS更新した。
  * <https://pyconjp.atlassian.net/browse/ISSHA-2482>
  * Debian GNU/Linux 13 に更新した。
* 現状、2024以降はダイナミックコンテンツのママ
  * <https://pyconjp.atlassian.net/browse/ISSHA-3530>
* pyconjpbot
  * <https://pyconjp.atlassian.net/browse/ISSHA-3528>
  * 全面刷新に着手。speckitの練習がてらがんばる予定(takanory

### CoC関連  (maaya、 低、なし)

* 特になし

## 次回

* 運営会議#81
  * 2026年5月26日(火) マイクロソフト
  * <https://pyconjp-staff.connpass.com/event/387756/>
  * 議題
    * PyCon JP 2026 イベント -> 今年は2025より2ヶ月早い
    * PyCon JP 2026 遠方支援 -> 別枠でMTG実施したほうがよさそう
    * PyCon JP 2027 場所、座長募集

