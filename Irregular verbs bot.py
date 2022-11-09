import telebot
from random import choice
bot = telebot.TeleBot('TOKEN')

v1 = ['abide', 'abode/abided', 'abode/abided', 'пребывать, держаться']
v2 = ['arise', 'arose', 'arisen', 'подняться, возникнуть']
v3 = ['awake', 'awoke', 'awaked/awoke', 'будить, проснуться']
v4 = ['backbite', 'backbitten', 'backbitten', 'клеветать']
v5 = ['backslide', 'backslid', 'backslid', 'отпадать']
v6 = ['be', 'was/were', 'been', 'быть, нести, родить']
v7 = ['bear', 'bore', 'born/borne', 'родить']
v8 = ['beat', 'beat', 'beaten', 'бить']
v9 = ['become', 'became', 'become', 'стать, сделаться']
v10 = ['befall', 'befell', 'befallen', 'случиться']
v11 = ['beget', 'begot/begat', 'begotten', 'порождать']
v12 = ['begin', 'began', 'begun', 'начать']
v13 = ['begird', 'begirt', 'begirt', 'опоясывать']
v14 = ['behold', 'beheld', 'beheld', 'зреть']
v15 = ['bend', 'bent', 'bent/bended', 'согнуть(ся)']
v16 = ['bereave', 'bereft/bereaved', 'bereft/bereaved', 'лишать']
v17 = ['beseech', 'besought/beseeched',
       'besought/beseeched', 'умолять, упрашивать']
v18 = ['beset', 'beset', 'beset', 'осаждать']
v19 = ['bespeak', 'bespoke', 'bespoke/bespoken', 'заказывать']
v20 = ['bespit', 'bespat', 'bespat', 'заплевывать']
v21 = ['bestride', 'bestrode', 'bestridden', 'садиться, сидеть верхом']
v22 = ['bet', 'bet/betted', 'bet/betted', 'держать пари']
v23 = ['betake', 'betook', 'betaken', 'приниматься, отправляться']
v24 = ['bid', 'bad/bade/bid', 'bid/bidden', 'велеть, просить']
v25 = ['bind', 'bound', 'bound', 'связать']
v26 = ['bite', 'bit', 'bit/bitten', 'кусать']
v27 = ['bleed', 'bled', 'bled', 'кровоточить']
v28 = ['bless', 'blessed', 'blessed/blest', 'благословлять']
v29 = ['blow', 'blew', 'blown/blowed', 'дуть']
v30 = ['break', 'broke', 'broken', '(с)ломать']
v31 = ['breed', 'bred', 'bred', 'выращивать']
v32 = ['bring', 'brought', 'brought', 'принести']
v33 = ['broadcast', 'broadcast', 'broadcast', 'распространять, разбрасывать']
v34 = ['browbeat', 'browbeat', 'browbeaten', 'запугивать']
v35 = ['build', 'built', 'built', 'строить']
v36 = ['burn', 'burnt/burned', 'burnt/burned', 'жечь, гореть']
v37 = ['burst', 'burst', 'burst', 'разразиться, взорваться']
v38 = ['bust', 'bust/busted', 'bust/busted', 'разжаловать']
v39 = ['buy', 'bought', 'bought', 'купить']
v40 = ['can', 'could', '-///been/able', 'мочь, уметь']
v41 = ['cast', 'cast', 'cast', 'кинуть, лить металл']
v42 = ['catch', 'caught', 'caught', 'ловить, поймать']
v43 = ['chide', 'chid/chided', 'chid/chided/chidden', 'бранить']
v44 = ['choose', 'chose', 'chosen', 'выбрать']
v45 = ['cleave', 'clove/cleft/cleaved', 'cloven/cleft/cleaved', 'рассечь']
v46 = ['cling', 'clung', 'clung', 'цепляться, льнуть']
v47 = ['come', 'came', 'come', 'прийти']
v48 = ['cost', 'cost', 'cost', 'стоить']
v49 = ['countersink', 'countersank', 'countersunk', 'зенковать']
v50 = ['creep', 'crept', 'crept', 'ползти']
v51 = ['crow', 'crowed/crew', 'crowed', 'петь (о петухе)']
v52 = ['cut', 'cut', 'cut', 'резать']
v53 = ['dare', 'durst/dared', 'dared', 'сметь']
v54 = ['deal', 'dealt', 'dealt', 'иметь дело']
v55 = ['dig', 'dug', 'dug', 'копать']
v56 = ['dive', 'dived/dove', 'dived', 'нырять, погружаться']
v57 = ['do', 'did', 'done', 'делать']
v58 = ['draw', 'drew', 'drawn', 'тащить, рисовать']
v59 = ['dream', 'dreamt/dreamed', 'dreamt/dreamed', 'грезить, мечтать']
v60 = ['drink', 'drank', 'drunk', 'пить, выпить']
v61 = ['drive', 'drove', 'driven', 'гнать, ехать']
v62 = ['dwell', 'dwelt', 'dwelt', 'обитать, задерживаться']
v63 = ['eat', 'ate', 'eaten', 'кушать, есть']
v64 = ['fall', 'fell', 'fallen', 'падать']
v65 = ['feed', 'fed', 'fed', 'кормить']
v66 = ['feel', 'felt', 'felt', 'чувствовать']
v67 = ['fight', 'fought', 'fought', 'сражаться']
v68 = ['find', 'found', 'found', 'находить']
v69 = ['flee', 'fled', 'fled', 'бежать, спасаться']
v70 = ['fling', 'flung', 'flung', 'бросить']
v71 = ['floodlight', 'floodlighted/floodlit',
       'floodlighted/floodlit', 'освещать прожектором']
