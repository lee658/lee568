import sys
sys.path.insert(0, '/workspace/kmleai/mysite/examination/diag')

from one import test

def diagnosis(queryItems):
    test(queryItems)
    items = {}
    for i in queryItems:
        items[i] = str(queryItems[i])
#    print('test!!')
#    print(items)
    result = {}
    print('Disease name : ', items['val'])
    if items['val'] == 'valueOne':
        #print('virus if')
        #print(list(items.keys()))
        if not('fatigue' in list(items.keys())):
            items['fatigue'] = 'false'
        if not('nausea' in list(items.keys())):
            items['nausea'] = 'false'
        if not('abdominal pain' in list(items.keys())):
            items['abdominal pain'] = 'false'
        if not('jaundice' in list(items.keys())):
            items['jaundice'] = 'false'
        if not('totalBilirubin' in list(items.keys())):
            items['totalBilirubin'] = 0
        if (items['totalBilirubin'] == ''):
            items['totalBilirubin'] = 0
        if not('AST' in list(items.keys())):
            items['AST'] = 0
        if (items['AST'] == ''):
            items['AST'] = 0
        if not('ALT' in list(items.keys())):
            items['ALT'] = 0
        if (items['ALT'] == ''):
            items['ALT'] = 0
        if not('IgM_anti_HAV' in list(items.keys())):
            items['IgM_anti_HAV'] = 'false'
        if not('IgG_anti_HAV' in list(items.keys())):
            items['IgG_anti_HAV'] = 'false'
        if not('HBsAg' in list(items.keys())):
            items['HBsAg'] = 'false'
        if not('IgM_anti_HBc' in list(items.keys())):
            items['IgM_anti_HBc'] = 'false'
        if not('IgG_anti_HBc' in list(items.keys())):
            items['IgG_anti_HBc'] = 'false'
        if not('HBeAg' in list(items.keys())):
            items['HBeAg'] = 'false'
        if not('HBV_DNA' in list(items.keys())):
            items['HBV_DNA'] = 'false'
        if not('Anti_HBs' in list(items.keys())):
            items['Anti_HBs'] = 'false'
        if not('Anti_HCV' in list(items.keys())):
            items['Anti_HCV'] = 'false'
        if not('HCV_RNA' in list(items.keys())):
            items['HCV_RNA'] = 'false'
        fatigue = items["fatigue"]
        nausea = items["nausea"]
        abdominalpain = items["abdominal pain"]
        jaundice = items["jaundice"]
        totalbilirubin = float(items["totalBilirubin"])
        AST = float(items["AST"])
        ALT = float(items["ALT"])
        IgM_anti_HAV = items["IgM_anti_HAV"]
        IgM_anti_HBc = items["IgM_anti_HBc"]
        Anti_HCV = items["Anti_HCV"]
        HCV_RNA = items["HCV_RNA"]
        if (fatigue == "true") or (nausea == "true") or (abdominalpain == "true") or (jaundice == "true") or (totalbilirubin > 1) or (AST > 40) or (ALT > 40):
            result['특이사항'] = "증상과 혈액수치로 보아 간병변이 있어 추가검사를 시행해본다."
            if IgM_anti_HAV == "true":
                result['이유'] = "IgM_anti_HAV가 양성이기 때문에"
                result['진단'] = "진단 : 급성 A형 간염"
                result['치료'] = "치료 : 함께 사는 사람 예방하기"
            if IgM_anti_HBc == "true":
                result['이유'] = "IgM_anti_HBc가 양성이기 때문에"
                result['진단'] = "진단 : 급성 B형 간염"
                result['치료'] = "치료 : HBIG 근육주사후 예방접종"
            if (ALT > 40) and (Anti_HCV == "false") and (HCV_RNA == "true"):
                result['이유'] = "Anti_HCV가 음성이고 HCV_RNA가 양성이기 때문에"
                result['진단'] = "진단 : 급성 C형 간염"
                result['치료'] = "치료 : 특별히 없음"

