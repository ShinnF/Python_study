def remove_punctuations(str_engsentences):
    str1 = str_engsentences.replace('.', '')
    str1 = str1.replace(',', '')
    str1 = str1.replace(':', '')
    str1 = str1.replace(';', '')
    str1 = str1.replace('!', '')
    str1 = str1.replace('?', '')
    return str1

print(remove_punctuations('Quiet, uh, donations, you want me to make a donation to, the coast guard youth auxiliary?') == ('Quiet uh donations you want me to make a donation to the coast guard youth auxiliary'))

def atgc_bppair(str_atgc):
    str2 = str_atgc.replace('A', 't')
    str2 = str2.replace('T', 'a')
    str2 = str2.replace('G', 'c')
    str2 = str2.replace('C', 'g')
    str2 = str2.upper()
    return str2
print(atgc_bppair('AAGCCCCATGGTAA') == 'TTCGGGGTACCATT')