v72 = ['fly', 'flew', 'flown', 'летать']
v73 = ['forbear', 'forbore', 'forborne', 'воздерживаться']
v74 = ['forbid', 'forbad/forbade', 'forbidden', 'запретить']
v75 = ['forecast', 'forecast/forecasted',
       'forecast/forecasted', 'предсказывать']
v76 = ['foresee', 'foresaw', 'foreseen', 'предвидеть']
v77 = ['foretell', 'foretold', 'foretold', 'предсказывать']
v78 = ['forget', 'forgot', 'forgotten', 'забыть']
v79 = ['forgive', 'forgave', 'forgiven', 'простить']
v80 = ['forsake', 'forsook', 'forsaken', 'покидать']
v81 = ['forswear', 'forswore', 'forsworn', 'отрекаться']
v82 = ['freeze', 'froze', 'frozen', 'замерзнуть, замораживать']
v83 = ['gainsay', 'gainsaid', 'gainsaid', 'отрицать, противоречить']
v84 = ['get', 'got', 'got', 'получить']
v85 = ['gild', 'gilt/gilded', 'gilt/gilded', 'позолотить']
v86 = ['gird', 'girded/girt', 'girded/girt', 'опоясывать']
v87 = ['give', 'gave', 'given', 'дать']
v88 = ['go', 'went', 'gone', 'идти, уходить']
v89 = ['grave', 'graved', 'graved/graven', 'гравировать']
v90 = ['grind', 'ground', 'ground', 'точить, молоть']
v91 = ['grow', 'grew', 'grown', 'расти']
v92 = ['hamstring', 'hamstringed/hamstrung',
       'hamstringed/hamstrung', 'подрезать поджилки']
