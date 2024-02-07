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


def lisa_voimalus(riik_pealinn: dict, voti_riik: str, voti_pealinn: str):

    if voti_riik not in riik_pealinn:
        riik_pealinn[voti_riik] = voti_pealinn
        print(f"Riik {voti_riik} pealinnaga {voti_pealinn} lisatud sõnastikus.")
    else:
        print(f"Error: riik {voti_riik} juba sõnastikus")


def paranda_viga(riik_pealinn: dict):

    riik = input("Sisestage selle riigi nimi, mille pealinna soovite muuta: ")
    if riik in riik_pealinn:
        vana_pealinn = riik_pealinn[riik]
        uus_pealinn = input(f"Sisestatud riik {riik} ja tema pealinn on {vana_pealinn}. Sisestage uus pealinn: ")
        riik_pealinn[riik] = uus_pealinn
        print(f"Riigil {riik} nüüd selline pealinn: {uus_pealinn}.")
    else:
        print(f"Error: {riik} ei ole sõnastikus.")


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
            uus_voti = input("Sisesta uus riik: ")
            uus_vaar = input("Sisesta uus pealinn: ")
            lisa_voimalus(riik_pealinn, uus_voti, uus_vaar)
            

        elif valik == "4":
            print("Valike mode:")
            print("1. Paranda viga")
            print("2. Välja")
    
            parandamise_reziim = input("Sisestage reziim (1 või 2): ")
    
            if parandamise_reziim == "1":
                paranda_viga(riik_pealinn)
            elif parandamise_reziim == "2":
                pass
            else:
                print("Error: vale mode.")


        elif valik == "5":
            kontrollimine(riik_pealinn, pealinn_riik, riigid)
            
        elif valik == "0":
            break

riik_2_pealinn(riik_pealinn, pealinn_riik, riigid)