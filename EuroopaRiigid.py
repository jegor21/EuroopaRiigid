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


def riik_2_pealinn(riik_pealinn:dict,pealinn_riik:dict,riigid:list):
    riik=""
    while (riik != " ") or (pealinn != " "):
        riik=input("Riik: ")
        if riik != " ":
            print(riik_pealinn[riik])

        pealinn=input("Pealinn: ")
        if pealinn != " ":
            print(pealinn_riik[riik])





