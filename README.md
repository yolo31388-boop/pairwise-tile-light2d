# pairwise-tile-light2d

顶视角手电筒扫过瓦片地图时，墙角漏光、阴影跳、远处一片黑：光照按 tile 中心采样；阴影多边形在 tile 边界被裁断；法线贴图用世界空间但精灵会旋转；光衰减用线性距离；HDR 光强和 bloom 阈值不匹配；排序层把光源和角色分到不同批次；图集边缘 bleeding；相机缩放后光照半径按像素算；子像素遮挡没做保守光栅；多光源叠加没做能量归一。render/tile_light2d.py 是核心，tests/test_tile_light2d.py 15个红。要修的是：连续光照采样；跨 tile 阴影缝合；法线随精灵旋转；物理衰减；HDR 阈值联动；排序层统一；图集边缘 clamp；半径按世界单位；保守光栅；能量归一。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