v93 = ['hang', 'hung/hanged', 'hung/hanged', 'висеть, повесить']
v94 = ['have', 'had', 'had', 'иметь']
v95 = ['hear', 'heard', 'heard', 'слушать']
v96 = ['heave', 'heaved/hove', 'heaved/hove', 'подымать(ся)']
v97 = ['hew', 'hewed/td>', 'hewed/hewn', 'рубить, тесать']
v98 = ['hide', 'hid', 'hidden', 'прятать(ся)']
v99 = ['hit', 'hit', 'hit', 'ударить, попасть']
v100 = ['hold', 'held', 'held', 'держать']
v101 = ['hurt', 'hurt', 'hurt', 'причинить боль']
v102 = ['inlay', 'inlaid', 'inlaid', 'вкладывать, выстилать']
v103 = ['input', 'input/inputted', 'input/inputted', 'входить']
v104 = ['inset', 'inset', 'inset', 'вставлять, вкладывать']
v105 = ['interweave', 'interwove', 'interwoven', 'воткать']
v106 = ['keep', 'kept', 'kept', 'хранить']
v107 = ['ken', 'kenned/kent', 'kenned', 'знать, узнавать по виду']
v108 = ['kneel', 'knelt/kneeled', 'knelt/kneeled', 'становиться на колени']
v109 = ['knit', 'knit/knitted', 'knit/knitted', 'вязать']
v110 = ['know', 'knew', 'known', 'знать']
v111 = ['lade', 'laded', 'laded/laden', 'грузить']
v112 = ['lay', 'laid', 'laid', 'класть, положить']
v113 = ['lead', 'led', 'led', 'вести']
v114 = ['lean', 'leant/leaned', 'leant/leaned', 'опереться, прислониться']
v115 = ['leap', 'leapt/leaped', 'leapt/leaped', 'прыгать']
v116 = ['learn', 'learnt/learned', 'learnt/learned', 'учить']
v117 = ['leave', 'left', 'left', 'оставить']
v118 = ['lend', 'lent', 'lent', 'одолжить']
v119 = ['let', 'let', 'let', 'пустить, дать']
v120 = ['lie', 'lay', 'lain', 'лежать']
v121 = ['light', 'lit/lighted', 'lit/lighted', 'осветить']
v122 = ['lose', 'lost', 'lost', 'терять']
v123 = ['make', 'made', 'made', 'делать']
v124 = ['may', 'might', 'might', 'мочь, иметь возможность']
v125 = ['mean', 'meant', 'meant', 'подразумевать']
v126 = ['meet', 'met', 'met', 'встретить']
v127 = ['miscast', 'miscast', 'miscast', 'неправильно распределять роли']
v128 = ['misdeal', 'misdealt', 'misdealt', 'поступать неправильно']
v129 = ['misgive', 'misgave', 'misgiven', 'внушать опасения']
v130 = ['mishear', 'misheard', 'misheard', 'ослышаться']
v131 = ['mishit', 'mishit', 'mishit', 'промахнуться']
v132 = ['mislay', 'mislaid', 'mislaid', 'класть не на место']
v133 = ['mislead', 'misled', 'misled', 'ввести в заблуждение']
v134 = ['misread', 'misread', 'misread', 'неправильно истолковывать']
v135 = ['misspell', 'misspelt/misspeled',
        'misspelt/misspeled', 'писать с ошибками']
v136 = ['misspend', 'misspent', 'misspent', 'экономить']
v137 = ['mistake', 'mistook', 'mistaken', 'неправильно понимать']
v138 = ['misunderstand', 'misunderstood',
        'misunderstood', 'неправильно понимать']
