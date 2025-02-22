import random

###########【Input machine data】#######################
# ooatari
atariKakuritsu = input()
# ST ooatari
STatariKakuritsu = input()
# ST totsunyuu
STtotsunyuritsu = input()
# ST kaisuu
STkaisu = input()
# jitan kaisuu
jitanKaisu = input()
# soukaitensuu
kaitensuuSum = input()
# 1000yen kaitensuu
senenKaitensuu = input()
# dedamasuu
ikaiOatariDedama = input()
# simday
simulationDay = input()
###########################################

########データ収集##########
# hamari kaisuu
hamariKaisu = 0
# saidai hamari kaisuu
saidaiHamari = 0
# kakuhenchuu renchan kaisuu
renchanKaisu = 0
# saidai renchan kaisuu
saidaiRenchanKaisu = 0
# kakuhen totsunyuu kaisuu
kakuhenTotsunyuKaisu = 0
# kakuhen hazure kaisuu
kakuhenNGKaisu = 0
# hatsuatari kaisuu
hatsuatariKakuritsu = 0
# hazure kaisuu
hazureKaisu = 0
# atari kaisuu
atariKaisu = 0
# saidai atari kaisuu
saidaiAtariKaisu = 0
# kakuhen kaisuu
kakuhenKaisu = 0
# saidai kakuhen kaisuu
saidaiKakuhenKaisu = 0
# sou ooatari kaisuu
atariKaisuSum = 0
# sou kakuhen kaisuu
kakuhenKaisuSum = 0
##########################

# 現在のパチンコの状態：0＝通常時、1＝大当たり時かつ確変中
pachinkoStatus = 0

# パチンコシミュレーション1回転分
def pachinko1KaitenSimulation():
    global atariKakurits
    global STatariKakuritsu
    global STkaisu
    global STtotsunyuritsu
    global kaitensuuSum
    global jitanKaisu
    global senenKaitensuu
    global ikaiOatariDedama
    global simulationDay

    global hamariKaisu
    global saidaiHamari
    global renchanKaisu
    global saidaiRenchanKaisu
    global kakuhenTotsunyuKaisu
    global kakuhenNGKaisu
    global hatsuatariKakuritsu
    global hazureKaisu
    global atariKaisu
    global saidaiAtariKaisu
    global kakuhenKaisu
    global saidaiKakuhenKaisu
    global atariKaisuSum
    global kakuhenKaisuSum

    global pachinkoStatus

    ##ユーザーの方が入力した数字をrandomで乱数を引き出すコード
    #通常時+時短時の当たり乱数
    atariKakuritsuUser = random.randint(1, atariKakuritsu)
    hamariKaisu += 1

    #ST中の当たり乱数
    STTotsunyuritsuUser = random.randint(1, 100)
    STatariKakuritsuUser = random.randint(1, STatariKakuritsu)

    ##通常時パターン
    if pachinkoStatus == 0:
        ##通常時から大当たり処理
        if atariKakuritsuUser == 1:
            atariKaisu += 1
            print("ATARI")
            print(hamariKaisu, "kaiten me de", atariKaisu, "kai me no ooatari")
            hamariKaisu = 0

            ##ST突入判定
            if STTotsunyuritsuUser <= STtotsunyuritsu:
                kakuhenTotsunyuKaisu += 1
                pachinkoStatus = 2
                print(kakuhenTotsunyuKaisu, "kaime, ST totsunyuu")

            ##ST突入せず時短へ
            else:
                kakuhenNGKaisu += 1
                print(kakuhenNGKaisu, "kaime, NO ST")
                pachinkoStatus = 1
        # 通常時から外れ処理
        else:
            hazureKaisu += 1
            #最大ハマり数
            if (hamariKaisu > saidaiHamari):
                saidaiHamari = hamariKaisu


    ##時短中処理
    elif pachinkoStatus == 1:
            #時短中大当たり&ST突入
            if atariKakuritsuUser == 1 & STTotsunyuritsuUser <= STtotsunyuritsu:
                atariKaisu += 1
                print("Jitan tyuu ooatari")
                print(hamariKaisu, "kaitenme de", atariKaisu, "kaime no ooatari")
                pachinkoStatus = 2
                kakuhenTotsunyuKaisu += 1
                print(kakuhenTotsunyuKaisu, "kaime, ST totsunyuu")
                hamariKaisu = 0

            #時短中大当たり&ST突入せず
            elif atariKakuritsuUser == 1 & STTotsunyuritsuUser > STtotsunyuritsu:
                atariKaisu += 1
                kakuhenNGKaisu += 1
                print("Jitantyuu ooatari")
                print(hamariKaisu, "kaitenme de", atariKaisu, "kaime no ooatari")
                print(kakuhenNGKaisu, "kaime, NO ST")
                print("===================")
                hamariKaisu = 0

            #時短終了
            elif hamariKaisu == jitanKaisu:
                print("Jitan end tuujou he")
                print("===================")
                pachinkoStatus = 0


    ##ST中パターン
    elif pachinkoStatus == 2:

            #ST中大当たり
            if STatariKakuritsuUser == 1:
                kakuhenKaisu += 1
                renchanKaisu += 1
                print((renchanKaisu + 1), "renchan!(ST chuu)")
                hamariKaisu = 0

            #ST中駆け抜け
            elif STkaisu == hamariKaisu:
                print("tuujou mode he")
                print("===================")
                if renchanKaisu > saidaiRenchanKaisu:
                    renchanKaisu += 1
                    saidaiRenchanKaisu = renchanKaisu
                renchanKaisu = 0
                pachinkoStatus = 0

