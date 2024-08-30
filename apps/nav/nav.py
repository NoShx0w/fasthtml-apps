from fasthtml.common import *


hdrs = [StyleX('apps/nav/nav.css')]
app, rt = fast_app(hdrs=hdrs)

@rt("/")
def get():
    return Div(id='t1', cls='ct')(
        Div(id='t2', cls='ct')(
            Div(id='t3', cls='ct')(
                Div(id='t4', cls='ct')(
                    Section(
                        Ul(
                            A(href='#t1:/todo/')(
                                Li(id='uno', cls='icon fa fa-home')
                            ),
                            A(href='#t2:/h2f/')(
                                Li(id='dos', cls='icon fa fa-keyboard-o')
                            ),
                            A(href='#t3')(
                                Li(id='tres', cls='icon fa fa-coffee')
                            ),
                            A(href='#t4')(
                                Li(id='cuatro', cls='icon fa fa-dribbble')
                            )
                        ),
                        Div(id='p1', cls='page')(
                            Li(cls='icon fa fa-home')(
                                Span('Home', cls='title'),
                                Span(cls='hint')(
                                    'Like this pen to see the magic!...',
                                    Br(),
                                    "Just kidding, it won't happen anything but I'll be really happy If you do so."
                                )
                            )
                        ),
                        Div(id='p2', cls='page')(
                            Li(cls='icon fa fa-keyboard-o')(
                                Span('Type', cls='title')
                            )
                        ),
                        Div(id='p3', cls='page')(
                            Li(cls='icon fa fa-coffee')(
                                Span('Coffee', cls='title')
                            )
                        ),
                        Div(id='p4', cls='page')(
                            Li(cls='icon fa fa-dribbble')(
                                Span('Dribbble', cls='title'),
                                Span(cls='hint')(
                                    A('Follow me on Dribbble', href='https://dribbble.com/rupok', target='_blank')
                                )
                            )
                        ),
                        P(cls='credit')(
                            'Original Pen by',
                            A('Alberto Hartzet', href='https://codepen.io/hrtzt/')
                        )
                    )
                )
            )
        )
    )
