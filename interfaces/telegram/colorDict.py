#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Color dict
"""
# Dictionary of colornames indexed by key _Hex:
# See https://bdhacker.wordpress.com/2010/02/27/python-tutorial-dictionaries-key-value-pair-maps-basics/
HexNameDict = { \
 "black":"#000000" \
,"gray0":"#000000" \
,"navy":"#000080" \
,"NavyBlue":"#000080" \
,"blue4":"#00008B" \
,"DarkBlue":"#00008B" \
,"MediumBlue":"#0000CD" \
,"blue3":"#0000CD" \
,"blue2":"#0000EE" \
,"blue":"#0000FF" \
,"blue1":"#0000FF" \
,"DarkGreen":"#006400" \
,"DeepSkyBlue4":"#00688B" \
,"WebGreen":"#008000" \
,"green":"#008000" \
,"teal":"#008080" \
,"turquoise4":"#00868B" \
,"green4":"#008B00" \
,"SpringGreen4":"#008B45" \
,"cyan4":"#008B8B" \
,"DarkCyan":"#008B8B" \
,"DeepSkyBlue3":"#009ACD" \
,"DeepSkyBlue2":"#00B2EE" \
,"DeepSkyBlue":"#00BFFF" \
,"DeepSkyBlue1":"#00BFFF" \
,"turquoise3":"#00C5CD" \
,"green3":"#00CD00" \
,"SpringGreen3":"#00CD66" \
,"cyan3":"#00CDCD" \
,"DarkTurquoise":"#00CED1" \
,"turquoise2":"#00E5EE" \
,"green2":"#00EE00" \
,"SpringGreen2":"#00EE76" \
,"cyan2":"#00EEEE" \
,"turquoise1":"#00F5FF" \
,"MediumSpringGreen":"#00FA9A" \
,"lime":"#00FF00" \
,"green":"#00FF00" \
,"green1":"#00FF00" \
,"X11Green":"#00FF00" \
,"SpringGreen":"#00FF7F" \
,"SpringGreen1":"#00FF7F" \
,"cyan1":"#00FFFF" \
,"aqua":"#00FFFF" \
,"cyan":"#00FFFF" \
,"gray40":"#026666" \
,"gray1":"#030303" \
,"gray2":"#050505" \
,"gray3":"#080808" \
,"gray4":"#0A0A0A" \
,"gray5":"#0D0D0D" \
,"gray6":"#0F0F0F" \
,"DodgerBlue4":"#104E8B" \
,"gray7":"#121212" \
,"gray8":"#141414" \
,"gray9":"#171717" \
,"DodgerBlue3":"#1874CD" \
,"MidnightBlue":"#191970" \
,"gray10":"#1A1A1A" \
,"gray11":"#1C1C1C" \
,"DodgerBlue2":"#1C86EE" \
,"DodgerBlue":"#1E90FF" \
,"DodgerBlue1":"#1E90FF" \
,"gray12":"#1F1F1F" \
,"LightSeaGreen":"#20B2AA" \
,"gray13":"#212121" \
,"ForestGreen":"#228B22" \
,"gray14":"#242424" \
,"gray15":"#262626" \
,"RoyalBlue4":"#27408B" \
,"gray16":"#292929" \
,"gray17":"#2B2B2B" \
,"gray18":"#2E2E2E" \
,"SeaGreen":"#2E8B57" \
,"SeaGreen4":"#2E8B57" \
,"DarkSlateGray":"#2F4F4F" \
,"gray19":"#303030" \
,"LimeGreen":"#32CD32" \
,"gray20":"#333333" \
,"gray21":"#363636" \
,"SteelBlue4":"#36648B" \
,"gray22":"#383838" \
,"RoyalBlue3":"#3A5FCD" \
,"gray23":"#3B3B3B" \
,"MediumSeaGreen":"#3CB371" \
,"gray24":"#3D3D3D" \
,"gray25":"#404040" \
,"turquoise":"#40E0D0" \
,"RoyalBlue":"#4169E1" \
,"gray26":"#424242" \
,"RoyalBlue2":"#436EEE" \
,"SeaGreen3":"#43CD80" \
,"gray27":"#454545" \
,"chartreuse4":"#458B00" \
,"aquamarine4":"#458B74" \
,"SteelBlue":"#4682B4" \
,"SlateBlue4":"#473C8B" \
,"gray28":"#474747" \
,"DarkSlateBlue":"#483D8B" \
,"RoyalBlue1":"#4876FF" \
,"MediumTurquoise":"#48D1CC" \
,"gray29":"#4A4A4A" \
,"SkyBlue4":"#4A708B" \
,"indigo":"#4B0082" \
,"gray30":"#4D4D4D" \
,"SeaGreen2":"#4EEE94" \
,"gray31":"#4F4F4F" \
,"SteelBlue3":"#4F94CD" \
,"gray32":"#525252" \
,"DarkSlateGray4":"#528B8B" \
,"CadetBlue4":"#53868B" \
,"gray33":"#545454" \
,"PaleGreen4":"#548B54" \
,"SeaGreen1":"#54FF9F" \
,"purple4":"#551A8B" \
,"DarkOliveGreen":"#556B2F" \
,"gray34":"#575757" \
,"gray35":"#595959" \
,"gray36":"#5C5C5C" \
,"SteelBlue2":"#5CACEE" \
,"MediumPurple4":"#5D478B" \
,"gray37":"#5E5E5E" \
,"CadetBlue":"#5F9EA0" \
,"LightSkyBlue4":"#607B8B" \
,"gray38":"#616161" \
,"gray39":"#636363" \
,"SteelBlue1":"#63B8FF" \
,"CornflowerBlue":"#6495ED" \
,"RebeccaPurple":"#663399" \
,"PaleTurquoise4":"#668B8B" \
,"chartreuse3":"#66CD00" \
,"MediumAquamarine":"#66CDAA" \
,"aquamarine3":"#66CDAA" \
,"DarkOrchid4":"#68228B" \
,"LightBlue4":"#68838B" \
,"SlateBlue3":"#6959CD" \
,"DimGray":"#696969" \
,"gray41":"#696969" \
,"OliveDrab4":"#698B22" \
,"DarkSeaGreen4":"#698B69" \
,"SlateBlue":"#6A5ACD" \
,"gray42":"#6B6B6B" \
,"OliveDrab":"#6B8E23" \
,"SlateGray4":"#6C7B8B" \
,"SkyBlue3":"#6CA6CD" \
,"gray43":"#6E6E6E" \
,"LightSteelBlue4":"#6E7B8B" \
,"DarkOliveGreen4":"#6E8B3D" \
,"gray44":"#707070" \
,"SlateGray":"#708090" \
,"gray45":"#737373" \
,"gray46":"#757575" \
,"chartreuse2":"#76EE00" \
,"aquamarine2":"#76EEC6" \
,"LightSlateGray":"#778899" \
,"gray47":"#787878" \
,"DarkSlateGray3":"#79CDCD" \
,"MediumOrchid4":"#7A378B" \
,"SlateBlue2":"#7A67EE" \
,"gray48":"#7A7A7A" \
,"LightCyan4":"#7A8B8B" \
,"CadetBlue3":"#7AC5CD" \
,"MediumSlateBlue":"#7B68EE" \
,"PaleGreen3":"#7CCD7C" \
,"LawnGreen":"#7CFC00" \
,"purple3":"#7D26CD" \
,"gray49":"#7D7D7D" \
,"SkyBlue2":"#7EC0EE" \
,"gray50":"#7F7F7F" \
,"chartreuse":"#7FFF00" \
,"chartreuse1":"#7FFF00" \
,"aquamarine":"#7FFFD4" \
,"aquamarine1":"#7FFFD4" \
,"WebMaroon":"#800000" \
,"maroon":"#800000" \
,"WebPurple":"#800080" \
,"purple":"#800080" \
,"olive":"#808000" \
,"WebGray":"#808080" \
,"gray":"#808080" \
,"gray51":"#828282" \
,"SlateBlue1":"#836FFF" \
,"honeydew4":"#838B83" \
,"azure4":"#838B8B" \
,"LightSlateBlue":"#8470FF" \
,"gray52":"#858585" \
,"gray53":"#878787" \
,"SkyBlue":"#87CEEB" \
,"LightSkyBlue":"#87CEFA" \
,"SkyBlue1":"#87CEFF" \
,"MediumPurple3":"#8968CD" \
,"BlueViolet":"#8A2BE2" \
,"gray54":"#8A8A8A" \
,"DarkRed":"#8B0000" \
,"red4":"#8B0000" \
,"DarkMagenta":"#8B008B" \
,"magenta4":"#8B008B" \
,"DeepPink4":"#8B0A50" \
,"firebrick4":"#8B1A1A" \
,"maroon4":"#8B1C62" \
,"VioletRed4":"#8B2252" \
,"brown4":"#8B2323" \
,"OrangeRed4":"#8B2500" \
,"tomato4":"#8B3626" \
,"IndianRed4":"#8B3A3A" \
,"HotPink4":"#8B3A62" \
,"coral4":"#8B3E2F" \
,"DarkOrange4":"#8B4500" \
,"SaddleBrown":"#8B4513" \
,"chocolate4":"#8B4513" \
,"sienna4":"#8B4726" \
,"PaleVioletRed4":"#8B475D" \
,"orchid4":"#8B4789" \
,"salmon4":"#8B4C39" \
,"LightSalmon4":"#8B5742" \
,"orange4":"#8B5A00" \
,"tan4":"#8B5A2B" \
,"LightPink4":"#8B5F65" \
,"pink4":"#8B636C" \
,"DarkGoldenrod4":"#8B6508" \
,"plum4":"#8B668B" \
,"goldenrod4":"#8B6914" \
,"RosyBrown4":"#8B6969" \
,"burlywood4":"#8B7355" \
,"gold4":"#8B7500" \
,"PeachPuff4":"#8B7765" \
,"NavajoWhite4":"#8B795E" \
,"thistle4":"#8B7B8B" \
,"bisque4":"#8B7D6B" \
,"MistyRose4":"#8B7D7B" \
,"wheat4":"#8B7E66" \
,"LightGoldenrod4":"#8B814C" \
,"AntiqueWhite4":"#8B8378" \
,"LavenderBlush4":"#8B8386" \
,"khaki4":"#8B864E" \
,"seashell4":"#8B8682" \
,"cornsilk4":"#8B8878" \
,"LemonChiffon4":"#8B8970" \
,"snow4":"#8B8989" \
,"yellow4":"#8B8B00" \
,"LightYellow4":"#8B8B7A" \
,"ivory4":"#8B8B83" \
,"gray55":"#8C8C8C" \
,"LightSkyBlue3":"#8DB6CD" \
,"DarkSlateGray2":"#8DEEEE" \
,"CadetBlue2":"#8EE5EE" \
,"gray56":"#8F8F8F" \
,"DarkSeaGreen":"#8FBC8F" \
,"LightGreen":"#90EE90" \
,"PaleGreen2":"#90EE90" \
,"purple2":"#912CEE" \
,"gray57":"#919191" \
,"MediumPurple":"#9370DB" \
,"DarkViolet":"#9400D3" \
,"gray58":"#949494" \
,"gray59":"#969696" \
,"PaleTurquoise3":"#96CDCD" \
,"DarkSlateGray1":"#97FFFF" \
,"CadetBlue1":"#98F5FF" \
,"PaleGreen":"#98FB98" \
,"DarkOrchid":"#9932CC" \
,"gray60":"#999999" \
,"DarkOrchid3":"#9A32CD" \
,"LightBlue3":"#9AC0CD" \
,"YellowGreen":"#9ACD32" \
,"OliveDrab3":"#9ACD32" \
,"PaleGreen1":"#9AFF9A" \
,"purple1":"#9B30FF" \
,"DarkSeaGreen3":"#9BCD9B" \
,"gray61":"#9C9C9C" \
,"gray62":"#9E9E9E" \
,"MediumPurple2":"#9F79EE" \
,"SlateGray3":"#9FB6CD" \
,"purple":"#A020F0" \
,"X11Purple":"#A020F0" \
,"sienna":"#A0522D" \
,"gray63":"#A1A1A1" \
,"LightSteelBlue3":"#A2B5CD" \
,"DarkOliveGreen3":"#A2CD5A" \
,"gray64":"#A3A3A3" \
,"LightSkyBlue2":"#A4D3EE" \
,"brown":"#A52A2A" \
,"gray65":"#A6A6A6" \
,"gray66":"#A8A8A8" \
,"DarkGray":"#A9A9A9" \
,"MediumPurple1":"#AB82FF" \
,"gray67":"#ABABAB" \
,"gray68":"#ADADAD" \
,"LightBlue":"#ADD8E6" \
,"GreenYellow":"#ADFF2F" \
,"PaleTurquoise2":"#AEEEEE" \
,"PaleTurquoise":"#AFEEEE" \
,"maroon":"#B03060" \
,"X11Maroon":"#B03060" \
,"gray69":"#B0B0B0" \
,"LightSteelBlue":"#B0C4DE" \
,"PowderBlue":"#B0E0E6" \
,"LightSkyBlue1":"#B0E2FF" \
,"firebrick":"#B22222" \
,"DarkOrchid2":"#B23AEE" \
,"LightBlue2":"#B2DFEE" \
,"gray70":"#B3B3B3" \
,"OliveDrab2":"#B3EE3A" \
,"MediumOrchid3":"#B452CD" \
,"LightCyan3":"#B4CDCD" \
,"DarkSeaGreen2":"#B4EEB4" \
,"gray71":"#B5B5B5" \
,"DarkGoldenrod":"#B8860B" \
,"gray72":"#B8B8B8" \
,"SlateGray2":"#B9D3EE" \
,"MediumOrchid":"#BA55D3" \
,"gray73":"#BABABA" \
,"PaleTurquoise1":"#BBFFFF" \
,"RosyBrown":"#BC8F8F" \
,"LightSteelBlue2":"#BCD2EE" \
,"DarkOliveGreen2":"#BCEE68" \
,"DarkKhaki":"#BDB76B" \
,"gray74":"#BDBDBD" \
,"gray":"#BEBEBE" \
,"X11Gray":"#BEBEBE" \
,"DarkOrchid1":"#BF3EFF" \
,"gray75":"#BFBFBF" \
,"LightBlue1":"#BFEFFF" \
,"silver":"#C0C0C0" \
,"OliveDrab1":"#C0FF3E" \
,"honeydew3":"#C1CDC1" \
,"azure3":"#C1CDCD" \
,"DarkSeaGreen1":"#C1FFC1" \
,"gray76":"#C2C2C2" \
,"gray77":"#C4C4C4" \
,"SlateGray1":"#C6E2FF" \
,"MediumVioletRed":"#C71585" \
,"gray78":"#C7C7C7" \
,"gray79":"#C9C9C9" \
,"LightSteelBlue1":"#CAE1FF" \
,"DarkOliveGreen1":"#CAFF70" \
,"gray80":"#CCCCCC" \
,"red3":"#CD0000" \
,"magenta3":"#CD00CD" \
,"DeepPink3":"#CD1076" \
,"firebrick3":"#CD2626" \
,"maroon3":"#CD2990" \
,"VioletRed3":"#CD3278" \
,"brown3":"#CD3333" \
,"OrangeRed3":"#CD3700" \
,"tomato3":"#CD4F39" \
,"IndianRed3":"#CD5555" \
,"coral3":"#CD5B45" \
,"IndianRed":"#CD5C5C" \
,"HotPink3":"#CD6090" \
,"DarkOrange3":"#CD6600" \
,"chocolate3":"#CD661D" \
,"sienna3":"#CD6839" \
,"PaleVioletRed3":"#CD6889" \
,"orchid3":"#CD69C9" \
,"salmon3":"#CD7054" \
,"LightSalmon3":"#CD8162" \
,"orange3":"#CD8500" \
,"peru":"#CD853F" \
,"tan3":"#CD853F" \
,"LightPink3":"#CD8C95" \
,"pink3":"#CD919E" \
,"DarkGoldenrod3":"#CD950C" \
,"plum3":"#CD96CD" \
,"goldenrod3":"#CD9B1D" \
,"RosyBrown3":"#CD9B9B" \
,"burlywood3":"#CDAA7D" \
,"gold3":"#CDAD00" \
,"PeachPuff3":"#CDAF95" \
,"NavajoWhite3":"#CDB38B" \
,"thistle3":"#CDB5CD" \
,"bisque3":"#CDB79E" \
,"MistyRose3":"#CDB7B5" \
,"wheat3":"#CDBA96" \
,"LightGoldenrod3":"#CDBE70" \
,"AntiqueWhite3":"#CDC0B0" \
,"LavenderBlush3":"#CDC1C5" \
,"seashell3":"#CDC5BF" \
,"khaki3":"#CDC673" \
,"cornsilk3":"#CDC8B1" \
,"LemonChiffon3":"#CDC9A5" \
,"snow3":"#CDC9C9" \
,"yellow3":"#CDCD00" \
,"LightYellow3":"#CDCDB4" \
,"ivory3":"#CDCDC1" \
,"gray81":"#CFCFCF" \
,"VioletRed":"#D02090" \
,"MediumOrchid2":"#D15FEE" \
,"gray82":"#D1D1D1" \
,"LightCyan2":"#D1EEEE" \
,"chocolate":"#D2691E" \
,"tan":"#D2B48C" \
,"LightGray":"#D3D3D3" \
,"gray83":"#D4D4D4" \
,"gray84":"#D6D6D6" \
,"thistle":"#D8BFD8" \
,"gray85":"#D9D9D9" \
,"orchid":"#DA70D6" \
,"goldenrod":"#DAA520" \
,"PaleVioletRed":"#DB7093" \
,"gray86":"#DBDBDB" \
,"crimson":"#DC143C" \
,"gainsboro":"#DCDCDC" \
,"plum":"#DDA0DD" \
,"burlywood":"#DEB887" \
,"gray87":"#DEDEDE" \
,"MediumOrchid1":"#E066FF" \
,"gray88":"#E0E0E0" \
,"honeydew2":"#E0EEE0" \
,"azure2":"#E0EEEE" \
,"LightCyan":"#E0FFFF" \
,"LightCyan1":"#E0FFFF" \
,"gray89":"#E3E3E3" \
,"gray90":"#E5E5E5" \
,"lavender":"#E6E6FA" \
,"gray91":"#E8E8E8" \
,"DarkSalmon":"#E9967A" \
,"gray92":"#EBEBEB" \
,"gray93":"#EDEDED" \
,"red2":"#EE0000" \
,"magenta2":"#EE00EE" \
,"DeepPink2":"#EE1289" \
,"firebrick2":"#EE2C2C" \
,"maroon2":"#EE30A7" \
,"VioletRed2":"#EE3A8C" \
,"brown2":"#EE3B3B" \
,"OrangeRed2":"#EE4000" \
,"tomato2":"#EE5C42" \
,"IndianRed2":"#EE6363" \
,"coral2":"#EE6A50" \
,"HotPink2":"#EE6AA7" \
,"DarkOrange2":"#EE7600" \
,"chocolate2":"#EE7621" \
,"sienna2":"#EE7942" \
,"PaleVioletRed2":"#EE799F" \
,"orchid2":"#EE7AE9" \
,"salmon2":"#EE8262" \
,"violet":"#EE82EE" \
,"LightSalmon2":"#EE9572" \
,"orange2":"#EE9A00" \
,"tan2":"#EE9A49" \
,"LightPink2":"#EEA2AD" \
,"pink2":"#EEA9B8" \
,"DarkGoldenrod2":"#EEAD0E" \
,"plum2":"#EEAEEE" \
,"goldenrod2":"#EEB422" \
,"RosyBrown2":"#EEB4B4" \
,"burlywood2":"#EEC591" \
,"gold2":"#EEC900" \
,"PeachPuff2":"#EECBAD" \
,"NavajoWhite2":"#EECFA1" \
,"thistle2":"#EED2EE" \
,"bisque2":"#EED5B7" \
,"MistyRose2":"#EED5D2" \
,"wheat2":"#EED8AE" \
,"LightGoldenrod2":"#EEDC82" \
,"LightGoldenrod":"#EEDD82" \
,"AntiqueWhite2":"#EEDFCC" \
,"LavenderBlush2":"#EEE0E5" \
,"seashell2":"#EEE5DE" \
,"khaki2":"#EEE685" \
,"PaleGoldenrod":"#EEE8AA" \
,"cornsilk2":"#EEE8CD" \
,"LemonChiffon2":"#EEE9BF" \
,"snow2":"#EEE9E9" \
,"yellow2":"#EEEE00" \
,"LightYellow2":"#EEEED1" \
,"ivory2":"#EEEEE0" \
,"LightCoral":"#F08080" \
,"khaki":"#F0E68C" \
,"gray94":"#F0F0F0" \
,"AliceBlue":"#F0F8FF" \
,"honeydew":"#F0FFF0" \
,"honeydew1":"#F0FFF0" \
,"azure":"#F0FFFF" \
,"azure1":"#F0FFFF" \
,"gray95":"#F2F2F2" \
,"SandyBrown":"#F4A460" \
,"wheat":"#F5DEB3" \
,"beige":"#F5F5DC" \
,"WhiteSmoke":"#F5F5F5" \
,"gray96":"#F5F5F5" \
,"MintCream":"#F5FFFA" \
,"gray97":"#F7F7F7" \
,"GhostWhite":"#F8F8FF" \
,"salmon":"#FA8072" \
,"AntiqueWhite":"#FAEBD7" \
,"linen":"#FAF0E6" \
,"LightGoldenrodYellow":"#FAFAD2" \
,"gray98":"#FAFAFA" \
,"gray99":"#FCFCFC" \
,"OldLace":"#FDF5E6" \
,"red":"#FF0000" \
,"red1":"#FF0000" \
,"magenta1":"#FF00FF" \
,"fuchsia":"#FF00FF" \
,"magenta":"#FF00FF" \
,"DeepPink":"#FF1493" \
,"DeepPink1":"#FF1493" \
,"firebrick1":"#FF3030" \
,"maroon1":"#FF34B3" \
,"VioletRed1":"#FF3E96" \
,"brown1":"#FF4040" \
,"OrangeRed":"#FF4500" \
,"OrangeRed1":"#FF4500" \
,"tomato":"#FF6347" \
,"tomato1":"#FF6347" \
,"HotPink":"#FF69B4" \
,"IndianRed1":"#FF6A6A" \
,"HotPink1":"#FF6EB4" \
,"coral1":"#FF7256" \
,"DarkOrange1":"#FF7F00" \
,"chocolate1":"#FF7F24" \
,"coral":"#FF7F50" \
,"sienna1":"#FF8247" \
,"PaleVioletRed1":"#FF82AB" \
,"orchid1":"#FF83FA" \
,"DarkOrange":"#FF8C00" \
,"salmon1":"#FF8C69" \
,"LightSalmon":"#FFA07A" \
,"LightSalmon1":"#FFA07A" \
,"orange":"#FFA500" \
,"orange1":"#FFA500" \
,"tan1":"#FFA54F" \
,"LightPink1":"#FFAEB9" \
,"pink1":"#FFB5C5" \
,"LightPink":"#FFB6C1" \
,"DarkGoldenrod1":"#FFB90F" \
,"plum1":"#FFBBFF" \
,"pink":"#FFC0CB" \
,"goldenrod1":"#FFC125" \
,"RosyBrown1":"#FFC1C1" \
,"burlywood1":"#FFD39B" \
,"gold":"#FFD700" \
,"gold1":"#FFD700" \
,"PeachPuff":"#FFDAB9" \
,"PeachPuff1":"#FFDAB9" \
,"NavajoWhite":"#FFDEAD" \
,"NavajoWhite1":"#FFDEAD" \
,"thistle1":"#FFE1FF" \
,"moccasin":"#FFE4B5" \
,"bisque":"#FFE4C4" \
,"bisque1":"#FFE4C4" \
,"MistyRose":"#FFE4E1" \
,"MistyRose1":"#FFE4E1" \
,"wheat1":"#FFE7BA" \
,"BlanchedAlmond":"#FFEBCD" \
,"LightGoldenrod1":"#FFEC8B" \
,"PapayaWhip":"#FFEFD5" \
,"AntiqueWhite1":"#FFEFDB" \
,"LavenderBlush":"#FFF0F5" \
,"LavenderBlush1":"#FFF0F5" \
,"seashell":"#FFF5EE" \
,"seashell1":"#FFF5EE" \
,"khaki1":"#FFF68F" \
,"cornsilk":"#FFF8DC" \
,"cornsilk1":"#FFF8DC" \
,"LemonChiffon":"#FFFACD" \
,"LemonChiffon1":"#FFFACD" \
,"FloralWhite":"#FFFAF0" \
,"snow":"#FFFAFA" \
,"snow1":"#FFFAFA" \
,"yellow":"#FFFF00" \
,"yellow1":"#FFFF00" \
,"LightYellow":"#FFFFE0" \
,"LightYellow1":"#FFFFE0" \
,"ivory":"#FFFFF0" \
,"ivory1":"#FFFFF0" \
,"white":"#FFFFFF" \
,"gray100":"#FFFFFF" \
}