######################################################################################

    elif items['val'] == 'valueTwo':
        #print('만성바이러스감염 if문 실행')
        if not('fatigue' in list(items.keys())):
            items['fatigue'] = 'false'
        if not('jaundice' in list(items.keys())):
            items['jaundice'] = 'false'
        if not('needle' in list(items.keys())):
            items['needle'] = 'false'
        if not('arthritis' in list(items.keys())):
            items['arthritis'] = 'false'
        if not('selfChronicHepatitisB' in list(items.keys())):
            items['selfChronicHepatitisB'] = 'false'
        if not('motherChronicHepatitisB' in list(items.keys())):
            items['motherChronicHepatitisB'] = 'false'
        if not('totalBilirubin' in list(items.keys())):
            items['totalBilirubin'] = 0
        if (items['totalBilirubin'] == ''):
            items['totalBilirubin'] = 0
        if not('AST' in list(items.keys())):
            items['AST'] = 0
        if (items['AST'] == ''):
            items['AST'] = 0
        if not('ALT' in list(items.keys())):
            items['ALT'] = 0
        if (items['ALT'] == ''):
            items['ALT'] = 0
        if not('albuminemia' in list(items.keys())):
            items['albuminemia'] = 0
        if (items['albuminemia'] == ''):
            items['albuminemia'] = 0
        if not('prothrombinTime' in list(items.keys())):
            items['prothrombinTime'] = 0
        if (items['prothrombinTime'] == ''):
            items['prothrombinTime'] = 0
        if not('IgM_anti_HAV' in list(items.keys())):
            items['IgM_anti_HAV'] = 'false'
        if not('IgG_anti_HAV' in list(items.keys())):
            items['IgG_anti_HAV'] = 'false'
        if not('HBsAg' in list(items.keys())):
            items['HBsAg'] = 'false'
        if not('HBeAg' in list(items.keys())):
            items['HBeAg'] = 'false'
        if not('Anti_HBe' in list(items.keys())):
            items['Anti_HBe'] = 'false'
        if not('IgM_anti_HBc' in list(items.keys())):
            items['IgM_anti_HBc'] = 'false'
        if not('IgG_anti_HBc' in list(items.keys())):
            items['IgG_anti_HBc'] = 'false'
        if not('HBV_DNA' in list(items.keys())):
            items['HBV_DNA'] = 'false'
        if not('Anti_HBs' in list(items.keys())):
            items['Anti_HBs'] = 'false'
        if not('Anti_HCV' in list(items.keys())):
            items['Anti_HCV'] = 'false'
        if not('HCV_RNA' in list(items.keys())):
            items['HCV_RNA'] = 'false'
        fatigue = items["fatigue"]
        jaundice = items["jaundice"]
        needle = items["needle"]
        arthritis = items["arthritis"]
        selfChronicHepatitisB = items["selfChronicHepatitisB"]
        motherChronicHepatitisB = items["motherChronicHepatitisB"]
        totalbilirubin = float(items["totalBilirubin"])
        albuminemia = items["albuminemia"]
        prothrombinTime = float(items["prothrombinTime"])
        AST = float(items["AST"])
        ALT = float(items["ALT"])
        IgM_anti_HAV = items["IgM_anti_HAV"]
        IgM_anti_HBc = items["IgM_anti_HBc"]
        Anti_HCV = items["Anti_HCV"]
        HCV_RNA = items["HCV_RNA"]
        HBsAg = items['HBsAg']
        HBeAg = items["HBeAg"]
        Anti_HBe = items["Anti_HBe"]
        if ((fatigue == "true") or (jaundice == "true") or (needle == "true") or (totalbilirubin > 1) or (AST > 40) or (ALT > 40) or (albuminemia < 3.8 or albuminemia > 4.8) or (prothrombinTime < 12.7 or prothrombinTime > 15.4)) and ((selfChronicHepatitisB == "true") or (motherChronicHepatitisB == "true")):
            result['특이사항'] = "증상과 혈액수치로 보아 간병변이 있고 본인 혹은 어머니가 만성 B형 간염 보균자이므로 만성 B형 간염 바이러스 감염으로 의심할 수 있다."
            if HBsAg == 'true':
                if ((0 < AST < 40) or (0 < ALT < 40)) and ((HBeAg == "true") and (Anti_HBe == "false")):
                    result['이유'] = "게다가 HBsAg 양성이므로 만성 B형 간염 바이러스 감염으로 확정짓고 stage를 알아보자. AST, ALT정상이고 (참고치 0 ~40) HBeAg 양성, Anti_HBe 음성이므로"
                    result['진단'] = "진단 : 만성 B형 간염 면역관용기"
                    if (AST > 80) or (ALT > 80):
                        result['이유'] = result['이유'] + "그리고 AST 또는 ALT값이 80이상일 경우"
                        result['치료'] = "치료 : 엔테카버 또는 테노포버 처방"
                elif ((AST > 40) or (ALT > 40)) and ((HBeAg == "true") and (Anti_HBe == "true")):
                    result['이유'] = "게다가 HBsAg 양성이므로 만성 B형 간염 바이러스 감염으로 확정짓고 stage를 알아보자. AST, ALT 상승했고 (참고치 0 ~40) HBeAg 양성, Anti_HBe 양성이므로"
                    result['진단'] = "진단 : 만성 B형 간염 면역반응기"
                    if (AST > 80) or (ALT > 80):
                        result['이유'] = result['이유'] + "AST 또는 ALT값이 80이상일 경우"
                        result['치료'] = "치료 : 엔테카버 또는 테노포버 처방"
                elif (HBeAg == "false") and (Anti_HBe == "true") :
                    result['이유'] = "게다가 HBsAg 양성이므로 만성 B형 간염 바이러스 감염으로 확정짓고 stage를 알아보자. HBeAg 음성, Anti_HBe 양성이므로"
                    result['진단'] = "진단 : 만성 B형 간염 비활동성"
                    if (AST > 80) or (ALT > 80):
                        result['이유'] = result['이유'] + "AST 또는 ALT값이 80이상일 경우"
                        result['치료'] = "치료 : 엔테카버 또는 테노포버 처방"
        if ((fatigue == "true") or (jaundice == "true") or (totalbilirubin > 1) or (AST > 40) or (ALT > 40) or (albuminemia < 3.8 or albuminemia > 4.8) or (prothrombinTime < 12.7 or prothrombinTime > 15.4)) and (needle == "true") :
            if (Anti_HCV == "true") or (HCV_RNA == "true"):
                result['이유'] = "증상과 혈액수치로 보아 간병변이 있고 주사 혹은 수혈받은 경력이 있기 때문에 만성 C형 간염으로 의심할 수 있다. Anti_HCV 또는 HCV_RNA가 양성이기 때문에"
                result['진단'] = "진단 : 만성 C형 간염"
                result['치료'] = "치료 : pegylated Inteferon + Ribavirin 처방. 최근에는 DAA( ~ vir) 병합투여도 많음"

