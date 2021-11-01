from distutils.core import setup
setup(
  name = 'javasoup',        
  packages = ['javasoup'],  
  version = '0.3',    
  license='MIT',       
  description = 'Simple python library that uses puppeteer to pull HTML from a loaded SPA (REQUIRES NODE, NPM, AND PUPPETEER)',   
  author = 'rs0n',                  
  author_email = 'rs0n.evolv3@gmail.com',     
  url = 'https://github.com/R-s0n/javasoup',  
  download_url = 'https://github.com/R-s0n/javasoup/archive/refs/tags/v_01.tar.gz',  
  keywords = ['webscraping', 'beautifulsoup', 'soup'],  
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)