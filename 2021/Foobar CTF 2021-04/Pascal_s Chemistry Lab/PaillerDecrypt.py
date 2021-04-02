#!/usr/bin/env python3

# Imports
from Crypto.Util.number import long_to_bytes
import gmpy2

# Paillier public parameters
g = 283553126615976472219372373584591655710189620701419388286568488684916710452787368827245954143968893781880232004553029839120479747701610686283348576171835784043546788355861285442697848428162312763712211489932420406199400965296253770782029582516869662362025521732152651594041890398121417468508203779355292308211264765688172637962096694471934021987838161734942754881088296439024302510851426449023094755451867683476357415112666372435051230671279268723993315628827267396323081999198097583551198473596471042756138167665737804253004490865803081061566722266590759061263522784021244289687324715125315495253819480740406701277635692477355980603490156017249197909199150491704517090604468674890636461909194928077516239159551240078781643127560601543830066359179014080123238220427779975114234589728432458700241098046012131758060758659793130867535055113103540161546220601838269298324980209251364898517114327763286537861788156575491822324259162799179643789391927743028743262360531050474556322167291153402283748756854662843134923651011698897467500467298853535830727169312555892631402139176288658479236364874889111458159864883714589798770518871627660856281105086287827256506276916847338003723518221933003470765733184337012688080489067958394185409850679361980335975854027570900568687474321040643051232092134719975281068810169777830510544697748820607559919634730748136676371105028398992197729995967259268460022363497150285395440003541085884482522530874004029842077366976876497413511284494766068774835274851420030484031768224116850873241921668780287697704323661592556244746095131647584324518652953445938155051362759024715686247291281065620329948340349266867161581764421243932739673105551546446911906201360236259481481116619087137960422955162685802540656462828611694062830853292918826108296945790520620627299927556178955245018959749306994438353031930804870396451922490151615638011080010143567882796379621907546395987660384455271436441242443678235383830349504451048884187312414414679649749121244661918258818473165719779117181706909916601457568151376758652838830561566582935536087324369226896931895480190607578443210209458898102110804712372490928998111850091607968415823456645132237010860623549522426820476824044459597017780502074924384652873769045864110683332468326626441007200574941823947199287637431570121257553466644653988532289878135579829340868797219585883447365861414100007674595854957435258089124244420374032330775168801981496988886333703959812041553005994677444580677268221248386525339517786532161152923987110330435182533361759649561057386253269031922100420795326866819520514685270661729635590624132796977376449820541458664016456988790379266517541201456720302649637811279813502091551027684972833562108234294135623459202445793207958192845075728056258557802431062881610455333486235518016736163278154172955499898093313669283556978764258700766055690543982842958892319420877351536385738692516965179092314751746546086414647490217057222464245218409337380237265216332397495677510399082610587841183802834815475996515555996551416595600153179316019071417438626386455120784192313753830461788480292899941126430469950166511323500113335271047396588163573197416202296629555290699614252034827580868720841196914543808556699582837434105701541418765505998938957742322212183596367790759417849310170081906817891109808193349616193354415432832117261007165944947448027705038988621705529391044746016761326454185918204209073060684603494618712284080081080106929061413557738685722474606661933957028734808835897059917699240206686138062203401593472732565499849223244988585130989567601245754247267713102133817694721200988475520102228866095102173137314672104509826536243224874297246072639450087125716238413870625436953565893453047735884055094017325365618641505846872354826521468384871023042900990330971379592137268178659024687423875693804245873104378920839474062753207518148787301641223919412878735440661012581619765312192214463819287054797490610170016473056231615464444419062497663850911654609765641400610936030228829833357842882008112463532850996691440572595062551465310685241422396912719744613612363822611293308424553029584125423894784554804389211227681493853001440033045415592670966917268973247063198498979999195643822001654969507229010497249428211445800751284121380400607290169934993783348819336702540732393793242141981027046120444204551124845473426522521636405758012683248101736062838518916368532502372631203035108410206462556711325994584010160193004879667217912742209143429749229837808465218935667025429380253128403663724315908654163831140499191305377725826659705505907529767342868725128326779100363063134287613592731890798002886659729534612416801917072974776758962467068817154956645595934188714073232309010438135752029654431247276381755062540640663257125982918304828564012266824063376713469354625316023796364160856248100478669094520499736462399744569058016669675177194096013442714851576634240935955621973873962127767968117065882942853698479960221689473463826946831967562850
n = 645112929026432431896835681383215798094857335385003555076064838558219895684792668177063930476834956225073128268590883368550408976742239476930849091221266961671657159011460813465127064066752373541839223723609403613047833622045052806887113745064238669191068843378581443086158031017447204138333212666639485272195460698595320682475296914416997495790132643867076368081931304358518097559724349042201012630335878269135237845734971411653985372585461578105182175206143595560118907825318729794428422349356014129823581280991522419055480674904880113759389602292195127416680373856795877343060276686461787555551273229716287308155725528833729602711756179293529403030380857256389910116881569602400018740721260844234830921343694984276962213728323311123033020318122084081791042257973494294433037811923864112595576000854513742977682353127829493390821953424264169849152008283451986350830491159417957988850994876036688699656959039305819240975554930288078896535172195229565800760569336134931411445761283635218971419938843921813711227067518347136245124634807245275222477057844804758388982997663297258151397708380570303191262435864746915244460538315527319818209161480923346280843524518900396887049771487699137656329916189832219616915227837861048985977274249807815101629604980577755741611156127243133907345394852593656350025670978127748678703057618338478422844601159600556573884896806521943574268755286183450519767265317097919057383153759937319233905793739833908262111888253486506978843748015305015810816125650294247653152217837475893777827868936498480501482471941158872613973986996659398691441483228291397451282478187746715858085713047504683357908581075367275330677150073104506888678300243060579273972121582707592622207556135878057008212612270237536863570294300920924259764874898030731463066209311052964274747847859584242065965443756112359887144414334663480139843335184505023632393297282279530604054513160789326054033851889382956357202566687830597062417675142486037910057837702167555157486081436772745657464239316999115096635179594332382611482855621677065597324023707544887656282868937081195657766306507668415586762358738148537948802640962303818194369300523046783695442258662203627449829781626516660674814803013397111396697275198853146900705297908322671588085245421000396563552243414129066431390783005479651796480390951976397413108708149767968891192283610122410770035718754717686047796104170306984088734415756620023879764760896013369695230063878802304765693793155333790382156366073221751913

