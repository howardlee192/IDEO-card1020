# -*- coding: utf-8 -*-
import os
import re
import html

repo_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\IDEO-card1020"

cards_02 = [
    {
        "id": "CON-01",
        "title": "01. 情緒板過濾（Moodboard Filter）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "全組只准保留 20 張最硬核的實物參考圖，刪光所有模糊重複的插畫。",
        "why": "防止美術各畫各的，用具體照片作為團隊溝通的唯一物理標準。",
        "example": "美術砍掉 50 張天馬行空的網圖，只留 3 張廢土生鏽材質照，半天定下全片基調。"
    },
    {
        "id": "CON-02",
        "title": "02. 色彩光譜帶（Color Script）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "按時間軸拉一條色塊條，用極簡色塊標註每場戲的冷暖與明暗高低點。",
        "why": "讓色彩直接參與說故事，確保情緒高潮時有精準的視覺色彩衝擊。",
        "example": "編導對照色塊帶發現決戰前太亮，強制壓暗前場色調，高潮爆發感翻倍。"
    },
    {
        "id": "CON-03",
        "title": "03. 純黑剪影測驗（Silhouette Test）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "將角色全塗黑成剪影，測試組員能否在 0.5 秒內認出性格與身份。",
        "why": "高速動態中觀眾只能辨識外輪廓，外型立不住畫再精緻也是白搭。",
        "example": "主角剪影被誤認為小兵，概念師立刻加大披風與頭盔角特徵，辨識度瞬間滿分。"
    },
    {
        "id": "CON-04",
        "title": "04. 旋轉三視圖（Turnaround Sheet）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "畫出正側背三視圖，並用水平虛線貫穿頭頂、眼線、髖骨與膝蓋。",
        "why": "給動畫師精準的骨骼比例尺，杜絕不同作畫人員導致的角色走形崩壞。",
        "example": "動畫師旋轉角色時臉部忽大忽小，對照三視圖水平線後 10 分鐘修正走形。"
    },
    {
        "id": "CON-05",
        "title": "05. 九宮格表情（Expression Matrix）",
        "cat": "Learn · Look · <b>[Ask]</b> · Try",
        "how": "畫出角色的 9 個極端表情，標明眉骨與嘴角的形變最大容許極限。",
        "why": "防止角色動起來變成千篇一律的面癱，賦予表演真實人性。",
        "example": "動畫師做出誇張大哭，概念師亮出表情表提醒「主角性格內斂，只准咬牙忍淚」，秒校正表演。"
    },
    {
        "id": "CON-06",
        "title": "06. 前中遠分層（Layered Environment）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "場景繪製時強制將前景、中景平台與遠景分離，並補齊被遮擋處。",
        "why": "確保場景拿進合成與分鏡時能直接拉視差運鏡，避免後期穿幫露底。",
        "example": "分鏡推軌鏡頭時房子穿幫露白，因預先做了分層補筆，合成 0 秒修復視差。"
    },
    {
        "id": "CON-07",
        "title": "07. 高光定裝圖（Target Look）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "全片只精細畫 2 張最高潮鏡頭的光影概念圖，定為全片渲染品質天花板。",
        "why": "拒絕浪費時間細化幾十張背景，給全團隊一眼看懂「成品最終能多美」。",
        "example": "團隊猶豫最終渲染質感，概念師甩出 1 張決戰 Keyframe，全員瞬間達成品質共識。"
    },
    {
        "id": "CON-08",
        "title": "08. 筆刷與線條手冊（Line & Texture Guide）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "規定輪廓線粗細與有無壓感，並在共用雲端釘上專案唯一指定筆刷包。",
        "why": "多人協同作畫時畫風極易割裂，統一線條規則才能拼成同一部片。",
        "example": "兩位美術筆觸一粗一細，依手冊統一改用 5px 無壓感硬邊筆刷，畫面割裂感秒消失。"
    },
    {
        "id": "CON-09",
        "title": "09. 道具展開拆解（Prop Breakdown）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "畫出關鍵道具的「收納態」與「展開態」機構，並放上手掌比例尺。",
        "why": "防止動畫師在畫打鬥互動時，才發現道具卡死、握持比例嚴重失真。",
        "example": "動畫師原本不知道武器怎麼拔出，看著機關拆解圖 1 分鐘畫出拔刀動態。"
    },
    {
        "id": "CON-10",
        "title": "10. 乾淨資產交接（Asset Handoff）",
        "cat": "Learn · Look · <b>[Ask]</b> · Try",
        "how": "檔案圖層必須標準命名（BG_ / MG_ / Char_），刪除所有空圖層與草稿。",
        "why": "杜絕把髒亂檔案丟給下游造成的猜測與溝通內耗，保證流水線暢通。",
        "example": "分鏡師拿到帶有 50 個未命名圖層的 PSD 直接退件，概念師依規則 5 分鐘整理完畢重新交接。"
    }
]

