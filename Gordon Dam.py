import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")


x = 0
y = 0
z = 140

vx = 5
vy = 0
vz = 0

x1 = x
y1 = y
z1 = z
v1x = vx
v1y = vy
v1z = vz
lst_x1 = [x1]
lst_y1 = [y1]
lst_z1 = [z1]

ux = -vx
uy = -vy
uz = -vz

wx = 0
wy = -3
wz = 0

n = 1.71 * 10 ** -5
po = 1.2
R = 0.13
S = 3.14 * 4 * R**2
m = 0.6
g = 10

dt = 0.4

lst_x = [x]
lst_y = [y]
lst_z = [z]

while True:
    if z > 0:
        vx = vx + ((-6*3.14*R*n*vx / m) + 2*S*po*R*(uy*wz - uz*wy) / m) * dt
        vy = vy + ((-6*3.14*R*n*vy / m) + 2*S*po*R*(uz*wx - ux*wz) / m) * dt
        vz = vz + ((-6*3.14*R*n*vz / m) - g + 2*S*po*R*(ux*wy - uy*wx) / m) * dt

        x = x + vx * dt
        y = y + vy * dt
        z = z + vz * dt
        ux = -vx
        uy = -vy
        uz = -vz

        lst_x.append(x)
        lst_y.append(y)
        lst_z.append(z)
    else:
        break

    if z1 > 0:
        x1 = x1 + v1x * dt
        y1 = y1 + v1y * dt
        z1 = z1 + v1z*dt - g*dt ** 2 / 2
        v1z = v1z - g * dt

        lst_x1.append(x1)
        lst_y1.append(y1)
        lst_z1.append(z1)

print(lst_x, lst_y, lst_z, sep='\n', end='\n')
print(lst_x1, lst_y1, lst_z1, sep='\n')

ax.plot3D(lst_x, lst_y, lst_z, 'red')
ax.plot3D(lst_x1, lst_y1, lst_z1, 'blue')
ax.scatter3D(lst_x1, lst_y1, lst_z1, c=lst_z1, cmap='cividis')
ax.scatter3D(lst_x, lst_y, lst_z, c=lst_z, cmap='cividis')
plt.show()
