#%%
import numpy as np, matplotlib.pyplot as plt
import csv
#%%
data = list(csv.DictReader(open('SN2020eyj.csv')))
t,mag,mag_err,band = [],[],[],[]
for i in range(len(data)):
    ti = float(data[i]['time'])
    mag_i = float(data[i]['magnitude'])
    err_i = float(data[i]['e_magnitude'])
    band_i = data[i]['band']
    t = np.append(t,ti)
    mag = np.append(mag,mag_i)
    mag_err = np.append(mag_err,err_i)
    band = np.append(band,band_i)
t0 = min(t)
t_plot = t-t0
tg,ti,tr = [],[],[]
mag_g,mag_i,mag_r = [],[],[]
err_g,err_i,err_r = [],[],[]
for m in range(len(t_plot)):
    if band[m] == "g":
        tg = np.append(tg,t_plot[m])
        mag_g = np.append(mag_g,mag[m])
        err_g = np.append(err_g,mag_err[m])
    elif band[m] == "i":
        ti = np.append(ti,t_plot[m])
        mag_i = np.append(mag_i,mag[m])
        err_i = np.append(err_i,mag_err[m])
    else:
        tr = np.append(tr,t_plot[m])
        mag_r = np.append(mag_r,mag[m])
        err_r = np.append(err_r,mag_err[m])
fig1 = plt.figure(figsize=(10, 8),dpi=100)
plt.xlim(-10,450)
plt.ylim(15.5,23.5)
plt.gca().invert_yaxis()
plt.xlabel('Days since first detection',fontsize=20)
plt.ylabel('AB magnitude',fontsize=20)
plt.errorbar(tg,mag_g+1.5,err_g,fmt='o',color='green',label = 'g+1.5')
plt.errorbar(ti,mag_i-1,err_i,fmt='o',color='yellow',label = 'i-1')
plt.errorbar(tr,mag_r,err_r,fmt='o',color='red',label = 'r')
plt.legend(fontsize=15,loc=1)
#%%

#%%
