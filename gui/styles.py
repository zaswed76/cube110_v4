#!/usr/bin/env python
# -*- coding: utf-8 -*-

border_view_color = '#b6b6b6'
border_style = 'solid'
border_size = '1px'
border_size_default = '0px'
background_color = "white"
background_color_toot_but = "green"
radius = "1em"

options = dict(size=border_size,
               style=border_style,
               color=border_view_color,
               bg=background_color,
               rad=radius,
               size_def = border_size_default,
               bg_tool_but=background_color_toot_but)

left_display_css = """
    QGraphicsView {{
    border-right: {size} {style} {color};
    border-left: {size} {style} {color};
    border-top: {size} {style} {color};
    border-bottom: {size} {style} {color};
    background-color: {bg};
    border-top-left-radius: {rad}
     }}
     """.format(**options)

default_display_css = """
    QGraphicsView {{
    border-right: {size_def} {style} {color};
    border-left: {size_def} {style} {color};
    border-top: {size_def} {style} {color};
    border-bottom: 1px {style} {color};
    background-color: {bg};
     }}
     """.format(**options)

right_display_css = """
    QGraphicsView {{
    border-right: {size} {style} {color};
    border-left: none;
    border-top: {size} {style} {color};
    border-bottom: {size} {style} {color};
    background-color: {bg};
    border-top-right-radius: {rad}
     }}
     """.format(**options)

tool_css = """
    QFrame {{
    border-right: {size} {style} {color};
    border-left: None;
    border-top: none;
    border-bottom: {size} {style} {color};
    background-color: {bg};
     }}
     """.format(**options)

tool_button_css = """
    QPushButton {{
    background-color: {bg};
    border-right: none;
    border-left: {size} {style} {color};
    border-top: none;
    border-bottom: None;
     }}
     """.format(**options)
