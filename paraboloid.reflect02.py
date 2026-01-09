import numpy as np
import plotly.graph_objects as go

# 参数设置
a = 1.0  # 抛物面参数：z = (x^2 + y^2) / (4f)，这里设 f = a => z = (x^2 + y^2)/(4a)
f = a  # 焦点在 (0, 0, f)

# 创建网格数据
theta = np.linspace(0, 2 * np.pi, 100)
r = np.linspace(0, 2, 50)
R, Theta = np.meshgrid(r, theta)
X = R * np.cos(Theta)
Y = R * np.sin(Theta)
Z = (X ** 2 + Y ** 2) / (4 * f)

# 准备绘制数据
paraboloid = go.Surface(
    x=X, y=Y, z=Z,
    colorscale='Viridis',
    showscale=False,
    opacity=0.7,
    name="Paraboloid"
)

# 设置入射光线（平行于 z 轴）
num_rays = 8
incident_rays = []
reflected_rays = []

for angle in np.linspace(0, 2 * np.pi, num_rays, endpoint=False):
    # 入射光线起点位置
    r_val = 1.8
    x0 = r_val * np.cos(angle)
    y0 = r_val * np.sin(angle)
    z_surface = (x0 ** 2 + y0 ** 2) / (4 * f)
    z_top = z_surface + 2

    # 计算法向量
    normal = np.array([-x0 / (2 * f), -y0 / (2 * f), 1])
    normal = normal / np.linalg.norm(normal)

    # 反射方向计算
    incident_dir = np.array([0, 0, -1])
    reflected_dir = incident_dir - 2 * np.dot(incident_dir, normal) * normal
    reflected_dir = reflected_dir / np.linalg.norm(reflected_dir)

    # 绘制入射光线和反射光线
    t = np.linspace(0, 3, 100)
    refl_x = x0 + reflected_dir[0] * t
    refl_y = y0 + reflected_dir[1] * t
    refl_z = z_surface + reflected_dir[2] * t

    incident_rays.append(go.Scatter3d(x=[x0, x0], y=[y0, y0], z=[z_top, z_surface],
                                      mode='lines', line=dict(color='red', width=4),
                                      name=f'Incident Ray {angle:.2f}'))

    reflected_rays.append(go.Scatter3d(x=refl_x, y=refl_y, z=refl_z,
                                       mode='lines', line=dict(color='green', width=3, dash='dot'),
                                       name=f'Reflected Ray {angle:.2f}'))

# 添加焦点
focus = go.Scatter3d(x=[0], y=[0], z=[f], mode='markers', marker=dict(size=6, color='black'), name='Focus')

# 创建图形
fig = go.Figure(data=[paraboloid] + incident_rays + reflected_rays + [focus])

# 更新布局
fig.update_layout(
    title_text="Paraboloid Reflecting Parallel Rays to Focus",
    showlegend=True,
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectratio=dict(x=1, y=1, z=0.75),
        camera_eye=dict(x=-1.5, y=-1.5, z=1.5)
    )
)

fig.show()