v139 = ['mow', 'mowed', 'mown/mowed', 'косить']
v140 = ['outbid', 'outbid', 'outbid', 'перебивать цену']
v141 = ['outdo', 'outdid', 'outdone', 'превосходить']
v142 = ['outfight', 'outfought', 'outfought', 'побеждать (в бою)']
v143 = ['outgrow', 'outgrew', 'outgrown', 'вырастать из']
v144 = ['output', 'output/outputted', 'output/outputted', 'выходить']
v145 = ['outrun', 'outran', 'outrun', 'перегонять, опережать']
v146 = ['outsell', 'outsold', 'outsold', 'продавать лучше или дороже']
v147 = ['outshine', 'outshone', 'outshone', 'затмевать']
v148 = ['overbid', 'overbid', 'overbid', 'повелевать']
v149 = ['overcome', 'overcame', 'overcome', 'компенсировать']
v150 = ['overdo', 'overdid', 'overdone', 'пережари(ва)ть']
v151 = ['overdraw', 'overdrew', 'overdrawn', 'превышать']
v152 = ['overeat', 'overate', 'overeaten', 'объедаться']
v153 = ['overfly', 'overflew', 'overflown', 'перелетать']
v154 = ['overhang', 'overhung', 'overhung', 'нависать']
v155 = ['overhear', 'overheard', 'overheard', 'подслуш(ив)ать']
v156 = ['overlay', 'overlaid', 'overlaid', 'покры(ва)ть']
v157 = ['overpay', 'overpaid', 'overpaid', 'переплачивать']
v158 = ['override', 'overrode', 'overridden', 'отвергать, отклонять']
v159 = ['overrun', 'overran', 'overrun', 'переливаться через край']
v160 = ['oversee', 'oversaw', 'overseen', 'надзирать за']
v161 = ['overshoot', 'overshot', 'overshot', 'расстрелять']
v162 = ['oversleep', 'overslept', 'overslept', 'прос(ы)пать']
v163 = ['overtake', 'overtook', 'overtaken', 'догонять']
v164 = ['overthrow', 'overthrew', 'overthrown', 'свергать']
v165 = ['partake', 'partook', 'partaken', 'принимать участие']
v166 = ['pay', 'paid', 'paid', 'платить']
v167 = ['plead', 'pleaded/pled', 'pleaded/pled', 'обращаться к суду']
v168 = ['prepay', 'prepaid', 'prepaid', 'платить вперед']
v169 = ['prove', 'proved', 'proved/proven', 'доказывать, оказаться']
v170 = ['put', 'put', 'put', 'класть']
v171 = ['quit', 'quit/quitted', 'quit/quitted', 'покидать, оставлять']
v172 = ['read', 'read/red', 'read/red', 'читать']
v173 = ['rebind', 'rebound', 'rebound', 'перевязывать']
v174 = ['rebuild', 'rebuilt', 'rebuilt', 'перестроить']
v175 = ['recast', 'recast', 'recast', 'видоизменять, преобразовывать']
v176 = ['redo', 'redid', 'redone', 'повторять сделанное']
v177 = ['rehear', 'reheard', 'reheard', 'слушать вторично']
v178 = ['remake', 'remade', 'remade', 'переделывать']
v179 = ['rend', 'rent', 'rent', 'раздирать']
v180 = ['repay', 'repaid', 'repaid', 'отдавать долг']
v181 = ['rerun', 'reran', 'rerun', 'выполнять повторно']
v182 = ['resell', 'resold', 'resold', 'перепродавать']
v183 = ['reset', 'reset', 'reset', 'возвращать']
v184 = ['resit', 'resat', 'resat', 'пересиживать']
v185 = ['retake', 'retook', 'retaken', 'забирать']
v186 = ['retell', 'retold', 'retold', 'пересказывать']
v187 = ['rewrite', 'rewrote', 'rewritten', 'пере(за)писать']
v188 = ['rid', 'rid/ridded', 'rid/ridded', 'избавлять']
v189 = ['ride', 'rode', 'ridden', 'ездить верхом']
v190 = ['ring', 'rang', 'rung', 'звонить']
v191 = ['rise', 'rose', 'risen', 'подняться']
v192 = ['rive', 'rived', 'riven', 'расщеплять']
v193 = ['run', 'ran', 'run', 'бежать, течь']
v194 = ['saw', 'sawed', 'sawn/sawed', 'пилить']
v195 = ['say', 'said', 'said', 'говорить, сказать']
v196 = ['see', 'saw', 'seen', 'видеть']
v197 = ['seek', 'sought', 'sought', 'искать']
v198 = ['sell', 'sold', 'sold', 'продавать']
v199 = ['send', 'sent', 'sent', 'послать']
v200 = ['set', 'set', 'set', 'устанавливать']
v201 = ['sew', 'sewed', 'sewed/sewn', 'шить']
v202 = ['shake', 'shook', 'shaken', 'трясти']
v203 = ['shave', 'shaved', 'shaved/shaven', 'брить(ся)']
v204 = ['shear', 'sheared', 'shorn/sheared', 'стричь']
v205 = ['shed', 'shed', 'shed', 'проливать']
v206 = ['shine', 'shone/shined', 'shone/shined', 'светить, сиять']
v207 = ['shoe', 'shod', 'shod', 'обувать, подковывать']
v208 = ['shoot', 'shot', 'shot', 'стрелять, давать побеги']
v209 = ['show', 'showed', 'shown/showed', 'показывать']
v210 = ['shred', 'shred/shredded', 'shred/shredded', 'кромсать, расползаться']
v211 = ['shrink', 'shrank/shrunk', 'shrunk',
        'сокращаться, сжиматься, отпрянуть']