# Ciphertext
c = 51239669900277406784468675248740735901802286613698075244112005527279986278761579474672158150698895534630782137055079466359776859321123275546689853378201066066515519830442797981103672831878437604759438956147961101067111231247928353974397538952963971149727459688953816233496294788412413958772699410485794707353713993774297008739471326293652928588082451266506899245280800675156950677848810761762176812072742646666254982879287146932388228457352509951756831302653978016608828461883857009843352061320869777022308554818825121203131755298217297380730669949633144473048619411329326100459805615365368167418069512940710133707268917688862713084755822359484285822744578876871765314697344564112527488758626154318734823324649895502635912833247157465958405643402434278553372572314058363032690517235603881625249540706670456692809264308940395873123069733397949597493520831357528309591862953031601405183664806386415210865116362104699150144540245432430991824006560027302365115635249176589456339583643997356476030867670656794992774037151274921957361960011738609457115817342696114114162506306150341674504756019969418337335863303239553222177741295322515021479004144557558947486111680065895366479642206077809406079711931720565677882773704660199409441184347578544595034588724648391530726125406297693236198127374819405626544011867500509543559828549106526778914672888585820101502449061950064163614239881001908194310462901643791709634167697286759447016426898098086397483903393108774600144001990139509178676591411472341782827863470695321858934593487746034615863984218538408896370033641986885895378190084850971429019188503867405478343783219473981650797514215835446855636523386469225016165783252792538764646496987020872988976553245924480798797686687381225759892179860963977161028632608834771514732783522695987254795652371935099462371068675185270881770909530470085242044594557481493478738208069621645732515733574826317641962634408926874877725483216369319661741439515232249731712529632451492266174282660351998587087221170504752142967672882697727623863133112383970867328923231706361796003662360062220509127819667692935019305960184126618651952100562089501566319755092493700591516573498459319522547257413678352445440283840971806746140877879495859106562545896351908041406663189950889338544378222913365400954242360580411106503515252321398928611310146077146285370590251649187326300461804094368119779762805042223846541342315522142302687027668256243220746370525012183171234661328145193949949945103695079930888605242263815493232397957846182489342811073865605012416325782269808624755484645186236149934103257521280136972867751152857946164904527200724714571864927965357080044753113016190741850824644659702895025094438085716870984971215749844742331274878909090802859061145162437651680928449069563283124446185069038511872866112301184367838342101964358143871360198781180880447224147366421968909801111819639400346142018372990406222927043666164375305747643411481272722418426944362500044240759732034884370086802937570629676610643568834272244900678921587419375168504925133465639606377972995107267892288527542903620816141037785877067436409081169459342758906122749826263667253025928007815594747251090209426556143643674436703437652783919310826557643965341544121896009129194141452714604074143124687608600942641473861665703758102172765751967028327587574980088817037147673265818928757226146912527218257431677589109487385560360085255944710288168714668767370704224816201664626107820395719321080454245144920417194631453321678633518249950772085993626298582392213657819585868944463544859201565342221159779741959826761565012879217905505379756835284059645579214613296049709365889122580086885985902897540900378530546710335109493074246650106806711350326384035088692329294959008009757245863884893214347527330660978363066841377626742328173474169451048922034442574338572813057939549597360614444043058023981989945194610069325093263109698449778820073681650341110487198473525278858210900682148143955134163887721322797934210998754781180429912880117753431339950914643693504437827955082560040373133009649905616286117052554026662327376229480425549978756629580305718748555359580181840216691755828196879593199755809190792983659385948648167582077718888274785882289823864043525552792677468513621602724369729412688625917046578371927019057901176111634182768333957354938634528946205225017557021891386190049374581324082130898476782384385948516397084627730769060793858187700142466563895639594583166823683773682361937721668643410474552622732869276158792298148466721132668470066866373175350504293108410079337756851827883477764478755408380689548148725947235993549632640782641782953985863766541581244551642579882047065727883224738832930477664485038335743895785871381405213471773886590295136032375679141010835192767761199911522075634433529310538323683621603254641566276435202964506342680138463766272630543229577434327209177799720094822023281688988448935864698857805603597920679760338979754149247768498135386266776013597227

