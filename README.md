# blumblumshub
A PseudoRandom Number Generator based on Miller-Rabin and BBS algorithm 

Personal project for the fun :D 

## How to use ? 

```python
#Max alea to choose prime = 50000 , generate numbers on 64 bits
bbs = BBS_Generator(1000000, 64)
#Generate 100 random numbers
bbs.generate_numbers(100)
bbs.print()


```
```bash
$ python bbs_generator.py 
** Choose p prime number **
==> p =  937207
** Choose q prime number **
==> q =  517999
** End generation BBS **
number  0  random value =  17155281329562506008
number  1  random value =  1028544561933547562
number  2  random value =  13011165069823917718
number  3  random value =  15874907428148534230
number  4  random value =  9390353369930168035
number  5  random value =  1275888887456824491
number  6  random value =  12204719699880236278
number  7  random value =  4963519338528969641
number  8  random value =  7901192682944610599
number  9  random value =  2566966174536248764
number  10  random value =  3491400644926011425
number  11  random value =  159351617659084430
number  12  random value =  16426512661993610232
number  13  random value =  16278269510973890467
number  14  random value =  16846444198744898037
number  15  random value =  1577532644361359138
number  16  random value =  9227912437362642968
number  17  random value =  17097850737098663333
number  18  random value =  1982094887093467657
number  19  random value =  2784247771810734641
number  20  random value =  14446418299083062410
number  21  random value =  5286950681444184521
number  22  random value =  14065802006086025441
number  23  random value =  16441087077523100758
number  24  random value =  6593960234754036502
number  25  random value =  12300944306319829579
number  26  random value =  13700979089711650482
number  27  random value =  16091763990536976099
number  28  random value =  9396439896429585886
number  29  random value =  5176217372785249999
number  30  random value =  12403206739166955518
number  31  random value =  13889603509004501420
number  32  random value =  4327026082638963612
number  33  random value =  15914106692700413309
number  34  random value =  1031225791876828252
number  35  random value =  1302795955773340370
number  36  random value =  13762496116603183782
number  37  random value =  1817080049614233536
number  38  random value =  5761340634131810928
number  39  random value =  8903312791471761377
number  40  random value =  8158677659222291420
number  41  random value =  3724490531843800876
number  42  random value =  958660162413494398
number  43  random value =  8279713942972795964
number  44  random value =  12861762476417649157
number  45  random value =  7006648764508794221
number  46  random value =  18148686151288747791
number  47  random value =  7235155026554948402
number  48  random value =  6919382334889536308
number  49  random value =  7610134589340648992
number  50  random value =  15737436809074328847
number  51  random value =  8068451493222984565
number  52  random value =  18368882863344932788
number  53  random value =  11844656113461005145
number  54  random value =  14127380800884514193
number  55  random value =  4233171003436068393
number  56  random value =  11517290889203371985
number  57  random value =  8995795461686616807
number  58  random value =  405411214073093590
number  59  random value =  7903230135531346404
number  60  random value =  8535019247253953862
number  61  random value =  5609123419936078617
number  62  random value =  15332807412503803319
number  63  random value =  5008474504611189821
number  64  random value =  9228550503344828839
number  65  random value =  7968280576035761119
number  66  random value =  1175348937137927231
number  67  random value =  4095525355780447638
number  68  random value =  8491031557547923689
number  69  random value =  7356806521983830978
number  70  random value =  2121380633430016866
number  71  random value =  13865248996324432755
number  72  random value =  1508668182286499012
number  73  random value =  5595674195883365918
number  74  random value =  9103434868125106529
number  75  random value =  6663419024571551766
number  76  random value =  1421385008985201090
number  77  random value =  2918875077870654937
number  78  random value =  3094791149010876631
number  79  random value =  3085052942490992288
number  80  random value =  11511370505575682039
number  81  random value =  6990918538326282410
number  82  random value =  16945999698670997669
number  83  random value =  5285526030739164962
number  84  random value =  16752221542765839284
number  85  random value =  14303245580102599197
number  86  random value =  13847896519867738941
number  87  random value =  16545532938557596972
number  88  random value =  9361887338832692716
number  89  random value =  13104187253884848989
number  90  random value =  12107601539549274978
number  91  random value =  6136843109161573420
number  92  random value =  214358994347503667
number  93  random value =  16777833105184556523
number  94  random value =  7091344980760312849
number  95  random value =  13647184643808024630
number  96  random value =  9994436490589963079
number  97  random value =  12285481052958370657
number  98  random value =  10509804447443535845
number  99  random value =  16722376291749742119
```