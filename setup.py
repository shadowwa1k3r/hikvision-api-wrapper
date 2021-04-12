from distutils.core import setup
setup(
  name = 'hikvision_isapi_wrapper',
  packages = ['hikvision_isapi_wrapper'],
  version = '0.3.0',
  license='MIT',
  description = 'Minimial API wrapper for hikvison ISAPI',
  author = 'shadowwa1k3r',
  author_email = 'ergash1994@gmail.com',
  url = 'https://github.com/shadowwa1k3r/hikvision-isapi-wrapper',
  download_url = 'https://github.com/shadowwa1k3r/hikvision-isapi-wrapper/archive/v_030.tar.gz',
  keywords = ['hikvision', 'ISAPI', 'wrapper'],
  install_requires=[
          'atomicwrites==1.4.0',
          'attrs==20.3.0',
          'certifi==2020.12.5',
          'chardet==4.0.0',
          'colorama==0.4.4',
          'idna==2.10',
          'iniconfig==1.1.1',
          'multidict==5.1.0',
          'packaging==20.8',
          'pluggy==0.13.1',
          'py==1.10.0',
          'pyparsing==2.4.7',
          'pytest==6.2.1',
          'pyyaml==5.3.1',
          'requests==2.25.1',
          'six==1.15.0',
          'toml==0.10.2',
          'urllib3==1.26.2',
          'vcrpy==4.1.1',
          'wrapt==1.12.1',
          'yarl==1.6.3',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)