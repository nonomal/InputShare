from enum import IntEnum

SDL_BUTTON = lambda X: 1 << ((X)-1)
SDL_BUTTON_LEFT   =   1
SDL_BUTTON_MIDDLE =   2
SDL_BUTTON_RIGHT  =   3
SDL_BUTTON_X1     =   4
SDL_BUTTON_X2     =   5

# --- --- --- --- --- ---

'''
SDL Keyboard Definition
'''

SDLK_SCANCODE_MASK = 1<<30
SDL_SCANCODE_TO_KEYCODE = lambda X: X | SDLK_SCANCODE_MASK

class SDL_KeyCode(IntEnum):
    SDLK_UNKNOWN = 0
    SDLK_RETURN = ord('\r')
    SDLK_ESCAPE = ord('\033')
    SDLK_BACKSPACE = ord('\b')
    SDLK_TAB = ord('\t')
    SDLK_SPACE = ord(' ')
    SDLK_EXCLAIM = ord('!')
    SDLK_QUOTEDBL = ord('"')
    SDLK_HASH = ord('#')
    SDLK_PERCENT = ord('%')
    SDLK_DOLLAR = ord('$')
    SDLK_AMPERSAND = ord('&')
    SDLK_QUOTE = ord('\'')
    SDLK_LEFTPAREN = ord('(')
    SDLK_RIGHTPAREN = ord(')')
    SDLK_ASTERISK = ord('*')
    SDLK_PLUS = ord('+')
    SDLK_COMMA = ord(',')
    SDLK_MINUS = ord('-')
    SDLK_PERIOD = ord('.')
    SDLK_SLASH = ord('/')
    SDLK_0 = ord('0')
    SDLK_1 = ord('1')
    SDLK_2 = ord('2')
    SDLK_3 = ord('3')
    SDLK_4 = ord('4')
    SDLK_5 = ord('5')
    SDLK_6 = ord('6')
    SDLK_7 = ord('7')
    SDLK_8 = ord('8')
    SDLK_9 = ord('9')
    SDLK_COLON = ord(':')
    SDLK_SEMICOLON = ord(';')
    SDLK_LESS = ord('<')
    SDLK_EQUALS = ord('=')
    SDLK_GREATER = ord('>')
    SDLK_QUESTION = ord('?')
    SDLK_AT = ord('@')

    '''
    Skip uppercase letters
    '''

    SDLK_LEFTBRACKET = ord('[')
    SDLK_BACKSLASH = ord('\\')
    SDLK_RIGHTBRACKET = ord(']')
    SDLK_CARET = ord('^')
    SDLK_UNDERSCORE = ord('_')
    SDLK_BACKQUOTE = ord('`')
    SDLK_a = ord('a')
    SDLK_b = ord('b')
    SDLK_c = ord('c')
    SDLK_d = ord('d')
    SDLK_e = ord('e')
    SDLK_f = ord('f')
    SDLK_g = ord('g')
    SDLK_h = ord('h')
    SDLK_i = ord('i')
    SDLK_j = ord('j')
    SDLK_k = ord('k')
    SDLK_l = ord('l')
    SDLK_m = ord('m')
    SDLK_n = ord('n')
    SDLK_o = ord('o')
    SDLK_p = ord('p')
    SDLK_q = ord('q')
    SDLK_r = ord('r')
    SDLK_s = ord('s')
    SDLK_t = ord('t')
    SDLK_u = ord('u')
    SDLK_v = ord('v')
    SDLK_w = ord('w')
    SDLK_x = ord('x')
    SDLK_y = ord('y')
    SDLK_z = ord('z')

    # Scancode-masked keys
    SDLK_CAPSLOCK = SDL_SCANCODE_TO_KEYCODE(57)
    SDLK_F1 = SDL_SCANCODE_TO_KEYCODE(58)
    SDLK_F2 = SDL_SCANCODE_TO_KEYCODE(59)
    SDLK_F3 = SDL_SCANCODE_TO_KEYCODE(60)
    SDLK_F4 = SDL_SCANCODE_TO_KEYCODE(61)
    SDLK_F5 = SDL_SCANCODE_TO_KEYCODE(62)
    SDLK_F6 = SDL_SCANCODE_TO_KEYCODE(63)
    SDLK_F7 = SDL_SCANCODE_TO_KEYCODE(64)
    SDLK_F8 = SDL_SCANCODE_TO_KEYCODE(65)
    SDLK_F9 = SDL_SCANCODE_TO_KEYCODE(66)
    SDLK_F10 = SDL_SCANCODE_TO_KEYCODE(67)
    SDLK_F11 = SDL_SCANCODE_TO_KEYCODE(68)
    SDLK_F12 = SDL_SCANCODE_TO_KEYCODE(69)

    SDLK_PRINTSCREEN = SDL_SCANCODE_TO_KEYCODE(70)
    SDLK_SCROLLLOCK = SDL_SCANCODE_TO_KEYCODE(71)
    SDLK_PAUSE = SDL_SCANCODE_TO_KEYCODE(72)
    SDLK_INSERT = SDL_SCANCODE_TO_KEYCODE(73)
    SDLK_HOME = SDL_SCANCODE_TO_KEYCODE(74)
    SDLK_PAGEUP = SDL_SCANCODE_TO_KEYCODE(75)
    SDLK_DELETE = ord('\177')
    SDLK_END = SDL_SCANCODE_TO_KEYCODE(77)
    SDLK_PAGEDOWN = SDL_SCANCODE_TO_KEYCODE(78)
    SDLK_RIGHT = SDL_SCANCODE_TO_KEYCODE(79)
    SDLK_LEFT = SDL_SCANCODE_TO_KEYCODE(80)
    SDLK_DOWN = SDL_SCANCODE_TO_KEYCODE(81)
    SDLK_UP = SDL_SCANCODE_TO_KEYCODE(82)

    SDLK_NUMLOCKCLEAR = SDL_SCANCODE_TO_KEYCODE(83)
    SDLK_KP_DIVIDE = SDL_SCANCODE_TO_KEYCODE(84)
    SDLK_KP_MULTIPLY = SDL_SCANCODE_TO_KEYCODE(85)
    SDLK_KP_MINUS = SDL_SCANCODE_TO_KEYCODE(86)
    SDLK_KP_PLUS = SDL_SCANCODE_TO_KEYCODE(87)
    SDLK_KP_ENTER = SDL_SCANCODE_TO_KEYCODE(88)
    SDLK_KP_1 = SDL_SCANCODE_TO_KEYCODE(89)
    SDLK_KP_2 = SDL_SCANCODE_TO_KEYCODE(90)
    SDLK_KP_3 = SDL_SCANCODE_TO_KEYCODE(91)
    SDLK_KP_4 = SDL_SCANCODE_TO_KEYCODE(92)
    SDLK_KP_5 = SDL_SCANCODE_TO_KEYCODE(93)
    SDLK_KP_6 = SDL_SCANCODE_TO_KEYCODE(94)
    SDLK_KP_7 = SDL_SCANCODE_TO_KEYCODE(95)
    SDLK_KP_8 = SDL_SCANCODE_TO_KEYCODE(96)
    SDLK_KP_9 = SDL_SCANCODE_TO_KEYCODE(97)
    SDLK_KP_0 = SDL_SCANCODE_TO_KEYCODE(98)
    SDLK_KP_PERIOD = SDL_SCANCODE_TO_KEYCODE(99)

    SDLK_APPLICATION = SDL_SCANCODE_TO_KEYCODE(101)
    SDLK_POWER = SDL_SCANCODE_TO_KEYCODE(102)
    SDLK_KP_EQUALS = SDL_SCANCODE_TO_KEYCODE(103)
    SDLK_F13 = SDL_SCANCODE_TO_KEYCODE(104)
    SDLK_F14 = SDL_SCANCODE_TO_KEYCODE(105)
    SDLK_F15 = SDL_SCANCODE_TO_KEYCODE(106)
    SDLK_F16 = SDL_SCANCODE_TO_KEYCODE(107)
    SDLK_F17 = SDL_SCANCODE_TO_KEYCODE(108)
    SDLK_F18 = SDL_SCANCODE_TO_KEYCODE(109)
    SDLK_F19 = SDL_SCANCODE_TO_KEYCODE(110)
    SDLK_F20 = SDL_SCANCODE_TO_KEYCODE(111)
    SDLK_F21 = SDL_SCANCODE_TO_KEYCODE(112)
    SDLK_F22 = SDL_SCANCODE_TO_KEYCODE(113)
    SDLK_F23 = SDL_SCANCODE_TO_KEYCODE(114)
    SDLK_F24 = SDL_SCANCODE_TO_KEYCODE(115)
    SDLK_EXECUTE = SDL_SCANCODE_TO_KEYCODE(116)
    SDLK_HELP = SDL_SCANCODE_TO_KEYCODE(117)
    SDLK_MENU = SDL_SCANCODE_TO_KEYCODE(118)
    SDLK_SELECT = SDL_SCANCODE_TO_KEYCODE(119)
    SDLK_STOP = SDL_SCANCODE_TO_KEYCODE(120)
    SDLK_AGAIN = SDL_SCANCODE_TO_KEYCODE(121)
    SDLK_UNDO = SDL_SCANCODE_TO_KEYCODE(122)
    SDLK_CUT = SDL_SCANCODE_TO_KEYCODE(123)
    SDLK_COPY = SDL_SCANCODE_TO_KEYCODE(124)
    SDLK_PASTE = SDL_SCANCODE_TO_KEYCODE(125)
    SDLK_FIND = SDL_SCANCODE_TO_KEYCODE(126)
    SDLK_MUTE = SDL_SCANCODE_TO_KEYCODE(127)
    SDLK_VOLUMEUP = SDL_SCANCODE_TO_KEYCODE(128)
    SDLK_VOLUMEDOWN = SDL_SCANCODE_TO_KEYCODE(129)

    # Additional scancode mappings
    SDLK_KP_COMMA = SDL_SCANCODE_TO_KEYCODE(133)
    SDLK_KP_EQUALSAS400 = SDL_SCANCODE_TO_KEYCODE(134)
    SDLK_ALTERASE = SDL_SCANCODE_TO_KEYCODE(153)
    SDLK_SYSREQ = SDL_SCANCODE_TO_KEYCODE(154)
    SDLK_CANCEL = SDL_SCANCODE_TO_KEYCODE(155)
    SDLK_CLEAR = SDL_SCANCODE_TO_KEYCODE(156)
    SDLK_PRIOR = SDL_SCANCODE_TO_KEYCODE(157)
    SDLK_RETURN2 = SDL_SCANCODE_TO_KEYCODE(158)
    SDLK_SEPARATOR = SDL_SCANCODE_TO_KEYCODE(159)
    SDLK_OUT = SDL_SCANCODE_TO_KEYCODE(160)
    SDLK_OPER = SDL_SCANCODE_TO_KEYCODE(161)
    SDLK_CLEARAGAIN = SDL_SCANCODE_TO_KEYCODE(162)
    SDLK_CRSEL = SDL_SCANCODE_TO_KEYCODE(163)
    SDLK_EXSEL = SDL_SCANCODE_TO_KEYCODE(164)

    SDLK_KP_00 = SDL_SCANCODE_TO_KEYCODE(176)
    SDLK_KP_000 = SDL_SCANCODE_TO_KEYCODE(177)
    SDLK_THOUSANDSSEPARATOR = SDL_SCANCODE_TO_KEYCODE(178)
    SDLK_DECIMALSEPARATOR = SDL_SCANCODE_TO_KEYCODE(179)
    SDLK_CURRENCYUNIT = SDL_SCANCODE_TO_KEYCODE(180)
    SDLK_CURRENCYSUBUNIT = SDL_SCANCODE_TO_KEYCODE(181)
    SDLK_KP_LEFTPAREN = SDL_SCANCODE_TO_KEYCODE(182)
    SDLK_KP_RIGHTPAREN = SDL_SCANCODE_TO_KEYCODE(183)
    SDLK_KP_LEFTBRACE = SDL_SCANCODE_TO_KEYCODE(184)
    SDLK_KP_RIGHTBRACE = SDL_SCANCODE_TO_KEYCODE(185)
    SDLK_KP_TAB = SDL_SCANCODE_TO_KEYCODE(186)
    SDLK_KP_BACKSPACE = SDL_SCANCODE_TO_KEYCODE(187)
    SDLK_KP_A = SDL_SCANCODE_TO_KEYCODE(188)
    SDLK_KP_B = SDL_SCANCODE_TO_KEYCODE(189)
    SDLK_KP_C = SDL_SCANCODE_TO_KEYCODE(190)
    SDLK_KP_D = SDL_SCANCODE_TO_KEYCODE(191)
    SDLK_KP_E = SDL_SCANCODE_TO_KEYCODE(192)
    SDLK_KP_F = SDL_SCANCODE_TO_KEYCODE(193)
    SDLK_KP_XOR = SDL_SCANCODE_TO_KEYCODE(194)
    SDLK_KP_POWER = SDL_SCANCODE_TO_KEYCODE(195)
    SDLK_KP_PERCENT = SDL_SCANCODE_TO_KEYCODE(196)
    SDLK_KP_LESS = SDL_SCANCODE_TO_KEYCODE(197)
    SDLK_KP_GREATER = SDL_SCANCODE_TO_KEYCODE(198)
    SDLK_KP_AMPERSAND = SDL_SCANCODE_TO_KEYCODE(199)
    SDLK_KP_DBLAMPERSAND = SDL_SCANCODE_TO_KEYCODE(200)
    SDLK_KP_VERTICALBAR = SDL_SCANCODE_TO_KEYCODE(201)
    SDLK_KP_DBLVERTICALBAR = SDL_SCANCODE_TO_KEYCODE(202)
    SDLK_KP_COLON = SDL_SCANCODE_TO_KEYCODE(203)
    SDLK_KP_HASH = SDL_SCANCODE_TO_KEYCODE(204)
    SDLK_KP_SPACE = SDL_SCANCODE_TO_KEYCODE(205)
    SDLK_KP_AT = SDL_SCANCODE_TO_KEYCODE(206)
    SDLK_KP_EXCLAM = SDL_SCANCODE_TO_KEYCODE(207)

    # More media and special keys
    SDLK_AUDIOREWIND = SDL_SCANCODE_TO_KEYCODE(285)
    SDLK_AUDIOFASTFORWARD = SDL_SCANCODE_TO_KEYCODE(286)

