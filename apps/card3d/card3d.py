from fasthtml.common import *

hdrs = [Style('''* { box-sizing: border-box; }
    html, body { width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; }
    body { 
        font-family: 'Arial Black', 'Arial Bold', Gadget, sans-serif;
        perspective: 1500px; background: linear-gradient(#666, #222);
    }''')]

app,rt = fast_app(hdrs=hdrs)
# Based on surreal.js version: https://gist.github.com/gnat/f094e947b3a785e1ed6b7def979132ae
# ...which is based on this web component: https://github.com/zachleat/hypercard
# ...which is from this version: https://codepen.io/markmiro/pen/wbqMPa

def card_3d(text, background, amt=1., left_align=False, **kw):
    scr = ScriptX('apps/card3d/card3d.js', amt=amt)
    align='left' if left_align else 'right'
    sty = StyleX('apps/card3d/card3d.css', background=f'url({background})', align=align)
    return Div(text, Div(), sty, scr, **kw)


def _card_bg(path):
    return f"url('https://tekeye.uk/playing_cards/images/svg_playing_cards/{path}.svg') center/cover"


def playing_card(suit, rank):
    "Create a flippable playing card component for any card"
    front = _card_bg(f'fronts/{suit}_{rank}')
    back = _card_bg('backs/blue2')
    return Div(
        Div(cls="front"), Div(cls="back"),
        StyleX('apps/card3d/playingcard.css', front=front, back=back),
        Script("me().on('click', ev => me(ev).classToggle('flipped'))"),
        cls="playing-card")


@rt('/')
def get():
    #url1 = "https://preview.redd.it/33i841e92m151.jpg?width=312&format=pjpg&auto=webp&s=142139f7b76f923636bc540d7ee10072323b1cf1"
    url1 = "https://product-images.s3.cardmarket.com/1/BLB/778436/778436.jpg"
    url2 = "https://ucarecdn.com/35a0e8a7-fcc5-48af-8a3f-70bb96ff5c48/-/preview/750x1000/"
    cards = [playing_card(*o) for o in [('clubs','jack'), ('hearts','queen'), ('spades','king')]]

    return Div(
        Div(card_3d('FastHTML', url1, 1.5, hx_get='/click'),
            card_3d('Components!', url2, 1.5, left_align=True, hx_get='/click')),
        Div(*cards),
        id="page-content"
    )


@rt('/click')
def get(): return P('Clicked!')
