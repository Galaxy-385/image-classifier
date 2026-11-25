import torch

"""
GPU verification script for the image classification project.

This module verifies that PyTorch can detect and use the NVIDIA GPU
available on the system and performs a simple CUDA computation.
"""

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.version.cuda}")
print(f"GPU: {torch.cuda.get_device_name(0)}")

x = torch.rand(5000, 5000, device=device)
y = torch.rand(5000, 5000, device=device)

z = x @ y

torch.cuda.synchronize()

print(f"Resultado calculado en: {z.device}")
print("Prueba de GPU completada correctamente.")