class SDL_Keymod(IntEnum):
    KMOD_NONE = 0x0000
    KMOD_LSHIFT = 0x0001
    KMOD_RSHIFT = 0x0002
    KMOD_LCTRL = 0x0040
    KMOD_RCTRL = 0x0080
    KMOD_LALT = 0x0100
    KMOD_RALT = 0x0200
    KMOD_LGUI = 0x0400
    KMOD_RGUI = 0x0800
    KMOD_NUM = 0x1000
    KMOD_CAPS = 0x2000
    KMOD_MODE = 0x4000
    KMOD_RESERVED = 0x8000

    # Combined keys
    KMOD_CTRL = KMOD_LCTRL | KMOD_RCTRL
    KMOD_SHIFT = KMOD_LSHIFT | KMOD_RSHIFT
    KMOD_ALT = KMOD_LALT | KMOD_RALT
    KMOD_GUI = KMOD_LGUI | KMOD_RGUI

class SDL_Scancode(IntEnum):
    SDL_SCANCODE_UNKNOWN = 0

    SDL_SCANCODE_A = 4
    SDL_SCANCODE_B = 5
    SDL_SCANCODE_C = 6
    SDL_SCANCODE_D = 7
    SDL_SCANCODE_E = 8
    SDL_SCANCODE_F = 9
    SDL_SCANCODE_G = 10
    SDL_SCANCODE_H = 11
    SDL_SCANCODE_I = 12
    SDL_SCANCODE_J = 13
    SDL_SCANCODE_K = 14
    SDL_SCANCODE_L = 15
    SDL_SCANCODE_M = 16
    SDL_SCANCODE_N = 17
    SDL_SCANCODE_O = 18
    SDL_SCANCODE_P = 19
    SDL_SCANCODE_Q = 20
    SDL_SCANCODE_R = 21
    SDL_SCANCODE_S = 22
    SDL_SCANCODE_T = 23
    SDL_SCANCODE_U = 24
    SDL_SCANCODE_V = 25
    SDL_SCANCODE_W = 26
    SDL_SCANCODE_X = 27
    SDL_SCANCODE_Y = 28
    SDL_SCANCODE_Z = 29

    SDL_SCANCODE_1 = 30
    SDL_SCANCODE_2 = 31
    SDL_SCANCODE_3 = 32
    SDL_SCANCODE_4 = 33
    SDL_SCANCODE_5 = 34
    SDL_SCANCODE_6 = 35
    SDL_SCANCODE_7 = 36
    SDL_SCANCODE_8 = 37
    SDL_SCANCODE_9 = 38
    SDL_SCANCODE_0 = 39

    SDL_SCANCODE_RETURN = 40
    SDL_SCANCODE_ESCAPE = 41
    SDL_SCANCODE_BACKSPACE = 42
    SDL_SCANCODE_TAB = 43
    SDL_SCANCODE_SPACE = 44

    SDL_SCANCODE_MINUS = 45
    SDL_SCANCODE_EQUALS = 46
    SDL_SCANCODE_LEFTBRACKET = 47
    SDL_SCANCODE_RIGHTBRACKET = 48
    SDL_SCANCODE_BACKSLASH = 49
    SDL_SCANCODE_NONUSHASH = 50
    SDL_SCANCODE_SEMICOLON = 51
    SDL_SCANCODE_APOSTROPHE = 52
    SDL_SCANCODE_GRAVE = 53 
    SDL_SCANCODE_COMMA = 54
    SDL_SCANCODE_PERIOD = 55
    SDL_SCANCODE_SLASH = 56
    SDL_SCANCODE_CAPSLOCK = 57
    SDL_SCANCODE_F1 = 58
    SDL_SCANCODE_F2 = 59
    SDL_SCANCODE_F3 = 60
    SDL_SCANCODE_F4 = 61
    SDL_SCANCODE_F5 = 62
    SDL_SCANCODE_F6 = 63
    SDL_SCANCODE_F7 = 64
    SDL_SCANCODE_F8 = 65
    SDL_SCANCODE_F9 = 66
    SDL_SCANCODE_F10 = 67
    SDL_SCANCODE_F11 = 68
    SDL_SCANCODE_F12 = 69

    SDL_SCANCODE_PRINTSCREEN = 70
    SDL_SCANCODE_SCROLLLOCK = 71
    SDL_SCANCODE_PAUSE = 72
    SDL_SCANCODE_INSERT = 73
    SDL_SCANCODE_HOME = 74
    SDL_SCANCODE_PAGEUP = 75
    SDL_SCANCODE_DELETE = 76
    SDL_SCANCODE_END = 77
    SDL_SCANCODE_PAGEDOWN = 78
    SDL_SCANCODE_RIGHT = 79
    SDL_SCANCODE_LEFT = 80
    SDL_SCANCODE_DOWN = 81
    SDL_SCANCODE_UP = 82

    SDL_SCANCODE_NUMLOCKCLEAR = 83
    SDL_SCANCODE_KP_DIVIDE = 84
    SDL_SCANCODE_KP_MULTIPLY = 85
    SDL_SCANCODE_KP_MINUS = 86
    SDL_SCANCODE_KP_PLUS = 87
    SDL_SCANCODE_KP_ENTER = 88
    SDL_SCANCODE_KP_1 = 89
    SDL_SCANCODE_KP_2 = 90
    SDL_SCANCODE_KP_3 = 91
    SDL_SCANCODE_KP_4 = 92
    SDL_SCANCODE_KP_5 = 93
    SDL_SCANCODE_KP_6 = 94
    SDL_SCANCODE_KP_7 = 95
    SDL_SCANCODE_KP_8 = 96
    SDL_SCANCODE_KP_9 = 97
    SDL_SCANCODE_KP_0 = 98
    SDL_SCANCODE_KP_PERIOD = 99

    SDL_SCANCODE_NONUSBACKSLASH = 100
    SDL_SCANCODE_APPLICATION = 101
    SDL_SCANCODE_POWER = 102
    SDL_SCANCODE_KP_EQUALS = 103
    SDL_SCANCODE_F13 = 104
    SDL_SCANCODE_F14 = 105
    SDL_SCANCODE_F15 = 106
    SDL_SCANCODE_F16 = 107
    SDL_SCANCODE_F17 = 108
    SDL_SCANCODE_F18 = 109
    SDL_SCANCODE_F19 = 110
    SDL_SCANCODE_F20 = 111
    SDL_SCANCODE_F21 = 112
    SDL_SCANCODE_F22 = 113
    SDL_SCANCODE_F23 = 114
    SDL_SCANCODE_F24 = 115
    SDL_SCANCODE_EXECUTE = 116
    SDL_SCANCODE_HELP = 117
    SDL_SCANCODE_MENU = 118
    SDL_SCANCODE_SELECT = 119
    SDL_SCANCODE_STOP = 120
    SDL_SCANCODE_AGAIN = 121 # redo
    SDL_SCANCODE_UNDO = 122
    SDL_SCANCODE_CUT = 123
    SDL_SCANCODE_COPY = 124
    SDL_SCANCODE_PASTE = 125
    SDL_SCANCODE_FIND = 126
    SDL_SCANCODE_MUTE = 127
    SDL_SCANCODE_VOLUMEUP = 128
    SDL_SCANCODE_VOLUMEDOWN = 129
    SDL_SCANCODE_LOCKINGCAPSLOCK = 130 
    SDL_SCANCODE_LOCKINGNUMLOCK = 131
    SDL_SCANCODE_LOCKINGSCROLLLOCK = 132
    SDL_SCANCODE_KP_COMMA = 133
    SDL_SCANCODE_KP_EQUALSAS400 = 134

    SDL_SCANCODE_INTERNATIONAL1 = 135
    SDL_SCANCODE_INTERNATIONAL2 = 136
    SDL_SCANCODE_INTERNATIONAL3 = 137 # yen
    SDL_SCANCODE_INTERNATIONAL4 = 138
    SDL_SCANCODE_INTERNATIONAL5 = 139
    SDL_SCANCODE_INTERNATIONAL6 = 140
    SDL_SCANCODE_INTERNATIONAL7 = 141
    SDL_SCANCODE_INTERNATIONAL8 = 142
    SDL_SCANCODE_INTERNATIONAL9 = 143
    SDL_SCANCODE_LANG1 = 144 # Hangul/English toggle
    SDL_SCANCODE_LANG2 = 145 # Hanja conversion
    SDL_SCANCODE_LANG3 = 146 # Katakana
    SDL_SCANCODE_LANG4 = 147 # Hiragana
    SDL_SCANCODE_LANG5 = 148 # Zenkaku/Hankaku
    SDL_SCANCODE_LANG6 = 149 # reserved
    SDL_SCANCODE_LANG7 = 150 # reserved
    SDL_SCANCODE_LANG8 = 151 # reserved
    SDL_SCANCODE_LANG9 = 152 # reserved

    SDL_SCANCODE_ALTERASE = 153 # Erase-Eaze
    SDL_SCANCODE_SYSREQ = 154
    SDL_SCANCODE_CANCEL = 155
    SDL_SCANCODE_CLEAR = 156
    SDL_SCANCODE_PRIOR = 157
    SDL_SCANCODE_RETURN2 = 158
    SDL_SCANCODE_SEPARATOR = 159
    SDL_SCANCODE_OUT = 160
    SDL_SCANCODE_OPER = 161
    SDL_SCANCODE_CLEARAGAIN = 162
    SDL_SCANCODE_CRSEL = 163
    SDL_SCANCODE_EXSEL = 164

    SDL_SCANCODE_KP_00 = 176
    SDL_SCANCODE_KP_000 = 177
    SDL_SCANCODE_THOUSANDSSEPARATOR = 178
    SDL_SCANCODE_DECIMALSEPARATOR = 179
    SDL_SCANCODE_CURRENCYUNIT = 180
    SDL_SCANCODE_CURRENCYSUBUNIT = 181
    SDL_SCANCODE_KP_LEFTPAREN = 182
    SDL_SCANCODE_KP_RIGHTPAREN = 183
    SDL_SCANCODE_KP_LEFTBRACE = 184
    SDL_SCANCODE_KP_RIGHTBRACE = 185
    SDL_SCANCODE_KP_TAB = 186
    SDL_SCANCODE_KP_BACKSPACE = 187
    SDL_SCANCODE_KP_A = 188
    SDL_SCANCODE_KP_B = 189
    SDL_SCANCODE_KP_C = 190
    SDL_SCANCODE_KP_D = 191
    SDL_SCANCODE_KP_E = 192
    SDL_SCANCODE_KP_F = 193
    SDL_SCANCODE_KP_XOR = 194
    SDL_SCANCODE_KP_POWER = 195
    SDL_SCANCODE_KP_PERCENT = 196
    SDL_SCANCODE_KP_LESS = 197
    SDL_SCANCODE_KP_GREATER = 198
    SDL_SCANCODE_KP_AMPERSAND = 199
    SDL_SCANCODE_KP_DBLAMPERSAND = 200
    SDL_SCANCODE_KP_VERTICALBAR = 201
    SDL_SCANCODE_KP_DBLVERTICALBAR = 202
    SDL_SCANCODE_KP_COLON = 203
    SDL_SCANCODE_KP_HASH = 204
    SDL_SCANCODE_KP_SPACE = 205
    SDL_SCANCODE_KP_AT = 206
    SDL_SCANCODE_KP_EXCLAM = 207
    SDL_SCANCODE_KP_MEMSTORE = 208
    SDL_SCANCODE_KP_MEMRECALL = 209
    SDL_SCANCODE_KP_MEMCLEAR = 210
    SDL_SCANCODE_KP_MEMADD = 211
    SDL_SCANCODE_KP_MEMSUBTRACT = 212
    SDL_SCANCODE_KP_MEMMULTIPLY = 213
    SDL_SCANCODE_KP_MEMDIVIDE = 214
    SDL_SCANCODE_KP_PLUSMINUS = 215
    SDL_SCANCODE_KP_CLEAR = 216
    SDL_SCANCODE_KP_CLEARENTRY = 217
    SDL_SCANCODE_KP_BINARY = 218
    SDL_SCANCODE_KP_OCTAL = 219
    SDL_SCANCODE_KP_DECIMAL = 220
    SDL_SCANCODE_KP_HEXADECIMAL = 221

    SDL_SCANCODE_LCTRL = 224
    SDL_SCANCODE_LSHIFT = 225
    SDL_SCANCODE_LALT = 226
    SDL_SCANCODE_LGUI = 227 # windows command (apple) meta
    SDL_SCANCODE_RCTRL = 228
    SDL_SCANCODE_RSHIFT = 229
    SDL_SCANCODE_RALT = 230 # alt gr option
    SDL_SCANCODE_RGUI = 231 # windows command (apple) meta

    SDL_SCANCODE_MODE = 257

    SDL_SCANCODE_AUDIONEXT = 258
    SDL_SCANCODE_AUDIOPREV = 259
    SDL_SCANCODE_AUDIOSTOP = 260
    SDL_SCANCODE_AUDIOPLAY = 261
    SDL_SCANCODE_AUDIOMUTE = 262
    SDL_SCANCODE_MEDIASELECT = 263
    SDL_SCANCODE_WWW = 264
    SDL_SCANCODE_MAIL = 265
    SDL_SCANCODE_CALCULATOR = 266
    SDL_SCANCODE_COMPUTER = 267
    SDL_SCANCODE_AC_SEARCH = 268
    SDL_SCANCODE_AC_HOME = 269
    SDL_SCANCODE_AC_BACK = 270
    SDL_SCANCODE_AC_FORWARD = 271
    SDL_SCANCODE_AC_STOP = 272
    SDL_SCANCODE_AC_REFRESH = 273
    SDL_SCANCODE_AC_BOOKMARKS = 274


    SDL_SCANCODE_BRIGHTNESSDOWN = 275
    SDL_SCANCODE_BRIGHTNESSUP = 276
    SDL_SCANCODE_DISPLAYSWITCH = 277
    SDL_SCANCODE_KBDILLUMTOGGLE = 278
    SDL_SCANCODE_KBDILLUMDOWN = 279
    SDL_SCANCODE_KBDILLUMUP = 280
    SDL_SCANCODE_EJECT = 281
    SDL_SCANCODE_SLEEP = 282

    SDL_SCANCODE_APP1 = 283
    SDL_SCANCODE_APP2 = 284


    SDL_SCANCODE_AUDIOREWIND = 285
    SDL_SCANCODE_AUDIOFASTFORWARD = 286

    SDL_NUM_SCANCODES = 512