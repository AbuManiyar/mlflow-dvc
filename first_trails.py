import mlflow

def calculate(a,b):
    return a/b

if __name__ =='__main__':
    x = 100
    y = 150
    with mlflow.start_run():
        res = calculate(x,y)
        mlflow.log_params({'x':x , 'y':y, 'res': res})
        print('Sum =', res)
    