######################################################################################

    elif items['val'] == 'valueThree':
        if not('fatigue' in list(items.keys())):
            items['fatigue'] = 'false'
        if not('nausea' in list(items.keys())):
            items['nausea'] = 'false'
        if not('abdominal pain' in list(items.keys())):
            items['abdominal pain'] = 'false'
        if not('jaundice' in list(items.keys())):
            items['jaundice'] = 'false'
        if not('alcohol' in list(items.keys())):
            items['alcohol'] = 'false'
        if not('totalBilirubin' in list(items.keys())):
            items['totalBilirubin'] = 0
        if (items['totalBilirubin'] == ''):
            items['totalBilirubin'] = 0
        if not('AST' in list(items.keys())):
            items['AST'] = 0
        if (items['AST'] == ''):
            items['AST'] = 0
        if not('ALT' in list(items.keys())):
            items['ALT'] = 0
        if (items['ALT'] == ''):
            items['ALT'] = 0
        if not('GGT' in list(items.keys())):
            items['GGT'] = 0
        if (items['GGT'] == ''):
            items['GGT'] = 0
        if not('prothrombinTime' in list(items.keys())):
            items['prothrombinTime'] = 0
        if (items['prothrombinTime'] == ''):
            items['prothrombinTime'] = 0
        #print('알코올성간질환 if문 실행')
        fatigue = items["fatigue"] 
        nausea = items["nausea"]
        abdominalpain = items["abdominal pain"]
        jaundice = items["jaundice"]
        totalbilirubin = float(items["totalBilirubin"]) 
        ast = float(items["AST"])
        alt = float(items["ALT"]) 
        prothrombinTime = float(items["prothrombinTime"])
        ggt = float(items["GGT"])
        alcohol = items["alcohol"]
        if ((fatigue == "true") or (nausea == "true") or (abdominalpain == "true") or (jaundice == "true") or (totalbilirubin > 1) or (ast > 40) or (alt > 40) or ((prothrombinTime < 12.7) or (prothrombinTime > 15.4)) or ((ggt < 11) or (ggt > 63))) and (alcohol == "true"):
            result['이유'] = "증상과 혈액수치로 보아 간병변이 있고 음주를 하고 있기 때문에"
            result['진단'] = "진단 : 알코올성 간질환"
            result['치료'] = "치료 : 금주가 가장 중요하고 프레드니솔론을 처방하기도 한다."

