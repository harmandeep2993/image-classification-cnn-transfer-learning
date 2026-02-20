
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

class Plot():

    def __init__(self, history, title):
        self.history = history
        self.title = title

    def plot_curve(self):
        plt.figure(figsize=(10,4))
        
        # Accuracy
        plt.subplot(1,2,1)
        plt.plot(self.history.history['accuracy'])
        plt.plot(self.history.history['val_accuracy'])
        plt.title(f"Accuracy Curve\n{self.title}", fontsize=8)
        plt.legend(["Train", "Val"])
        plt.xlabel("Epochs")

        # Loss
        plt.subplot(1,2,2)
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.title(f"Loss Curve\n{self.title}", fontsize=8)
        plt.legend(["Train", "Val"])
        plt.xlabel("Epochs")

        plt.tight_layout()
        plt.show()

    # Confusion Matrix
    def heatmap(self, y_true, y_pred, class_names):
        cm = confusion_matrix(y_true, y_pred)

        plt.figure(figsize=(8,6))
        sns.heatmap(cm,
                    annot=True,
                    fmt='d',
                    cmap='Blues',
                    xticklabels=class_names,
                    yticklabels=class_names)

        plt.title(f"Confusion Matrix\n{self.title}", fontsize= 8)
        plt.xlabel("Predicted Class")
        plt.ylabel("Actual Class")
        plt.show()