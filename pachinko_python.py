import random
global tryagain
global tagain

print("start simulate? y or n")
tryagain = input()
while tryagain == str("y"):

    ###########【台入力データ】#######################
    # 大当たり確率
    print("win is ")
    atariKakuritsu = input()
    if str(atariKakuritsu) == (""):
        print("error!")
        break
    # 確変突入率
    print("dive to ST is ")
    kakuhenTotsunyuritsu = input()
    if kakuhenTotsunyuritsu == (""):
        print("error!")
        break
    # 確変継続率
    print("chain number is ")
    kakuhenKeizokuritsu = input()
    if kakuhenKeizokuritsu == (""):
        print("error!")
        break
    # 総回転数
    print("total try is ")
    kaitensuuSum = input()
    if kaitensuuSum == (""):
        print("error!")
        break
    # 1000円辺りの回転率
    print("time rolling per 1000 yen")
    senenKaitensuu = input()
    if senenKaitensuu == (""):
        print("error!")
        break
    #大当たり一回辺りの出玉数
    print("can take 1 win is")
    ikaiOatariDedama = input()
    if ikaiOatariDedama == (""):
        print("error!")
        break 
    #日数分のシミュレーション
    print("days")
    simulationDay = input()
    if simulationDay == (""):
        print("error!")
        break
    ################################################

    ########データ収集##########
    # ハマり回数
    hamariKaisu = 0
    # 最大ハマり回数
    saidaiHamari = 0
    # 確変中連チャン回数
    renchanKaisu = 0
    # 最大連チャン回数
    saidaiRenchanKaisu = 0
    # 確変突入率回数
    kakuhenTotsunyuKaisu = 0
    # 確変突入出来なかった回数
    kakuhenNGKaisu = 0
    # 初当たり確率
    hatsuatariKakuritsu = 0
    #外れ回数
    hazureKaisu = 0
    #当たり回数
    atariKaisu = 0
    # 最大当たり回数
    saidaiAtariKaisu = 0
    # 確変回数
    kakuhenKaisu = 0
    # 最大確変回数
    saidaiKakuhenKaisu = 0
    # 総大当たり回数
    atariKaisuSum = 0
    # 総大当たり回数
    kakuhenKaisuSum = 0
    ##########################

    # 現在のパチンコの状態：0＝通常時、1＝大当たり時かつ確変中
    pachinkoStatus = 0

    # パチンコシミュレーション1回転分
    def pachinko1KaitenSimulation():
        global atariKakuritsu
        global kakuhenTotsunyuritsu
        global kakuhenKeizokuritsu
        global kaitensuuSum
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

        #ユーザーの方が入力した数字をrandomで乱数を引き出すコード
        atariKakuritsuUser = random.randrange(1, int(atariKakuritsu))
        kakuhenTotsunyuritsuUser = random.randint(1, 100)
        kakuhenKeizokuritsuUser = random.randint(1, 100)
        kakuhenOatariKakuritsuUser = random.randrange(1, int(int(atariKakuritsu) / 10))

        ##通常時パターン
        if pachinkoStatus == 0:
            ##通常時から大当たり処理
            if atariKakuritsuUser == 1:
                atariKaisu += 1
                print("OoAtari")
                print(hamariKaisu, "kaitenme de", atariKaisu, "kaime no ooatari")
                hamariKaisu = 0
                ##確変突入判定
                if int(kakuhenTotsunyuritsuUser) <= int(kakuhenTotsunyuritsu):
                    kakuhenTotsunyuKaisu += 1
                    pachinkoStatus = 1
                    print(kakuhenTotsunyuKaisu, "kaime, kakuhen totsunyuu")
                ##確変突入せず
                else:
                    kakuhenNGKaisu += 1
                    print(kakuhenNGKaisu, "kaime, no kakuhen")
                    print("===================")
            # 通常時から外れ処理
            else:
                hamariKaisu += 1
                hazureKaisu += 1
                #最大ハマり数
                if (hamariKaisu > saidaiHamari):
                    saidaiHamari = hamariKaisu

        elif pachinkoStatus == 1:
            ##確変時の処理
            if kakuhenOatariKakuritsuUser == 1:
                kakuhenKaisu += 1
                renchanKaisu += 1
                print((renchanKaisu + 1), "renchan(kakuhen chuu)")
                #④確変継続判定】
                if int(kakuhenKeizokuritsuUser) <= int(kakuhenKeizokuritsu):
                    pachinkoStatus = 1
                else:
                    print("Go to normal mode")
                    print("===================")
                    pachinkoStatus = 0
                    if renchanKaisu > saidaiRenchanKaisu:
                        renchanKaisu += 1
                        saidaiRenchanKaisu = renchanKaisu
                    renchanKaisu = 0

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
        global max_saidaihamari
        

        #【決めた回転数分回す】入っているデータ：大当たり回数(確変突入 / 非突入含む)・確変回数
        for _ in range(0, int(kaitensuuSum)):
                pachinko1KaitenSimulation()

        ##出玉計測
        hazureDedama = (int(250 / int(senenKaitensuu)) * int(hazureKaisu))
        atariDedama = int(int(atariKaisu + kakuhenKaisu) * int(ikaiOatariDedama))
        ichinichiDedamaSum = int(int(atariDedama) - int(hazureDedama))
        ##出玉分を4円に換算
        ichinichiShushi = int(ichinichiDedamaSum * 4)
        ##合計収支に加算
        goukeiShushi += ichinichiShushi
        ##一日における最大勝ち額・最大負け額の算出
        if ichinichiShushi > 0 and saidaiKachigaku < ichinichiShushi:
            saidaiKachigaku = ichinichiShushi
        elif ichinichiShushi < 0 and saidaiMakegaku > ichinichiShushi:
            saidaiMakegaku = ichinichiShushi

        ##一日における各種(a: 総大当たり回数・b: 総確変回数・c: 最大大当たり回数・d: 最大確変数・e: 最大ハマり数）
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
    for _ in range(0, int(simulationDay)):
        pachinkoDailySimulation()
        daily_count += 1
        print("")
        print("======【", daily_count, "day result 】======")
        print(daily_count, "days result is", ichinichiShushi, "yen")
        print(daily_count, "days atarikaisuu is：　", atariKaisu, "time")
        print(daily_count, "days kakuhen is：　", kakuhenKaisu, "time")
        print(daily_count, "days hamari is：　", saidaiHamari, "time")
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


    #= == == データ収集結果出力 == == = 
    print("")
    print("")
    print("====simulation result of this time====")

    #= == =日数シミュレーションの結果表示 == == =
    # 何日シミュレーションしたのか
    print(simulationDay, "days simulation result")
    # 総回転数
    print("Total rolling is：　", int(kaitensuuSum) * int(simulationDay), "time")
    # 総収支金額
    print(simulationDay, "days total pay：　", int(goukeiShushi), "yen")
    # 平均収支
    print(simulationDay, "average pay：　", int(goukeiShushi) / int(simulationDay), "yen")
    # 最大勝ち額
    print(simulationDay, "max winning：　", int(saidaiKachigaku), "yen")
    # 最大負け額
    print(simulationDay, "max loses：　", int(saidaiMakegaku), "yen")
    # 総大当たり回数
    print(simulationDay, "days total winning is：　", atariKaisuSum, "time")
    # 総確変回数
    print(simulationDay, "days total ST is：　", kakuhenKaisuSum, "time")
    # 最大大当たり回数
    print(simulationDay, "days max win is：　", saidaiAtariKaisu, "time")
    # 最大確変回数
    print(simulationDay, "days max ST time is：　", saidaiKakuhenKaisu, "time")
    # 最大連チャン回数
    print(simulationDay, "days max chain is：　", saidaiRenchanKaisu, "time")
    # 最大ハマり回数
    print(simulationDay, "days max no win is：　", max_saidaihamari, "time")


    print("simulate again? y or n")
    tagain = input()
    if tagain == ("n"):
        break