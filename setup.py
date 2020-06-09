from setuptools import setup, find_packages
import qecsim

setup(
    name='qecsim',
    version=qecsim.__version__,
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3',
    install_requires=[
        'click',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'qecsim = qecsim.cli:cli',
        ],
        'run_codes': [
            'five_qubit = qecsim.models.basic:FiveQubitCode',
            'steane = qecsim.models.basic:SteaneCode',
        ],
        'run_error_models': [
            'generic.depolarizing = qecsim.models.generic:DepolarizingErrorModel',
            'generic.bit_flip = qecsim.models.generic:BitFlipErrorModel',
            'generic.phase_flip = qecsim.models.generic:PhaseFlipErrorModel',
            'generic.bit_phase_flip = qecsim.models.generic:BitPhaseFlipErrorModel',
        ],
        'run_decoders': [
            'naive = qecsim.models.generic:NaiveDecoder',
        ],
    }
)