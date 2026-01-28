# 2026年1月19日(月) 一般社団法人PyCon JP Association運営会議#78

* 日時: 2026年1月19日(月) 19:30-21:00
* 場所: CMSコミュニケーションズ、Zoom
* 参加者 <https://pyconjp-staff.connpass.com/event/378400/>
  * 理事: takanory, shimizukawa, yoshida, terada, jonas, maaya
  * オブザーバー: ryu22e, yoshi-tsukamo, kanan, sano

## PyCon JP

### PyCon JP 2025(nishimotz、高、報告)

* 残タスクがあるが、進行していないものがある。(terada
  * スタックしている状況だと思う。
  * クリティカルな課題を把握できているか？(takanory
    * わかっていない状況だと思う(terada
    * terada or yoshidaが主導して日程調整して、座長やリーダー的な人を集め、まずは残件を洗い出す作業をした方がいいのでは。(takanory
      * なんらかの働きかけは必要。この方法が一番良いのでは(shimizukawa
      * オンライン上で作業会をやるしかないかな(yoshida
    * **TODO:** 調整して実施する(terada

### PyCon JPの開催の最低要件(terada、低、報告)

* 最終版とした: [PyCon JPの構成要素(案)ISSHA-3491](https://docs.google.com/spreadsheets/d/131WSpp5mhy1JzdFcZOPofc3L-Zt3-CwzaGOC5erzNQQ/edit?gid=0#gid=0)
* 2026チームに共有した
* 前回議論した、このドキュメントの公開については無しで進める
  * 前回議事録より: 公開しますか？してもいいと思うけどMUSTに縛られると動きづらくなるのでそれは避けたい気持ちがありますね

### PyCon JP 2026(sano、takanory、中、報告)

* 会場
  * 広島国際会議場
* 会場利用申請
  * 2026年8月20日(木) 午後から準備、ヒマワリ（2025スポンサーブース）のみ18時から
  * 2026年8月21日(金)、22日(土) 全館
    * 全館を借りていると廊下が結構自由に使えるはず(terada
  * 2026年8月23日(日) 会議運営事務室、ヒマワリ
    * 会場の使い方はまだまだこれから
* PyCon JP 2026のJIRAスペースを作った
  * [ISSHA-3768: PyCon JP 2026用JIRAの準備](https://pyconjp.atlassian.net/browse/ISSHA-3768)
    * 今は共同座長のみが使用している、今後主催メンバーが使用していく予定
  * <https://pyconjp.atlassian.net/jira/core/projects/HRS/board?filter=&groupBy=status>
  * 新規に作ったらカテゴリの設定方法がわからない...(takanory
    * しょうがないのでカスタムフィールドでカテゴリを作った
    * JIRA APIで値が取得できることは確認した
* [HRS-4: PyCon JP 2026の方向性まとめ](https://pyconjp.atlassian.net/browse/HRS-4)
  * スプシでやること、やらないことを擦り合わせ中→あと1回で「必須」「やるべき」は終わる予定
  * [PyCon JP 2026でやりたいこと、やらないこと、維持するとこ](https://docs.google.com/spreadsheets/d/1nvjmebcVOhvXQWcK4V29Qu3mRijRhjQLhEHhJdpBmlE/edit?gid=0#gid=0)
  * その後企画書を作っていってタスク化していく予定
    * [HRS-16: 企画書の作成サポートするAIの運用を行う](https://pyconjp.atlassian.net/browse/HRS-16)
    * 作ってみてるドキュメント: [pyconjp2026 企画書AIサポートを考える](https://docs.google.com/document/d/1wnhi0N2Y0sqQvyRhoMFXdA5O5sdE3fFSJ1i1dX6E1GU/edit?tab=t.mart6kjjfy78)
* 質疑応答
  * 主催メンバーは何名くらい登録されていますか？(terada
    * Slackチャンネル上で22名。takanory, sanoも含む(takanory
    * 内アクティブ率は 50%程度 (sano
    * 学生がそれなりに多い。(sano
  * 主催メンバーの経験者率は？ (terada
    * 90%くらい?(takanory
    * 2025の主催メンバーが多い (sano

### PyCon JPの一般社団法人とイベントチームの役割分担について(terada、中、相談

* 一社として2026イベントチームと話し合いして、役割分担を検討するか？
* だれがこの件を引き継ぐのか？またはteradaがこのまま対応していくか？＜ここは相談したい
* teradaさんはどうしたいの?(takanory
  * やった方がいいと思う。主導する気もある(terada
* sanoさんはどう思います?(takanory
  * 一社が役割分担として負担するのはありがたいと思う。やってほしい。内容としてなにをするのかは考える必要がある。役割分担のイメージはわいていない。2026としては外部の業者に作業を依頼することも考えている(sano
* takanoryさんの意見
  * 役割分担の検討はできるなら検討を続けたいが、うまくいくかわからない。
  * とはいえ「やりたい人がいるなら、やるでいいじゃん」って思っている。うまくいかないかも知れないけどそれはそれでしょうがない
* これを実現するとなると、大きな決め事になると思っているが、みんながどう思っているかの反応がないのであまり期待されていないように感じている(terada
* 役割分担としての分担先のイメージが人によって違うのではないか。遠方支援のところを一社がやる。イベント会社に依頼をする(yoshida
* 業者は1つのオプションであって、それだけじゃなくてイベント主体を一社がする、座長の教育みたいなこととかも考えるとか(terada
* 難しいと思うのは、イベントチームからのニーズは出てきにくそう。どういう形になるかのイメージがわいていない気がする。ただ、イベント側の負荷が高いという状況をなんとかしようということが発端なので、話を進めるのはよいと思う(shimizukawa
* 外部の業者へ依頼するのはイベントチームから行うことをやるべきと思っていた(sano
* PyCon JPイベントの運営がいろいろ大変なのは合意している(takanory
* 話の方向性としては座長の権限を減らすとなるとかもあるので、慎重に進める必要があると考えている(terada
* 人によっては縛りが増えたと思ったりするし、逆に楽になったと思うかもしれない(shimizukawa
* イベントのタスク全部は一社でできない。一社でできるタスクを分担したらいいのかと思うので、そういう**「できるタスク」のリスト**を作ったらよいのでは。例えば遠方支援。今後の座長にそのリストを伝えて、座長に選んでもらうというアイディアはどうか(jonas
* 会場とのやりとりはイベントのチームに近いところじゃないとできないのではと感じている。遠方支援は一社でお世話になったりしていたので、手順としてできているものはお願いしたいかも(sano
  * 遠方支援は過去の経緯があり、pycampの支援とイベントの支援で窓口が別で混乱していたので、窓口をまとめた。これはイベントからタスクをとった状態とも言える。1社がやるべきと思って変更したわけではない(shimizukawa
* まずはリストを作ってみるのはありかも知れない。会計、受付など。すでに会場契約は一社で行っている(terada
* 一般的な会社がバックオフィスを分社化したことがあったが、その形式が真似（参考）できるのかもしれない会計や人事(スタッフ受け入れ)など(yoshida
* **TODO**: まずは「一社でできる/できないタスクリスト」を作って2026チームと相談できそうなので進めている(terada
  * 会場契約はすでに行っている
  * 長い目で試してみる
  * JIRAを作って進める
  * これはやらない方がいい、少し手伝えるとかも書くとよい(jonas
  * イベントの要件のリストを元に書いていくといいのでは(takanory

## 一社運営関連

### 総会準備

* [ISSHA-3810: 社員総会2026年2月の開催](https://pyconjp.atlassian.net/browse/ISSHA-3810)
* 行政書士塩野先生に開催通知の作成依頼メールをしているけど反応無し、今日の10時に再度メールした
* **TODO**: 理事の追加募集をするブログを書く(takanory

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

* [https://pyconjp.atlassian.net/browse/ISSHA-3638](https://pyconjp.atlassian.net/browse/ISSHA-3638) 
* 松山さんという専門家に業務委託をして、一緒に月2回ペースでMTGを実施して進めている
* Ikeさんにも参加いただき、現在は、teradaとtakanoryも入って3名で対応している
* 最初の対策方針案を理事で合意した。
  * [情報セキュリティ対策のための方針](https://docs.google.com/document/d/1qjlORbB3kt4nyyoIK9CA23N4zAXBYhBRXG96l8_dKvE/edit?tab=t.0#heading=h.8n1tqv9kmmjt)
  * 具体的な作業（対策など）を進めていく予定
* Google Workspaceのアカウント作成を早めに進める予定 (terada
  * **TODO**: ルールを決めてアカウント作成

## 会計関連

### 2025年 遠方支援(shimizukawa、低、共有)

* **Done:** 感想をblogにした（2025/12/22）
  * [PyCon JP 遠方支援を支える技術; Pretalx & PayForex編](https://pyconjp.blogspot.com/2025/12/technology-for-pycon-jp-travel-support-pretalx-payforex.html) 
* 次回に向けてメモ
  * [ISSHA-3839: PyCon JP 2026 遠方支援](https://pyconjp.atlassian.net/browse/ISSHA-3839)に転記済み 

### 2026年 決算(shimizukawa、高、報告)

* [ISSHA-3809: 2025年 決算](https://pyconjp.atlassian.net/browse/ISSHA-3809)
  * ✅[ISSHA-3828: 2025年 支払調書送付](https://pyconjp.atlassian.net/browse/ISSHA-3828)
  * [ISSHA-3838: 2025年末時点の未収金、未払金まとめ](https://pyconjp.atlassian.net/browse/ISSHA-3838)
* 会計事務所さんと相談を進めています(shimizukawa
* 決算のことを考えるとイベントチーム側でJIRAと証憑とかをどういう風に管理するといいか、は先にルールを確認したい(takanory
  * 銀行にログインしてJIRAチケット番号を書くとか(shimizukawa
  * **TODO**: やり方はちょっと整理したい。イベントチームでお金が動き始める段階で、どういうルールだと運用しやすいか相談したい(takanory
    * 今回の決算で突き合わせに困ったところをメモっておきます(shimizukawa

## PyCamp、PyLadies関連

### PyCamp状況報告(ryu22e、低、報告)

* 運営メンバー: ryu22e、yamate、nishimoto、kobatomo
* [Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP](https://www.pycon.jp/support/bootcamp.html)
* 2026年1月以降の開催見込み
  * 長崎（現地スタッフ: 平山さん）
    * 平山さんはryu22eの同僚
    * 4月のオンライン相談会にも来てくれた
    * 佐世保で開催したいとのこと
    * 今のところ具体的な動きはなし
  * 山口県周南市（しゅうなんし）（現地スタッフ: 中嶋さん）
    * 現地スタッフ受け入れ手続き進行中
    * 今仕事が忙しいので、2026年3月末から動ける見込みとのこと

### OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)

* 運営メンバー: yoshi-tsukamo
* 出展申込済み
  * [OSC2026 東京春](https://event.ospn.jp/osc2026-spring/)
    * 2026/2/27(金)・28(土) 東京春
    * 駒澤大学
    * 28土曜日のみの参加
    * たかのりさん、塚本の予定
      * 28は福岡pyladiesなんだなー(maaya
* 2025振り返り＆2026活動方針ミーティング
  * 1/20(火) 20:00〜
  * [https://pyconjp-staff.connpass.com/event/381165/](https://pyconjp-staff.connpass.com/event/381165/)
  * どの会場に行くか、どんなブースにするかなどを話し合いたい

### PyLadies関係報告(maaya, 中, 報告)

* **PyLadies Caravan
  * PyLadies Caravan in 静岡 12月13日【開催済】
    * 地元スタッフ：mizukiちゃん、yoluさん (サポート佐野さん)
    * テーマ：データクレンジングと可視化のハンズオン
    * 場所：[静岡市 コ・クリエーションスペース](https://coc-shizuoka.jp/about/)
    * 参加人数7名
    * [PyCon JP Blog: PyLadies Caravan in 静岡 を開催しました！](https://pyconjp.blogspot.com/2025/12/plcaravan-shizuoka.html)
  * PyLadies Caravan in 福岡 2nd 2月28日
    * 地元スタッフ：みゆきさん、Ziiさん
      * みゆきさんcaravan広島＆PyCon JP 2025で直接MTG済み、ZiiさんPyCon JP 2025でリアルご挨拶済み
    * 場所：[Engineer Cafe｜福岡天神に誕生、エンジニアのためのハッカースペース](https://engineercafe.jp/ja/)
    * 宿泊が予算より高い金額で予約
      * kanan（福岡滞在中）分の交通費がかからないので結果予算内
  * 金沢大学の学生さんからcaravanやりたい旨お問い合わせあり
    * 大学入試関係で冬は大学が使えない＆雪で大学にたどり着けないとのことなので春に開催の方向で調整中
    * PyCon JP 2025 でリアルご挨拶済み

* その他PyLadies
  * [PyLadiesCon](https://2025.conference.pyladies.com/en/) 今年もありました(12/6)
* 次の一手をかんがえねば

### PyCon JP TV(terada、低、報告)

* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* <https://www.youtube.com/user/PyConJP>
* Web <https://tv.pycon.jp/>
* 60回配信済み
  * [#60: Pythonistaに聞く2025重大ニュースと2026の展望 - 2026-01-09](https://tv.pycon.jp/episode/60.html)
* 次回は、2月6日（金）予定
  * 開発関係の内容にする予定
* ネタ募集中です(takanory
  * [開発系とイベント紹介系を軸に進めていくつもり](https://docs.google.com/spreadsheets/d/1N7QVU9uTcZeoHCrnzWw0LLZQ5lb82ocHopCbUO5biwo/edit#gid=0)
  * 特に技術ネタのアイデアが欲しい
* 質疑応答、コメント
  * 金曜は出かけることが多い→月曜はありかも。土日は昼がうれしい
  * 出張放送はまだ1回しかできていないので、また開催して練度を上げていきたい(takanory
  * PyCon JP 2026座長をゲストにする会はやるかも(terada

## コミュニティー支援

### PyCon mini 東海 2025（shimizukawa、低、報告）

* [ISSHA-3534](https://pyconjp.atlassian.net/browse/ISSHA-3534)
* 開催報告blog: 
  * 1/6 済み✅️ [PyCon mini 東海 2025を開催しました！](https://pyconjp.blogspot.com/2026/01/pycon-mini-2025.html) 
  * 会計報告blog: 未🌀

### SciPyDataJapan2026 広報支援（shimizukawa、低、報告）

* [ISSHA-3665](https://pyconjp.atlassian.net/browse/ISSHA-3665)  （理事で合意し手続きを進行中）
* [https://scipydata.connpass.com/event/364718/](https://scipydata.connpass.com/event/364718/)
* 日程: 2026年1月24日(土)
* 会場: 御茶ノ水ソラシティ
* Blog: アカウント付与済み、作成済み✅️
* メディア告知: 済み✅️
* 開催: 1/24
* 開催報告blog 未🌀

### PyCon mini Shizuoka 2026（shimizukawa、中、報告）

* [ISSHA-3813: PyCon mini Shizuoka 2026 支援（親チケット）](https://pyconjp.atlassian.net/browse/ISSHA-3813)
* <https://pycon-shizu.connpass.com/event/372943/>
* 日程: 2026年2月21日(土)
* 会場: 静岡市 コ・クリエーションスペース
* 支援予定
  * [ISSHA-3831: PyCon mini Shizuoka 2026 スポンサー 支払い](https://pyconjp.atlassian.net/browse/ISSHA-3831)
  * [ISSHA-3829: PyCon mini Shizuoka 2026 イベントキャンセル保険の検討](https://pyconjp.atlassian.net/browse/ISSHA-3829)
    * Yutaro Ikeda さんにとりまとめ依頼中
    * [PyCon JP Associationによるイベント保険](https://docs.google.com/document/d/1AjX2MvFP85HMPSx8ojnvcwVegjTJHrdOfZyf5GLpnU8/edit?tab=t.0) 
    * 予算をどうする？
      * 仮予算の10万円を充てるか・・検討します(shimizukawa
    * 情報まとまったらぜひ[www.pycon.jp](http://www.pycon.jp)で公開して、ブログでもアピールしたい
  * [ISSHA-3830: PyCon mini Shizuoka 2026 ピザ支援](https://pyconjp.atlassian.net/browse/ISSHA-3830)

## 海外コミュニティ連携

### PAO(PythonAsia)関連(terada、低、報告)

* PAO (Python Asia Organization) の活動が始まっている。
  * [PyCon JP Blog: PythonAsia (カンファレンス) の紹介とOnline Charity Talk H2イベントの紹介](https://pyconjp.blogspot.com/2025/12/pythonasia-online-charity-talk-h2.html)
  * PythonAsia（カンファレンス）は3月にフィリピンで開催
  * オンラインイベントを1月末に開催
  * 宣伝協力をお願いします。
* 一社PyCon JP AssociationとしてPAOに協力できることなどのアイデアがあれば知りたい(takanory
  * Python PH(フィリピン)は年間Silverになっていて継続の予定。
  * PyCon JP Associationとしても年間でスポンサーしてもらえるとうれしい(terada
  * [https://github.com/PythonAsiaOrganization/public-docs/blob/main/sponsorship.md](https://github.com/PythonAsiaOrganization/public-docs/blob/main/sponsorship.md) 
    * Silver 600 Euro
    * TODO: 予算申請する。(terada

### 海外イベント参加予定

* この後は、PythonAsia(Philippines) / PyCon US / SG / Euroと続く
* 日本からスタッフのみなさんへのお土産が持って行くという動きが、アジア内で多く見かけるようになり一般化してきている。
  * 【決定】来年度は初期から予算を決めて3000円*10回とか実施する
    * 1回目は仮予算として3000円が決定している。
  * TODO: 予算申請する。(terada

## その他

### 運営メンバー (terada、 低、相談)

* 運営メンバー入りの後にタスクを進めてもらったり、一緒に作業したりする流れをもう少し整備したい。
* Ikedaさんには、mini Shizuokaの保険について取りまとめてもらっている
* 2026決算を一緒にやるとか?(takanory
  * Makinoさん興味ありっぽい(takanory
  * **TODO**: タスクが発生したら声をかける(shimizukawa

### PyCon JP共有インフラについて(yoshida、 中、報告)

* OS更新した。
  * [https://pyconjp.atlassian.net/browse/ISSHA-2482](https://pyconjp.atlassian.net/browse/ISSHA-2482)
  * Debian GNU/Linux 13 に更新した。
  * 固定IPエラスティックIPにはできてない
    * AWSメンテナンスでIPが変わる可能性がある
    * [https://pyconjp.atlassian.net/browse/ISSHA-3529](https://pyconjp.atlassian.net/browse/ISSHA-3529)
    * 変更するとconnpassのAPI制限の再申請が必要
    * ↑connpass API v2ではAPIキーがあればよいので、固定IPが不要になった。APIキーは1passwordに書いてある(takanory
* 現状、2024以降はダイナミックコンテンツのママ
  * [https://pyconjp.atlassian.net/browse/ISSHA-3530](https://pyconjp.atlassian.net/browse/ISSHA-3530)
* pyconjpbot
  * [https://pyconjp.atlassian.net/browse/ISSHA-3528](https://pyconjp.atlassian.net/browse/ISSHA-3528)
  * 全面刷新に着手。speckitの練習がてらがんばる予定(takanory
* 古いインスタンスについて
  * [https://pyconjp.atlassian.net/browse/ISSHA-3529](https://pyconjp.atlassian.net/browse/ISSHA-3529)
  * インスタンス実行で費用がかかっているので、停止した

## 次回

* 総会 & 運営会議#79
  * 2026年2月26日(木) [https://pyconjp-staff.connpass.com/event/379087/](https://pyconjp-staff.connpass.com/event/379087/)
  * 総会と予算の話がメインとなると思います。他の事業の話とかはちょっとできないと思います。
