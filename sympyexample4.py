import sympy as sp

# 定义符号变量
x, y, z = sp.symbols('x y z')
a, b = sp.symbols('a b')

print("=== 基本符号运算 ===")
# 创建符号表达式
expr1 = x**2 + 2*x + 1
expr2 = (x + 1)**2

print(f"表达式1: {expr1}")
print(f"表达式2: {expr2}")
print(f"是否相等: {expr1 == expr2}")  # 注意：这比较对象身份
print(f"是否数学相等: {sp.simplify(expr1 - expr2) == 0}")

# 展开表达式
expr3 = (x + y)**3
print(f"\n展开 (x+y)³: {sp.expand(expr3)}")

# 因式分解
expr4 = x**2 - 4
print(f"因式分解 x²-4: {sp.factor(expr4)}")
