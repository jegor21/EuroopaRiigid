from random import *
def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    file=open(f,'r',encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid

riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnad.txt")


def lisa_voimalus(sona: dict, voti: str, vaar: str):
    if voti not in sona:
        sona[voti] = vaar
        print(f"{voti} lisatud sõnastikku.")
    else:
        print(f"{voti} on juba sõnastikus.")

def paranda_viga(sona: dict, voti: str, uus_vaar: str):
    if voti in sona:
        sona[voti] = uus_vaar
        print(f"{voti} on parandatud. Uus väärtus: {uus_vaar}.")
    else:
        print(f"{voti} ei leitud sõnastikust.")

def kontrollimine(riik_pealinn: dict, pealinn_riik: dict, riigid: list):
    shuffle(riigid)
    õiged_vastused = 0
    küsimuste_arv = min(10, len(riigid))  
    for riik in riigid[:küsimuste_arv]:
        vastus = input(f"Pealinn riigis {riik}: ")
        õige_pealinn = riik_pealinn[riik]
        if vastus.lower() == õige_pealinn.lower():
            print("Õige!")
            õiged_vastused += 1
        else:
            print(f"Vale! Õige vastus: {õige_pealinn}")
    protsent = (õiged_vastused / küsimuste_arv) * 100
    print(f"\nKontrolli tulemus: {protsent}% õigeid vastuseid.")

riik_pealinn, pealinn_riik, riigid = failist_to_dict("riigid_pealinnad.txt")

def riik_2_pealinn(riik_pealinn: dict, pealinn_riik: dict, riigid: list):
    while True:
        print("\n1. Näita pealinna riigi järgi")
        print("2. Näita riiki pealinna järgi")
        print("3. Lisa uus sõna sõnastikku")
        print("4. Paranda viga sõnastikus")
        print("5. Kontrollimine(kokku 10 küsimusi)")
        print("0. Välju")
        
        valik = input("\nVali tegevus (0-5): ")
        
        if valik == "1":
            riik = input("Sisesta riik: ")
            if riik in riik_pealinn:
                print(f"Pealinn: {riik_pealinn[riik]}")
            else:
                print("Sellist riiki ei leitud.")
                
        elif valik == "2":
            pealinn = input("Sisesta pealinn: ")
            if pealinn in pealinn_riik:
                print(f"Riik: {pealinn_riik[pealinn]}")
            else:
                print("Sellist pealinna ei leitud.")
                
        elif valik == "3":
            uus_voti = input("Sisesta uus riik või pealinn: ")
            uus_vaar = input("Sisesta sellele vastav pealinn või riik: ")
            lisa_voimalus(riik_pealinn, uus_voti, uus_vaar)
            
        elif valik == "4":
            vigane_sõna = input("Sisesta vigane riik või pealinn: ")
            uus_vaar = input("Sisesta uus pealinn või riik: ")
            paranda_viga(riik_pealinn, vigane_sõna, uus_vaar)
            paranda_viga(pealinn_riik, vigane_sõna, uus_vaar)
            
        elif valik == "5":
            kontrollimine(riik_pealinn, pealinn_riik, riigid)
            
        elif valik == "0":
            break

riik_2_pealinn(riik_pealinn, pealinn_riik, riigid)