employees={'antony':55000,'susan':45000,'kiran':60000}
z=dict(map(lambda x:(x[0],'high' if x[1]>50000 else 'low'),employees.items()))
print(z)