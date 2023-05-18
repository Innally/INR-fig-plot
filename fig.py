import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cifarpath = f'cifar.xlsx'
flopath = f'flo.xlsx'
minipath = f'mini.xlsx'
x_lable = [1, 2, 3, 4, 5, 6, 7, 8, 'INR']


def plotting(data, ax, title):
    y_baseline = np.array(data['baseline'].to_list(), dtype=float)
    y_dali = np.array(data['DALI'].to_list(), dtype=float)
    y_inr = np.array(data['INR'][0], dtype=float)
    # norm_factor= y_baseline[0]
    # y_baseline/=norm_factor
    # y_dali/=norm_factor
    # y_inr/=norm_factor
    ax.bar(x[0:8] - 0.2, y_baseline, 0.4, label='Baseline', color='#aed6dc')
    ax.bar(x[0:8] + 0.2, y_dali, 0.4, label='DALI', color='#afc151')
    ax.bar(x[8], y_inr, 0.4, label='INR', color='#59a523')
    ax.set_xticks(x, x_lable)
    ax.legend(title='Methods')
    ax.set_title(title)
    ax.title.set_fontsize(13)
    ax.xaxis.label.set_fontsize(13)
    ax.yaxis.label.set_fontsize(13)
    ax.tick_params(axis='x', labelsize=13)
    ax.tick_params(axis='y', labelsize=13)


if __name__ == '__main__':
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    plt.rc('font', size=13)
    cifar = pd.read_excel(cifarpath)
    print(cifar)
    x_axis = cifar['cifar'].to_list()
    x_axis.append('INR')
    x = np.arange(len(x_axis))
    print(x_axis)
    plotting(cifar, ax1, "CIFAR-10")
    # text
    # ax1.text(0.2, 1, str(cifar['baseline'][0]), horizontalalignment='center',
    #  verticalalignment='center')

    # flo
    flo = pd.read_excel(flopath)
    print(flo)
    x_axis = flo['flo'].to_list()
    x_axis.append('INR')
    x = np.arange(len(x_axis))
    print(x_axis)
    plotting(flo, ax2, "102flowers")

    #mini
    mini = pd.read_excel(minipath)
    print(mini)
    x_axis = mini['mini'].to_list()
    x_axis.append('INR')
    x = np.arange(len(x_axis))
    print(x_axis)
    plotting(mini, ax3, "Mini-ImageNet")

    ax1.set_ylabel('Time Cost (sec.)')
    ax2.set_xlabel('Threads number')

    plt.show()