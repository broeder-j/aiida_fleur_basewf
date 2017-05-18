# -*- coding: utf-8 -*-
"""
setup: usage: pip install -e .
"""

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='aiida-fleur-basewf',
        version='0.1b',
        description='Basic AiiDA workflows/workchains for running the FLEUR-code (scf, dos, band, eos, relax). Plus some utility',
        url='https://github.com/broeder-j/aiida_fleur_basewf',
        author='Jens Broeder',
        author_email='j.broeder@fz-juelich.de',
        license='MIT License, see LICENSE.txt file.',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Plugins',
            'Framework :: AiiDA',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Scientific/Engineering :: Physics'
        ],
        keywords='fleur aiida inpgen workflows scf dos band eos DFT FLAPW',
        packages=find_packages(exclude=['aiida']),
        include_package_data=True,
        setup_requires=[
            'reentry'
        ],
        reentry_register=True,
        install_requires=[
            'aiida-core',
            'ase',
            'lxml >= 3.6.4',
            'aiida-fleur'
        ],
        extras_require={
            'graphs': ['matplotlib'],
        },
        entry_points={
            'aiida.workflows': [
                'fleur.scf = fleur_workflows.scf:fleur_scf_wc',
                'fleur.dos = fleur_workflows.dos:fleur_dos_wc',
                'fleur.band = fleur_workflows.band:fleur_band_wc',
                'fleur.eos = fleur_workflows.eos:fleur_eos_wc'
                
            ]

        },
    )
