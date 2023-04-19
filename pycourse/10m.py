dagslön=0.01
totalön=dagslön
dag=1

while totalön < 10_000_000:
    print(f"{dag:3} {dagslön:6} kr {totalön:7} kr")
    dag=dag+1
    dagslön=dagslön*2
    totalön=totalön+dagslön
print(dag)