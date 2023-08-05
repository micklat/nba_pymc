from nbag.gen_wrappers import wrap_module

if __name__ == "__main__":
    header = ["from pymc.util import UNSET"]
    wrap_module("pymc", ".", header)
    wrap_module("pymc.math", ".", header)