######################################################################################

    elif items['val'] == 'valueFour':
        #print('대사성알칼리즘 if문 실행')
        if not('HTN' in list(items.keys())):
            items['HTN'] = 'false'
        if not('PH' in list(items.keys())):
            items['PH'] = 0
        if (items['PH'] == ''):
            items['PH'] = 0
        if not('PaCO2' in list(items.keys())):
            items['PaCO2'] = 0
        if (items['PaCO2'] == ''):
            items['PaCO2'] = 0
        if not('PaO2' in list(items.keys())):
            items['PaO2'] = 0
        if (items['PaO2'] == ''):
            items['PaO2'] = 0
        if not('bloodHCO3Mi' in list(items.keys())):
            items['bloodHCO3Mi'] = 0
        if (items['bloodHCO3Mi'] == ''):
            items['bloodHCO3Mi'] = 0
        if not('bloodNaPl' in list(items.keys())):
            items['bloodNaPl'] = 0
        if (items['bloodNaPl'] == ''):
            items['bloodNaPl'] = 0
        if not('bloodKPl' in list(items.keys())):
            items['bloodKPl'] = 0
        if (items['bloodKPl'] == ''):
            items['bloodKPl'] = 0
        if not('bloodClMi' in list(items.keys())):
            items['bloodClMi'] = 0
        if (items['bloodClMi'] == ''):
            items['bloodClMi'] = 0
        if not('PeeNaPl' in list(items.keys())):
            items['PeeNaPl'] = 0
        if (items['PeeNaPl'] == ''):
            items['PeeNaPl'] = 0
        if not('PeeKPl' in list(items.keys())):
            items['PeeKPl'] = 0
        if (items['PeeKPl'] == ''):
            items['PeeKPl'] = 0
        if not('PeeClMi' in list(items.keys())):
            items['PeeClMi'] = 0
        if (items['PeeClMi'] == ''):
            items['PeeClMi'] = 0
        if not('PeeCr' in list(items.keys())):
            items['PeeCr'] = 0
        if (items['PeeCr'] == ''):
            items['PeeCr'] = 0
        if not('PeeCaPlPl' in list(items.keys())):
            items['PeeCaPlPl'] = 0
        if (items['PeeCaPlPl'] == ''):
            items['PeeCaPlPl'] = 0
        HTN = items["HTN"]
        PH = float(items["PH"])
        PaCO2 = float(items["PaCO2"])
        PaO2 = float(items["PaO2"])
        bloodHCO3Mi = float(items["bloodHCO3Mi"])
        bloodNaPl = float(items["bloodNaPl"])
        bloodKPl = float(items["bloodKPl"])
        bloodClMi = float(items["bloodClMi"])
        PeeNaPl = float(items["PeeNaPl"])
        PeeKPl = float(items["PeeKPl"])
        PeeClMi = float(items["PeeClMi"])
        PeeCr = float(items["PeeCr"])
        PeeCaPlPl = float(items["PeeCaPlPl"])
        if PH > 7.4:
            result['진단'] = "ph가 7.4이상이므로 일단 '대사알칼리증'을 의심해볼 수 있다."
            Npaco2 = 40 - 1.25*(24 - bloodHCO3Mi)
            if (Npaco2 - 2) < PaCO2 < (Npaco2 + 2):
                result['진단'] = result['진단'] + " 그리고 호흡성 보상작용은 정상적이다."
                if HTN == "true":
                    result['진단'] = result['진단'] + " 고혈압이 있기 때문에 '최종진단 : primary aldosteronism, cushing syndrome, liddle's syndrome'으로 추정할 수 있다."
                if HTN == "false":
                    if PeeClMi < 10:
                        result['진단'] = result['진단'] + " 소변 Cl-가 10보다 작으므로 '최종진단 : vomiting, NG suction'이다"
                    if PeeClMi > 20:
                        if (PeeCaPlPl/PeeCr) < 0.15:
                            result['진단'] = result['진단'] + " urine Ca/Cr이 0.15미만이므로 '최종진단 : gitelmans syndrome'이다"
                        if (PeeCaPlPl/PeeCr) > 2.0:
                            result['진단'] = result['진단'] + " urine Ca/Cr이 2.0이상이므로 '최종진단 : Bartter syndrome'이다"

