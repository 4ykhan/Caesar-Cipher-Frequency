cipher = 'IHRB VMMLYZ HAAYHJAPVUZ MVY LCLYFIVKF: ZBUUF ILHJOLZ WYVCPKL H WYPTL ZWVA AV BUDPUK, DOPSL LSLNHUA AOLHALYZ HUK XBPYRF TBZLBTZ DPSS ZHAPZMF AOL JBSABYLK AVBYPZA. TVKLYU HYJOPALJABYL JYLHALZ HU VAOLYDVYSKSF JVUAYHZA DPAO VSK JPAF XBHYALYZ, DOPSL ILHBAPMBSSF KLZPNULK WHYRZ WYVCPKL AOL WLYMLJA WSHJL AV BUDPUK PU H ZLYLUL LUCPYVU.  AYLUKF JHMLZ HUK UPNOAZ JSBIZ HAAYHJA FVBUN WLVWSL, HUK KLSPJPVBZ JBPZPUL DPSS ZHAPZMF AHZAL IBKZ VM LCLYF AFWL. AOL JPAF VMMLYZ KVGLUZ VM WLKLZAYPHU-MYPLUKSF ZAYLLAZ HUK LUALYAHPUTLUA JLUALYZ MVY AOL JVTMVYA VM PAZ YLZPKLUAZ HUK CPZPAVYZ. UV THAALY FVBY HNL VY ZWOLYL VM PUALYLZA, IHRB’Z KPCLYZPAF HUK MLZAPCL CPIL HYL OHYK AV YLZPZA.JVTL LUJVBUALY AOPZ JPAF VM DPUK HUK MSHTLZ, DOLYL LHZALYU HUK DLZALYU JBSABYL TLSKZ PUAV VUL, DPAO VBY IHRB AYHCLS NBPKL.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_letter_count(message):
    """Returns a dictionary with keys of single letters and values of the
    count of how many times they appear in the message parameter."""
    letter_count = {}
    for letter in message.upper():  # Uniform letters to uppercase
        if letter in [' ', ',', '.']:
            continue
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    return letter_count


def get_most_frequent_letter(message):
    """Return the most frequent letter in the given message dictionary"""
    most_freq_value = 0
    most_freq_index = None
    for letter in message:
        if message[letter] >= most_freq_value:
            most_freq_value = message[letter]
            most_freq_index = letter
    return most_freq_index, most_freq_value

plaintext = ''

letter_count = get_letter_count(cipher)
print(letter_count)

most_frequent_letter = get_most_frequent_letter(letter_count)
print(most_frequent_letter)

e_position = LETTERS.index('E')
m_position = LETTERS.index(most_frequent_letter[0])
key = m_position - e_position

if key < 0:
    key = key + len(LETTERS)
print (key)

for symbol in cipher:
    try:
        position = LETTERS.index(symbol)
        position = position - key
        if position < 0:
            position = position + len(LETTERS)
        plaintext = plaintext + LETTERS[position]
    except:
        plaintext = plaintext + symbol

print(plaintext)