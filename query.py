#!/usr/bin/python3

__description__ = 'CLI to look up color details'
__author__ = 'Adhiraj Sirohi'
__version__ = '0.1'

import os
import urllib.request
import requests
import json

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *

CONST_API_URL = ('http://thecolorapi.com/id?')

def help():
    print("ColorQuery is a simple cli tool written to give quick and small details about colors\n")
    print("You can either enter a HEX code or a RGB Value\n")
    print('''Details returned include:
                - HEX / RGB value
                - HSL values
                - HSV values
                - CMYK values
                - Name of closest named color and it's HEX value
             ''')
    exit()

def enter_hex():
   os.system('clear')

   print("Enter HEX Code (without #): ")
   hex_input = input()
   
   print("\nFetching details for %s ....\n" % hex_input)

   with urllib.request.urlopen(CONST_API_URL+"hex="+hex_input) as url:
       result = json.loads(url.read().decode())

       rgb_r = result['rgb']['r']
       rgb_g = result['rgb']['g']
       rgb_b = result['rgb']['b']

       hsl_h = result['hsl']['h']
       hsl_s = result['hsl']['s']
       hsl_l = result['hsl']['l']

       hsv_h = result['hsv']['h']
       hsv_s = result['hsv']['s']
       hsv_v = result['hsv']['v']

       cmyk_c = result['cmyk']['c']
       cmyk_y = result['cmyk']['m']
       cmyk_m = result['cmyk']['y']
       cmyk_k = result['cmyk']['k']

       name = result['name']['value']
       closest_hex = result['name']['closest_named_hex']

       print("RGB Values: \033[31m%s\033[0m \033[32m%s\033[0m \033[34m%s\033[0m \n" % (rgb_r, rgb_g, rgb_b))
       
       printing(hsl_h, hsl_s, hsl_l, hsv_h, hsv_s, hsv_v, cmyk_c, cmyk_m, cmyk_y, cmyk_k, name, closest_hex)

       exit()

def enter_rgb():
   os.system('clear')

   rgb_input = input("Enter RGB Values (seperated by comma):")
   
   print("\nFetching details for %s ....\n" %  rgb_input)

   with urllib.request.urlopen(CONST_API_URL+"rgb=rgb("+rgb_input+")") as url:
      result = json.loads(url.read().decode())

      hex_value = result['hex']['value']

      hsl_h = result['hsl']['h']
      hsl_s = result['hsl']['s']
      hsl_l = result['hsl']['l']

      hsv_h = result['hsv']['h']
      hsv_s = result['hsv']['s']
      hsv_v = result['hsv']['v']
       
      cmyk_c = result['cmyk']['c']
      cmyk_y = result['cmyk']['m']
      cmyk_m = result['cmyk']['y']
      cmyk_k = result['cmyk']['k']

      name = result['name']['value']
      closest_hex = result['name']['closest_named_hex']
       
      print("HEX Code:   %s \n" % hex_value)
      printing(hsl_h, hsl_s, hsl_l, hsv_h, hsv_s, hsv_v, cmyk_c, cmyk_m, cmyk_y, cmyk_k, name, closest_hex)

      exit()

def printing(hsl_h, hsl_s, hsl_l, hsv_h, hsv_s, hsv_v, cmyk_c, cmyk_m, cmyk_y, cmyk_kv, name, closest_hex):
    print("HSL Values: %s %s %s \n" % (hsl_h, hsl_s, hsl_l))

   # print ('\033[91m' + 'Red' + '\033[0m')
      
    print("HSV Values: %s %s %s \n" % (hsv_h, hsv_s, hsv_v))

    print("CMYK Value: \033[96m%s\033[0m \033[93m%s\033[0m \033[95m%s\033[0m  \033[30m%s\033[0m \n" % (cmyk_c, cmyk_m, cmyk_y, cmyk_kv))
       
    print("\nClosest named color is %s and it's HEX Code is %s" % (name, closest_hex))


def menu_create():
    format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER) \
            .set_prompt("Choice->") \
            .set_title_align('center') \
            .set_subtitle_align('center') \
            .set_right_margin(2) \
            .set_left_margin(2) \
            .show_header_bottom_border(True)

    menu = ConsoleMenu("ColorQuery", "A simple CLI tool to help you look up details about colors", formatter=format)
    
    hex_input = FunctionItem("To enter a HEX Code", enter_hex)
    rgb_input = FunctionItem("To enter  a RGB Code", enter_rgb)
    help_func = FunctionItem("To display the help section", help)

    menu.append_item(hex_input)
    menu.append_item(rgb_input)
    menu.append_item(help_func)
    
    menu.show()

def main():
    os.system('clear')
    menu_create()

if __name__ == "__main__":
    main()