# 日数シミュレーション
saidaiKachigaku = 0
saidaiMakegaku = 0
goukeiShushi = 0
heikinShushi = 0
ichinichiShushi = 0
daily_count = 0
max_saidaihamari = 0

#日数分の収支データ(出玉計測 / 日 + 最大データ算出 + その日の当たり・確変回数のリセット)
def pachinkoDailySimulation():
    global atariKakurits
    global STatariKakuritsu
    global STkaisu
    global STtotsunyuritsu
    global kaitensuuSum
    global jitanKaisu
    global senenKaitensuu
    global ikaiOatariDedama
    global simulationDay

    global hamariKaisu
    global saidaiHamari
    global renchanKaisu
    global saidaiRenchanKaisu
    global kakuhenTotsunyuKaisu
    global kakuhenNGKaisu
    global hatsuatariKakuritsu
    global hazureKaisu
    global atariKaisu
    global saidaiAtariKaisu
    global kakuhenKaisu
    global saidaiKakuhenKaisu
    global atariKaisuSum
    global kakuhenKaisuSum
    global pachinkoStatus

    ##日数シミュレーションのグローバル変数宣言
    global saidaiKachigaku
    global saidaiMakegaku
    global saidaiHamari
    global max_saidaihamari
    global goukeiShushi
    global heikinShushi
    global ichinichiShushi

    #【決めた回転数分回す】入っているデータ：大当たり回数(確変突入 / 非突入含む)・確変回数
    for _ in range(1, kaitensuuSum):
            pachinko1KaitenSimulation()

    ##出玉計測
    hazureDedama = ((250 / senenKaitensuu) * hazureKaisu)
    atariDedama = ((atariKaisu + kakuhenKaisu) * ikaiOatariDedama)
    ichinichiDedamaSum = (atariDedama) - (hazureDedama)

    ##出玉分を4円に換算
    ichinichiShushi = (ichinichiDedamaSum * 4)

    ##合計収支に加算
    goukeiShushi += ichinichiShushi

    ##一日における最大勝ち額・最大負け額の算出
    if ichinichiShushi > 0 and saidaiKachigaku < ichinichiShushi:
        saidaiKachigaku = ichinichiShushi
    elif ichinichiShushi < 0 and saidaiMakegaku > ichinichiShushi:
        saidaiMakegaku = ichinichiShushi

    ##一日における各種(総大当たり回数・総確変回数・ 最大大当たり回数・ 最大確変数・最大ハマり数）
    #総大当たり回数
    atariKaisuSum += atariKaisu

    #総確変回数
    kakuhenKaisuSum += kakuhenKaisu

    #最大大当たり回数
    if atariKaisu > saidaiAtariKaisu:
        saidaiAtariKaisu = atariKaisu

    #最大確変回数
    if kakuhenKaisu > saidaiKakuhenKaisu:
        saidaiKakuhenKaisu = kakuhenKaisu

    #最大ハマり回数の集計
    if saidaiHamari > max_saidaihamari:
        max_saidaihamari = saidaiHamari

# パチンコシミュレーター処理回数
for _ in range(1, (simulationDay + 1)):
    pachinkoDailySimulation()
    daily_count += 1
    print("")
    print("======【", daily_count, "day result 】======")
    print(daily_count, "day result is", (ichinichiShushi), "yen")
    print(daily_count, "day kaitensuu is: ", atariKaisu, "kai")
    print(daily_count, "day ST kaisuu is: ", kakuhenKaisu, "kai")
    print(daily_count, "day saidaihamari is: ", saidaiHamari, "kai")
    print("==============================")
    print("")
    ##出玉リセット(ハマり回数・確変突入回数・確変突入しなかった回数・初当たり回数・外れ回数・当たり回数・確変回数)
    hamariKaisu = 0
    kakuhenTotsunyuKaisu = 0
    kakuhenNGKaisu = 0
    hatsuatariKakuritsu = 0
    hazureKaisu = 0
    atariKaisu = 0
    kakuhenKaisu = 0
    saidaiHamari = 0

#= == == データ収集結果出力 == == = //
print("")
print("")
print("====simulation result====")

#= == =日数シミュレーションの結果表示 == == =
# 何日シミュレーションしたのか
print(simulationDay, "days simulation result")
# 総回転数
print("soukaitensuu: ", (kaitensuuSum * simulationDay), "kaiten")
# 総収支金額
print(simulationDay, "days soushuushi is: ", (goukeiShushi), "yen")
# 平均収支
print(simulationDay, "average: ", (goukeiShushi / simulationDay), "yen")
# 最大勝ち額
print(simulationDay, "max winning: ", (saidaiKachigaku), "yen")
# 最大負け額
print(simulationDay, "max losess: ", (saidaiMakegaku), "yen")
# 総大当たり回数
print(simulationDay, "days sou ooatari: ", atariKaisuSum, "kai")
# 総確変回数
print(simulationDay, "days sou ST: ", kakuhenKaisuSum, "kai")
# 最大大当たり回数
print(simulationDay, "max atari kaisuu: ", saidaiAtariKaisu, "kai")
# 最大確変回数
print(simulationDay, "max ST kaisuu: ", saidaiKakuhenKaisu, "kai")
# 最大連チャン回数
print(simulationDay, "max renchan kaisuu: ", saidaiRenchanKaisu, "kai")
# 最大ハマり回数
print(simulationDay, "days max hamari kaisuu", max_saidaihamari, "kai")