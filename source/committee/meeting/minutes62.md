# 2023年9月21日(木) 一般社団法人PyCon JP Association運営会議#62

* 日時: 2023年9月21日(木) 19:30-21:50
  * <https://pyconjp-staff.connpass.com/event/283673/>
* 場所: Zoom
* 参加者
  * 理事: terada, takanory, yoshida, shimizukawa
  * オブザーバー: selina, ryu22e, yoshi-tsukamo

```{contents}
:local: true
```

## PyCon JP


### PyCon JP 2022(Selina、低、報告)

* TODO: Web(2022.pycon.jp)静的化のマージ(yoshida
    * <https://pyconjp.atlassian.net/browse/ISSHA-2950>

### PyCon APAC 2023(Selina、高、報告)

* 全体に関して
  * 現時点では予定通り開催できる見込み
    * 10/26木 tutorial, 27金,28土 talk, 29日 sprint
  * 直近で9月19日に行い26日にも全体ミーティングを行う。
  * [20230919_PyCon APAC 2023 全体ミーティング#8](https://docs.google.com/document/d/1HMNcyR4fAzr3iRdO3xCd2M_6Hw9qknpIEw_pzBVAodE/edit#heading=h.6g2uievotd9j)
* WEBサイト
  * 本番ページ公開中
  * <https://2023-apac.pycon.jp/>
  * タイムテーブルページ実装
    * <https://feature-timetable.pycon-jp-2023.pages.dev/timetable>
    * 例年通りトークごとのURLも発行
      * 例: <https://feature-timetable.pycon-jp-2023.pages.dev/timetable?id=YAW3KH>
      * Twitterで紹介する場合などにご利用出来る
* コンテンツチーム
  * スピーカー（30分、15分、LT）およびポスター採択者に連絡し、問題なく進めている。
  * キーノート（基調講演）
    * 海外：Lorena Mesaさん
    * 日本：喜多 一さん(英語の予定)
* 会場について
  * 契約手続き完了、支払いも完了
    * カンファレンス終了後に、追加費用などを精算し別途支払う予定。
    * 関連JIRA
      * <https://pyconjp.atlassian.net/browse/ISSHA-2954>
      * <https://pyconjp.atlassian.net/browser/USA-342>
      * <https://pyconjp.atlassian.net/browser/USA-341>
      * <https://pyconjp.atlassian.net/browser/USA-340>
  * TOC有明コンベンションホール
    * [https://www.toc.co.jp/saiji/ariake/](https://www.toc.co.jp/saiji/ariake/)
    * 東京都江東区有明3丁目5番7号
  * 日程候補：**2023年10月26日（木）～29日（日）**
    * [部屋借りパターン2023](https://docs.google.com/spreadsheets/d/1UI6jNexbvhDZTri614_7HfazTrAF76_EpuDMh1fyz0w/edit#gid=1903528639)
    * [会場レイアウト 4F 10月27-28日.pdf](https://drive.google.com/file/d/1o3czHNS3_PdBlK_RpSUNDCz6Vzn32SIU/view?usp=share_link)
    * [会場レイアウト20F 10月27-28日.pdf](https://drive.google.com/file/d/1yEh5fq-oQ3w3V1x3gwlcONB7ZxjHbhG-/view?usp=share_link)
    * 最終日10/29(日)に関して、スプリント会場はHENNGE(4F)で行う。
      * スプリントの目安は100名
* デザイン関連
  * デザイン専任(chiaki)を筆頭に、各グッズなどの納期を確認し、進めている
  * デザイナーは外注
  * [2023デザインタスク](https://docs.google.com/spreadsheets/d/1u6jMApEEKhAQ3tXhn--TLuIT8kMaWCA0JAyZeQH4K30/edit#gid=0)
  * 冊子（簡易版）を作ります 。紙で欲しいがタイムテーブルは除外
* 広報(media)
  * 広報強化のために寺田さんが先週からチームに加わった。
  * リーダーOJIを筆頭に動いている。
  * 9/20に再度見直しミーティングを行った。
    * [20230920_PyCon APAC 2023 media reboot MTG](https://docs.google.com/document/d/1T4QkAXo_XzQDig1VL69YzQ8bMjhzCt4B1ynyhzQlpk8/edit)
* チケットシステム
  * <https://pretix.eu/pyconjp/2023-apac/>
  * Pretixのシステムを使い、販売開始。
    * 9/21現在289枚売れている(詳細をPeacockに確認中)
      * スタッフ、スポンサー含めてのチケット枚数ではないか?(selina, terada
    * Connpassに比べて、長所短所ある
  * Standardのアーリーバード(9,000円)は完売。そして今はStandardセミアーリーバード(10,000円)を9/25まで限定販売する。
  * プレスリリースを出した。
    * [https://prtimes.jp/main/html/rd/p/000000002.000105617.html](https://prtimes.jp/main/html/rd/p/000000002.000105617.html)
  * pretixのチケットもぎり方法確認必要
* 予算
  * [予算2023](https://docs.google.com/spreadsheets/d/1PeiDICXuwvS7tp4d60B_oNBAiDg9jqfj-ImFK3m-fJs/edit#gid=926180703)
  * **支出：21,211,354円／収入：26,830,000円　収支：プラス5,618,646円**
    * 確度A：80-100%(最低限やりたい)
  * トラベルグラントが未確認だが予定より多い
    * トラベルグラントでPSFからのスポンサー費(200万円)よりも大きい予算(600万円)をかけている(yoshida
    * PayPalでのお金を渡すことを考えている(yoshida
    * 国によって受け取れるかわからないので、帰ったあとにPayPalだとだめだっただと大変になる。最終手段は現金として、当日までに確定させたい(shimizukawa
    * PyCon USは何種類かあったが、日本人はPayPalを選んで本人確認をしていた(terada, takanory
    * メールで「PayPalはだめなので現金でほしい」と連絡している人はすでにいる(takanory
    * **TODO**: yoshida, shimizukawaで個別に進めた方がよさそう(terada
  * 現在予想では、確度Aでプラス561万円の見込み。
    * チケットは何枚売れた想定?(terada
    * Aは「360枚」の見込み(takanory
  * 引き続き、精査が必要(Selina, Peacock
    * 9/25のタスク確認会でChairsで過不足ないか精査したい
  * パーティ費用、食事関連が物価高騰で変動の可能性はある。
  * ウェルカムパーティは、運営費用から捻出
    * ウェルカムパーティーは今「B」になっている。これは「A」の間違いでは(takanory
    * 前述の収支には現在計算に入っていない(selina
  * day2パーティについては、別払い(5000円)とする。
    * Day2パーティにビールスポンサーが入った。
* スポンサー関連
  * 公式ページにてブログ公開済み
    * PyCon APAC 2023 スポンサーシップ募集経過報告
    * [PyCon JP Blog: PyCon APAC 2023 スポンサーシップ募集経過報告](https://pyconjp.blogspot.com/2023/06/pyconjp2022-sponsorship-result-ja.html)
  * [PyCon APAC 2023 Sponsorship package materials](https://docs.google.com/presentation/d/1pAsSFyrggLvUM2ohXpYjMe0O-vXaxUSkRmDhr5uk5pc/edit)
    * 内訳
      * Diamond 300万円 x1
      * Platinum 150万円 x3
      * Gold 75万円 x18
      * Sliver 40万円 x20
      * Bronze 10万円 x??
    * スポンサー募集状況
      * スポンサー募集状況**（9/26締め切り）**
        * Diamond: 1（募集終了）Google Cloud
        * Platinum: 3（募集終了）HENNGE, Findly, カケハシ(新)
        * Gold: 13/18
        * Silver: 17/20
        * Bronze: 9/∞
        * Sprint会場: HENNGE(託児の場所は検討中)
        * 検討中企業: 3社
      * 朝食・ランチ・ドリンクスポンサー、パーティースポンサー募集中
      * スポンサーインタビュー実施予定
        * ダイヤモンドとプラチナスポンサーにインタビューする予定です
      * スポンサーシールラリーを実施
        * カンファレンス中にスポンサー6社を回った参加者にノベルティグッズとして記念タオル（イイヤツ製作中）を渡す。
  * その他、PSFにTravel Grantの費用補助をお願いした（申請額はPlatinum相当）
    * USドルで15,000ドルを申請：1,950,000円のプラス見込み（予算計上済み）
      * 45,000ドルでの再申請は通らず
    * 15,000ドルで確定し、Jonasが振込手続き(W-8BEN-E)を行った。
      * [https://pyconjp.slack.com/files/USLACKBOT/F05RSKYRB19/pycon_apac_2023_grant_invoice](https://pyconjp.slack.com/files/USLACKBOT/F05RSKYRB19/pycon_apac_2023_grant_invoice)
      * 楽天銀行に海外送金が到着していることを確認。teradaが受け取り処理する(takanory
* 招聘状(VISA用Invitation letter)について(yoshida
  * 2023年度の座長も含めて慎重に検討した結果、一般の海外参加者及びスタッフに対しては、原則として招待状を発行できないという結論に至りました。招待状は外務省（大使館・領事館）のVISA審査に使用されます。招待状には招待の理由を明確に記載し、会議の開催には現地での招集が不可欠であることを合理的に説明する必要があります。 
  * その他にもスピーカーではないが招聘状が欲しいという希望者がいる
    * フィリピンからの参加者でtakanoryがPyCon Taiwanであった知り合いで、スピーカーのMicaelaも知り合いなので招聘状を出してあげたい(takanory
    * 身元保証するか、しないかを確認したい(terada
      * 以前は保証しないほうに統一していた(terada
      * 今回、スピーカーは身元保証している(yoshida
    * APACを日本でやることを決めたとき、イクバルさんから「APAC地域からの参加者には、一般参加者にもなるべく招聘状を出してほしい」というコメントがあったように記憶している（要確認）(terada
      * フィリピン、インド、バングラディッシュ、は招聘状が必要
      * インドネシア、マレーシアはパスポートにICチップが無ければ招聘状が必要
      * 活動が見えている人、直接の知り合いの紹介、であれば出してあげたい気持ち(terada
        * +1 (takanory, shimizukawa, selina
        * 保証無しで出すのはありではないか(yoshida
      * 身元保証する場合は、それなりの責任が生じる。そのための準備の時間もないだろう
  * スピーカーにはできる限り招聘状を発行する
* PyCon APAC 2023中に一般社団法人PyCon JP Associationとして何をやるか (terada)
  * >https://pyconjp.atlassian.net/browse/ISSHA-3008>
  * ​​法人からの報告（クロージング）・・15分で確保済み
  * 公開ミーティング（ランチタイミング）
    * 60分程度欲しいが、45分でも構わない
    * 現在、場所の調整中。
    * 20階のオープンスペースがありそう
  * PyCon JP Associationブース（PSFブースと共同）
    * キラキラステッカー募金
    * PSF Member募集
    * PyCon APAC関連
    * 場所確保済み。机1個、椅子2個
    * Goldがあいてたらもう1つ机もらえないかな...(takanory
      * PSF兼ねるPyCon APACブースとかできないかなぁ?(takanory
      * 人がはりつけないので、なくていいのではないか(terada
  * APACメンバーランチ　（公開ミーティングとは別で）
    * APAC関連で来ている人向けに、英語でコミュニケーションを取る場
    * 未定。調整中
    * 20Fのアンカンファレンス(オープンスペース)でできるのではないか?(takanory
* その他
  * PSF KitはまだNoahのところ？
    * <https://pyconjp.slack.com/archives/C024JGVAU/p1693820698809849>
    * Noahと連絡がとれていないのでそのままです。今年はあきらめてください(takanory
  * 他ITイベントでのPyCon宣伝
    * Tsukamotoさんと相談してOSCなどでスタッフのLTやPyCon APACの宣伝をしたい。
      * ODC 2023(8/26)→Selinaが登壇し、カンファレンスの話もした。
      * PyCon TW 2023でkame-chan&PeacockがLTした。
      * OSC2023 Online/Fall 2日目(9/30)→Selina登壇予定
      * DjangoCongress(10/7)→複数スタッフが登壇するので誰かにお願いする。
  * ご協力のお願い
    * このミーティングに参加している皆さんへ
    * 現在、メディアチームが発信に力を尽くしているが、可能であれば、皆さんからもSNS拡散やシェアのご協力をお願いしたいです。
      * #randomあたりで「拡散希望」とかしてくれるとありがたいです(takanory
  * セキュリティ的な心配
    * スタッフで不安な動きをしている人がいた。
    * PyCon JP(今年のAPAC含む)は、申し込みと同時にGoogleドライブやslack、JIRAに入ることが出来るが、次回以降は段階的に設定する流れにした方がよさそう。
      * 可能であれば現時点で実績がないメンバーは、権限を全部絞った方がいいと思います(takanory
      * すぐやります(selina

#### 後で相談

* Webサイトのタイムテーブル、4Fと20Fをクリックしないとそれぞれが表示されないので、タイムテーブルの全体像がわかりにくいと思います。クリティカルではないが可能なら当日までに修正した方がよいと思う(takanory
  * <https://feature-timetable.pycon-jp-2023.pages.dev/timetable>
  * 確かに一画面で20Fと4Fが見えるようにすると良いと思う(selina
  * システムチームに共有する(selina
  * トラックごとに1,2,3,4,5分けるアイデア(terada)
* 当日の現金持ち歩き (yoshida
  * どう管理したら良いかな？
  * 現金ではなく、カードを使ったほうが良いと思う (shimizukawa
  * クレカ必要であればfreee unlimited作れます(takanory
    * yoshida用とか作るのは全然あり(takanory
    * [経営を強くする、 統合型コーポレートカード freeeカード Unlimited](https://www.freee.co.jp/card/unlimitedcard/)
    * **TODO**: yoshida用のfreee unlimitedカード作る(takanory
      * <https://pyconjp.atlassian.net/browse/ISSHA-3012>
* Amazonで購入予定はありますか？(shimizukawa
  * あります. NOCで(yoshida
  * Amazon Business アカウント発行します(shimizukawa
  * 10月上旬には使いたい(yoshida
  * **TODO**: 9/28木〜30土頃に打合せセッティングします(shimizukawa
    * トラベルグラントのPayPal以外の方法も合わせてやりましょう
* 懸念点は他にないか？ (terada
  * 具体的な抜け漏れがわからないので9/25に確認する(selina
  * 相談会をやるのも一つの方法(terada
  * 各副座長から過去の経験者に範囲をしぼって聞くとかありだと思う。そのために抜け漏れがないと思っている状態のリストアップが出せるとよい(shimizukawa
  * コンテンツチームに最近入ったが、残件のタスクリストは存在しなかった。そのため、9月20日(水)夜にtakanoryとpeacockでタスクリストを作成した。現在koyhoge、masamori、nikkieに見てもらっている状況(takanory
    * [コンテンツ: タスク一覧](https://docs.google.com/spreadsheets/d/1QfNDgLzh7UIOhN7MMZxYySjls8O0Vp__X7wF_pn4emQ/edit?pli=1#gid=0)
    * そのため「抜け漏れがないか」はわからない状況だと思っている(takanory
  * タスクリストを再確認する必要がある
    * 26日に全体会があるので、各チームリーダー、担当者にタスクリストをまとめてもらい、残タスク、済みタスクをまとめ、大きなタスク漏れがないかなどを確認する(Selina
    * いつ誰が、どこで、誰が、何をするか、流れも含めて確認する必要がある。(Selina
  * コンテンツとメディアが壊滅的でtakanory、teradaに入ってもらって立て直し中(yoshida
    * 受付はまだなにも動けていない(yoshida
  * 今までは目の前のタスクをやるので一杯だったが、残りのタスクをリスト化していく必要があると思う(selina
    * 開催前にCMScomに集まって最終確認をして安心して進めたい(selina
  * 別途時間をとって運営についての話をするとよさそう(terada
    * スタッフとしても関わっているので、理事としての話とスタッフとしての話がまざっている(shimizukawa
    * **TODO**: 仕切り直しましょう(terada,selina
      * 9/25週（10/1週は寺田海外のためNG
      * 一社現地でやるなら 9/25月 or 9/28木
      * オンラインでもOK
      * 9/26にイベントの全体会があるので、9/28木、オンライン希望(seliina
      * **9/28木 19:30~** オンライン
        * <https://pyconjp-staff.connpass.com/event/297147/>
  * CMScomでの物の棚卸し会をやりたい(yoshida
    * **TODO**: 10月の中旬で日程調整をお願いします(terada→yoshida

### PyCon JP 2024(terada、低、相談)

* 今後の事も考え、2024年の仮予約を完了。
  * 2024年9月26日（木）～29日（日）でFIX
  * <https://pyconjp.atlassian.net/browse/ISSHA-2943>
  * 詳細はJIRAに記載
* 次期座長募集(takanory)
  * <https://pyconjp.atlassian.net/browse/ISSHA-3010>
  * Blogの下書きを書いた
  * 来週くらいに公開して、PyCon APAC一週間前くらいに締め切りはどうか?
    * いいと思います(terada, shimizukawa, selina

## PyCamp、PyLadies関連

### PyCamp状況報告(ryu22e、低、報告)

* 運営メンバー: ryu22e、kobatomo
* [Python Boot Camp(初心者向けPythonチュートリアル) — PyCon JP](https://www.pycon.jp/support/bootcamp.html)
* 9月以降の開催状況（予算：50万円）(9/21 実績：13/50万円)
  * 10/14 PyCamp徳島2nd(講師 : 筒井さん🎉)
    * <https://pyconjp.connpass.com/event/293032/>
    * 参加者（一般）: 2/8、 学生: 0/2、 TA: 1/3、 スタッフ: 1/2
    * 担当コアスタッフ: kobatomo
  * 福岡で3回目の開催に向けて会場の選定中（現地スタッフ: kuga）
    * 今の所具体的な動きはなし
  * 東京都八王子市で開催立候補あり（現地スタッフ: uniq）
    * 日程は、11月以降
    * 今月中に候補日をリストアップいただける予定
    * <https://pyconjp.slack.com/archives/C0RE71RHD/p1693721980188569?thread_ts=1687945762.563209&cid=C0RE71RHD>
* オンラインフォローアップ会をやりたいと思ったが、まったく動けていない(takanory
  * <https://pyconjp.atlassian.net/browse/ISSHA-2878>
* その他
  * PyCamp & PyLadies 参加者向けPyCon APAC 遠方者支援について(ISSHA-2960) (予算：45万円）15名まで支援する
    * 9/21時点 
      * 応募者 - 11名
      * 当選確定連絡 - 7名(仙台〜鹿児島まで幅広く応募いただく)
      * 確定していない理由は?(shimizukawa
        * 1名は少なくともpycamp関係ない人だったため却下(takanory
  * PyCon APACのポスターセッション当選。作成中。
  * コアスタッフ募集について動き出す(ISSHA-2822)
    * 1名打診。9/末に回答いただける。
  * PyCampテキストUpdateも進める。(ISSHA-2645)
  * PyCampでの領収書インボイス対応（10月以降開催)
    * 領収書対応については10/1 以降に再度決める
    * connpassの領収データがインボイスに対応するので、対応しなくてよいです(takanory
      * [お知らせ — connpassご利用ガイド ドキュメント](https://help.connpass.com/news#news20230915)

### OSC出展(Python Boot Camp Caravan)(yoshi-tsukamoto、中、報告)

* 運営メンバー: yoshi-tsukamo
* 8/26(土) ODC(selina)
* 今後の予定(予算: 36 / 62万円)
  * 9月/30(土) オンラインFall(selina)
    * 11:00〜11:45
    * **TODO**: サイトに掲載する情報をもらう(yoshi→selina
  * 10月21(土) 東京Fall
    * 大田区産業プラザPiO(展示)
    * 2名参加予定(Iosif・ryu22e)
  * 10月28(土) 島根 (PyCon APAC 2023と被る)
    * 松江テルサ
  * 11月12(日) 広島
    * サテライトキャンパスひろしま
  * 11月25(土) 新潟
  * 12月9(土) 福岡
    * 福岡ソフトリサーチパーク(SRP)
  * 2024年1-2月 オンライン大阪
  * 2024年1月27(土) 大阪
    * 大阪産業創造館
  * 2024年3月10(日) 東京
    * 東京都立産業貿易センター台東館
  * 2024年2-3月 オンラインSpring
* KOF(11/10(金)、11(土))は出さない?(takanory
  * 参加したいと考えています
  * <https://www.k-of.jp/2023/>
  * 会場: [大阪南港ATC ITM棟 10F](https://www.atc-co.com/guide/floor.php?tenant_area=23)
  * 協賛について
    * 協賛金1口50,000円（法人）
    * 特典：懇親会2名招待(11/10)
    * <https://www.k-of.jp/2023/sponsorship/>
  * 翌日11/12(日)にOSC広島があるが、さすがに連続参加は厳しいか
    * どちらかなら、KOFのほうが規模が大きくて良い(yoshida
  * 予算はこれから?(terada
    * 年間予算に63万円に対して36万円を使用しているので予算内でいける(yoshi-tsukamo
    * 賛成(terada, shimizukawa, takanory, yoshida
    * 行くなら、運営側コアな人(理事、運営メンバー、PyCon APACのコアなスタッフ)に行ってもらい、展示や発表などしてほしい(takanory
    * takanoryはいけません!!!😢
    * **TODO**: KOF参加進める(yoshi-tsukamo

### PyLadies関係報告(kanan, 低, 報告)

* **PyLadies Caravan **
  * 今のところ次の開催予定なし
* **Python Boot Camp TA **
  * 9月富山 maaya参加済み
    * 学生さん2名PyCon APAC来るようなのでcaravan勧誘再チャレンジしたい
    * 別途Boot Campには来れなかったけれど富山で活動している女性エンジニアの方との連絡を取り始めました
* その他
  * PSFや米国PyLadiesとの連携の強化ができるのではないか？
    * とりあえずPyLadiesConの告知お手伝いからスタート
  * LorenaさんがキーノートでPyCon APAC 2023に来る。PyLadiesのメンバーだと思うし、食事会とかを企画してもよいのでは
    * なつこ・ゆうか主導で進めてもらってます
    * ランチの場所がとれず、夜もイベントが続いているため最悪PyCampの飲み会の裏での開催になりそう・・・？日程調整中
  * PyLadies Tokyo活動をAPACでポスターを出す
    * Caravanの活動も一緒にポスターに入れてもらう予定

### PyCon JP TV(terada、中、報告)

* パーソナリティー: takanory, terada
* 運営メンバー: peacock、nana
* <https://www.youtube.com/user/PyConJP>
* Web <https://tv.pycon.jp/>
* 31回(8月)〜32回(9月)配信済み
  * [#32: PyCon Korea、PyCon Taiwan 2023振り返り - 2023-09-08](https://tv.pycon.jp/episode/32.html)
  * [#31: Python 3.12の新機能を試す - 2023-08-04](https://tv.pycon.jp/episode/31.html)
* 次回は、10月13日（金）予定
  * 10月: PyCon APAC 2023事前
    * 集客関連でなにかうまくできないか妄想中(terada
  * 11月: PyCon APAC 2023振り返り
* ネタ募集中です(takanory
  * PyCamp Caravan, PyLadies Caravanのこととかやってもいいかも(takanory
  * PSFって何やっているの？(terada
  * PyLadies全般の話をするのもありかも(takanory

## コミュニティー支援

### オープンセミナー香川(takanory、中、相談

* <https://pyconjp.atlassian.net/browse/ISSHA-2945>
* [オープンセミナー香川](https://osk.connpass.com/)
* teradaが発表をしてきた

## 海外コミュニティ連携

### APAC関連(terada、中、相談)

* PyCon APAC 2023のPSFブース
  * 寺田が中心にマネージメントしたい（はいOK
  * バナーボードがない。なにか作る？？許される？
    * APACボードを作るならあり(3,4万)？
    * 今回のイベントは布なしで紙の予定(yoshida
    * テーブルクロスだけ(1,2万)でも良い(terada
    * APACなら楽に作れるのでは無いか(yoshida
    * 【決定】APACロゴのテーブルクロスならJPが負担して作るのはよいのではないか(yoshida, takanory, shimizukawa
    * **TODO**: テーブルクロスの制作を進める(terada
* Asia Python Society改め、Python Asia構想
  * 定期的なMTGが行われている??
* エストニアで法人を作る方向で考えている。シンガポールのサポートする企業ともiqbalさんが話している(jonas
  * PyCon APAC前にミーティングをする。PyCon APAC 2023で決めたい(jonas
  * エストニアはオンラインでできるので、よさそう(jonas
* PyCon APAC 2023の中でPyCon APACの人達の話とかしないの?(takanory
  * 場所がほしい(jonas
* 予算やお金の流れについてもIqbalさんの方でまとめている(jonas
  * $15,000 USDが初期費用としてあれば3年は組織が運営できそう(jonas
  * 次回のPyCon APAC開催も考慮するとそれくらい。最小でなら$2,000 USD
* TODO: 一社PyCon JP Associationとして参加するのか、どう動くか考える(terada
* 次回ミーティングも参加するつもり。何か話したいことあれば言ってください(jonas
* 前回の議事録
  * [Python Asia Meetup 2023-07-17](https://docs.google.com/document/d/1mqEkwsrDTyjqzrh3sRE0bpT2IBN6hwPJU4eJ8X2Y56E/edit#heading=h.o7eequlqojru)

### PyCon APAC 2024(takanory、低、報告

* 2024の主催募集に対して現在インドネシア、韓国がProposalを出している
* <https://github.com/PyConAPAC/proposals/tree/master/2024/submissions>
* 以下の日程で投票依頼がくるので、理事でSlack、JIRAでディスカッションして投票する予定
  * 2nd Oct (Mon) 2023 - Deadline for amended and final proposals, if any (2)
  * 9th Oct (Mon) 2023 - Voting starts for PyCon APAC 2024 host
  * 23th Oct (Mon) 2023 - Voting ends
* PyCon APAC 2023クロージングのPyCon JP Associationの時間を使って開催地を発表する
  * スライドとかももらいたいなぁ
  * 28st Oct (Sat) 2023 - We'll announce the host for PyCon APAC 2024 on the final day of PyCon APAC JP 2023

### APACロゴ関係(terada、低、報告)

* ロゴを改修してPSFからの指摘に対応した（PyCon USでステッカーを配るために）
* ロゴは確定した
* 現在、ロゴキットを取りまとめ中

## 次回

* 運営会議#63
  * 11月21日(火) <https://pyconjp-staff.connpass.com/event/297313/>

## TODO

