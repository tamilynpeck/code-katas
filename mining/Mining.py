class Mine:
    COPPER = "copper"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"
    PRECIOUS = {COPPER, SILVER, GOLD, PLATINUM}

    Ore = {
        "zexewjilxhbekrkerzkxjqobrooloxerbylwzbirplewfjjyyr",
        "lyhilfzwrhhhfwxqjrbhoiypqqhffvsiefkerryffxkhhjebwz",
        "jxrjlibyhhpoelzpkhzboypobykxioelbqqfzrpeijykbwzfzl",
        "yikpowhjbbykfohjjoboijfbhzebqkpibfbxqwxkehleoqlofk",
        "whzzqrorjxikhzyyeyofqlpyhfewyijxjpjhbffyqibpizzbxf",
        "yhpltlbxranbkzifrheirimllbwirfiyobjyibyhzrzyjeyiou",
        "ofpppyzfeffwceplflewrwofhlzhkrboiplrrfqbpbqobxrbzl",
        "bflipibphffoyqqfrxbbrljblywyyiizrkxepkeblzlfwwelop",
        "ywryylzzxrlyjerzojbjflxhzrrqljzlklorpfprfqwwbqpflb",
        "zyzeyblwfwrpzqxiiykkrpfhlsxqizrjwrkvbhfhlxzeefrrbe",
        "lpqbpheiyjporpjehypozizqypwfokhpxjjowbzxhxhlxpiqwh",
        "ylbjloyixlwefrhirxhhewhwrheqziyklqkbeehehlifzyxlqe",
        "oqjwzijbchziexrljpyqxwzkfizybyywekhpbjexkpfpfjkqep",
        "owwpkfrzerzkfeizixezzhepprhfolpwkxelkihjriplikqehl",
        "zfywxhjezorzijzzqpopwxkbifreqbbkryjxlpwfwfeoxhpofq",
        "qrfixkpiqofweizhepbwrhrlrhzzihoqyorjrerelbyikzpowx",
        "xlfqbrgbrbizrfxqyifhyirljpopjjwrdkohezrbopyqzqoqly",
        "zqkqibypfbzzkybkeoobolwxfbfxwohiiiexyirpkezxilkzwh",
        "breohkbiwlzoopoofhlbepfebjobeepeqbbjrhhpoyrwzewjco",
        "qwreyljqjkqbwirjqlilkyfipilxbypyqiljqxriibhfbqpixx",
        "zbeokqrpplxqppjhhxwzczihqkzheqqobjrlyewbwbekebybpi",
        "hwxtefiqiojayikuqrwhwknzehwwlblmoopbekeplxrzixoybf",
        "ibbwooarlfwxflkheqzzpxbeilrpwfytfehqlwwmohnqowxoyu",
        "jfbwqirqhhjlrollwbhfjhkbyrzbqqljryofiypgjwepxwfdkl",
        "kylxqhhbjhjbzlqqprjhweyjpljoowhyxyqjxfzbhpbxewkzxz",
        "yooqllqgjjpxjjiphypwxxrrbfyjjkilelfldbojoxolbxqofh",
        "hkpiqrijhqolbbpejizxwkbwwlqriieryxepyohlkxkqkzxyze",
        "beipzkiqxroixpkherqleriiserqzqjblxoblqxvebifkihejl",
        "niwokqehryxqrjhebaoxptwiiokplizyfkbilzkeiyubmqozpj",
        "xhxjkzetjypqbkyyrphbpkmalnoohrwhflwwbhpbpwulowiqqe",
    }


def MineOre():
    print(f"Ore Item Count: {len(Mine.Ore)}")
    precious_counts = {k: 0 for k in Mine.PRECIOUS}
    for (i, ore_chunk) in enumerate(Mine.Ore):
        oreCount = 0
        for metal in Mine.PRECIOUS:
            if all([letter in ore_chunk for letter in metal]):
                oreCount += 1
                precious_counts[metal] += 1

        print(f"Ore Chunk {i} has {oreCount} precious metals")

    for metal in precious_counts:
        print(f"{metal}: {precious_counts[metal]}")
    print(f"empty: {len(Mine.Ore) - sum(precious_counts.values())}")


MineOre()