cards_03 = [
    {
        "id": "STB-01",
        "title": "01. 拇指草圖流（Thumbnail Flow）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "在便簽紙小框內只畫火柴人與動態箭頭，每卡限時 2 分鐘，只抓動態連續感。",
        "why": "分鏡忌諱過早雕琢細節，極低成本試驗才能快速挑出最炸裂的運鏡組合。",
        "example": "分鏡師 20 分鐘畫出 3 套追逐戲草圖，導演當場挑中節奏最緊湊的一套。"
    },
    {
        "id": "STB-02",
        "title": "02. 景別心理距離（Shot Framing）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "依情緒高低選擇景別——冷靜交代用遠景，內心劇烈情緒與壓迫感必切特寫。",
        "why": "景別是掌控觀眾心理親密度的武器，胡亂切景會直接摧毀戲劇張力。",
        "example": "角色得知噩耗時原本用遠景，分鏡強制切成眼角抽搐的極特寫，悲傷感直擊人心。"
    },
    {
        "id": "STB-03",
        "title": "03. 運鏡動機律（Camera Dynamics）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "用雙框（起止點）標註推拉搖移，鏡頭每次運動都必須有角色心理動機。",
        "why": "禁止無意義的晃動與炫技運鏡，運動必須服務於角色的情緒或空間威脅。",
        "example": "原本無故橫移的鏡頭被改成緩慢推向門鎖，懸疑感與威脅感瞬間拉滿。"
    },
    {
        "id": "STB-04",
        "title": "04. 180度軸線鎖定（180-Degree Rule）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "在角色視線間畫一條軸線，所有機位必須放在同側，確保 A 永遠看右、B 永遠看左。",
        "why": "跳軸會摧毀觀眾的空間定位，讓對話變成兩人背對背的空間錯亂。",
        "example": "追逐戰中反派突然轉向左跑造成即將相撞的錯覺，修正機位後方向感立刻順暢。"
    },
    {
        "id": "STB-05",
        "title": "05. 粗剪動態測試（Animatic Test）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "把草圖排進時間軸對齊音軌播放，不滿意的秒數在剪輯軟體裡當場拉長或裁切。",
        "why": "90% 的節奏問題必須在動態腳本解決，嚴禁沒測過秒數就讓動畫師動筆。",
        "example": "實測發現對話中間空了 2 秒冷場，剪輯師手動砍掉 48 幀，整場戲瞬間俐落。"
    },
    {
        "id": "STB-06",
        "title": "06. 視線焦點追蹤（Focal Point Continuity）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "在前後兩格標出視覺焦點紅點，確保切鏡時紅點距離極近、視線不亂跳。",
        "why": "好的分鏡能催眠觀眾的眼球，視線大幅度亂跳會讓觀眾疲勞且漏看關鍵資訊。",
        "example": "主角拔槍鏡頭切換後槍出現在反方向，修正構圖讓槍口留在原視覺焦點，出槍快如閃電。"
    },
    {
        "id": "STB-07",
        "title": "07. 動作半途切鏡（Cut on Action）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "出拳、轉身或跳躍時，在動作進行到 50% 時切鏡，並保留 2 幀重疊動態。",
        "why": "利用高速動作掩蓋剪輯痕跡，創造行雲流水的隱形轉場。",
        "example": "揮劍砍下瞬間切特寫，動作完美銜接，觀眾完全感受不到切鏡的停頓。"
    },
    {
        "id": "STB-08",
        "title": "08. 動作與秒數標註（Timing & Action Notes）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "分鏡欄嚴格標註「鏡頭號、精確秒數、具體物理動詞、音效點」，禁止寫抒情散文。",
        "why": "分鏡是施工圖紙，寫「內心悲痛」只會引發歧義，寫「低頭落淚」動畫師才能直接做。",
        "example": "動畫師看不懂散文描述卡住，分鏡師改為標註「轉頭24幀+嘆氣音效」，立刻開工。"
    },
    {
        "id": "STB-09",
        "title": "09. 空間走位俯視圖（Floor Plan Blocking）",
        "cat": "Learn · Look · <b>[Ask]</b> · Try",
        "how": "在紙上畫出房間俯視圖，標註角色移動軌跡與攝影機視錐角度。",
        "why": "解決多角色對話時空間透視打架、人物瞬移或距離邏輯不通的底層 bug。",
        "example": "四人圓桌會議分鏡畫到打架，畫了俯視走位圖後 5 分鐘理清所有人視線。"
    },
    {
        "id": "STB-10",
        "title": "10. 分鏡鏡頭凍結（Picture Lock）",
        "cat": "Learn · Look · <b>[Ask]</b> · Try",
        "how": "全體觀看動態腳本 2 次並簽字凍結，正式開工後非編導特批嚴禁增減鏡頭。",
        "why": "動畫製作最大的浪費，就是辛辛苦苦畫完動態後才被告知「這個鏡頭故事不需要」。",
        "example": "動畫師開工後有人提議加一場打戲，全員拿出 Picture Lock 協議，1 秒否決無效加戲。"
    }
]

