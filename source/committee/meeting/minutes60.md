# 2023年5月10日(水) 一般社団法人PyCon JP Association運営会議#60

* 日時: 2023年5月10日(水) 19:30-21:30
  * <https://pyconjp-staff.connpass.com/event/277360/>
* 場所: Zoom
* 参加者
  * 理事: terada, yoshida, jonas, shimizukawa, takanory
  * オブザーバー: nishi, selina, ainamori, kanan, yoshi-tsukamo, ryu22e, kiyota, kobatomo, peacock

```{contents}
:local: true
```

# PyCon JP


## PyCon JP 2022(Selina、低、報告)

* 一社のホームページ( [https://www.pycon.jp/](https://www.pycon.jp/) )からPyCon JP 2022の情報を削除その代わり、PyCon APAC 2023の情報を記載。(完了済み)
* TODO: Web(2022.pycon.jp)静的化のマージ(yoshida
  * チケット確認する
* [TRA-404] 支払い: グラフィックへクレジットカード支払いの実行 
  * 再オープン状態となっている(takanory
  * <https://pyconjp.atlassian.net/browse/TRA-404>

## PyCon APAC 2023(Selina、高、報告)

* JP→APACとしての正式開催発表をBLOGで行う。（4月7日）
  * <https://pyconjp.blogspot.com/2023/04/pyconapac2023-ja.html>
  * <https://pyconjp.blogspot.com/2023/04/pyconapac2023-en.html>
* ティザーサイト公開
  * <https://2023-apac.pycon.jp/>
* コンテンツチーム
  * CfPページ公開
    * <https://pretalx.com/pyconapac2023/cfp>
    * 募集開始日: 2023-04-22
    * 募集終了日 : 2023-05-31 (AoE)
    * 採択会議は6月18日（日）を仮で設定。
    * 採用可否連絡 : 7月上旬(予定)
    * 集まり具合は?(terada
      * まだ20件くらい。いまのところは英語が多い(jonas
      * 日本語の応募状況が少なく感じるので案内等をする(Selina
      * こちらでCfPを書く会を開催してくれている様子
        * <https://hannari-python.connpass.com/event/283291/>
  * キーノート（基調講演）
    * 海外：Lorena Mesaさん
      * <https://lorenamesa.com/>
      * 承諾済み
    * 日本：喜多 一さん(英語の予定)
      * <https://kdb.iimc.kyoto-u.ac.jp/profile/ja.f021a84eddbfafa4.html>
      * 承諾済み
* 会場について
  * 契約手続き進行中
    * <https://pyconjp.atlassian.net/browse/ISSHA-2755>
    * 代表理事の確認・捺印完了→Mary→TOC有明担当者（今ココ）
    * 戻ってきたら請求書が来るので、そのあと支払いを依頼予定(selina
  * TOC有明コンベンションホール（変更無し）
    * <https://www.toc.co.jp/saiji/ariake/>
    * 東京都江東区有明3丁目5番7号
  * 日程候補：2023年10月26日（木）～29日（日）
    * 部屋借りパターン2023
    * 会場レイアウト 4F.pdf
    * 会場レイアウト20F.pdf
    * 最終日29日に関して、スプリント会場提供者が見つかった場合はTOC有明をキャンセルし、会場提供企業になる可能性あり。
  * 今後の事も考え、2024年の会場候補や仮予約も動きたい。
    * スケジュールの観点とかはあるか?(terada
    * Maryさんからは1000人規模の会場を押さえるのであれば1年半前から動いた方がよいのではないか。(selina
    * 来年もTOC有明なら1年前でも大丈夫だと思う。ただ3年連続同じ会場を使ったことはいままでない。PiOの改修が終わっているが全体を借りるのが難しくなっている(yoshida
    * 同じ所を使うのは「わかっているから」、場所が変わるのは金額があがったとか(shimizukawa
    * 会場候補としてTOCとPiO以外にいいところあるんですか?(takanory
      * [TRC](https://www.trc-event.jp/)(東京流通センター), [横浜大さん橋ホール](https://osanbashi.jp/hall/)とか
      * TRCとTOCは料金は同じくらい(selina
* システムチーム（WEB）
  * 進行中、ティザーサイトはOPEN
  * その後については、次回（5月14日）のミーティングで話す。
  * スタッフ内で巻き取れなかった場合外注も視野に入れている。
* デザインロゴ
  * 進行中
  * スタッフ内で巻き取れなかった場合外注も視野に入れている
* スポンサーチーム(kame-chanリーダー)
  * 進行中
* 予算
  *  収入(最大)約5000万円/支出4000万円くらい
  * 赤字にならないように気をつけて進めて(terada
    * 過去最大の収入が2019年の2900万なので、Aだけでそれに匹敵する規模になっているようです(shimizukawa
    * Aは2022年の結果に合わせて計画するのがよさそう(yoshida
  * 精査が必要(Selina, Peacock
* スポンサープラン
  * PyCon APAC 2023 スポンサーシップパッケージ資料
    * Diamond 300万円 x1, Platinum 150万円 x3, Gold 75万円 x18, Sliver 40万円 x20, Bronze 10万円 x??
  * #2023-t-advisorsで話を進めている
  * その他、PSFにTravel Grantの費用補助をお願いする予定（申請額はPlatinum相当）
    * いいと思います(takanory
    * もっともらってもいいんじゃない?APACの旅費には力を入れてほしい(terada
      * PSFの2022の収入は、 約 $4,000,000なので
    * USドルで15,000ドルでもよいのでは(jonas
    * PSFへメールするとき、
* その他
  * PyCon US 2023の「PyCons LT」で開催の発表をした。
  * 余力があれば、Tsukamotoさんと相談してOSCなどでスタッフのLTやPyCon APACの宣伝をしたい。
  * 困っていることはないですか?(takanory
    * 参加している人数によって動きが違う(selina
    * 海外からの非日本語話者からスタッフ応募がたくさん(フォームは止めた)あり、ハンドリングで困っている
      * いまは応募をとめた?(takanory
      * 17日にオンボーディング会をやる予定
    * **TODO**: 別途相談会やりましょう(terada

# 会計

## 消費税インボイス制度の申請(shimizukawa、低、報告)	

* 登録手続き完了
* **適格請求書発行登録番号**はこちら
  * 一社PyCon JP 住所・銀行口座
* 2023年10月以降は請求書とかに必要となる(terada
* イベントの会計まわりの人にもインボイス制度を理解してもらう必要がありそう(takanory
  * インボイス勉強会をスタッフ向けに行う予定をshimizukawaとteradaで計画中。
  * 時期を決めていない。(terada
  * 5月下旬には実施したい(terada
    * 5月中旬のスポンサー募集や、5月下旬の一般参加募集の頃には実施したい
    * 準備します(shimizukawa

## 消費税の件(terada、低、報告)

* <https://pyconjp.atlassian.net/browse/ISSHA-2778>
* 決算書的に消費税の支払いがあると清水川さんが勘違いしていた。支払いは不要だった。
  * 🙇 (shimizukawa
* 詳細は、上記チケットに記載されている。
* 今までの消費税支払額についても問題ないことを確認した。

# PyCamp、PyLadies関連

## PyCamp状況報告(ryu22e、低、報告)

* 運営メンバー: ryu22e、kobatomo
* [Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP](https://www.pycon.jp/support/bootcamp.html)
* 5月以降の開催状況
  * 5/20 PyCamp鹿児島 2nd (講師 : たかのりさん)
    * <https://pyconjp.connpass.com/event/278007/>
    * 参加者（一般）: 5/10、 学生: 1/10、 TA: 4/4、 スタッフ: 5/5
    * 担当コアスタッフ; ryu22e
  * 6/3 PyCamp愛知2nd(講師 : 清水川さん)
    * <https://pyconjp.connpass.com/event/280530/>
    * 参加者（一般）: 4/15、 学生: 1/5、 TA: 3/3、 スタッフ: 2/2
    * 担当コアスタッフ: kobatomo
  * 福岡で3回目の開催に向けて会場の選定中（現地スタッフ: kuga）
    * 今の所具体的な動きはなし
* その他
  * 今年のPyCon APACのポスターセッションに応募する予定（プロポーザルはまだ書いている途中）
  * コアスタッフ募集について動き出す(ISSHA-2822)

## OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)

* 運営メンバー: yoshi-tsukamo
* 4/1(土) 東京出展しました
  * 出展者・来場者ともに予想よりも多かった印象
  * 東京以外の地方からの参加者も結構いた
  * 作成したチラシがまだ残っているので使用しているが追加印刷する際には直したい箇所がある（『一般社団法人PyCon JP』となったままの箇所あり）
    * 即作り直そう。(terada)
  * PyCampの魅力を伝えるべく動画作成(TVコラボ) <https://youtu.be/rmQjT2EAJ_s> (terada
    * またやりたい。PyCon JPの宣伝とかでも(terada
    * よかった(tsukamoto
* 今後の予定
  * 5月20(土) オンライン/名古屋
  * 5月28(日 名古屋
    * 展示のみ現地開催
    * 塚本が参加予定（日帰り）
    * 1週間後のpycamp愛知2ndの現地スタッフ・岩佐さんも参加してくれる予定
    * yoshida現地参加予定。PyCon USのステッカーとか折り紙を持っていく予定(yoshida
    * Python関連ステッカーが大量にあるので、送りたい。住所教えてくださ(takanory
      * <https://pyconjp.atlassian.net/browse/ISSHA-2856>
  * 2023年6月 北海道（予定外だったため不参加の予定）
    * 6/17(土) オンライン
      * **TODO**: PyCon APACスタッフで話す人いないか聞いてみる(selina
      * 登録締め切りは過ぎているが、まだ応募可能なはず(yoshida
    * 6/24(土) 現地開催
      * いまがチャンスなんじゃないかということで、福岡なしにしてでもこちらに予算を回しては？ (terada
      * 上記を検討してみる (tsukamoto
  * 2023年7月 京都
    * 7/22(土）展示のみ現地開催
    * 7/29(土）セミナーのみオンライン
  * 2023年10月 東京
    * 10/21(土) 大田区産業プラザPiO(展示)
* 2023年度協賛金の支払い完了しています

## PyLadies関係報告(kanan, 低, 報告)

* PyLadies Caravan in Osaka 3/11開催済
  * [[オフライン] PyLadies Caravan in 大阪 - connpass](https://pyladies-tokyo.connpass.com/event/274708/)
  * PyLadiesTokyo共催でオンライン会場も設置
  * 満員御礼、全員学生(専門生)
* **PyLadies Caravan 予算概算申請**：計30万(仮予算含む)
  * 今のところ開催予定なし
  * PyLadies Tokyoも運営超多忙により春イベントできておらず。6月合宿イベあり
* **Python Boot Camp TA 予算概算申請**: 計15万
  * 5/20,6/3 共にmaaya 予定あり参加不可 またの機会に・・・
  * 5/20 kanan参加できるかも
    * 鹿児島女性の参加者いるのでよさそう(takanory
* その他(terada)
  * PSF や 米国PyLadiesとの連携の強化ができるのではないか？
  * LorenaさんがキーノートでPyCon APAC 2023に来る。PyLadiesのメンバーだと思うし、食事会とかを企画してもよいのでは
  * 活動をAPACでポスターを出すとよいのでは？
    * 2カ月前にポスターセッションやれたらいいなという話をしていた。前向きに検討したい(kanan

## PyCon JP TV(terada、中、報告)

* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* <https://www.youtube.com/user/PyConJP>
* Web <https://tv.pycon.jp/>
* 26回(3月), 27回(4月)配信済み
  * [#26: PyCon JP Association 理事ってどんなことしてるの？ - 2023-03-10](https://tv.pycon.jp/episode/26.html)
  * [#27: Python公式ドキュメントを読みながら開発しよう！ - 2023-04-07](https://tv.pycon.jp/episode/27.html)
* 次回は、5月12日（金）予定
  * [#28: PyCon US 2023振り返り - 2023-05-12](https://tv.pycon.jp/episode/28.html)
* 4月のPyCon USでは、コミュニティとスポンサーブースのインタビューをtakanory, terada で撮ってきた。現在、動画編集中で、近日中に公開予定。
* ネタ募集中です(takanory
  * PyCamp Caravan, PyLadies Caravanのこととかやってもいいかも(takanory
  * PSFって何やっているの？(terada
  * PyLadies全般の話をするのもありかも(takanory

# コミュニティー支援

## PyCon JP地域開催サポートプログラム(kiyota、中、報告?)←進んでいない。。。（清田）

* 2022年12月にtakanory, yoshidaと意見交換した(kiyota
  * PyCon JP地域開催の件の共有 <https://pyconjp.atlassian.net/browse/ISSHA-2729>
  * PyCon JP地方開催サポートプログラム準備会 #1
* 最初の提案だともりもりだった。資金的な支援を考えている(kiyota
* 開催予算案
  * <https://docs.google.com/spreadsheets/d/1pUruLK9l_Rrww6CQFKuCPl91XypDYHyFpVJFeR_EFx8/edit?usp=sharing>
* まずはブログを書いて反応を見つつ、その間に予算や内容を詰めていく予定(kiyota
* **TODO**まとめ
  * <https://pyconjp.atlassian.net/browse/ISSHA-2742>
* ミーティングをしていたようだが(takanory
  * どういう風にひろげるか、どう伝えたらいいかなどを全体で考えている途中(terada

# 海外コミュニティ連携

## APAC関連(terada、中、報告)

* PyCon US 2023でPyCon APACコミュニティブースを設置
  * Iqbalさんと韓国のKwonHanが中心になってブースを設置
  * 日本からは折り紙（別途予算化したもの）を持参した
  * Asia内でのオーガナイザー同士(日本、韓国、台湾、香港、フィリピン)の横のつながりが強まった
  * APACイベントへの興味を持ってくれる人が多くなったと思う
* Asia Python Society改め、Python Asia構想
  * PyCon US中に、Iqbalさんを中心に、韓国、香港、台湾、日本のメンバーが集まり今後のAPACコミュニティやAsiaをまとめる組織づくりが必要なのではないかと議論が始まった
  * お金のことや運営のことなどまだまだ課題が多い
  * 反面、Asiaがまとまることで、EuroPythonと同レベルの組織が作れる可能性も感じている。PSFからの資金的な援助、PSFとの関係性を強められるのではないかと思っている

## APACロゴ関係(terada、低、報告)

* ロゴを改修してPSFからの指摘に対応した（PyCon USでステッカーを配るために）
* ロゴは確定した
* 現在、ロゴキットを取りまとめ中


# その他

## 法務担当的立場  (terada、中、相談)

* 寺田が代表理事から降りて、主に何を担当するのが良いかと考えている。（まずは提案
  * 現状は、「TV」と「APAC関連」が主な担当になっていると思う。
* その中で、法務担当的な立場が馴染むのではないかと思っている。
* 主に担当する業務の想定
  * 契約書や申込書などのレビュー責任者
  * 法的解釈必要な場合の、相談相手や調査担当者
  * 弁護士とのやりとりを主に行う
* 最初の業務の想定
  * プライバシーポリシーの策定を弁護士と行う
* 個人的には助かる(takanory, yoshida
* 寺田が担当するってことで進める。

# TODO

* Web(2022.pycon.jp)静的化のマージ(yoshida

# 次回

* 運営会議#61
  * 2023年7月28日(金) 19:30-21:30
  * PyCon APACの予算の状況を見て、追加予算どうするかを決めたい
  * 次の座長?→募集どうするかの話はありそう