v212 = ['shrive', 'shrove/shrived', 'shriven/shrived', 'исповедовать']
v213 = ['shut', 'shut', 'shut', 'закрывать']
v214 = ['sing', 'sang', 'sung', 'петь']
v215 = ['sink', 'sank', 'sunk', 'опускаться, погружаться, тонуть']
v216 = ['sit', 'sat', 'sat', 'сидеть']
v217 = ['slay', 'slew', 'slain', 'убивать']
v218 = ['sleep', 'slept', 'slept', 'спать']
v219 = ['slide', 'slid', 'slid', 'скользить']
v220 = ['sling', 'slung', 'slung', 'швырять, подвешивать']
v221 = ['slink', 'slunk', 'slunk', 'идти крадучись']
v222 = ['slit', 'slit', 'slit', 'раздирать(ся), разрезать (вдоль)']
v223 = ['smell', 'smelt/smelled', 'smelt/smelled', 'пахнуть, нюхать']
v224 = ['smite', 'smote', 'smitten', 'ударять, разбивать']
v225 = ['sow', 'sowed', 'sowed/sown', '(по)сеять']
v226 = ['speak', 'spoke', 'spoken', 'говорить']
v227 = ['speed', 'sped/speeded', 'sped/speeded', 'ускорять, спешить']
v228 = ['spell', 'spelt/spelled', 'spell/spelled',
        'писать или читать по буквам']