cards_04 = [
    {
        "id": "ANI-01",
        "title": "01. 黃金極值姿態（Key Poses First）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "先不畫補間，只畫出動作起點、最高受力點（Peak）與落點 3 張極限姿態。",
        "why": "關鍵姿態決定了動作的張力與靈魂；骨架姿態軟弱，畫再多中割也救不回來。",
        "example": "出拳動作無力，動畫師重調受力極值幀的扭腰與重心，打擊張力立刻翻倍。"
    },
    {
        "id": "ANI-02",
        "title": "02. 蓄力反向預備（Anticipation & Cushion）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "角色向前衝前必須先後仰蓄力，停下時必須往前衝過頭再回彈（Overshoot）。",
        "why": "沒有預備像抽筋，沒有緩衝像撞牆；蓄力是給觀眾大腦預判動作的時間。",
        "example": "跳躍動作加了 4 幀深蹲蓄力與落地膝蓋回彈，角色從紙片人瞬間變得有骨有肉。"
    },
    {
        "id": "ANI-03",
        "title": "03. 體積守恆變形（Squash & Stretch）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "落地擠壓扁平時橫向必須等比外擴，高速位移時拉長，肉眼總體積必須恆定。",
        "why": "賦予肉體彈性與生命力，同時守住物理體積，防止角色忽胖忽瘦走形。",
        "example": "角色下墜時被壓扁但未橫向外擴像縮小了，修正體積守恆後彈性肉感十足。"
    },
    {
        "id": "ANI-04",
        "title": "04. 圓潤運動弧線（Arcs & Spacing）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "在關節點連出運動軌跡，消除生硬直線，起步與結尾間距密集、中間拉大。",
        "why": "生物的有機旋轉都是弧線運動，弧線與慢入慢出是消除機械生硬感的關鍵。",
        "example": "手臂揮劍走直線像機器人，改成圓滑拋物線軌跡後動作行雲流水。"
    },
    {
        "id": "ANI-05",
        "title": "05. 一拍二律動表（X-Sheet Timing）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "全片常態鎖定一拍二（12fps），唯有極速爆發瞬間切換為一拍一（24fps）。",
        "why": "盲目全畫一拍一會耗盡產能，快慢對比才能產生最高級的打擊節奏。",
        "example": "平淡的打鬥全改為「靜止維持 6 幀 + 2 幀極速出刀」，省下一半工時且帥度爆表。"
    },
    {
        "id": "ANI-06",
        "title": "06. 通用元件資產庫（Puppet Library）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "預先繪製好 10 種標準手勢、8 種常用口型與原地循環走跑動態，供全組調用。",
        "why": "小團隊絕不能每卡從零手繪重複動作，資產複用率直接決定能否如期交片。",
        "example": "對白鏡頭直接套用標準口型庫，半天完成整場戲的對白動態。"
    },
    {
        "id": "ANI-07",
        "title": "07. 次級延遲慣性（Secondary Overlapping）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "頭髮、斗篷與飄帶比身體主幹延遲 2~4 幀運動，身體停下後飄帶繼續甩動。",
        "why": "次級動態是區分「業餘學生木偶戲」與「頂級生動動畫」的最強分水嶺。",
        "example": "主角急停後斗篷延遲往前翻卷再落下，動態層次感瞬間提升一個檔次。"
    },
    {
        "id": "ANI-08",
        "title": "08. 間距樹狀中割（In-between Chart）",
        "cat": "Learn · Look · <b>[Ask]</b> · Try",
        "how": "原畫右上角畫出間距標記樹（例：1---3-4-5），明確標註先割哪一幀。",
        "why": "消除中割助理的憑感覺瞎猜，保證補間動畫的加速度完全符合原畫意圖。",
        "example": "中割助理按照清晰的間距樹 1 小時補完中間幀，完全無需返工修改。"
    },
    {
        "id": "ANI-09",
        "title": "09. 真人錄影表演參考（Video Reference）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "畫複雜表演前，動畫師自己拿手機把動作演出來錄成短片，對照著抓重量感。",
        "why": "大腦憑空想像的動作容易缺乏重力反饋，真實人體才能提供肌肉受力的細節。",
        "example": "動畫師畫不出搬箱子的吃力感，錄下自己搬水桶的下沉姿態後 10 分鐘畫出重量感。"
    },
    {
        "id": "ANI-10",
        "title": "10. 閉合清線防抖檢驗（Clean-up & Boil QC）",
        "cat": "Learn · Look · <b>[Ask]</b> · Try",
        "how": "24fps 全速回放抓取線條閃爍（Boiling），並確認所有填色線條完全閉合。",
        "why": "漏色與抖動會導致下游特效合成徹底崩潰，動態工程必須乾淨無瑕疵。",
        "example": "著色前開啟自動閉合間隙功能，避免油漆桶溢出，省下整整 2 天補色時間。"
    }
]

