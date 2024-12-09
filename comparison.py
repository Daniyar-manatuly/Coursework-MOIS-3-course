import matplotlib.pyplot as plt


models = ['Gradient Boosting', 'KNN', 'Random Forest']
accuracies = [80, 77, 81]


plt.bar(models, accuracies, color=['skyblue', 'turquoise', 'green'], edgecolor='black')

plt.ylabel('Accuracy (%)', fontsize=12)
plt.ylim(0, 100)  # Ограничение по оси Y
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, accuracy in enumerate(accuracies):
    plt.text(i, accuracy + 1, f"{accuracy}", ha='center', fontsize=10)

plt.tight_layout()
plt.show()
