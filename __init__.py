# import launch
# if not launch.is_installed("ninja"):
#     launch.run_pip("install --upgrade ninja", "Requirement of GAN-Generator")
# if not launch.is_installed("scipy"):
#     launch.run_pip("install --upgrade scipy", "Requirement of GAN-Generator")
# if not launch.is_installed("torchvision"):
#     launch.run_pip("install --upgrade torchvision", "Requirement of GAN-Generator")
# if not launch.is_installed("torch"):
#     launch.run_pip("install --upgrade torch", "Requirement of GAN-Generator")
# if not launch.is_installed("torch-utils"):
#     launch.run_pip("install --upgrade torch-utils", "Requirement of GAN-Generator")

from .stylegan_nodes import NODE_CLASS_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS']

