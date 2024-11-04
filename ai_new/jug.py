import matplotlib.pyplot as plt

def show_jug(jug1, jug2, step):
    plt.bar(1, 4, width=0.5, color='none', edgecolor='black')
    plt.bar(1, jug1, width=0.5, color='lightblue')
    plt.text(1, 4.2, '4L Jug')  
    plt.text(1, 1, f'{jug1}L', color='black')
    plt.bar(2, 3, width=0.5, color='none', edgecolor='black')
    plt.bar(2, jug2, width=0.5, color='lightblue')
    plt.text(2, 3.2, '3L Jug')
    plt.text(2, 1, f'{jug2}L', color='black')
    plt.axis('off')
    plt.title(f"step {step}")
    plt.show()

steps = [
    (0, 0), 
    (0, 3),
    (3, 0),
    (3, 3),
    (4, 2),
    (0, 2),
    (2, 0)
]
count = 1
for i in steps:
    show_jug(i[0], i[1], count)
    count += 1