v229 = ['spend', 'spent', 'spent', 'тратить']
v230 = ['spill', 'spilt/spilled', 'spilt/spilled', 'пролить']
v231 = ['spin', 'spun/span', 'spun', 'прясть']
v232 = ['spit', 'spat/spit', 'spat/spit', 'плевать']
v233 = ['split', 'split', 'split', 'расщепить(ся)']
v234 = ['spoil', 'spoilt/spoiled', 'spoilt/spoiled', 'портить']
v235 = ['spotlight', 'spotlit/spotlighted', 'spotlit/spotlighted', 'осветить']
v236 = ['spread', 'spread', 'spread', 'распространиться']
v237 = ['spring', 'sprang', 'sprung', 'вскочить, возникнуть']
v238 = ['stand', 'stood', 'stood', 'стоять']
v239 = ['stave', 'staved/stove', 'staved/stove', 'проламывать, разби(ва)ть']
v240 = ['steal', 'stole', 'stolen', 'украсть']
v241 = ['stick', 'stuck', 'stuck', 'уколоть, приклеить']
v242 = ['sting', 'stung', 'stung', 'ужалить']
v243 = ['stink', 'stank/stunk', 'stunk', 'вонять']
v244 = ['strew', 'strewed', 'strewn/strewed', 'усеять, устлать']
v245 = ['stride', 'strode', 'stridden', 'шагать']
v246 = ['strike', 'struck', 'struck', 'ударить, бить, бастовать']
v247 = ['string', 'strung', 'strung', 'нанизать, натянуть']
v248 = ['strive', 'strove', 'striven', 'стараться']
v249 = ['sublet', 'sublet', 'sublet', 'передавать в субаренду']
v250 = ['swear', 'swore', 'sworn', '(по)клясться, присягнуть']
v251 = ['sweep', 'swept', 'swept', 'мести, промчаться']
v252 = ['swell', 'swelled', 'swollen/swelled', 'вздуться']
v253 = ['swim', 'swam', 'swum', 'плыть']
v254 = ['swing', 'swung', 'swung', 'качаться']
v255 = ['take', 'took', 'taken', 'взять, брать']
v256 = ['teach', 'taught', 'taught', 'учить']
v257 = ['tear', 'tore', 'torn', 'рвать']
v258 = ['tell', 'told', 'told', 'рассказывать, сказать']
v259 = ['think', 'thought', 'thought', 'думать']
v260 = ['thrive', 'throve/trived', 'thriven/trived', 'процветать']
v261 = ['throw', 'threw', 'thrown', 'бросить']
v262 = ['thrust', 'thrust', 'thrust', 'толкнуть, сунуть']
v263 = ['tread', 'trod', 'trod/trodden', 'ступать']
v264 = ['unbend', 'unbent', 'unbent', 'разогнуть(ся)']
v265 = ['underbid', 'underbid', 'underbid', 'снижать цену']
v266 = ['undercut', 'undercut', 'undercut', 'сбивать цены']
v267 = ['undergo', 'underwent', 'undergone', 'проходить, подвергаться']
v268 = ['underlie', 'underlay', 'underlain', 'лежать в основе']
v269 = ['underpay', 'underpaid', 'underpaid', 'оплачивать слишком низко']
v270 = ['undersell', 'undersold', 'undersold', 'продавать дешевле']
v271 = ['understand', 'understood', 'understood', 'понимать']
v272 = ['undertake', 'undertook', 'undertaken', 'предпринять']
v273 = ['underwrite', 'underwrote', 'underwritten', 'подписыва(ть)ся']
v274 = ['undo', 'undid', 'undone', 'уничтожать сделанное']
v275 = ['unfreeze', 'unfroze', 'unfrozen', 'размораживать']
v276 = ['unsay', 'unsaid', 'unsaid', 'брать назад свои слова']
v277 = ['unwind', 'unwound', 'unwound', 'развертывать']
v278 = ['uphold', 'upheld', 'upheld', 'поддерживать']
v279 = ['upset', 'upset', 'upset', 'опрокинуть(ся)']
v280 = ['wake', 'woke/waked', 'woken/waked', 'просыпаться, будить']
v281 = ['waylay', 'waylaid', 'waylaid', 'подстерегать']
v282 = ['wear', 'wore', 'worn', 'носить(одежду)']
v283 = ['weave', 'wove/weaved', 'woven/weaved', 'ткать']
v284 = ['wed', 'wed/wedded', 'wed/wedded', 'выдавать замуж']
v285 = ['weep', 'wept', 'wept', 'плакать']
v286 = ['wet', 'wet/wetted', 'wet/wetted', 'мочить, увлажнять']
v287 = ['win', 'won', 'won', 'выиграть']
v288 = ['wind', 'wound', 'wound', 'заводить (механизм)']
v289 = ['withdraw', 'withdrew', 'withdrawn', 'взять назад, отозвать']
v290 = ['withhold', 'withheld', 'withheld', 'удерживать']
v291 = ['withstand', 'withstood', 'withstood', 'противиться']
v292 = ['work', 'worked/wrought', 'worked/wrought', 'работать']
v293 = ['wring', 'wrung', 'wrung', 'скрутить, сжать']
v294 = ['write', 'wrote', 'written', 'писать']

