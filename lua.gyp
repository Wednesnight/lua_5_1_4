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

      'target_name': 'liblua',

      'type': 'static_library',

      'default_configuration': 'Debug',

# TODO: re-check need for manual definition
#      'msvs_guid': '8AAE7A8A-8DAC-204C-8BA8-1013866E2AD4',

      'configurations': {

        'Common': {
          'abstract': 1,
          'xcode_settings': {
            'ARCHS': '$(NATIVE_ARCH_ACTUAL)',
            'ONLY_ACTIVE_ARCH': 'YES',
            'VALID_ARCHS': 'i386 x86_64 armv6',
            'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
            'GCC_C_LANGUAGE_STANDARD': 'c99',
            'GCC_WARN_ABOUT_RETURN_TYPE': 'YES',
            'GCC_WARN_UNUSED_VARIABLE': 'YES',
            'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
            'GCC_PFE_FILE_C_DIALECTS': 'c++ objective-c++',
            'GCC_INCREASE_PRECOMPILED_HEADER_SHARING': 'YES',
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
            'GCC_OBJC_CALL_CXX_CDTORS': 'YES',
            'ALWAYS_SEARCH_USER_PATHS': 'NO',
          },
          'msvs_settings': {
            'VCCLCompilerTool': {
              'ObjectFile': '$(IntDir)\\%(RelativeDir)',
             },
          },
        },

        'Debug': {
          'inherit_from': ['Common'],
          'xcode_settings': {
            'GCC_OPTIMIZATION_LEVEL': '0',
          },
          'msvs_settings': {
            'VCCLCompilerTool': {
              'Optimization': '0',
              'PreprocessorDefinitions': ['_DEBUG'],
            },
            'VCLinkerTool': {
              'AdditionalDependencies': ['msvcrtd.lib'],
              'AdditionalOptions': ['/DEBUG', '/NODEFAULTLIB:msvcrt.lib'],
            },
          },
          'defines': [
            '_DEBUG',
          ],
        },

        'Release': {
          'inherit_from': ['Common'],
          'xcode_settings': {
            'GCC_OPTIMIZATION_LEVEL': '3',
          },
          'msvs_settings': {
            'VCCLCompilerTool': {
              'Optimization': '2',
              'PreprocessorDefinitions': ['NDEBUG'],
            },
          },
          'defines': [
            'NDEBUG',
          ],
        },

      },

      'include_dirs': [

        './include',

      ],

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

      'conditions': [

        ['OS == "win"', {
          'defines': [
            'WIN32',
            'UNICODE',
            '_LIB',
#            '_CHAR16T',
          ],
        }],

      ],
    },

  ],

}
