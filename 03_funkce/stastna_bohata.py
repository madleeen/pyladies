stastna_retezec = input("Jsi stastna? (ano/ne):")
if stastna_retezec == "ano":
    stastna = True;
elif stastna_retezec == "ne":
    stastna = False;
else:
    print ("Nerozumim.")

bohata_retezec = input("Jsi bohata? (ano/ne):")
if bohata_retezec == "ano":
    bohata = True;
elif bohata_retezec == "ne":
    bohata = False;
else:
    print ("Nerozumim.")


if bohata and stastna:
    print ("Jsi stastna i bohata! Gratuluju!")
elif bohata:
    print ("Alespon jsi bohata! Stesti prijde casem...")
elif stastna:
    print ("Alespon jsi stastna! Penize nejsou dulezite..")
else:
    print ("To je mi lito :(")

print ("Bohata:",bohata)
print ("stastna:",stastna)
