import matplotlib.pyplot as plt

def plot_results(train_acc=None, train_loss=None, test_acc=None, test_loss=None, last_n=-2000, normalize_loss=False):
    fig, axes = plt.subplots(2, 2)
    fig.set_figheight(12)
    fig.set_figwidth(15)
    ((ax1, ax2), (ax3, ax4)) = axes

    if train_acc:
        ax1.plot(range(len(train_acc)), train_acc, '-', color='blue', label='train_acc')
        ax3.plot(range(len(train_acc[last_n:])), train_acc[last_n:], '-', color='blue', label='train_acc')
    if test_acc:
        ax1.plot(range(len(test_acc)), test_acc, '-', color='red', label='test_acc')
        ax3.plot(range(len(test_acc[last_n:])), test_acc[last_n:], '-', color='red', label='test_acc')
        
    ax1.set_title('Accuracy')
    ax3.set_title('Last %d Accuracy' % (-1*last_n))

    if train_loss:
        ax2.plot(range(len(train_loss)), train_loss, '-', color='blue', label='train_loss')
        ax4.plot(range(len(train_loss[last_n:])), train_loss[last_n:], '-', color='blue', label='train_loss')
    if test_loss:
        if normalize_loss:
            tl = [x/100 for x in test_loss]
            ax2.plot(range(len(tl)), tl, '-', color='red', label='test_loss')
            ax4.plot(range(len(tl[last_n:])), tl[last_n:], '-', color='red', label='test_loss')
        else:
            ax2.plot(range(len(test_loss)), test_loss, '-', color='red', label='test_loss')
            ax4.plot(range(len(test_loss[last_n:])), test_loss[last_n:], '-', color='red', label='test_loss')
        
    ax2.set_title('Loss')
    ax4.set_title('Last %d Loss' % (-1*last_n))

    for a1, a2 in axes:
        a1.grid(True)
        a2.grid(True)
        a1.legend()
        a2.legend()

    fig.tight_layout()
    plt.show()