cards_05 = [
    {
        "id": "VFX-01",
        "title": "01. 五層通道規範（Layer Passes Pipeline）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "圖層嚴格按「大氣/前景/特效/角色/背景」5層命名，全數保留 Alpha 透明通道。",
        "why": "防止調一個光效就把背後的角色背景一起壓死，確保後期隨時可獨立微調。",
        "example": "導演臨時要求調亮背景，合成師因通道完全獨立，10 秒內調整完畢無需重導。"
    },
    {
        "id": "VFX-02",
        "title": "02. 地面接觸陰影（Contact Shadow & AO）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "腳底接觸面加一條極薄極黑的接觸影，外圍羽化漫射，並染上微量地面反彈光。",
        "why": "角色沒有接觸陰影會像漂浮在空中的貼圖，接地陰影是扎根世界的重力證明。",
        "example": "合成師提取角色腳底做出一道緊貼暗線，原本懸浮的角色立刻踩實地面。"
    },
    {
        "id": "VFX-03",
        "title": "03. 空氣透視衰減（Atmosphere & Fog）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "遠景明暗對比度強制壓低，色彩向天光色偏移，並在光柱處加緩慢飄動微粒。",
        "why": "二維畫面極易顯得扁平，空氣透視是營造數公里縱深感的最高效手法。",
        "example": "平淡的走廊疊加了一層淡藍遠景霧氣與丁達爾光，空間縱深感翻倍。"
    },
    {
        "id": "VFX-04",
        "title": "04. 風格化二維特效（Stylized 2D FX）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "煙霧用球體聚散、火焰用S形銳角撕裂，嚴禁直接貼真實電影爆炸罐頭素材。",
        "why": "寫實素材會摧毀手繪動畫的藝術世界觀，特效必須具備符號化的手繪動態。",
        "example": "拿掉寫實火球，換上手繪三色分階的動態火焰，全片美術風格瞬間統一。"
    },
    {
        "id": "VFX-05",
        "title": "05. 撞擊瞬時爆發（Impact Momentum Sync）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "碎石與火星在受力第 1 幀生成 80% 粒子極速噴出，隨後施加空氣阻力減速。",
        "why": "勻速飄動的粒子毫無打擊反饋，瞬時爆發才能傳遞出毀天滅地的破壞力。",
        "example": "粒子從均勻散落改為撞擊瞬間呈扇形高速炸裂，重拳落地衝擊力翻倍。"
    },
    {
        "id": "VFX-06",
        "title": "06. 微量光學瑕疵（Film Grain & Vignette）",
        "cat": "Learn · <b>[Look]</b> · Ask · Try",
        "how": "全片疊加 2% 細緻膠片噪點，四角壓低 5% 暗角，邊緣微量色散 1 像素。",
        "why": "適度光學缺陷能消除電腦繪圖的冰冷塑料感，是大腦辨識電影質感的開關。",
        "example": "純數位色塊疊加微噪點與暗角後，各圖層像素質地完美融合，電影感十足。"
    },
    {
        "id": "VFX-07",
        "title": "07. 色彩腳本統一調色（Color Grading LUT）",
        "cat": "<b>[Learn]</b> · Look · Ask · Try",
        "how": "依據色彩腳本統一全片色溫，暗部壓冷青、高光帶微暖，輸出唯一風格 LUT。",
        "why": "消除多人協同繪畫時無可避免的色差，讓所有鏡頭擁有大片級的整齊色調。",
        "example": "套用統一風格 LUT 後，原本不同繪師畫的 10 個場景瞬間像同一部片。"
    },
    {
        "id": "VFX-08",
        "title": "08. 殘影速度線轉場（Smear & Speedlines）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "位移超過畫面 15% 時加方向性模糊，撞擊瞬切 1 幀閃白（Impact Flash）。",
        "why": "手繪幀率有限，視覺暫留與閃白是克服卡頓、爆發速度感的終極利器。",
        "example": "高速揮刀瞬間插入 1 幀純白負片，切鏡時打擊感震撼全場。"
    },
    {
        "id": "VFX-09",
        "title": "09. 音畫同幀重音打擊（Audio-Visual Sync）",
        "cat": "Learn · Look · Ask · <b>[Try]</b>",
        "how": "光效最大亮度和鏡頭震動第 1 幀，必須精確踩在音效音頻波形的垂直尖峰上。",
        "why": "差 1 幀（0.04 秒）打擊感就會從「拳拳到肉」變成「棉花打架」。",
        "example": "鏡頭震動提前 2 幀對齊重音鼓點，原本綿軟的爆炸瞬間震撼耳膜。"
    },
    {
        "id": "VFX-10",
        "title": "10. 雙母帶跨設備驗收（Master Render QC）",
        "cat": "Learn · Look · <b>[Ask]</b> · Try",
        "how": "導出 ProRes 422 HQ 無損母帶與 MP4 預覽版，在手機和投影機各完整放映一次。",
        "why": "防止在專業螢幕好看、放到廉價手機暗部全死黑或投屏音畫不同步的悲劇。",
        "example": "手機實測發現夜戲暗部全黑看不清臉，合成師提亮中間調 5%，全設備完美過審。"
    }
]

