using System.Linq;

public class Mine
{
    public static string COPPER = "copper";
    public static string SILVER = "silver";
    public static string GOLD = "gold";
    public static string PLATINUM = "platinum";
    public static string[] PRECIOUS = new[] { COPPER, SILVER, GOLD, PLATINUM };
    public static string[] Ore =
    {
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
    };
    public static void MineOre()
    {
        Console.WriteLine("Ore Item Count: {0}", Mine.Ore.Length);
        var test = Mine.PRECIOUS.Select(x => Mine.Ore.Select(y => OreContainsMetal(y, x)).ToList()).ToList();
        var minedOres = Mine.Ore.Select(x => OreContainsAnyMetal(x)).ToList();
        var results = minedOres.GroupBy(x => x).ToDictionary(x => x.Key, x => x.Count());

        foreach (var metal in PRECIOUS)
        {
            Console.WriteLine("{0}: {1}", metal, results[metal]);
        }
        Console.WriteLine("empty: {0}", results[String.Empty]);
    }

    public static string OreContainsMetal(string ore, string metal)
    {
        var letters = metal.ToCharArray();
        var check = letters.Select(x => ore.Contains(x)).ToList();
        return check.Any(x => !x) ? string.Empty : metal;
    }

    public static string OreContainsMetal2(string ore, string metal)
    {
        var intersect = metal.Where(x=>ore.Contains(x)).ToList();
        var match = string.Join("", intersect);
        var check = match.Equals(metal);
        return check ? metal : string.Empty;
    }

    public static string OreContainsAnyMetal(string ore)
    {
        var test = PRECIOUS.Select(x => OreContainsMetal2(ore, x)).Where(x => !string.IsNullOrEmpty(x)).ToList();
        if (test.Any())
            return test.First();
        return string.Empty;
    }
}
