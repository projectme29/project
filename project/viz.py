
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('DT', 'RF', 'KMeans', 'MLP')
y_pos = np.arange(len(objects))
performance = [92.9,92.7,93.0,92.3]

plt.bar(y_pos, performance, align='center', alpha=0.5, color='red')
plt.xticks(y_pos, objects)
plt.ylabel('Execution Time')
plt.xlabel('Classification Types')
plt.title("Analysis of Performance Accuracy")
plt.savefig('data/t2.png')
plt.show()
