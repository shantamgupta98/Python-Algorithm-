import numpy as np

x=np.array([9. , 8. , 7.5, 5.1, 8.6, 9.9])
y=np.array([8. , 7. , 6.6, 3. , 7.5, 9. ])

df=pd.DataFrame({'Year':x,'Salary':y})

x_avg = np.sum(x) / len(x)
y_avg = np.sum(y) / len(y)

a=x-x_avg
b=y-y_avg
c=(x-x_avg)**2
d=(y-y_avg)**2
e=(x-x_avg)*(y-y_avg)

sum_a = np.sum(a)
sum_b = np.sum(b)
sum_c = np.sum(c)
sum_d = np.sum(d)
sum_e = np.sum(e)

r = sum_e/ np.sqrt(sum_c*sum_d)
sx = np.sqrt(sum_c)
sy = np.sqrt(sum_d)

m = r*(sy/sx)
c= y_avg - m*x_avg

new_x  =input("Please Enter X:")
new_x = int(new_x)
pre = m*new_x + c

print("Predicted Salary for Year of Experience {} is {}".format(new_x,round(pre)))