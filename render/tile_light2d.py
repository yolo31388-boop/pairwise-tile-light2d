"""第 51 批：顶视角手电筒扫过瓦片地图时，墙角漏光、阴影跳、远..."""

def sample_bilinear(p00, p10, p01, p11, u, v):
    """在四个瓦片采样点之间做双线性插值。"""
    raise NotImplementedError("TODO: sample_bilinear")

def attenuation(distance, radius):
    """返回物理光衰减。"""
    raise NotImplementedError("TODO: attenuation")

def bloom_excess(hdr_luminance, threshold):
    """返回超过 bloom 阈值的亮度。"""
    raise NotImplementedError("TODO: bloom_excess")

def clamp_uv(uv, size):
    """把图集 UV 钳制在可用范围内。"""
    raise NotImplementedError("TODO: clamp_uv")

def world_radius(pixel_radius, pixels_per_unit):
    """把像素半径换算成世界半径。"""
    raise NotImplementedError("TODO: world_radius")

def normalize_energy(energies):
    """把多光源能量归一化。"""
    raise NotImplementedError("TODO: normalize_energy")
