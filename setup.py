from setuptools import setup
import re, io

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('hlda/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

setup(
  name = 'hlda',
  version = __version__,
  packages = ['hlda'], # this must be the same as the name above
  description = 'Gibbs sampler for the Hierarchical Latent Dirichlet Allocation topic model. This is based on the hLDA implementation from Mallet, having a fixed depth on the nCRP tree.',
  author = 'Jon Reades (adapted from Py2 version by Joe Wandy)',
  author_email = 'jon@reades.com',
  url = 'https://github.com/jreades/hlda', # use the URL to the github repo
  download_url = 'https://github.com/jreades/hlda/archive/0.3.tar.gz', # I'll explain this in a second
  keywords = ['topic', 'model', 'lda', 'gibbs', 'sampler', 'hlda'], # arbitrary keywords
  classifiers = [],
)
