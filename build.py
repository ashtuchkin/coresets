from pybind11.setup_helpers import Pybind11Extension, build_ext

def build(setup_kwargs):
    setup_kwargs.update({
        "ext_modules": [
            Pybind11Extension('coresets.sensitivity', ['src/sensitivity.cpp']),
            Pybind11Extension('coresets.algorithms.weighted_kmeans_', ['src/weighted_kmeans.cpp']),
        ],
        "cmdclass": {"build_ext": build_ext},
        "zip_safe": False,
    })
