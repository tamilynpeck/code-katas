from caesar_word_salad import caesar_word_salad

test_text = """
FtqDampZafFmwqz
NKDANQDFRDAEF

Fiadampepuhqdsqpuzmkqxxaiiaap,
MzpeaddkUoagxpzaffdmhqxnaft
Mzpnqazqfdmhqxqd,xazsUefaap
MzpxaawqppaizazqmermdmeUoagxp
Faitqdqufnqzfuzftqgzpqdsdaift;

Ftqzfaawftqaftqd,mevgefmermud,
Mzptmhuzsbqdtmbeftqnqffqdoxmuy,
Nqomgequfimesdmeekmzpimzfqpiqmd;
Ftagstmeradftmfftqbmeeuzsftqdq
Tmpiadzftqydqmxxkmnagfftqemyq,

Mzpnaftftmfyadzuzsqcgmxxkxmk
Uzxqmhqezaefqbtmpfdappqznxmow.
At,Uwqbfftqrudefradmzaftqdpmk!
Kqfwzaiuzstaiimkxqmpeazfaimk,
UpagnfqpurUetagxpqhqdoayqnmow.

Uetmxxnqfqxxuzsftueiuftmeust
Eayqitqdqmsqemzpmsqetqzoq:
Fiadampepuhqdsqpuzmiaap,mzpU—
Ufaawftqazqxqeefdmhqxqpnk,
Mzpftmftmeympqmxxftqpurrqdqzoq."""


def test_function():
    result = caesar_word_salad(test_text)

    assert result == ""
