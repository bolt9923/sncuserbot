import random

fonts = [
    "𝓐𝓑𝓒𝓓𝓔𝓕𝓖",
    "𝔸𝔹ℂ𝔻𝔼𝔽𝔾",
    "ＡＢＣＤＥＦＧ",
    "𝐀𝐁𝐂𝐃𝐄𝐅𝐆",
    "𝘈𝘉𝘊𝘋𝘌𝘍𝘎",
    "𝙰𝙱𝙲𝙳𝙴𝙵𝙶",
]

def style_text(text):
    font = random.choice(fonts)

    styled = ""
    for i, ch in enumerate(text):
        if ch.isalpha():
            try:
                styled += chr(ord(font[i % len(font)]))
            except:
                styled += ch
        else:
            styled += ch

    return styled
