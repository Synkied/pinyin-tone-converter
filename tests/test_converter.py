from pinyin_tone_converter.pinyin_tone_converter import PinyinToneConverter

correct_input_and_output = {
    "bo1": "bō",
    "bo2": "bó",
    "bo3": "bǒ",
    "bo4": "bò",
    "ba1": "bā",
    "ba2": "bá",
    "ba3": "bǎ",
    "ba4": "bà",
    "bai1": "bāi",
    "bai2": "bái",
    "bai3": "bǎi",
    "bai4": "bài",
    "bei1": "bēi",
    "bei2": "béi",
    "bei3": "běi",
    "bei4": "bèi",
    "bao1": "bāo",
    "bao2": "báo",
    "bao3": "bǎo",
    "bao4": "bào",
    "ban1": "bān",
    "ban2": "bán",
    "ban3": "bǎn",
    "ban4": "bàn",
    "ben1": "bēn",
    "ben2": "bén",
    "ben3": "běn",
    "ben4": "bèn",
    "bang1": "bāng",
    "bang2": "báng",
    "bang3": "bǎng",
    "bang4": "bàng",
    "beng1": "bēng",
    "beng2": "béng",
    "beng3": "běng",
    "beng4": "bèng",
    "bu1": "bū",
    "bu2": "bú",
    "bu3": "bǔ",
    "bu4": "bù",
    "bi1": "bī",
    "bi2": "bí",
    "bi3": "bǐ",
    "bi4": "bì",
    "bie1": "biē",
    "bie2": "bié",
    "bie3": "biě",
    "bie4": "biè",
    "biao1": "biāo",
    "biao2": "biáo",
    "biao3": "biǎo",
    "biao4": "biào",
    "bian1": "biān",
    "bian2": "bián",
    "bian3": "biǎn",
    "bian4": "biàn",
    "bin1": "bīn",
    "bin2": "bín",
    "bin3": "bǐn",
    "bin4": "bìn",
    "bing1": "bīng",
    "bing2": "bíng",
    "bing3": "bǐng",
    "bing4": "bìng",
    "po1": "pō",
    "po2": "pó",
    "po3": "pǒ",
    "po4": "pò",
    "pa1": "pā",
    "pa2": "pá",
    "pa3": "pǎ",
    "pa4": "pà",
    "pai1": "pāi",
    "pai2": "pái",
    "pai3": "pǎi",
    "pai4": "pài",
    "pei1": "pēi",
    "pei2": "péi",
    "pei3": "pěi",
    "pei4": "pèi",
    "pao1": "pāo",
    "pao2": "páo",
    "pao3": "pǎo",
    "pao4": "pào",
    "pou1": "pōu",
    "pou2": "póu",
    "pou3": "pǒu",
    "pou4": "pòu",
    "pan1": "pān",
    "pan2": "pán",
    "pan3": "pǎn",
    "pan4": "pàn",
    "pen1": "pēn",
    "pen2": "pén",
    "pen3": "pěn",
    "pen4": "pèn",
    "pang1": "pāng",
    "pang2": "páng",
    "pang3": "pǎng",
    "pang4": "pàng",
    "peng1": "pēng",
    "peng2": "péng",
    "peng3": "pěng",
    "peng4": "pèng",
    "pu1": "pū",
    "pu2": "pú",
    "pu3": "pǔ",
    "pu4": "pù",
    "pi1": "pī",
    "pi2": "pí",
    "pi3": "pǐ",
    "pi4": "pì",
    "pie1": "piē",
    "pie2": "pié",
    "pie3": "piě",
    "pie4": "piè",
    "piao1": "piāo",
    "piao2": "piáo",
    "piao3": "piǎo",
    "piao4": "piào",
    "pian1": "piān",
    "pian2": "pián",
    "pian3": "piǎn",
    "pian4": "piàn",
    "pin1": "pīn",
    "pin2": "pín",
    "pin3": "pǐn",
    "pin4": "pìn",
    "ping1": "pīng",
    "ping2": "píng",
    "ping3": "pǐng",
    "ping4": "pìng",
    "mo1": "mō",
    "mo2": "mó",
    "mo3": "mǒ",
    "mo4": "mò",
    "ma1": "mā",
    "ma2": "má",
    "ma3": "mǎ",
    "ma4": "mà",
    "me1": "mē",
    "me2": "mé",
    "me3": "mě",
    "me4": "mè",
    "mai1": "māi",
    "mai2": "mái",
    "mai3": "mǎi",
    "mai4": "mài",
    "mei1": "mēi",
    "mei2": "méi",
    "mei3": "měi",
    "mei4": "mèi",
    "mao1": "māo",
    "mao2": "máo",
    "mao3": "mǎo",
    "mao4": "mào",
    "mou1": "mōu",
    "mou2": "móu",
    "mou3": "mǒu",
    "mou4": "mòu",
    "man1": "mān",
    "man2": "mán",
    "man3": "mǎn",
    "man4": "màn",
    "men1": "mēn",
    "men2": "mén",
    "men3": "měn",
    "men4": "mèn",
    "mang1": "māng",
    "mang2": "máng",
    "mang3": "mǎng",
    "mang4": "màng",
    "meng1": "mēng",
    "meng2": "méng",
    "meng3": "měng",
    "meng4": "mèng",
    "mu1": "mū",
    "mu2": "mú",
    "mu3": "mǔ",
    "mu4": "mù",
    "mi1": "mī",
    "mi2": "mí",
    "mi3": "mǐ",
    "mi4": "mì",
    "mie1": "miē",
    "mie2": "mié",
    "mie3": "miě",
    "mie4": "miè",
    "miao1": "miāo",
    "miao2": "miáo",
    "miao3": "miǎo",
    "miao4": "miào",
    "miu1": "miū",
    "miu2": "miú",
    "miu3": "miǔ",
    "miu4": "miù",
    "mian1": "miān",
    "mian2": "mián",
    "mian3": "miǎn",
    "mian4": "miàn",
    "min1": "mīn",
    "min2": "mín",
    "min3": "mǐn",
    "min4": "mìn",
    "ming1": "mīng",
    "ming2": "míng",
    "ming3": "mǐng",
    "ming4": "mìng",
    "fo1": "fō",
    "fo2": "fó",
    "fo3": "fǒ",
    "fo4": "fò",
    "fa1": "fā",
    "fa2": "fá",
    "fa3": "fǎ",
    "fa4": "fà",
    "fei1": "fēi",
    "fei2": "féi",
    "fei3": "fěi",
    "fei4": "fèi",
    "fou1": "fōu",
    "fou2": "fóu",
    "fou3": "fǒu",
    "fou4": "fòu",
    "fan1": "fān",
    "fan2": "fán",
    "fan3": "fǎn",
    "fan4": "fàn",
    "fen1": "fēn",
    "fen2": "fén",
    "fen3": "fěn",
    "fen4": "fèn",
    "fang1": "fāng",
    "fang2": "fáng",
    "fang3": "fǎng",
    "fang4": "fàng",
    "feng1": "fēng",
    "feng2": "féng",
    "feng3": "fěng",
    "feng4": "fèng",
    "fu1": "fū",
    "fu2": "fú",
    "fu3": "fǔ",
    "fu4": "fù",
    "de1": "dē",
    "de2": "dé",
    "de3": "dě",
    "de4": "dè",
    "da1": "dā",
    "da2": "dá",
    "da3": "dǎ",
    "da4": "dà",
    "dai1": "dāi",
    "dai2": "dái",
    "dai3": "dǎi",
    "dai4": "dài",
    "dei1": "dēi",
    "dei2": "déi",
    "dei3": "děi",
    "dei4": "dèi",
    "dao1": "dāo",
    "dao2": "dáo",
    "dao3": "dǎo",
    "dao4": "dào",
    "dou1": "dōu",
    "dou2": "dóu",
    "dou3": "dǒu",
    "dou4": "dòu",
    "dan1": "dān",
    "dan2": "dán",
    "dan3": "dǎn",
    "dan4": "dàn",
    "den1": "dēn",
    "den2": "dén",
    "den3": "děn",
    "den4": "dèn",
    "dang1": "dāng",
    "dang2": "dáng",
    "dang3": "dǎng",
    "dang4": "dàng",
    "deng1": "dēng",
    "deng2": "déng",
    "deng3": "děng",
    "deng4": "dèng",
    "dong1": "dōng",
    "dong2": "dóng",
    "dong3": "dǒng",
    "dong4": "dòng",
    "du1": "dū",
    "du2": "dú",
    "du3": "dǔ",
    "du4": "dù",
    "duo1": "duō",
    "duo2": "duó",
    "duo3": "duǒ",
    "duo4": "duò",
    "dui1": "duī",
    "dui2": "duí",
    "dui3": "duǐ",
    "dui4": "duì",
    "duan1": "duān",
    "duan2": "duán",
    "duan3": "duǎn",
    "duan4": "duàn",
    "dun1": "dūn",
    "dun2": "dún",
    "dun3": "dǔn",
    "dun4": "dùn",
    "di1": "dī",
    "di2": "dí",
    "di3": "dǐ",
    "di4": "dì",
    "dia1": "diā",
    "dia2": "diá",
    "dia3": "diǎ",
    "dia4": "dià",
    "die1": "diē",
    "die2": "dié",
    "die3": "diě",
    "die4": "diè",
    "diao1": "diāo",
    "diao2": "diáo",
    "diao3": "diǎo",
    "diao4": "diào",
    "diu1": "diū",
    "diu2": "diú",
    "diu3": "diǔ",
    "diu4": "diù",
    "dian1": "diān",
    "dian2": "dián",
    "dian3": "diǎn",
    "dian4": "diàn",
    "ding1": "dīng",
    "ding2": "díng",
    "ding3": "dǐng",
    "ding4": "dìng",
    "te1": "tē",
    "te2": "té",
    "te3": "tě",
    "te4": "tè",
    "ta1": "tā",
    "ta2": "tá",
    "ta3": "tǎ",
    "ta4": "tà",
    "tai1": "tāi",
    "tai2": "tái",
    "tai3": "tǎi",
    "tai4": "tài",
    "tei1": "tēi",
    "tei2": "téi",
    "tei3": "těi",
    "tei4": "tèi",
    "tao1": "tāo",
    "tao2": "táo",
    "tao3": "tǎo",
    "tao4": "tào",
    "tou1": "tōu",
    "tou2": "tóu",
    "tou3": "tǒu",
    "tou4": "tòu",
    "tan1": "tān",
    "tan2": "tán",
    "tan3": "tǎn",
    "tan4": "tàn",
    "tang1": "tāng",
    "tang2": "táng",
    "tang3": "tǎng",
    "tang4": "tàng",
    "teng1": "tēng",
    "teng2": "téng",
    "teng3": "těng",
    "teng4": "tèng",
    "tong1": "tōng",
    "tong2": "tóng",
    "tong3": "tǒng",
    "tong4": "tòng",
    "tu1": "tū",
    "tu2": "tú",
    "tu3": "tǔ",
    "tu4": "tù",
    "tuo1": "tuō",
    "tuo2": "tuó",
    "tuo3": "tuǒ",
    "tuo4": "tuò",
    "tui1": "tuī",
    "tui2": "tuí",
    "tui3": "tuǐ",
    "tui4": "tuì",
    "tuan1": "tuān",
    "tuan2": "tuán",
    "tuan3": "tuǎn",
    "tuan4": "tuàn",
    "tun1": "tūn",
    "tun2": "tún",
    "tun3": "tǔn",
    "tun4": "tùn",
    "ti1": "tī",
    "ti2": "tí",
    "ti3": "tǐ",
    "ti4": "tì",
    "tie1": "tiē",
    "tie2": "tié",
    "tie3": "tiě",
    "tie4": "tiè",
    "tiao1": "tiāo",
    "tiao2": "tiáo",
    "tiao3": "tiǎo",
    "tiao4": "tiào",
    "tian1": "tiān",
    "tian2": "tián",
    "tian3": "tiǎn",
    "tian4": "tiàn",
    "ne1": "nē",
    "ne2": "né",
    "ne3": "ně",
    "ne4": "nè",
    "na1": "nā",
    "na2": "ná",
    "na3": "nǎ",
    "na4": "nà",
    "nai1": "nāi",
    "nai2": "nái",
    "nai3": "nǎi",
    "nai4": "nài",
    "nei1": "nēi",
    "nei2": "néi",
    "nei3": "něi",
    "nei4": "nèi",
    "nao1": "nāo",
    "nao2": "náo",
    "nao3": "nǎo",
    "nao4": "nào",
    "nou1": "nōu",
    "nou2": "nóu",
    "nou3": "nǒu",
    "nou4": "nòu",
    "nan1": "nān",
    "nan2": "nán",
    "nan3": "nǎn",
    "nan4": "nàn",
    "nen1": "nēn",
    "nen2": "nén",
    "nen3": "něn",
    "nen4": "nèn",
    "nang1": "nāng",
    "nang2": "náng",
    "nang3": "nǎng",
    "nang4": "nàng",
    "neng1": "nēng",
    "neng2": "néng",
    "neng3": "něng",
    "neng4": "nèng",
    "nong1": "nōng",
    "nong2": "nóng",
    "nong3": "nǒng",
    "nong4": "nòng",
    "nu1": "nū",
    "nu2": "nú",
    "nu3": "nǔ",
    "nu4": "nù",
    "nuo1": "nuō",
    "nuo2": "nuó",
    "nuo3": "nuǒ",
    "nuo4": "nuò",
    "nuan1": "nuān",
    "nuan2": "nuán",
    "nuan3": "nuǎn",
    "nuan4": "nuàn",
    "nun1": "nūn",
    "nun2": "nún",
    "nun3": "nǔn",
    "nun4": "nùn",
    "ni1": "nī",
    "ni2": "ní",
    "ni3": "nǐ",
    "ni4": "nì",
    "nie1": "niē",
    "nie2": "nié",
    "nie3": "niě",
    "nie4": "niè",
    "niao1": "niāo",
    "niao2": "niáo",
    "niao3": "niǎo",
    "niao4": "niào",
    "niu1": "niū",
    "niu2": "niú",
    "niu3": "niǔ",
    "niu4": "niù",
    "nian1": "niān",
    "nian2": "nián",
    "nian3": "niǎn",
    "nian4": "niàn",
    "niang1": "niāng",
    "niang2": "niáng",
    "niang3": "niǎng",
    "niang4": "niàng",
    "nin1": "nīn",
    "nin2": "nín",
    "nin3": "nǐn",
    "nin4": "nìn",
    "ning1": "nīng",
    "ning2": "níng",
    "ning3": "nǐng",
    "ning4": "nìng",
    "le1": "lē",
    "le2": "lé",
    "le3": "lě",
    "le4": "lè",
    "la1": "lā",
    "la2": "lá",
    "la3": "lǎ",
    "la4": "là",
    "lai1": "lāi",
    "lai2": "lái",
    "lai3": "lǎi",
    "lai4": "lài",
    "lei1": "lēi",
    "lei2": "léi",
    "lei3": "lěi",
    "lei4": "lèi",
    "lao1": "lāo",
    "lao2": "láo",
    "lao3": "lǎo",
    "lao4": "lào",
    "lou1": "lōu",
    "lou2": "lóu",
    "lou3": "lǒu",
    "lou4": "lòu",
    "lan1": "lān",
    "lan2": "lán",
    "lan3": "lǎn",
    "lan4": "làn",
    "lang1": "lāng",
    "lang2": "láng",
    "lang3": "lǎng",
    "lang4": "làng",
    "leng1": "lēng",
    "leng2": "léng",
    "leng3": "lěng",
    "leng4": "lèng",
    "long1": "lōng",
    "long2": "lóng",
    "long3": "lǒng",
    "long4": "lòng",
    "lu1": "lū",
    "lu2": "lú",
    "lu3": "lǔ",
    "lu4": "lù",
    "luo1": "luō",
    "luo2": "luó",
    "luo3": "luǒ",
    "luo4": "luò",
    "luan1": "luān",
    "luan2": "luán",
    "luan3": "luǎn",
    "luan4": "luàn",
    "lun1": "lūn",
    "lun2": "lún",
    "lun3": "lǔn",
    "lun4": "lùn",
    "li1": "lī",
    "li2": "lí",
    "li3": "lǐ",
    "li4": "lì",
    "lia1": "liā",
    "lia2": "liá",
    "lia3": "liǎ",
    "lia4": "lià",
    "lie1": "liē",
    "lie2": "lié",
    "lie3": "liě",
    "lie4": "liè",
    "liao1": "liāo",
    "liao2": "liáo",
    "liao3": "liǎo",
    "liao4": "liào",
    "liu1": "liū",
    "liu2": "liú",
    "liu3": "liǔ",
    "liu4": "liù",
    "lian1": "liān",
    "lian2": "lián",
    "lian3": "liǎn",
    "lian4": "liàn",
    "liang1": "liāng",
    "liang2": "liáng",
    "liang3": "liǎng",
    "liang4": "liàng",
    "lin1": "līn",
    "lin2": "lín",
    "lin3": "lǐn",
    "lin4": "lìn",
    "ling1": "līng",
    "ling2": "líng",
    "ling3": "lǐng",
    "ling4": "lìng",
    "ge1": "gē",
    "ge2": "gé",
    "ge3": "gě",
    "ge4": "gè",
    "ga1": "gā",
    "ga2": "gá",
    "ga3": "gǎ",
    "ga4": "gà",
    "gai1": "gāi",
    "gai2": "gái",
    "gai3": "gǎi",
    "gai4": "gài",
    "gei1": "gēi",
    "gei2": "géi",
    "gei3": "gěi",
    "gei4": "gèi",
    "gao1": "gāo",
    "gao2": "gáo",
    "gao3": "gǎo",
    "gao4": "gào",
    "gou1": "gōu",
    "gou2": "góu",
    "gou3": "gǒu",
    "gou4": "gòu",
    "gan1": "gān",
    "gan2": "gán",
    "gan3": "gǎn",
    "gan4": "gàn",
    "gen1": "gēn",
    "gen2": "gén",
    "gen3": "gěn",
    "gen4": "gèn",
    "gang1": "gāng",
    "gang2": "gáng",
    "gang3": "gǎng",
    "gang4": "gàng",
    "geng1": "gēng",
    "geng2": "géng",
    "geng3": "gěng",
    "geng4": "gèng",
    "gong1": "gōng",
    "gong2": "góng",
    "gong3": "gǒng",
    "gong4": "gòng",
    "gu1": "gū",
    "gu2": "gú",
    "gu3": "gǔ",
    "gu4": "gù",
    "gua1": "guā",
    "gua2": "guá",
    "gua3": "guǎ",
    "gua4": "guà",
    "guo1": "guō",
    "guo2": "guó",
    "guo3": "guǒ",
    "guo4": "guò",
    "guai1": "guāi",
    "guai2": "guái",
    "guai3": "guǎi",
    "guai4": "guài",
    "gui1": "guī",
    "gui2": "guí",
    "gui3": "guǐ",
    "gui4": "guì",
    "guan1": "guān",
    "guan2": "guán",
    "guan3": "guǎn",
    "guan4": "guàn",
    "guang1": "guāng",
    "guang2": "guáng",
    "guang3": "guǎng",
    "guang4": "guàng",
    "gun1": "gūn",
    "gun2": "gún",
    "gun3": "gǔn",
    "gun4": "gùn",
    "ke1": "kē",
    "ke2": "ké",
    "ke3": "kě",
    "ke4": "kè",
    "ka1": "kā",
    "ka2": "ká",
    "ka3": "kǎ",
    "ka4": "kà",
    "kai1": "kāi",
    "kai2": "kái",
    "kai3": "kǎi",
    "kai4": "kài",
    "kei1": "kēi",
    "kei2": "kéi",
    "kei3": "kěi",
    "kei4": "kèi",
    "kao1": "kāo",
    "kao2": "káo",
    "kao3": "kǎo",
    "kao4": "kào",
    "kou1": "kōu",
    "kou2": "kóu",
    "kou3": "kǒu",
    "kou4": "kòu",
    "kan1": "kān",
    "kan2": "kán",
    "kan3": "kǎn",
    "kan4": "kàn",
    "ken1": "kēn",
    "ken2": "kén",
    "ken3": "kěn",
    "ken4": "kèn",
    "kang1": "kāng",
    "kang2": "káng",
    "kang3": "kǎng",
    "kang4": "kàng",
    "keng1": "kēng",
    "keng2": "kéng",
    "keng3": "kěng",
    "keng4": "kèng",
    "kong1": "kōng",
    "kong2": "kóng",
    "kong3": "kǒng",
    "kong4": "kòng",
    "ku1": "kū",
    "ku2": "kú",
    "ku3": "kǔ",
    "ku4": "kù",
    "kua1": "kuā",
    "kua2": "kuá",
    "kua3": "kuǎ",
    "kua4": "kuà",
    "kuo1": "kuō",
    "kuo2": "kuó",
    "kuo3": "kuǒ",
    "kuo4": "kuò",
    "kuai1": "kuāi",
    "kuai2": "kuái",
    "kuai3": "kuǎi",
    "kuai4": "kuài",
    "kui1": "kuī",
    "kui2": "kuí",
    "kui3": "kuǐ",
    "kui4": "kuì",
    "kuan1": "kuān",
    "kuan2": "kuán",
    "kuan3": "kuǎn",
    "kuan4": "kuàn",
    "kuang1": "kuāng",
    "kuang2": "kuáng",
    "kuang3": "kuǎng",
    "kuang4": "kuàng",
    "kun1": "kūn",
    "kun2": "kún",
    "kun3": "kǔn",
    "kun4": "kùn",
    "he1": "hē",
    "he2": "hé",
    "he3": "hě",
    "he4": "hè",
    "ha1": "hā",
    "ha2": "há",
    "ha3": "hǎ",
    "ha4": "hà",
    "hai1": "hāi",
    "hai2": "hái",
    "hai3": "hǎi",
    "hai4": "hài",
    "hei1": "hēi",
    "hei2": "héi",
    "hei3": "hěi",
    "hei4": "hèi",
    "hao1": "hāo",
    "hao2": "háo",
    "hao3": "hǎo",
    "hao4": "hào",
    "hou1": "hōu",
    "hou2": "hóu",
    "hou3": "hǒu",
    "hou4": "hòu",
    "han1": "hān",
    "han2": "hán",
    "han3": "hǎn",
    "han4": "hàn",
    "hen1": "hēn",
    "hen2": "hén",
    "hen3": "hěn",
    "hen4": "hèn",
    "hang1": "hāng",
    "hang2": "háng",
    "hang3": "hǎng",
    "hang4": "hàng",
    "heng1": "hēng",
    "heng2": "héng",
    "heng3": "hěng",
    "heng4": "hèng",
    "hong1": "hōng",
    "hong2": "hóng",
    "hong3": "hǒng",
    "hong4": "hòng",
    "hu1": "hū",
    "hu2": "hú",
    "hu3": "hǔ",
    "hu4": "hù",
    "hua1": "huā",
    "hua2": "huá",
    "hua3": "huǎ",
    "hua4": "huà",
    "huo1": "huō",
    "huo2": "huó",
    "huo3": "huǒ",
    "huo4": "huò",
    "huai1": "huāi",
    "huai2": "huái",
    "huai3": "huǎi",
    "huai4": "huài",
    "hui1": "huī",
    "hui2": "huí",
    "hui3": "huǐ",
    "hui4": "huì",
    "huan1": "huān",
    "huan2": "huán",
    "huan3": "huǎn",
    "huan4": "huàn",
    "huang1": "huāng",
    "huang2": "huáng",
    "huang3": "huǎng",
    "huang4": "huàng",
    "hun1": "hūn",
    "hun2": "hún",
    "hun3": "hǔn",
    "hun4": "hùn",
    "zi1": "zī",
    "zi2": "zí",
    "zi3": "zǐ",
    "zi4": "zì",
    "za1": "zā",
    "za2": "zá",
    "za3": "zǎ",
    "za4": "zà",
    "ze1": "zē",
    "ze2": "zé",
    "ze3": "zě",
    "ze4": "zè",
    "zai1": "zāi",
    "zai2": "zái",
    "zai3": "zǎi",
    "zai4": "zài",
    "zei1": "zēi",
    "zei2": "zéi",
    "zei3": "zěi",
    "zei4": "zèi",
    "zao1": "zāo",
    "zao2": "záo",
    "zao3": "zǎo",
    "zao4": "zào",
    "zou1": "zōu",
    "zou2": "zóu",
    "zou3": "zǒu",
    "zou4": "zòu",
    "zan1": "zān",
    "zan2": "zán",
    "zan3": "zǎn",
    "zan4": "zàn",
    "zen1": "zēn",
    "zen2": "zén",
    "zen3": "zěn",
    "zen4": "zèn",
    "zang1": "zāng",
    "zang2": "záng",
    "zang3": "zǎng",
    "zang4": "zàng",
    "zeng1": "zēng",
    "zeng2": "zéng",
    "zeng3": "zěng",
    "zeng4": "zèng",
    "zong1": "zōng",
    "zong2": "zóng",
    "zong3": "zǒng",
    "zong4": "zòng",
    "zu1": "zū",
    "zu2": "zú",
    "zu3": "zǔ",
    "zu4": "zù",
    "zuo1": "zuō",
    "zuo2": "zuó",
    "zuo3": "zuǒ",
    "zuo4": "zuò",
    "zui1": "zuī",
    "zui2": "zuí",
    "zui3": "zuǐ",
    "zui4": "zuì",
    "zuan1": "zuān",
    "zuan2": "zuán",
    "zuan3": "zuǎn",
    "zuan4": "zuàn",
    "zun1": "zūn",
    "zun2": "zún",
    "zun3": "zǔn",
    "zun4": "zùn",
    "ci1": "cī",
    "ci2": "cí",
    "ci3": "cǐ",
    "ci4": "cì",
    "ca1": "cā",
    "ca2": "cá",
    "ca3": "cǎ",
    "ca4": "cà",
    "ce1": "cē",
    "ce2": "cé",
    "ce3": "cě",
    "ce4": "cè",
    "cai1": "cāi",
    "cai2": "cái",
    "cai3": "cǎi",
    "cai4": "cài",
    "cao1": "cāo",
    "cao2": "cáo",
    "cao3": "cǎo",
    "cao4": "cào",
    "cou1": "cōu",
    "cou2": "cóu",
    "cou3": "cǒu",
    "cou4": "còu",
    "can1": "cān",
    "can2": "cán",
    "can3": "cǎn",
    "can4": "càn",
    "cen1": "cēn",
    "cen2": "cén",
    "cen3": "cěn",
    "cen4": "cèn",
    "cang1": "cāng",
    "cang2": "cáng",
    "cang3": "cǎng",
    "cang4": "càng",
    "ceng1": "cēng",
    "ceng2": "céng",
    "ceng3": "cěng",
    "ceng4": "cèng",
    "cong1": "cōng",
    "cong2": "cóng",
    "cong3": "cǒng",
    "cong4": "còng",
    "cu1": "cū",
    "cu2": "cú",
    "cu3": "cǔ",
    "cu4": "cù",
    "cuo1": "cuō",
    "cuo2": "cuó",
    "cuo3": "cuǒ",
    "cuo4": "cuò",
    "cui1": "cuī",
    "cui2": "cuí",
    "cui3": "cuǐ",
    "cui4": "cuì",
    "cuan1": "cuān",
    "cuan2": "cuán",
    "cuan3": "cuǎn",
    "cuan4": "cuàn",
    "cun1": "cūn",
    "cun2": "cún",
    "cun3": "cǔn",
    "cun4": "cùn",
    "cin1": "cīn",
    "cin2": "cín",
    "cin3": "cǐn",
    "cin4": "cìn",
    "si1": "sī",
    "si2": "sí",
    "si3": "sǐ",
    "si4": "sì",
    "sa1": "sā",
    "sa2": "sá",
    "sa3": "sǎ",
    "sa4": "sà",
    "se1": "sē",
    "se2": "sé",
    "se3": "sě",
    "se4": "sè",
    "sai1": "sāi",
    "sai2": "sái",
    "sai3": "sǎi",
    "sai4": "sài",
    "sao1": "sāo",
    "sao2": "sáo",
    "sao3": "sǎo",
    "sao4": "sào",
    "sou1": "sōu",
    "sou2": "sóu",
    "sou3": "sǒu",
    "sou4": "sòu",
    "san1": "sān",
    "san2": "sán",
    "san3": "sǎn",
    "san4": "sàn",
    "sen1": "sēn",
    "sen2": "sén",
    "sen3": "sěn",
    "sen4": "sèn",
    "sang1": "sāng",
    "sang2": "sáng",
    "sang3": "sǎng",
    "sang4": "sàng",
    "seng1": "sēng",
    "seng2": "séng",
    "seng3": "sěng",
    "seng4": "sèng",
    "song1": "sōng",
    "song2": "sóng",
    "song3": "sǒng",
    "song4": "sòng",
    "su1": "sū",
    "su2": "sú",
    "su3": "sǔ",
    "su4": "sù",
    "suo1": "suō",
    "suo2": "suó",
    "suo3": "suǒ",
    "suo4": "suò",
    "sui1": "suī",
    "sui2": "suí",
    "sui3": "suǐ",
    "sui4": "suì",
    "suan1": "suān",
    "suan2": "suán",
    "suan3": "suǎn",
    "suan4": "suàn",
    "sun1": "sūn",
    "sun2": "sún",
    "sun3": "sǔn",
    "sun4": "sùn",
    "zhi1": "zhī",
    "zhi2": "zhí",
    "zhi3": "zhǐ",
    "zhi4": "zhì",
    "zha1": "zhā",
    "zha2": "zhá",
    "zha3": "zhǎ",
    "zha4": "zhà",
    "zhe1": "zhē",
    "zhe2": "zhé",
    "zhe3": "zhě",
    "zhe4": "zhè",
    "zhai1": "zhāi",
    "zhai2": "zhái",
    "zhai3": "zhǎi",
    "zhai4": "zhài",
    "zhei1": "zhēi",
    "zhei2": "zhéi",
    "zhei3": "zhěi",
    "zhei4": "zhèi",
    "zhao1": "zhāo",
    "zhao2": "zháo",
    "zhao3": "zhǎo",
    "zhao4": "zhào",
    "zhou1": "zhōu",
    "zhou2": "zhóu",
    "zhou3": "zhǒu",
    "zhou4": "zhòu",
    "zhan1": "zhān",
    "zhan2": "zhán",
    "zhan3": "zhǎn",
    "zhan4": "zhàn",
    "zhen1": "zhēn",
    "zhen2": "zhén",
    "zhen3": "zhěn",
    "zhen4": "zhèn",
    "zhang1": "zhāng",
    "zhang2": "zháng",
    "zhang3": "zhǎng",
    "zhang4": "zhàng",
    "zheng1": "zhēng",
    "zheng2": "zhéng",
    "zheng3": "zhěng",
    "zheng4": "zhèng",
    "zhong1": "zhōng",
    "zhong2": "zhóng",
    "zhong3": "zhǒng",
    "zhong4": "zhòng",
    "zhu1": "zhū",
    "zhu2": "zhú",
    "zhu3": "zhǔ",
    "zhu4": "zhù",
    "zhua1": "zhuā",
    "zhua2": "zhuá",
    "zhua3": "zhuǎ",
    "zhua4": "zhuà",
    "zhuo1": "zhuō",
    "zhuo2": "zhuó",
    "zhuo3": "zhuǒ",
    "zhuo4": "zhuò",
    "zhuai1": "zhuāi",
    "zhuai2": "zhuái",
    "zhuai3": "zhuǎi",
    "zhuai4": "zhuài",
    "zhui1": "zhuī",
    "zhui2": "zhuí",
    "zhui3": "zhuǐ",
    "zhui4": "zhuì",
    "zhuan1": "zhuān",
    "zhuan2": "zhuán",
    "zhuan3": "zhuǎn",
    "zhuan4": "zhuàn",
    "zhuang1": "zhuāng",
    "zhuang2": "zhuáng",
    "zhuang3": "zhuǎng",
    "zhuang4": "zhuàng",
    "zhun1": "zhūn",
    "zhun2": "zhún",
    "zhun3": "zhǔn",
    "zhun4": "zhùn",
    "chi1": "chī",
    "chi2": "chí",
    "chi3": "chǐ",
    "chi4": "chì",
    "cha1": "chā",
    "cha2": "chá",
    "cha3": "chǎ",
    "cha4": "chà",
    "che1": "chē",
    "che2": "ché",
    "che3": "chě",
    "che4": "chè",
    "chai1": "chāi",
    "chai2": "chái",
    "chai3": "chǎi",
    "chai4": "chài",
    "chao1": "chāo",
    "chao2": "cháo",
    "chao3": "chǎo",
    "chao4": "chào",
    "chou1": "chōu",
    "chou2": "chóu",
    "chou3": "chǒu",
    "chou4": "chòu",
    "chan1": "chān",
    "chan2": "chán",
    "chan3": "chǎn",
    "chan4": "chàn",
    "chen1": "chēn",
    "chen2": "chén",
    "chen3": "chěn",
    "chen4": "chèn",
    "chang1": "chāng",
    "chang2": "cháng",
    "chang3": "chǎng",
    "chang4": "chàng",
    "cheng1": "chēng",
    "cheng2": "chéng",
    "cheng3": "chěng",
    "cheng4": "chèng",
    "chong1": "chōng",
    "chong2": "chóng",
    "chong3": "chǒng",
    "chong4": "chòng",
    "chu1": "chū",
    "chu2": "chú",
    "chu3": "chǔ",
    "chu4": "chù",
    "chua1": "chuā",
    "chua2": "chuá",
    "chua3": "chuǎ",
    "chua4": "chuà",
    "chuo1": "chuō",
    "chuo2": "chuó",
    "chuo3": "chuǒ",
    "chuo4": "chuò",
    "chuai1": "chuāi",
    "chuai2": "chuái",
    "chuai3": "chuǎi",
    "chuai4": "chuài",
    "chui1": "chuī",
    "chui2": "chuí",
    "chui3": "chuǐ",
    "chui4": "chuì",
    "chuan1": "chuān",
    "chuan2": "chuán",
    "chuan3": "chuǎn",
    "chuan4": "chuàn",
    "chuang1": "chuāng",
    "chuang2": "chuáng",
    "chuang3": "chuǎng",
    "chuang4": "chuàng",
    "chun1": "chūn",
    "chun2": "chún",
    "chun3": "chǔn",
    "chun4": "chùn",
    "shi1": "shī",
    "shi2": "shí",
    "shi3": "shǐ",
    "shi4": "shì",
    "sha1": "shā",
    "sha2": "shá",
    "sha3": "shǎ",
    "sha4": "shà",
    "she1": "shē",
    "she2": "shé",
    "she3": "shě",
    "she4": "shè",
    "shai1": "shāi",
    "shai2": "shái",
    "shai3": "shǎi",
    "shai4": "shài",
    "shei1": "shēi",
    "shei2": "shéi",
    "shei3": "shěi",
    "shei4": "shèi",
    "shao1": "shāo",
    "shao2": "sháo",
    "shao3": "shǎo",
    "shao4": "shào",
    "shou1": "shōu",
    "shou2": "shóu",
    "shou3": "shǒu",
    "shou4": "shòu",
    "shan1": "shān",
    "shan2": "shán",
    "shan3": "shǎn",
    "shan4": "shàn",
    "shen1": "shēn",
    "shen2": "shén",
    "shen3": "shěn",
    "shen4": "shèn",
    "shang1": "shāng",
    "shang2": "sháng",
    "shang3": "shǎng",
    "shang4": "shàng",
    "sheng1": "shēng",
    "sheng2": "shéng",
    "sheng3": "shěng",
    "sheng4": "shèng",
    "shu1": "shū",
    "shu2": "shú",
    "shu3": "shǔ",
    "shu4": "shù",
    "shua1": "shuā",
    "shua2": "shuá",
    "shua3": "shuǎ",
    "shua4": "shuà",
    "shuo1": "shuō",
    "shuo2": "shuó",
    "shuo3": "shuǒ",
    "shuo4": "shuò",
    "shuai1": "shuāi",
    "shuai2": "shuái",
    "shuai3": "shuǎi",
    "shuai4": "shuài",
    "shui1": "shuī",
    "shui2": "shuí",
    "shui3": "shuǐ",
    "shui4": "shuì",
    "shuan1": "shuān",
    "shuan2": "shuán",
    "shuan3": "shuǎn",
    "shuan4": "shuàn",
    "shuang1": "shuāng",
    "shuang2": "shuáng",
    "shuang3": "shuǎng",
    "shuang4": "shuàng",
    "shun1": "shūn",
    "shun2": "shún",
    "shun3": "shǔn",
    "shun4": "shùn",
    "ri1": "rī",
    "ri2": "rí",
    "ri3": "rǐ",
    "ri4": "rì",
    "re1": "rē",
    "re2": "ré",
    "re3": "rě",
    "re4": "rè",
    "rao1": "rāo",
    "rao2": "ráo",
    "rao3": "rǎo",
    "rao4": "rào",
    "rou1": "rōu",
    "rou2": "róu",
    "rou3": "rǒu",
    "rou4": "ròu",
    "ran1": "rān",
    "ran2": "rán",
    "ran3": "rǎn",
    "ran4": "ràn",
    "ren1": "rēn",
    "ren2": "rén",
    "ren3": "rěn",
    "ren4": "rèn",
    "rang1": "rāng",
    "rang2": "ráng",
    "rang3": "rǎng",
    "rang4": "ràng",
    "reng1": "rēng",
    "reng2": "réng",
    "reng3": "rěng",
    "reng4": "rèng",
    "rong1": "rōng",
    "rong2": "róng",
    "rong3": "rǒng",
    "rong4": "ròng",
    "ru1": "rū",
    "ru2": "rú",
    "ru3": "rǔ",
    "ru4": "rù",
    "rua1": "ruā",
    "rua2": "ruá",
    "rua3": "ruǎ",
    "rua4": "ruà",
    "ruo1": "ruō",
    "ruo2": "ruó",
    "ruo3": "ruǒ",
    "ruo4": "ruò",
    "rui1": "ruī",
    "rui2": "ruí",
    "rui3": "ruǐ",
    "rui4": "ruì",
    "ruan1": "ruān",
    "ruan2": "ruán",
    "ruan3": "ruǎn",
    "ruan4": "ruàn",
    "run1": "rūn",
    "run2": "rún",
    "run3": "rǔn",
    "run4": "rùn",
    "ji1": "jī",
    "ji2": "jí",
    "ji3": "jǐ",
    "ji4": "jì",
    "jia1": "jiā",
    "jia2": "jiá",
    "jia3": "jiǎ",
    "jia4": "jià",
    "jie1": "jiē",
    "jie2": "jié",
    "jie3": "jiě",
    "jie4": "jiè",
    "jiao1": "jiāo",
    "jiao2": "jiáo",
    "jiao3": "jiǎo",
    "jiao4": "jiào",
    "jiu1": "jiū",
    "jiu2": "jiú",
    "jiu3": "jiǔ",
    "jiu4": "jiù",
    "jian1": "jiān",
    "jian2": "jián",
    "jian3": "jiǎn",
    "jian4": "jiàn",
    "jiang1": "jiāng",
    "jiang2": "jiáng",
    "jiang3": "jiǎng",
    "jiang4": "jiàng",
    "jin1": "jīn",
    "jin2": "jín",
    "jin3": "jǐn",
    "jin4": "jìn",
    "jing1": "jīng",
    "jing2": "jíng",
    "jing3": "jǐng",
    "jing4": "jìng",
    "jiong1": "jiōng",
    "jiong2": "jióng",
    "jiong3": "jiǒng",
    "jiong4": "jiòng",
    "ju1": "jū",
    "ju2": "jú",
    "ju3": "jǔ",
    "ju4": "jù",
    "jue1": "juē",
    "jue2": "jué",
    "jue3": "juě",
    "jue4": "juè",
    "juan1": "juān",
    "juan2": "juán",
    "juan3": "juǎn",
    "juan4": "juàn",
    "jun1": "jūn",
    "jun2": "jún",
    "jun3": "jǔn",
    "jun4": "jùn",
    "qi1": "qī",
    "qi2": "qí",
    "qi3": "qǐ",
    "qi4": "qì",
    "qia1": "qiā",
    "qia2": "qiá",
    "qia3": "qiǎ",
    "qia4": "qià",
    "qie1": "qiē",
    "qie2": "qié",
    "qie3": "qiě",
    "qie4": "qiè",
    "qiao1": "qiāo",
    "qiao2": "qiáo",
    "qiao3": "qiǎo",
    "qiao4": "qiào",
    "qiu1": "qiū",
    "qiu2": "qiú",
    "qiu3": "qiǔ",
    "qiu4": "qiù",
    "qian1": "qiān",
    "qian2": "qián",
    "qian3": "qiǎn",
    "qian4": "qiàn",
    "qiang1": "qiāng",
    "qiang2": "qiáng",
    "qiang3": "qiǎng",
    "qiang4": "qiàng",
    "qin1": "qīn",
    "qin2": "qín",
    "qin3": "qǐn",
    "qin4": "qìn",
    "qing1": "qīng",
    "qing2": "qíng",
    "qing3": "qǐng",
    "qing4": "qìng",
    "qiong1": "qiōng",
    "qiong2": "qióng",
    "qiong3": "qiǒng",
    "qiong4": "qiòng",
    "qu1": "qū",
    "qu2": "qú",
    "qu3": "qǔ",
    "qu4": "qù",
    "que1": "quē",
    "que2": "qué",
    "que3": "quě",
    "que4": "què",
    "quan1": "quān",
    "quan2": "quán",
    "quan3": "quǎn",
    "quan4": "quàn",
    "qun1": "qūn",
    "qun2": "qún",
    "qun3": "qǔn",
    "qun4": "qùn",
    "xi1": "xī",
    "xi2": "xí",
    "xi3": "xǐ",
    "xi4": "xì",
    "xia1": "xiā",
    "xia2": "xiá",
    "xia3": "xiǎ",
    "xia4": "xià",
    "xie1": "xiē",
    "xie2": "xié",
    "xie3": "xiě",
    "xie4": "xiè",
    "xiao1": "xiāo",
    "xiao2": "xiáo",
    "xiao3": "xiǎo",
    "xiao4": "xiào",
    "xiu1": "xiū",
    "xiu2": "xiú",
    "xiu3": "xiǔ",
    "xiu4": "xiù",
    "xian1": "xiān",
    "xian2": "xián",
    "xian3": "xiǎn",
    "xian4": "xiàn",
    "xiang1": "xiāng",
    "xiang2": "xiáng",
    "xiang3": "xiǎng",
    "xiang4": "xiàng",
    "xin1": "xīn",
    "xin2": "xín",
    "xin3": "xǐn",
    "xin4": "xìn",
    "xing1": "xīng",
    "xing2": "xíng",
    "xing3": "xǐng",
    "xing4": "xìng",
    "xiong1": "xiōng",
    "xiong2": "xióng",
    "xiong3": "xiǒng",
    "xiong4": "xiòng",
    "xu1": "xū",
    "xu2": "xú",
    "xu3": "xǔ",
    "xu4": "xù",
    "xue1": "xuē",
    "xue2": "xué",
    "xue3": "xuě",
    "xue4": "xuè",
    "xuan1": "xuān",
    "xuan2": "xuán",
    "xuan3": "xuǎn",
    "xuan4": "xuàn",
    "xun1": "xūn",
    "xun2": "xún",
    "xun3": "xǔn",
    "xun4": "xùn",
    "a1": "ā",
    "a2": "á",
    "a3": "ǎ",
    "a4": "à",
    "o1": "ō",
    "o2": "ó",
    "o3": "ǒ",
    "o4": "ò",
    "e1": "ē",
    "e2": "é",
    "e3": "ě",
    "e4": "è",
    "ai1": "āi",
    "ai2": "ái",
    "ai3": "ǎi",
    "ai4": "ài",
    "ei1": "ēi",
    "ei2": "éi",
    "ei3": "ěi",
    "ei4": "èi",
    "ao1": "āo",
    "ao2": "áo",
    "ao3": "ǎo",
    "ao4": "ào",
    "ou1": "ōu",
    "ou2": "óu",
    "ou3": "ǒu",
    "ou4": "òu",
    "an1": "ān",
    "an2": "án",
    "an3": "ǎn",
    "an4": "àn",
    "en1": "ēn",
    "en2": "én",
    "en3": "ěn",
    "en4": "èn",
    "ang1": "āng",
    "ang2": "áng",
    "ang3": "ǎng",
    "ang4": "àng",
    "ong1": "ōng",
    "ong2": "óng",
    "ong3": "ǒng",
    "ong4": "òng",
    "wu1": "wū",
    "wu2": "wú",
    "wu3": "wǔ",
    "wu4": "wù",
    "wa1": "wā",
    "wa2": "wá",
    "wa3": "wǎ",
    "wa4": "wà",
    "wo1": "wō",
    "wo2": "wó",
    "wo3": "wǒ",
    "wo4": "wò",
    "wai1": "wāi",
    "wai2": "wái",
    "wai3": "wǎi",
    "wai4": "wài",
    "wei1": "wēi",
    "wei2": "wéi",
    "wei3": "wěi",
    "wei4": "wèi",
    "wan1": "wān",
    "wan2": "wán",
    "wan3": "wǎn",
    "wan4": "wàn",
    "wang1": "wāng",
    "wang2": "wáng",
    "wang3": "wǎng",
    "wang4": "wàng",
    "wen1": "wēn",
    "wen2": "wén",
    "wen3": "wěn",
    "wen4": "wèn",
    "weng1": "wēng",
    "weng2": "wéng",
    "weng3": "wěng",
    "weng4": "wèng",
    "yi1": "yī",
    "yi2": "yí",
    "yi3": "yǐ",
    "yi4": "yì",
    "ya1": "yā",
    "ya2": "yá",
    "ya3": "yǎ",
    "ya4": "yà",
    "ye1": "yē",
    "ye2": "yé",
    "ye3": "yě",
    "ye4": "yè",
    "yao1": "yāo",
    "yao2": "yáo",
    "yao3": "yǎo",
    "yao4": "yào",
    "you1": "yōu",
    "you2": "yóu",
    "you3": "yǒu",
    "you4": "yòu",
    "yan1": "yān",
    "yan2": "yán",
    "yan3": "yǎn",
    "yan4": "yàn",
    "yang1": "yāng",
    "yang2": "yáng",
    "yang3": "yǎng",
    "yang4": "yàng",
    "yin1": "yīn",
    "yin2": "yín",
    "yin3": "yǐn",
    "yin4": "yìn",
    "ying1": "yīng",
    "ying2": "yíng",
    "ying3": "yǐng",
    "ying4": "yìng",
    "yong1": "yōng",
    "yong2": "yóng",
    "yong3": "yǒng",
    "yong4": "yòng",
    "yu1": "yū",
    "yu2": "yú",
    "yu3": "yǔ",
    "yu4": "yù",
    "yue1": "yuē",
    "yue2": "yué",
    "yue3": "yuě",
    "yue4": "yuè",
    "yuan1": "yuān",
    "yuan2": "yuán",
    "yuan3": "yuǎn",
    "yuan4": "yuàn",
    "yun1": "yūn",
    "yun2": "yún",
    "yun3": "yǔn",
    "yun4": "yùn",
    "nv1": "nǖ",
    "nv2": "nǘ",
    "nv3": "nǚ",
    "nv4": "nǜ",
    "nve1": "nüē",
    "nve2": "nüé",
    "nve3": "nüě",
    "nve4": "nüè",
    "lv1": "lǖ",
    "lv2": "lǘ",
    "lv3": "lǚ",
    "lv4": "lǜ",
    "lve1": "lüē",
    "lve2": "lüé",
    "lve3": "lüě",
    "lve4": "lüè",
}