######################################################################################

    elif items['val'] == 'valueFive':
        #print('대사성산증 if문 실행')
        if not('PH' in list(items.keys())):
            items['PH'] = 0
        if (items['PH'] == ''):
            items['PH'] = 0
        if not('PaCO2' in list(items.keys())):
            items['PaCO2'] = 0
        if (items['PaCO2'] == ''):
            items['PaCO2'] = 0
        if not('PaO2' in list(items.keys())):
            items['PaO2'] = 0
        if (items['PaO2'] == ''):
            items['PaO2'] = 0
        if not('bloodHCO3Mi' in list(items.keys())):
            items['bloodHCO3Mi'] = 0
        if (items['bloodHCO3Mi'] == ''):
            items['bloodHCO3Mi'] = 0
        if not('bloodNaPl' in list(items.keys())):
            items['bloodNaPl'] = 0
        if (items['bloodNaPl'] == ''):
            items['bloodNaPl'] = 0
        if not('bloodKPl' in list(items.keys())):
            items['bloodKPl'] = 0
        if (items['bloodKPl'] == ''):
            items['bloodKPl'] = 0
        if not('bloodClMi' in list(items.keys())):
            items['bloodClMi'] = 0
        if (items['bloodClMi'] == ''):
            items['bloodClMi'] = 0
        if not('PeeNaPl' in list(items.keys())):
            items['PeeNaPl'] = 0
        if (items['PeeNaPl'] == ''):
            items['PeeNaPl'] = 0
        if not('PeeKPl' in list(items.keys())):
            items['PeeKPl'] = 0
        if (items['PeeKPl'] == ''):
            items['PeeKPl'] = 0
        if not('PeeClMi' in list(items.keys())):
            items['PeeClMi'] = 0
        if (items['PeeClMi'] == ''):
            items['PeeClMi'] = 0
        PH = float(items["PH"])
        PaCO2 = float(items["PaCO2"])
        PaO2 = float(items["PaO2"])
        bloodHCO3Mi = float(items["bloodHCO3Mi"])
        bloodNaPl = float(items["bloodNaPl"])
        bloodKPl = float(items["bloodKPl"])
        bloodClMi = float(items["bloodClMi"])
        PeeNaPl = float(items["PeeNaPl"])
        PeeKPl = float(items["PeeKPl"])
        PeeClMi = float(items["PeeClMi"])
        if PH <7.4:
            Npaco2 = 40 - 1.25*(24 - bloodHCO3Mi)
            if (Npaco2 - 2) < PaCO2 < (Npaco2 + 2):
                AG = bloodNaPl - bloodHCO3Mi - bloodClMi
                if 10 <= AG <=14:
                    result['진단'] = "ph가 7.4미만이고 음이온차이가 정상(10-14)이므로 '진단 : 정상음이온차이대사산증'이다"
                    UAG = PeeNaPl + PeeKPl - PeeClMi
                    if UAG >0:
                        if bloodKPl < 3.5:
                            result['진단'] = result['진단'] + " 그리고 소변음이온차이가 0이상이고 혈역 K+가 3.5미만이므로 '최종진단 : type1 or type2 RTA'이다"
                            result['치료'] = "치료 : 기저질환을 치료하고 ph가 7.2미만일때는 중탄산염을 투여한다"
                        if bloodKPl > 5.5:
                            result['진단'] = result['진단'] + " 그리고 소변음이온차이가 0미만이고 혈액 K+가 5.5이상이므로 '최종진단 : type4 RTA'이다"
                            result['치료'] = "치료 : 기저질환을 치료하고 ph가 7.2미만일때는 중탄산염을 투여한다"
                    if UAG <0:
                        result['진단'] = result['진단'] + " 그리고 소변음이온차이가 0미만이므로 '최종진단 : 설사'이다"
                        result['치료'] = "치료 : 기저질환을 치료하고 ph가 7.2미만일때는 중탄산염을 투여한다"
                if AG >15:
                    result['진단'] = result['진단'] + " 음이온차이가 15이상이므로 Lactic acidosis, DKA, Alcoholic ketoacidosis, intoxication등을 의심해볼 수 있다."
                    dAG = abs(AG - 12)
                    dHCO3 = abs(bloodHCO3Mi - 24)
                    if (dAG/dHCO3) > 2:
                        result['진단'] = result['진단'] + " 그리고 (Δ음이온차이/Δ혈중중탄산염)이 2이상이므로 '최종진단 : 고음이온차이대사산증 + 대사알칼리증'이다"
                        result['치료'] = "치료 : 기저질환을 치료하고 ph가 7.2미만일때는 중탄산염을 투여한다"
                    if (dAG/dHCO3) < 1:
                        result['진단'] = result['진단'] + " 그리고 (Δ음이온차이/Δ혈중중탄산염)이 1미만이므로 '최종진단 : 고음이온차이대사산증 + 정상음이온대사산증'이다"
                        result['치료'] = "치료 : 기저질환을 치료하고 ph가 7.2미만일때는 중탄산염을 투여한다"
                    else:
                        result['진단'] = result['진단'] + " 그리고 (Δ음이온차이/Δ혈중중탄산염)이 (1 ~ 2)이므로 '최종진단 : 고음이온차이대사산증'이다"
                        result['치료'] = "치료 : 기저질환을 치료하고 ph가 7.2미만일때는 중탄산염을 투여한다"
            else:
                result['진단'] = "PaCO2 = " + str(PaCO2) + "이므로 보상이 적절히 이루어지지 않는 '대사성산증'이다"
    else :
        pass
#print('else문 실행')
#    print(items)
    return result