# Fermat factorisation of N (done with online tools)
p = int("803 189223 674242 551709 532003 299448 441895 927059 124089 347207 037492 567487 451983 045667 439516 223949 123448 292479 543409 223207 543410 300608 786356 345390 833621 232596 068405 357909 767226 028932 111800 803275 506564 641737 059331 491014 115419 239563 437475 896512 336295 180259 968029 966663 803420 838711 632581 468862 450025 972533 186345 666149 059860 712114 143749 324589 956461 612084 605482 528274 311006 706566 963762 065872 751462 975861 565043 111023 307160 488218 060573 179618 469800 691836 658955 675043 891433 104940 102969 258712 400991 916983 129397 968636 401757 658244 018782 179822 504649 888610 671657 440290 622897 270326 426690 492281 964296 716971 465458 786505 920285 411461 828677 317816 719098 884736 581175 186451 213255 108837 199471 710746 708016 181061 984225 264062 586950 794487 072007 786874 614841 029840 267687 538299 589424 383129 182938 384394 386262 419963 849395 551082 517421 117437 235627 316656 573754 697978 923722 962297 273436 325267 290151 721299 287013 894986 499549 519835 413978 242466 982260 557654 668235 105939 113502 241810 197464 345187 056270 455136 897081 446593 260142 653501 575479 352397 259625 559072 365647 311509 438722 311434 981533 395974 008407 279636 392824 161016 072865 816041 203636 558293 194699 710699 582697 506843 521374 064367 452334 048139 796391 351983 687009 128754 752321 972963 144955 691883 787997 686093 350313 272731 773486 967765 110028 704221".replace(' ',''))
q = int("803 189223 674242 551709 532003 299448 441895 927059 124089 347207 037492 567487 451983 045667 439516 223949 123448 292479 543409 223207 543410 300608 786356 345390 833621 232596 068405 357909 767226 028932 111800 803275 506564 641737 059331 491014 115419 239563 437475 896512 336295 180259 968029 966663 803420 838711 632581 468862 450025 972533 186345 666149 059860 712114 143749 324589 956461 612084 605482 528274 311006 706566 963762 065872 751462 975861 565043 111023 307160 488218 060573 179618 469800 691836 658955 675043 891433 104940 102969 258712 400991 916983 129397 968636 401757 658244 018782 179822 504649 888610 671657 440290 622897 270326 426690 492281 964296 716971 465458 786505 920285 411461 828677 317816 719098 884736 581175 186451 213255 108837 199471 710746 708016 181061 984225 264062 586950 794487 072007 786874 614841 029840 267687 538299 589424 383129 182938 384394 386262 419963 849395 551082 517421 117437 235627 316656 573754 697978 923722 962297 273436 325267 290151 721299 287013 894986 499549 519835 413978 242466 982260 557654 668235 105939 113502 241810 197464 345187 056270 455136 897081 446593 260142 653501 575479 352397 259625 559072 365647 311509 438722 311434 981533 395974 008407 279636 392824 161016 072865 816041 203636 558293 194699 710699 582697 506843 521374 064367 452334 048139 796391 351983 687009 128754 752321 972963 144955 691883 787997 686093 350313 272731 773486 967765 110028 704253".replace(' ',''))

# Paillier Function
def L(x):
    if (x-1) % n == 0:
        return (x-1)//n
    else:
        return 'HELP'
    
# Lambda and mu: Paillier private parameters
lm = gmpy2.lcm( p-1 , q-1 )
mu = gmpy2.invert( L( pow(g, lm, n**2) ) , n)

# Decrypt and print
m = ( L(pow(c, lm, n**2)) * mu ) % n
print(long_to_bytes(m))