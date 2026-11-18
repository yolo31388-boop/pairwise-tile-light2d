import pytest
from render import tile_light2d as mod

CASES = [
    ("bilinear_origin", "m.sample_bilinear(0.0, 10.0, 20.0, 30.0, 0.0, 0.0) == approx(0.0)"),
    ("bilinear_center", "m.sample_bilinear(0.0, 10.0, 20.0, 30.0, 0.5, 0.5) == approx(15.0)"),
    ("bilinear_x", "m.sample_bilinear(0.0, 10.0, 20.0, 30.0, 1.0, 0.0) == approx(10.0)"),
    ("attenuation_full", "m.attenuation(0.0, 10.0) == approx(1.0)"),
    ("attenuation_edge", "m.attenuation(10.0, 10.0) == approx(0.0)"),
    ("attenuation_outside", "m.attenuation(20.0, 10.0) == approx(0.0)"),
    ("bloom_below", "m.bloom_excess(1.0, 2.0) == approx(0.0)"),
    ("bloom_above", "m.bloom_excess(3.0, 2.0) == approx(2.0)"),
    ("clamp_high", "m.clamp_uv(1.2, 1.0) == approx(1.0)"),
    ("clamp_low", "m.clamp_uv(-0.2, 1.0) == approx(0.0)"),
    ("world_radius", "m.world_radius(10.0, 2.0) == approx(5.0)"),
    ("energy_sum", "sum(m.normalize_energy([2.0, 2.0])) == approx(1.0)"),
    ("energy_equal", "m.normalize_energy([2.0, 2.0])[0] == approx(0.5)"),
    ("attenuation_monotonic", "m.attenuation(2.0, 10.0) > m.attenuation(8.0, 10.0)"),
    ("bloom_edge", "m.bloom_excess(2.0, 2.0) == approx(0.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
