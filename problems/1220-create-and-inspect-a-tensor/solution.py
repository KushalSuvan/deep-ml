import torch

def make_tensor():
    """Return a 2x3 float32 tensor [[1, 2, 3], [4, 5, 6]]."""
    # TODO
    return torch.arange(1, 7, 1).to(torch.float32).reshape(2, 3)