def make_markdown(title_h1, subtitle, cards):
    lines = [f"# 動畫製作 IDEO 方法卡（精簡高效版）\n\n## {title_h1}\n\n> {subtitle}\n\n---"]
    for c in cards:
        cat_plain = re.sub(r"<.*?>", "", c["cat"])
        lines.append(f"\n### {c['title']}\n")
        lines.append(f"* **頂部分類**：{cat_plain}")
        lines.append(f"* **HOW**：{c['how']}")
        lines.append(f"* **WHY**：{c['why']}")
        lines.append(f"* **案例**：{c['example']}\n\n---")
    return "\n".join(lines)

# Write clean markdown files
with open(os.path.join(repo_dir, "02_Concept.md"), "w", encoding="utf-8") as f:
    f.write(make_markdown("模組二：概念設計 Concept（10張）", "視覺世界觀、風格資產與角色場景規範", cards_02))

with open(os.path.join(repo_dir, "03_Storyboard.md"), "w", encoding="utf-8") as f:
    f.write(make_markdown("模組三：分鏡 Storyboard（10張）", "鏡頭語言、動態腳本與節奏工程", cards_03))

with open(os.path.join(repo_dir, "04_Animation.md"), "w", encoding="utf-8") as f:
    f.write(make_markdown("模組四：動畫 Animation（10張）", "12法則實務、極值姿態與表演生命力", cards_04))

