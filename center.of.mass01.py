import matplotlib.pyplot as plt
import numpy as np

# Set figure size
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()  # Flatten 2x2 subplot array to 1D for easy traversal

# ===================== Case 1: 3 particles (largest mass in the middle) =====================
x1 = [0, 2, 4]
m1 = [1, 4, 1]
cm1 = np.sum(np.array(x1) * np.array(m1)) / np.sum(m1)  # Calculate center of mass

# Plot Case 1
ax1 = axes[0]
# Plot particles (bubble size represents mass)
ax1.scatter(x1, [0]*3, s=np.array(m1)*50, color=['lightblue', 'red', 'lightblue'], zorder=3)
# Label mass and position
for i, (x, m) in enumerate(zip(x1, m1)):
    ax1.text(x, 0.1, f'm={m}\nx={x}', ha='center', va='bottom', fontsize=10)
# Plot center of mass
ax1.scatter(cm1, 0, s=150, marker='*', color='black', label=f'Center of Mass={cm1:.1f}', zorder=4)
# Style settings
ax1.set_title('Case 1: 3 Particles (Largest Mass in the Middle)', fontsize=12)
ax1.set_xlim(-1, 5)
ax1.set_ylim(-0.5, 0.8)
ax1.set_yticks([])  # Hide y-axis ticks
ax1.grid(axis='x', alpha=0.3)
ax1.legend()

# ===================== Case 2: 4 particles (largest mass at the far left) =====================
x2 = [1, 3, 5, 7]
m2 = [5, 1, 1, 1]
cm2 = np.sum(np.array(x2) * np.array(m2)) / np.sum(m2)

# Plot Case 2
ax2 = axes[1]
ax2.scatter(x2, [0]*4, s=np.array(m2)*50, color=['red', 'lightblue', 'lightblue', 'lightblue'], zorder=3)
for i, (x, m) in enumerate(zip(x2, m2)):
    ax2.text(x, 0.1, f'm={m}\nx={x}', ha='center', va='bottom', fontsize=10)
ax2.scatter(cm2, 0, s=150, marker='*', color='black', label=f'Center of Mass={cm2:.1f}', zorder=4)
ax2.set_title('Case 2: 4 Particles (Largest Mass at Far Left)', fontsize=12)
ax2.set_xlim(0, 8)
ax2.set_ylim(-0.5, 0.8)
ax2.set_yticks([])
ax2.grid(axis='x', alpha=0.3)
ax2.legend()

# ===================== Case 3: 3 particles (largest mass on the left) =====================
x3 = [2, 6, 10]
m3 = [3, 1, 2]
cm3 = np.sum(np.array(x3) * np.array(m3)) / np.sum(m3)

# Plot Case 3
ax3 = axes[2]
ax3.scatter(x3, [0]*3, s=np.array(m3)*50, color=['red', 'lightblue', 'orange'], zorder=3)
for i, (x, m) in enumerate(zip(x3, m3)):
    ax3.text(x, 0.1, f'm={m}\nx={x}', ha='center', va='bottom', fontsize=10)
ax3.scatter(cm3, 0, s=150, marker='*', color='black', label=f'Center of Mass={cm3:.2f}', zorder=4)
ax3.set_title('Case 3: 3 Particles (Largest Mass on the Left)', fontsize=12)
ax3.set_xlim(1, 11)
ax3.set_ylim(-0.5, 0.8)
ax3.set_yticks([])
ax3.grid(axis='x', alpha=0.3)
ax3.legend()

# ===================== Case 4: 4 particles (largest mass at 2nd position) =====================
x4 = [0, 2, 4, 6]
m4 = [1, 4, 2, 1]
cm4 = np.sum(np.array(x4) * np.array(m4)) / np.sum(m4)

# Plot Case 4
ax4 = axes[3]
ax4.scatter(x4, [0]*4, s=np.array(m4)*50, color=['lightblue', 'red', 'orange', 'lightblue'], zorder=3)
for i, (x, m) in enumerate(zip(x4, m4)):
    ax4.text(x, 0.1, f'm={m}\nx={x}', ha='center', va='bottom', fontsize=10)
ax4.scatter(cm4, 0, s=150, marker='*', color='black', label=f'Center of Mass={cm4:.2f}', zorder=4)
ax4.set_title('Case 4: 4 Particles (Largest Mass at 2nd Position)', fontsize=12)
ax4.set_xlim(-1, 7)
ax4.set_ylim(-0.5, 0.8)
ax4.set_yticks([])
ax4.grid(axis='x', alpha=0.3)
ax4.legend()

# ===================== Global Settings =====================
fig.suptitle('Center of Mass of Linearly Distributed Particles (Red=Largest Mass, Orange=2nd Largest, Black Star=Center of Mass)',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Reserve space for main title
plt.show()
