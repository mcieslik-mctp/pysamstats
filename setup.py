from setuptools import setup, Extension, find_packages
import pysam


def get_version():
    """Extract version number from source file."""
    from ast import literal_eval
    with open('pysamstats/__init__.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return literal_eval(line.partition('=')[2].lstrip())
    raise ValueError("__version__ not found")


try:
    from Cython.Build import cythonize
    print('[pysamstats] build with Cython')
    extensions = cythonize([
        Extension('pysamstats.opt',
                  sources=['pysamstats/opt.pyx'],
                  include_dirs=pysam.get_include(),
                  define_macros=pysam.get_defines())]
    )

except ImportError:
    print('[pysamstats] build from C')
    extensions = [Extension('pysamstats.opt',
                            sources=['pysamstats/opt.c'],
                            include_dirs=pysam.get_include(),
                            define_macros=pysam.get_defines())]


setup(
    name='pysamstats',
    version=get_version(),
    author='Alistair Miles',
    author_email='alimanfoo@googlemail.com',
    url='https://github.com/alimanfoo/pysamstats',
    license='MIT Licenses',
    description='A Python utility for calculating statistics against genome '
                'position based on sequence alignments from a SAM, '
                'BAM or CRAM file.',
    scripts=['scripts/pysamstats'],
    package_dir={'': '.'},
    install_requires=[
        "numpy",
        "pysam",
    ],
    packages=find_packages(),
    setup_requires=[
        "nose2",
    ],
    tests_require=[
        "nose2",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    ext_modules=extensions,
)