# VFX & Rules
lines_05 = [make_markdown("模組五：特效與合成 VFX & Comp（10張）", "圖層通道、接地陰影、大氣透視與全片調色", cards_05)]
rule_card_md = """

## 核心規則模組：5人小團隊兼任矩陣與秒級決策律（Rule Card）

---

### RULE-01. 5人團隊多工兼任角色矩陣
* **頂部分類**：[Learn] · 全局協同
* **HOW**：成員 A 主導編導與剪輯聲音；成員 B 主導概念與背景；成員 C 主導分鏡與原畫；成員 D 主導動畫執行與中割；成員 E 主導特效合成與母帶 QC。
* **WHY**：5 人小組不准有純指揮官，全員皆兵、主責一道工序並兼任下游，產能最大化。
* **案例**：分鏡師畫完立刻接手關鍵原畫，避免交接解釋成本，作畫進度直接提前 1 週。

---

### RULE-02. IDEO 卡牌三階調用機制
* **頂部分類**：[Try] · 敏捷排障
* **HOW**：每日立會抽 1 張當前卡作為產出標準；任何環節卡關超 1 天立刻亮紅燈強制按卡執行；驗收依交付標的點交。
* **WHY**：用客觀工具卡代替主觀爭論，把溝通與扯皮成本降到最低。
* **案例**：概念設計卡關 2 天，全員亮出「情緒板過濾卡」強制砍到剩 20 張參考圖，當天下午順利定案。

---

### RULE-03. 爭端終結三秒律
* **頂部分類**：[Ask] · 秒級定案
* **HOW**：故事時長爭議由成員 A（編導）一票否決；畫風審美由成員 B（概念）一票定奪；產能超時由成員 C/D/E（製作組）一票拒絕。
* **WHY**：告別無休止的民主投票與空耗會議，賦予各領域負責人絕對裁決權。
* **案例**：會議爭論結局要不要死人超過 1 小時，編導行使一票否決權 3 秒定案，團隊立刻散會開工。
"""
lines_05.append(rule_card_md)
with open(os.path.join(repo_dir, "05_VFX_Comp_Rules.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines_05))

print("Updated all markdown files cleanly!")
