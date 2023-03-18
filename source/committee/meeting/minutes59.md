# 2023年3月6日(金) 一般社団法人PyCon JP Association運営会議#59

* 日時: 2023年3月6日(月) 19:30-21:30
  * <https://pyconjp-staff.connpass.com/event/276461/>
* 場所: Zoom
* 参加者
  * 理事: takanory, yoshida, shimizukawa, jonas, terada
  * オブザーバー: peacock, ryu22e, yoshi-tsukamo, kanan,kobatomo

```{contents}
:local: true
```

## 課題のレビュー {#課題のレビュー}


* 予算の議論に時間を使いたいので、クリティカルなタスクだけ確認(takanory
* [PyCon JP Association(一社のみ)](https://pyconjp.atlassian.net/issues/?filter=11500)の課題一覧
* [PyCon JP Association(一社以外)](https://pyconjp.atlassian.net/issues/?filter=15948&jql=project%20%3D%20ISSHA%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20component%20in%20(EMPTY%2C%20%22Pycamp%20Caravan%22%2C%20%22PyCon%20JP%20TV%22%2C%20%22Python%20Boot%20Camp%22)%20ORDER%20BY%20due%20ASC%2C%20component%20ASC%2C%20updated%20DESC)の課題一覧

## 議事の進行(terada、高、相談)

* 議事の進行は、今まで寺田が進めてきたが、たかのりさん or 吉田さんが進める形が良いかと思う。(terada
  * 今日は私がやるつもりです(takanory
* 議事録については、進行役とは別の方々でやったほうがスムーズだと思う。(terada
  * がんばって書いてみようかなぁ(yoshida
* 理事で持ち回りにするのはどうかなと思った(takanory
  * 持ち回りを試すのはいいのでは(yoshida
  * どっちでもあり(terada
  * ありだと思います(shimizukawa
* jonasは厳しいのであれば対象外でもよいかな(takanory
  * ありがたい(jonas
* 代表理事が変わったことで、たかのりさんが担当していたものを、別の担当にしたほうが良いかと思う。(terada
  * 例えば、PyCon JP TVは、寺田が引き継ぐとか
  * 今のところどっちでもOK。引き継ぐのはありだと思います(takanory
  * 逆に今までがどうだったかわからない(yoshida
  * 予算、理事改選などをteradaが担当していた。pycampとかTVとか減らした方がいいんじゃないかなと思っている(terada
  * 私はありだと思う(takanory


## PyCon JP


### PyCon JP 2022(selina、高、報告)



* 無事、カンファレンス終了しました。
* 会計関連も終わりました。
  * 詳細、吉田さんにお任せしました。
  * 2022の会計関連をご報告おねがいできますでしょうか(selina
  * **TODO**: 収支報告Blogを書く
    * Blog書きます。固定費と変動費。スポンサー収入、参加者収入の粗い集計をした。(yoshida 
    * 満額に近い感じでスポンサーは集まったが、全体としてはトントンで納まったので、固定費が高かったと思われる(yoshida
    * 全体は黒で一社では赤でしたと報告しようかと(yoshida
    * そこまで書かなくてもいいのでは(terada
    * 一社のことは書かなくてもいいのでは。イベント単体では黒字だったので、加える話としてはとくに報告しなくてよいのではないか(shimizukawa
    * 同意です。「それを伝えて、どう思ってほしいのか」がないなら言わなくていいと思う(takanory
    * 「スポンサーもっと来てほしい」「去年参加費を値上げしたが、その分サービスにかかっている、還元されている」(yoshida
    * 伝え方難しそう(terada
    * 値上げしたのでイベントが黒字になった、来年は安くなってもいいのではないかと思っている人がいるかもしれない。来年は同じくらいの値段で進めるよと伝えるとよいのではないか(jonas

### PyCon JP 2023(selina、低、報告)

* APACから連絡あり、正式にJPメンバーが動いていく
  * **PyCon APAC 2023**として進めて行く
  * 3月23日(木)にJPの全体会があるので、その前までに、APAC メンバーと打ち合わせし、要望・希望などを聞いてできる範囲で落としていく。
    * APACメンバー(iqbalさん)との打ち合わせ: 3/10 or 13 or 14
    * **TODO**: ミーティング呼んでください!!!(jonas→peacock
  * 要望が難しいものは相談して調整しつつ、JPメンバーが動きやすい方向へ持っていく。
    * 無理しない方がよいと思っている。MUSTなのかとかも確認した方がよさそう(takanory
    * 開催するのは日本のチームなので「日本のチームがどうしたいか、どうできるか」を考えるのがよいと思う。聞きすぎなくて良い、今までもそうしてきた認識(terada
* 会場について
  * TOC有明コンベンションホール
    * <https://www.toc.co.jp/saiji/ariake/>
    * 東京都江東区有明3丁目5番7号
  * 日程候補：2023年10月26日（木）～29日（日）
    * **TODO**: 会場不要なところは削る
  * 内容とすりあわせて時間と場所削減したい
    * 半年前(4/24)迄にTOC連絡
    * **3月末くらいには(最大規模見積もりで)FIXする予定**
* デザイン・スポンサー・コンテンツも走り出している(peacock
* チームとか集まり、立ち上がりどうですか?(takanory
  * 座長: selina、副座長: peacock, ainamori、アドバイザー: yoshida
  * デザイン　nanaさんがやりはじめている
  * スポンサー　初期構築を副座長レベルでやるつもり。稲森さんとかと合わせてやる(peacock。担当者がいないのでヤバそう。(yoshida
  * コンテンツ: 去年のリーダーが継続リーダーはできないが、アドバイザーで動いて貰えそう。昨日キックオフをした
  * 多少形はできてきたけど、手が少し足りない感じ?(takonary
  * 会場はメンバー集まっている。(yoshida
  * システムチームも去年のメンバーが少しいるが、もう少し欲しい(yoshida)
  * 個別の声かけとかもしていった方がよさそうですねー(takanory
    * selinaさんが合間を見つつやっている(peacock
  * selinaがメディアのチームを作りたいという話をしている(yoshida
  * 結構はじめましての方が来ているので、オンボーディングをやっていく必要がありそう。(peacock
    * 1on1とかやっていきたい(peacock
    * オンボーディング大事ですね(takanory

## 会計

### 消費税インボイス制度の申請(terada、低、報告)	


* 登録手続き完了
* **適格請求書発行登録番号**はこちら
  * [一社PyCon JP 住所・銀行口座](https://docs.google.com/document/d/1rNk9yeaRVNjIW6X_2TSi-lZDWdZHgiyvdxLCABZkWEE/edit#)
* 2023年10月以降は請求書とかに必要となる(terada
* イベントの会計まわりの人にもインボイス制度を理解してもらう必要がありそう(takanory
  * **TODO**: 勉強会の開催とかを検討した方がよさそう(terada, shimizukawa
  * PyCon JP 2023が忙しくなる前にはやりたい(takanory

### 2023予算の方向性(takanory、高、相談)

* 予算の方向性としてどのように使うかを議論したい(takanory
  * 理事や担当者がどう考えているか、意見を出し合ったほうが良いと思う。（takanory
* 目的別だと以下のような感じかなと(takanory
  * 参考: [決算報告 — PyCon JP](https://www.pycon.jp/annualreport/index.html)
  * 地方でのPython盛り上げ(73万円)
    * Python Boot Camp
    * Python Boot Camp Caravan
    * 地域PyCon・コミュニティ支援
  * ジェンダーギャップの解消(11万円)
    * PyLadies Caravan
    * →ここ増やしたいけどまだやれることが思いついていない(takanory
  * オンラインでのつながり?(17万円)
    * PyCon JP TV
    * Python Charity Talks?
  * 法人固定費(95万円)
    * 会計、行政書士、法人税、消費税
    * システム費
* どこに力を入れるのか、こういう意義もあるんじゃないか?などを議論したい(takanory
  * Iqbalさんから上がってくるD&I、APACのキーワードがあるが、PyCon JPはそれより手前「ジェンダーギャップ」「地域コミュニティのつながり」の方がコロナで少し戻ってしまったように感じることもあり、引きつづきやっていくのがよいのではないか。広げすぎると中途半端になるのでは(shimizukawa
  * コミュニティ支援は増やして良い。ジェンダーギャップはアイデアが浮かんでいない。Charity Talksはネタがあれば開催で良いのでは、PSFの会計は前ほどやばくなさそう。消費税は赤字決算なら還付ができるのではないか(yoshida
    * 消費税の件は別途でよさそう(takanory
  * 並べてみるとバランスがおかしい。ジェンダーギャップについてもっと力を入れたい。お金でできることがあるならやった方がよい。Charity Talksは年に1回やるといいと思う、PSFのつながりが良くなる。いいイベントだと思う(jonas
  * 資産の10%~20%くらい、収益につながらない新しい物に使っていいのではないか。適切なものに使っていくことが重要。適切に意義のある活動に使うべきではないか。今年なら資産の15%(約230万円)を固定費(80万)含めて使用してよいのではないか。減らすよりは増やす方がいいのではないか。バランスは変えずにもっと入れてよいのでは(terada
  * ジェンダーギャップの解消はもうちょい予算かけてもいいのではと思っているが、推進する女性がもっといないといろいろできなそうな気持ちもある。TVは他に比べるとそこまで予算かけてないので、このままでもいいんじゃね?って気もしている。PyCon JP 2023は200万円の黒字になるとうれしいなー(takanory
  * コミュニティ支援。オフラインでの開催がようやくできるようになってきたので、これから力を入れていきたい。コロナ禍で3年たっているので、オフラインで集まってわいわいする楽しさを忘れていそう。若い人は知らない可能性もある。「こういう文化がある」ということを伝えるためにもコミュニティ支援に力を入れたい(ryu22e
  * 地域でコミュニティをやっている。3年オフラインでやれていないので、元に戻るきっかけを作れるとよい。PyLadies Caravanがもっとたくさんあるといいなと思っている(yoshi-tsukamo
  * PyCon JP TVの視聴者が固定化されていることに対して、何かできないかなと思っているが(ジャストアイデア)でTwitter広告を打ってみてもいいかな。**海外特別遠方支援・海外渡航支援**(日本に来る人、日本から出る人両方)は今年APACなのでやりたい。地域PyCon, PyCampはCOVID-19が落ち着いてきたのもあり、2019と同じくらいの金額積んでもいいかな。ここもTwitter/Facebook広告打ち所? 収入は2023の予算設計を根本的に見直して2,300黒まで持って行きたい、副座長2年目の個人的な目標にしている(peacock
  * コロナで落ち込んで、去年PyLadies Caravanは2回開催できた。Boot Campを追随して開催していきたい。お子さんがいて開催が躊躇されやすい。今年は初めての地域で開催したい。PyCon JPにPyLadies Caravanからやってくることをしたい。PyCon JP TVとかは「前見て面白かったけど、時間忘れて見れない」とかがあるので、告知を工夫するとよいのでは(kanan
    * 他のメンバーが「ジェンダーギャップ」の解消のところはどう思いますか?(takanory
    * 別のやり方もあるかもしれないが、今はPyLadies Caravanで精一杯(kanan
  * Python Boot Campは継続してやっていきたい。ここから5年を考えると講師を増やしたい。PyLadiesの人も講師になれるロードマップがあるとよいのでは(kobatomo
* まとめ
  * 全体的には既存の予算ベースでより活動を活発にやりたいという感じ(takanory
  * ジェンダーギャップの解消には力を入れたいが、回す人やアイデアが今は足りていない感じ(takanory
* 前回の社員総会で「あんまり赤字を出したくない」と言っていたが、難しい(terada
* 「赤字を出さない」と考えちゃうと固まってしまう。ロードマップを決めていないので、「このくらいまでの赤字を許容する」という話がないのが問題の一つかなと思う(shimizukawa

### 予算(terada、高、相談)

* 予算申請を各パートから出してもらう
* 急ぎで検討すべき予算があるか？
* 半分に割って全部を決めないという方針もある。PyCon JP 2023が金額的に順調に行くのかを見て、残りの予算を決めるのはどうか?(terada
  * 現時点では予算としては半分or 2/3とかにする感じ?(takanory
  * そのあたりの見通しがつくのは9月くらい?(shimizukawa
  * もう少し早く見通しは立つのでは無いか。7月くらいには見えるのでは無いか(yoshida
  * 2/3の予算をたてて、スポンサーがつかなくてもある程度の赤字で落ち着けるのでよいのではないか(shimizukawa
  * **TODO**: 予算の見直しを7月後半くらいに行う(takanory
  * Python Charity Talks の開催は?(shimizukawa
    * 必要経費(Zoom、PayPal手数料、振込手数料)を全て引いて寄付するのはどうか?(takanory
    * それなら予算ゼロで実施できる。よさそう(shimizukawa
* 消費税について(shimizukawa
  * 消費税も一社としては予算計上したほうが良いんだろうなと思いました。今回相談したい。PyCon JP イベント分の予算は毎年計画していなくて、消費税もその一部として計画外になっていると思います。でも、消費税は2022年度分は16万円超あり、イベント会計分では計上されていません。これが「イベント単体に比べて一社の支出が超過している」要因の1つな気もします。(shimizukawa
  * なぜ赤字なのに消費税がかかっているのかは気になる(terada
  * 2022年度は収入と支出はいくらか?(terada
    * 収入: 22,386,268円、支出: 22,924,492円
    * [第10期決算報告書（2022）.pdf](https://drive.google.com/file/d/1C4-9Ptf0_4cvBUHgjHwNeY0wtETTDHd1/view)
    * 消費税が164,500円となっている(shimizukawa
    * この金額はおかしいのではないか(terada, yoshida
    * **TODO**: 別途ミーティングを行う(terada

#### 予算申請

* 主催事業
  * 当初は「減額後」の予算で進める。2023年7月後半に見直す

| 項目 | 金額 | 減額後 | 備考 |
| -- | -- | -- | -- |
| PyCon JP | 0円 | - | 例年通り、収支トントンを目指す
| Python Boot Camp | 500,000円 | 350,000円 | |
| 遠方支援 | 450,000円 | 300,000円 | |
| Python Boot Camp Caravan | 620,000円 | 400,000円 | |
| PyLadies Caravan | 300,000円 | 200,000円 | |
| PyLadies->PyCamp TA参加 | 150,000円 | 100,000円 | |
| PyCon JP TV | 120,000円 | 80,000円 | |
| Python Charity Talks | 0円 | - | 収入から経費を引いて寄付
| 予備予算 | なし | | 項目削除
| 合計 | **2,140,000円** | **1,430,000円** | |

* 法人諸経費

| 項目 | 金額 |
| -- | -- |
| 会計事務所 | 630,000円 |
| 行政書士（塩野先生） | 60,000円 |
| 法人税 | 70,000円 |
| 消費税 | 170,000円 |
|  合計 | **930,000円** |

* システム費

| 項目 | 金額 |
| -- | -- |
| さくらインターネット | 4,000円 |
| AWS | 30,000円 |
| Flickr | 20,000円 |
| Zoom Meeting | 10,000円 |
| Freee | 30,000円 |
| ZAPIER | 30,000円 |
| 合計 | **124,000円** |

* コミュニティサポート
  * PyCon JP地域開催サポートプログラム 発生時検討
* APAC支援
  * PyCon APACへの支援	0円
* スポット
  * 弁護士への相談		100,000円
    * プライバシーポリシーの作成
  * 海外渡航支援			発生時検討
  * 海外特別遠方支援		発生時検討


## PyCamp、PyLadies関連

### PyCamp状況報告(ryu22e、低、報告)

* 運営メンバー: ryu22e、kobatomo
* [Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP](https://www.pycon.jp/support/bootcamp.html)
* 
* **2023年予算概算申請**
* [01]Python Boot Camp: 50万円
  * 7回の開催を想定 (1回あたり 7 万円)
* [02]PyLadies、PyCamp 参加者向けPyCon APAC遠方参加者支援：45万円
  * PyCon APAC 2023 に参加するための交通費・宿泊費の一部もしくは全額の補助。
  * 使用用途（想定)対象者：15名
  * (PyLadies : 5名、PyCamp : 10名 を予定)一人当たり上限（3万円）まで
* 3月以降の開催状況
  * 福岡で3回目の開催に向けて会場の選定中（現地スタッフ: kuga）
    * 候補にしていた会場が開催前に参加者のリストを提出するルールになっていたため、別の会場を探すことになった。
    * 時期は決まってますか?(kanan
      * 未定です。決まったらkananさんに共有(ryu22e2
  * 愛知で開催を検討中（現地スタッフ: f2snowman（岩佐さん））
    * 会場選定中。4月か5月に開催の見込み。
  * 鹿児島県で開催立候補あり（現地スタッフ: tadachi2ds（足立さん））


### OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)

* 運営メンバー: yoshi-tsukamo
* 今後の予定
  * 3月10日(金)・11日(土) オンライン/Spring
    * 11(土) 10:00〜10:45
    * [Pythonを学習するコツ教えます 〜初心者向けPython Boot Campを開こう〜](https://pyconjp.connpass.com/event/275279/)
      * 参加者が順調(yoshi-tsukamo
  * 4月1(土) Tokyo/Spring
    * **展示のみ現地開催**
    * 東京都立産業貿易センター 台東館（浅草駅 徒歩5分）
    * <https://www.sanbo.metro.tokyo.lg.jp/taito/access/>
    * 荷物を当日持ち込まないといけない。自分が持っていこうと考えている(yoshi-tsukamo
  * 5月20(土・予定) オンライン/名古屋
  * 5月28(日）名古屋
    * **展示のみ現地開催**
  * 2023年6月下旬頃 北海道(おそらくオンラインのみ)
  * 2023年7月下旬〜8月上旬頃 京都(2days)
    * 7/15(土・仮）セミナーのみオンライン
    * 7/22(土・仮）**展示のみ現地開催**
* **2023年度予算申請**
  * 62万円
    * 協賛費: 210,000円
    * 出展6回: 400,000円
    * 備品: 10,000円
* 1回あたりの金額感はいままでどおり?(shimizukawa
  * 過去の実績をベースにしている(yoshi-tsukamo
  * 物価が若干あがっているので、気をつけた方がよいかも(shimizukawa
* 出展6回は6箇所に1人ずついく想定?(takanory
  * その想定(yoshi-tsukamo

### PyLadies関係報告(kanan, 低, 報告)

* **PyLadies Caravan 予算概算申請**：計30万(仮予算含む)
  * 2名 x 3回開催と仮定して(内1回大阪)
  * 実績だと2名2回で12万円くらいだが?(shimizukawa
    * 前回2回とも旅行支援を使っている(kanan
    * 東北などの行きにくい場所にも行きたいので、多めの予算としている(shimizukawa
* **Python Boot Camp TA 予算概算申請**: 計15万
  * Python Boot Camp TA 3回参加予定と仮定して(各回1名参加)
* PyLadies Caravan in Osaka 3/11で予定して作業進捗中
  * [[オフライン] PyLadies Caravan in 大阪 - connpass](https://pyladies-tokyo.connpass.com/event/274708/)
  * 2月1週にconnpass公開済
  * 学生集客イベントになりそうなので、はじめてのPython+結果がわかりやすい画像系で実施
  * オフライン会場満席のため、PyLadiesTokyo共催でオンライン会場も設置

### PyCon JP TV(terada、低、報告)

* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* <https://www.youtube.com/user/PyConJP>
* Web <https://tv.pycon.jp/>
* 第24回(1月)、だい25回(2月)配信済み
  * [#24: Pythonistaに聞く2022年重大ニュースと2023年の展望 - 2023-01-13](https://tv.pycon.jp/episode/24.html)
  * [#25: Sphinxライブデモ Python製静的サイトジェネレーターでWebサイトの構築から公開まで - 2023-02-03](https://tv.pycon.jp/episode/25.html)
* 次回は3月10日(金)予定。内容は「PyCon JP Association 理事ってどんなことしてるの？」
  * [#26: PyCon JP Association 理事ってどんなことしてるの？ - 2023-03-10](https://tv.pycon.jp/episode/26.html)
  * simizukawa、yoshida、jonasインタビュー協力ありがとうございました!!
* ネタ募集中です(takanory
* **予算**:
  * 懇親会: 12万円
  * 機材費: なし
* 広報で予算をたてるとかは今は考えられていない(terada
* 予算半減している(shimizukawa
  * 品質を上げるために機材費を使っていたが、今年は機材費をまるっと削っている(terada

## コミュニティー支援

### PyCon JP地域開催サポートプログラム(kiyota、中、報告?)

* 2022年12月にtakanory, yoshidaと意見交換した(kiyota
  * PyCon JP地域開催の件の共有 <https://pyconjp.atlassian.net/browse/ISSHA-2729>
  * 
* 最初の提案だともりもりだった。資金的な支援を考えている(kiyota
* 開催予算案
  * <https://docs.google.com/spreadsheets/d/1pUruLK9l_Rrww6CQFKuCPl91XypDYHyFpVJFeR_EFx8/edit?usp=sharing>
* まずはブログを書いて反応を見つつ、その間に予算や内容を詰めていく予定(kiyota
* **TODO**まとめ
  * <https://pyconjp.atlassian.net/browse/ISSHA-2742>
* ミーティングをしていたようだが(takanory
  * どういう風にひろげるか、どう伝えたらいいかなどを全体で考えている途中(terada

## 海外コミュニティ連携

### APAC関連(terada、低、報告)

* Asia Python Society
  * イクバルさんが提案している

### APACロゴ関係(terada、低、相談)

* 進展なし

## その他

### origin.pycon.jp OSバージョンアップ  (yoshida)

* <https://pyconjp.atlassian.net/browse/ISSHA-2482>
* 3月が忙しいので一年延期する(yoshida

## 次回

* 運営会議#60
  * 2023年5月10日(水) 19:30-21:30
  * https://pyconjp-staff.connpass.com/event/277360/

## TODO

* [PyCon JP 2022収支報告ブログを書く](https://pyconjp.atlassian.net/browse/TRA-473)(yoshida
* PyCon APACメンバーとのミーティングにjonasを呼ぶ(selina
* PyCon APAC 2023の会場で不要なところは削る(selina
* [イベント会計の人も含めて、インボイス制度についての勉強会を実施する](https://pyconjp.atlassian.net/browse/ISSHA-2811)(terada、shimizukawa
* [予算の見直しを7月後半に行う](https://pyconjp.atlassian.net/browse/ISSHA-2812)(takanory
* [2022年度の消費税について確認するミーティングを行う](https://pyconjp.atlassian.net/browse/ISSHA-2778)(terada

