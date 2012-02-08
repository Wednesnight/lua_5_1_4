#
# Copyright (c) 2011 Timo Boll, Tony Kostanjsek
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
{

  'targets': [

    {

      'target_name': 'lua',
      'type': 'none',

      'all_dependent_settings': {

        'include_dirs': [
          './include',
        ],

      },

      'direct_dependent_settings': {

        'sources': [
          # thirdparty/lua
          './source/src/lzio.c',
          './source/src/lvm.c',
          './source/src/lundump.c',
          './source/src/ltm.c',
          './source/src/ltablib.c',
          './source/src/ltable.c',
          './source/src/lstrlib.c',
          './source/src/lstring.c',
          './source/src/lstate.c',
          './source/src/lparser.c',
          './source/src/loslib.c',
          './source/src/lopcodes.c',
          './source/src/lobject.c',
          './source/src/loadlib.c',
          './source/src/lmem.c',
          './source/src/lmathlib.c',
          './source/src/llex.c',
          './source/src/liolib.c',
          './source/src/linit.c',
          './source/src/ldblib.c',
          './source/src/ldebug.c',
          './source/src/lauxlib.c',
          './source/src/lbaselib.c',
          './source/src/ldo.c',
          './source/src/lfunc.c',
          './source/src/ldump.c',
          './source/src/lapi.c',
          './source/src/lcode.c',
          './source/src/lgc.c',
        ],

      },

    },

  ],

}