list_of_verbs = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, v50, v51, v52, v53, v54, v55, v56, v57, v58, v59, v60, v61, v62, v63, v64, v65, v66, v67, v68, v69, v70, v71, v72, v73, v74, v75, v76, v77, v78, v79, v80, v81, v82, v83, v84, v85, v86, v87, v88, v89, v90, v91, v92, v93, v94, v95, v96, v97, v98, v99, v100, v101, v102, v103, v104, v105, v106, v107, v108, v109, v110, v111, v112, v113, v114, v115, v116, v117, v118, v119, v120, v121, v122, v123, v124, v125, v126, v127, v128, v129, v130, v131, v132, v133, v134, v135, v136, v137, v138, v139, v140, v141, v142, v143, v144, v145, v146, v147, v148, v149, v150, v151, v152, v153, v154, v155,
                 v156, v157, v158, v159, v160, v161, v162, v163, v164, v165, v166, v167, v168, v169, v170, v171, v172, v173, v174, v175, v176, v177, v178, v179, v180, v181, v182, v183, v184, v185, v186, v187, v188, v189, v190, v191, v192, v193, v194, v195, v196, v197, v198, v199, v200, v201, v202, v203, v204, v205, v206, v207, v208, v209, v210, v211, v212, v213, v214, v215, v216, v217, v218, v219, v220, v221, v222, v223, v224, v225, v226, v227, v228, v229, v230, v231, v232, v233, v234, v235, v236, v237, v238, v239, v240, v241, v242, v243, v244, v245, v246, v247, v248, v249, v250, v251, v252, v253, v254, v255, v256, v257, v258, v259, v260, v261, v262, v263, v264, v265, v266, v267, v268, v269, v270, v271, v272, v273, v274, v275, v276, v277, v278, v279, v280, v281, v282, v283, v284, v285, v286, v287, v288, v289, v290, v291, v292, v293, v294]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, {message.from_user.first_name}. Давай учить неправильные глаголы.')
    bot.send_message(
        message.chat.id, 'Я буду просить тебя вписать корректную форму глагола. Для того, чтобы начать проверять свои знания, введи команду /learn')


@bot.message_handler(commands=['learn'])
def learn2(message):
    global random_verb
    random_verb = choice(list_of_verbs)
    bot.send_message(
        message.chat.id, f'Напиши вторую форму глагола {random_verb[0].capitalize()} ({random_verb[3]})')
    bot.register_next_step_handler(message, learn3)


def learn3(message):
    try:
        if message.text.lower().strip() == f'{random_verb[1]}':
            bot.send_message(message.from_user.id,
                             'Правильно!\nТеперь напиши третью форму этого глагола.')
        elif message.text.lower().strip() == f'{random_verb[1].split("/")[0]}':
            bot.send_message(
                message.from_user.id, f'Правильно! Также корректным ответом является {random_verb[1].split("/")[1]}.\nТеперь напиши третью форму этого глагола.')
        elif message.text.lower().strip() == f'{random_verb[1].split("/")[1]}':
            bot.send_message(
                message.from_user.id, f'Правильно! Также корректным ответом является {random_verb[1].split("/")[0]}.\nТеперь напиши третью форму этого глагола.')
        else:
            raise IndexError
    except IndexError:
        bot.send_message(
            message.from_user.id, f'Нет, корректный ответ: {random_verb[1]}.\nТеперь напиши третью форму этого глагола.')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        if message.text.lower().strip() == f'{random_verb[2]}':
            bot.send_message(
                message.from_user.id, 'Правильно!\nПродолжаем?\n/learn')
            bot.register_next_step_handler(message, learn2)
        elif message.text.lower().strip() == f'{random_verb[2].split("/")[0]}':
            bot.send_message(
                message.from_user.id, f'Правильно! Также корректным ответом является {random_verb[2].split("/")[1]}.\nПродолжаем?\n/learn')
            bot.register_next_step_handler(message, learn2)
        elif message.text.lower().strip() == f'{random_verb[2].split("/")[1]}':
            bot.send_message(
                message.from_user.id, f'Правильно! Также корректным ответом является {random_verb[2].split("/")[0]}.\nПродолжаем?\n/learn')
            bot.register_next_step_handler(message, learn2)
        else:
            raise IndexError
    except IndexError:
        bot.send_message(
            message.from_user.id, f'Нет, корректный ответ: {random_verb[2]}.\nПродолжаем?\n/learn')
        bot.register_next_step_handler(message, learn2)


bot.polling(none_stop=True)
