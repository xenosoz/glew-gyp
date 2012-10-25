#
# glew_static.gypi
#
{
  'targets': [
    {
      'target_name': 'glew_static',
      'type': 'static_library',
      'product_name': 'glew',
      'direct_dependent_settings': {
        'include_dirs': [
          'glew-1.9.0/include/',
        ],
        'defines': [
          'GLEW_STATIC',
        ],
      },
      'defines': [
        'WIN32',
        '_LIB',
        'WIN32_LEAN_AND_MEAN',
        'VC_EXTRALEAN',
        'GLEW_STATIC',
        '_MBCS',
      ],
      'sources': [
        'glew-1.9.0/build/glew.rc',
        'glew-1.9.0/include/GL/glew.h',
        'glew-1.9.0/include/GL/wglew.h',
        'glew-1.9.0/src/glew.c',
      ],
      'include_dirs': [
        'glew-1.9.0/include/',
      ],
    },
  ],
}
# vim:sts=2:sw=2:norl
