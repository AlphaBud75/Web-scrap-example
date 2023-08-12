from selenium import webdriver
import re
from bs4 import BeautifulSoup

html_text = '''<br> 1. <a href="jinpingmei/ch1/zhs">西门庆热结十弟兄　武二郎冷遇亲哥嫂</a>
<br>　2. <a href="jinpingmei/ch2/zhs">俏潘娘帘下勾情　老王婆茶坊说技</a>
<br>　3. <a href="jinpingmei/ch3/zhs">定挨光王婆受贿　设圈套浪子私挑</a>
<br>　4. <a href="jinpingmei/ch4/zhs">赴巫山潘氏幽欢　闹茶坊郓哥义愤</a>
<br>　5. <a href="jinpingmei/ch5/zhs">捉奸情郓哥定计　饮鸩药武大遭殃</a>
<br>　6. <a href="jinpingmei/ch6/zhs">何九受贿瞒天　王婆帮闲遇雨</a>
<br>　7. <a href="jinpingmei/ch7/zhs">薛媒婆说娶孟三儿　杨姑娘气骂张四舅</a>
<br>　8. <a href="jinpingmei/ch8/zhs">盼情郎佳人占鬼卦　烧夫灵和尚听淫声</a>
<br>　9. <a href="jinpingmei/ch9/zhs">西门庆偷娶潘金莲　武都头误打李皂隶</a>
<br>　10. <a href="jinpingmei/ch10/zhs">义士充配孟州道　妻妾玩赏芙蓉亭</a>
<br>　11. <a href="jinpingmei/ch11/zhs">潘金莲激打孙雪娥　西门庆梳笼李桂姐</a>
<br>　12. <a href="jinpingmei/ch12/zhs">潘金莲私仆受辱　刘理星魇胜求财</a>
<br>　13. <a href="jinpingmei/ch13/zhs">李瓶姐墙头密约　迎春儿隙底私窥</a>
<br>　14. <a href="jinpingmei/ch14/zhs">花子虚因气丧身　李瓶儿迎奸赴会</a>
<br>　15. <a href="jinpingmei/ch15/zhs">佳人笑赏玩灯楼　狎客帮嫖丽春院</a>
<br>　16. <a href="jinpingmei/ch16/zhs">西门庆择吉佳期　应伯爵追欢喜庆</a>
<br>　17. <a href="jinpingmei/ch17/zhs">宇给事劾倒杨提督　李瓶儿许嫁蒋竹山</a>
<br>　18. <a href="jinpingmei/ch18/zhs">赂相府西门脱祸　见娇娘敬济销魂</a>
<br>　19. <a href="jinpingmei/ch19/zhs">草里蛇逻打蒋竹山　李瓶儿情感西门庆</a>
<br>　20. <a href="jinpingmei/ch20/zhs">傻帮闲趋奉闹华筵　痴子弟争锋毁花院</a>
<br>　21. <a href="jinpingmei/ch21/zhs">吴月娘扫雪烹茶　应伯爵替花邀酒</a>
<br>　22. <a href="jinpingmei/ch22/zhs">蕙莲儿偷期蒙爱　春梅姐正色闲邪</a>
<br>　23. <a href="jinpingmei/ch23/zhs">赌棋枰瓶儿输钞　觑藏春潘氏潜踪</a>
<br>　24. <a href="jinpingmei/ch24/zhs">敬济元夜戏娇姿　惠祥怒詈来旺妇</a>
<br>　25. <a href="jinpingmei/ch25/zhs">吴月娘春昼秋千　来旺儿醉中谤仙</a>
<br>　26. <a href="jinpingmei/ch26/zhs">来旺儿递解徐州　宋蕙莲含羞自缢</a>
<br>　27. <a href="jinpingmei/ch27/zhs">李瓶儿私语翡翠轩　潘金莲醉闹葡萄架</a>
<br>　28. <a href="jinpingmei/ch28/zhs">陈敬济徼幸得金莲　西门庆糊涂打铁棍</a>
<br>　29. <a href="jinpingmei/ch29/zhs">吴神仙冰鉴定终身　潘金莲兰汤邀午战</a>
<br>　30. <a href="jinpingmei/ch30/zhs">蔡太师擅恩锡爵　西门庆生子加官</a>
<br>　31. <a href="jinpingmei/ch31/zhs">琴童儿藏壶构衅　西门庆开宴为欢</a>
<br>　32. <a href="jinpingmei/ch32/zhs">李桂姐趋炎认女　潘金莲怀妒惊儿</a>
<br>　33. <a href="jinpingmei/ch33/zhs">陈敬济失钥罚唱　韩道国纵妇争锋</a>
<br>　34. <a href="jinpingmei/ch34/zhs">献芳樽内室乞恩　受私贿后庭说事</a>
<br>　35. <a href="jinpingmei/ch35/zhs">西门庆为男宠报仇　书童儿作女妆媚客</a>
<br>　36. <a href="jinpingmei/ch36/zhs">翟管家寄书寻女子　蔡状元留饮借盘缠</a>
<br>　37. <a href="jinpingmei/ch37/zhs">冯妈妈说嫁韩爱姐　西门庆包占王六儿</a>
<br>　38. <a href="jinpingmei/ch38/zhs">王六儿棒槌打捣鬼　潘金莲雪夜弄琵琶</a>
<br>　39. <a href="jinpingmei/ch39/zhs">寄法名官哥穿道服　散生日敬济拜冤家</a>
<br>　40. <a href="jinpingmei/ch40/zhs">抱孩童瓶儿希宠　妆丫鬟金莲市爱</a>
<br>　41. <a href="jinpingmei/ch41/zhs">两孩儿联姻共笑嬉　二佳人愤深同气苦</a>
<br>　42. <a href="jinpingmei/ch42/zhs">逞豪华门前放烟火　赏元宵楼上醉花灯</a>
<br>　43. <a href="jinpingmei/ch43/zhs">争宠爱金莲惹气　卖富贵吴月攀亲</a>
<br>　44. <a href="jinpingmei/ch44/zhs">避马房侍女偷金　下象棋佳人消夜</a>
<br>　45. <a href="jinpingmei/ch45/zhs">应伯爵劝当铜锣　李瓶儿解衣银姐</a>
<br>　46. <a href="jinpingmei/ch46/zhs">元夜游行遇雪雨　妻妾戏笑卜龟儿</a>
<br>　47. <a href="jinpingmei/ch47/zhs">苗青贪财害主　西门枉法受赃</a>
<br>　48. <a href="jinpingmei/ch48/zhs">弄私情戏赠一枝桃　走捷径探归七件事</a>
<br>　49. <a href="jinpingmei/ch49/zhs">请巡按屈体求荣　遇胡僧现身施药</a>
<br>　50. <a href="jinpingmei/ch50/zhs">琴童潜听燕莺欢　玳安嬉游蝴蝶巷</a>
<br>　51. <a href="jinpingmei/ch51/zhs">打猫儿金莲品玉　斗叶子敬济输金</a>
<br>　52. <a href="jinpingmei/ch52/zhs">应伯爵山洞戏春娇　潘金莲花园调爱婿</a>
<br>　53. <a href="jinpingmei/ch53/zhs">潘金莲惊散幽欢　吴月娘拜求子息</a>
<br>　54. <a href="jinpingmei/ch54/zhs">应伯爵隔花戏金钏　任医官垂帐诊瓶儿</a>
<br>　55. <a href="jinpingmei/ch55/zhs">西门庆两番庆寿旦　苗员外一诺送歌童</a>
<br>　56. <a href="jinpingmei/ch56/zhs">西门庆捐金助朋友　常峙节得钞傲妻儿</a>
<br>　57. <a href="jinpingmei/ch57/zhs">开缘簿千金喜舍　戏雕栏一笑回嗔</a>
<br>　58. <a href="jinpingmei/ch58/zhs">潘金莲打狗伤人　孟玉楼周贫磨镜</a>
<br>　59. <a href="jinpingmei/ch59/zhs">西门庆露阳惊爱月　李瓶儿睹物哭官哥</a>
<br>　60. <a href="jinpingmei/ch60/zhs">李瓶儿病缠死孽　西门庆官作生涯</a>
<br>　61. <a href="jinpingmei/ch61/zhs">西门庆乘醉烧阴户　李瓶儿带病宴重阳</a>
<br>　62. <a href="jinpingmei/ch62/zhs">潘道士法遣黄巾士　西门庆大哭李瓶儿</a>
<br>　63. <a href="jinpingmei/ch63/zhs">韩画士传真作遗爱　西门庆观戏动深悲</a>
<br>　64. <a href="jinpingmei/ch64/zhs">玉箫跪受三章约　书童私挂一帆风</a>
<br>　65. <a href="jinpingmei/ch65/zhs">愿同穴一时丧礼盛　守孤灵半夜口脂香</a>
<br>　66. <a href="jinpingmei/ch66/zhs">翟管家寄书致赙　黄真人发牒荐亡</a>
<br>　67. <a href="jinpingmei/ch67/zhs">西门庆书房赏雪　李瓶儿梦诉幽情</a>
<br>　68. <a href="jinpingmei/ch68/zhs">应伯爵戏衔玉臂　玳安儿密访蜂媒</a>
<br>　69. <a href="jinpingmei/ch69/zhs">招宣府初调林太太　丽春院惊走王三官</a>
<br>　70. <a href="jinpingmei/ch70/zhs">老太监引酌朝房　二提刑庭参太尉</a>
<br>　71. <a href="jinpingmei/ch71/zhs">李瓶儿何家托梦　提刑官引奏朝仪</a>
<br>　72. <a href="jinpingmei/ch72/zhs">潘金莲抠打如意儿　王三官义拜西门庆</a>
<br>　73. <a href="jinpingmei/ch73/zhs">潘金莲不愤忆吹箫　西门庆新试白绫带</a>
<br>　74. <a href="jinpingmei/ch74/zhs">潘金莲香腮偎玉　薛姑子佛口谈经</a>
<br>　75. <a href="jinpingmei/ch75/zhs">因抱恙玉姐含酸　为护短金莲泼醋</a>
<br>　76. <a href="jinpingmei/ch76/zhs">春梅娇撒西门庆　画童哭躲温葵轩</a>
<br>　77. <a href="jinpingmei/ch77/zhs">西门庆踏雪访爱月　贲四嫂带水战情郎</a>
<br>　78. <a href="jinpingmei/ch78/zhs">林太太鸳帏再战　如意儿茎露独尝</a>
<br>　79. <a href="jinpingmei/ch79/zhs">西门庆贪欲丧命　吴月娘失偶生儿</a>
<br>　80. <a href="jinpingmei/ch80/zhs">潘金莲售色赴东床　李娇儿盗财归丽院</a>
<br>　81. <a href="jinpingmei/ch81/zhs">韩道国拐财远遁　汤来保欺主背恩</a>
<br>　82. <a href="jinpingmei/ch82/zhs">陈敬济弄一得双　潘金莲热心冷面</a>
<br>　83. <a href="jinpingmei/ch83/zhs">秋菊含恨泄幽情　春梅寄柬谐佳会</a>
<br>　84. <a href="jinpingmei/ch84/zhs">吴月娘大闹碧霞宫　曾静师化缘雪涧洞</a>
<br>　85. <a href="jinpingmei/ch85/zhs">吴月娘识破奸情　春梅姐不垂别泪</a>
<br>　86. <a href="jinpingmei/ch86/zhs">雪娥唆打陈敬济　金莲解渴王潮儿</a>
<br>　87. <a href="jinpingmei/ch87/zhs">王婆子贪财忘祸　武都头杀嫂祭兄</a>
<br>　88. <a href="jinpingmei/ch88/zhs">陈敬济感旧祭金莲　庞大姐埋尸托张胜</a>
<br>　89. <a href="jinpingmei/ch89/zhs">清明节寡妇上新坟　永福寺夫人逢故主</a>
<br>　90. <a href="jinpingmei/ch90/zhs">来旺偷拐孙雪娥　雪娥受辱守备府</a>
<br>　91. <a href="jinpingmei/ch91/zhs">孟玉楼爱嫁李衙内　李衙内怒打玉簪儿</a>
<br>　92. <a href="jinpingmei/ch92/zhs">陈敬济被陷严州府　吴月娘大闹授官厅</a>
<br>　93. <a href="jinpingmei/ch93/zhs">王杏庵义恤贫儿　金道士娈淫少弟</a>
<br>　94. <a href="jinpingmei/ch94/zhs">大酒楼刘二撒泼　洒家店雪娥为娼</a>
<br>　95. <a href="jinpingmei/ch95/zhs">玳安儿窃玉成婚　吴典恩负心被辱</a>
<br>　96. <a href="jinpingmei/ch96/zhs">春梅姐游旧家池馆　杨光彦作当面豺狼</a>
<br>　97. <a href="jinpingmei/ch97/zhs">假弟妹暗续鸾胶　真夫妇明谐花烛</a>
<br>　98. <a href="jinpingmei/ch98/zhs">陈敬济临清逢旧识　韩爱姐翠馆遇情郎</a>
<br>　99. <a href="jinpingmei/ch99/zhs">刘二醉骂王六儿　张胜窃听张敬济</a>
<br>　100. <a href="jinpingmei/ch100/zhs">韩爱姐路遇二捣鬼　普静师幻度孝哥儿</a>'''
base_url = 'https://ctext.org/'
l1 = []
dir_name = '小说-金瓶梅/'
file_extension = '.txt'
# file_extension = '.html'

# <br>　8. <a href="jinpingmei/ch8/zhs">盼情郎佳人占鬼卦　烧夫灵和尚听淫声</a>

for line in html_text.splitlines():
    l1.append([
        base_url + '/' + line[line.find("=\"") + 2: line.find("\">")],  # link
        re.search("\s\d?\d?\d?\.", line.replace('\u3000', ' ')).group()[1:-1],  # chap number
        line[line.find("\">") + 2: line.find("</a")].replace('\u3000', '_'),  # title
    ])

# print(l1)
# l1 = l1[1:2]

driver = webdriver.Chrome()
for e in l1:
    driver.get(e[0])
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print('###############')
    print(dir_name + e[1] + '_' + e[2] + file_extension)

    for c in list(soup.find(id="content3").findAll('td')):
        # print('###############')
        temp = str(c.text).replace('打开字典', '').replace(e[2][:4]+'... :', '')
        print(temp)

        with open(dir_name + e[1] + '_' + e[2] + file_extension, "a+", encoding='utf-8') as f:
            # print(dir_name + e[1] + '_' + e[2] + file_extension)
            f.write(temp)
            f.write('\n\n')
