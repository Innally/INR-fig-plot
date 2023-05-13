import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns

cifarpath=f'/home/yh/INR_draw/cifar.xlsx'
flopath=f'/home/yh/INR_draw/flo.xlsx'
minipath=f'/home/yh/INR_draw/mini.xlsx'
x_lable=[1,2,3,4,5,6,7,8,'INR']
def plotting(data,ax,title):
    y_baseline=np.array(data['baseline'].to_list(),dtype=float)
    y_dali=np.array(data['DALI'].to_list(),dtype=float)
    y_inr=np.array(data['INR'][0],dtype=float)
    # norm_factor= y_baseline[0] 
    # y_baseline/=norm_factor
    # y_dali/=norm_factor
    # y_inr/=norm_factor
    ax.bar(x[0:8] -0.2,y_baseline,0.4,label='Baseline',color='#aed6dc')
    ax.bar(x[0:8] +0.2,y_dali,0.4,label='DALI',color='#afc151')
    ax.bar(x[8] ,y_inr,0.4,label='INR',color='#59a523')
    ax.set_xticks(x,x_lable)
    ax.set_xlabel('Threads num')
    ax.set_ylabel('Normalized time cost')
    ax.legend(title='Methods')
    ax.set_title(title +' time Profiling')
    


if __name__ =='__main__':
    fig, (ax1,ax2,ax3) = plt.subplots(1,3)
    sns.color_palette("pastel")
    #cifar
    cifar=pd.read_excel(cifarpath)
    print(cifar)
    x_axis=cifar['cifar'].to_list()
    x_axis.append('INR')
    x = np.arange(len(x_axis))
    print(x_axis)
    plotting(cifar,ax1,"Cifar-10")
    # text
    # ax1.text(0.2, 1, str(cifar['baseline'][0]), horizontalalignment='center',
    #  verticalalignment='center')
    
    # flo
    flo=pd.read_excel(flopath)
    print(flo)
    x_axis=flo['flo'].to_list()
    x_axis.append('INR')
    x = np.arange(len(x_axis))
    print(x_axis)
    plotting(flo,ax2,"Flower")
    
    #mini
    mini=pd.read_excel(minipath)
    print(mini)
    x_axis=mini['mini'].to_list()
    x_axis.append('INR')
    x = np.arange(len(x_axis))
    print(x_axis)
    plotting(mini,ax3,"MiniImagenet")
    
    plt.show()