class TestPinyinToneConverter:
    def test_get_accent_map(self):
        accent_map = PinyinToneConverter().get_accent_map()
        assert accent_map == {
            "A": "A*",
            "AI": "A*I",
            "AO": "A*O",
            "E": "E*",
            "EI": "E*I",
            "I": "I*",
            "IA": "IA*",
            "IAO": "IA*O",
            "IE": "IE*",
            "IO": "IO*",
            "IU": "IU*",
            "O": "O*",
            "OU": "O*U",
            "U": "U*",
            "UA": "UA*",
            "UAI": "UA*I",
            "UE": "UE*",
            "UI": "UI*",
            "UO": "UO*",
            "a": "a*",
            "ai": "a*i",
            "ao": "a*o",
            "e": "e*",
            "ei": "e*i",
            "i": "i*",
            "ia": "ia*",
            "iao": "ia*o",
            "ie": "ie*",
            "io": "io*",
            "iu": "iu*",
            "o": "o*",
            "ou": "o*u",
            "u": "u*",
            "ua": "ua*",
            "uai": "ua*i",
            "ue": "ue*",
            "ui": "ui*",
            "uo": "uo*",
            "Ü": "Ü*",
            "ÜE": "ÜE*",
            "ü": "ü*",
            "üe": "üe*",
        }

    def test_pinyin_tone_converter_convert_word(self):
        converted_pinyin = PinyinToneConverter().convert_text("lu4")
        assert converted_pinyin == "lù"

    def test_pinyin_tone_converter_convert_text(self):
        converted_pinyin = PinyinToneConverter().convert_text("wo3 fei1chang2 xi3huan1 lv4 cha2")
        assert converted_pinyin == "wǒ fēicháng xǐhuān lǜ chá"

    def test_all_input_output(self):
        for input, output in correct_input_and_output.items():
            converted_pinyin = PinyinToneConverter().convert_text(input)
            assert converted_pinyin == output
