import mlflow

def calculate(x,y):
    return x+y

if __name__ == '__main__':
    with mlflow.start_run():
        result = calculate(2,5)
        print(result)
        