"""
Template for embedding font files into CSS files:
    You can modify as needed just make sure that
    you have place holders for for where the data
    will be embedded
"""

CSS_TEMPLATE = """\
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: normal;
    font-weight: 400;
    src: url(data:font/ttf;charset-utf-8;base64,{regular});
}}
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: normal;
    font-weight: 700;
    src: url(data:font/ttf;charset-utf-8;base64,{bold});
}}
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: italic;
    font-weight: 400;
    src: url(data:font/ttf;charset-utf-8;base64,{italic});
}}
@font-face {{
    font-family: "{name} Nerd Font";
    font-style: italic;
    font-weight: 700;
    src: url(data:font/ttf;charset-utf-8;base64,{bold_italic});
}}
"""
