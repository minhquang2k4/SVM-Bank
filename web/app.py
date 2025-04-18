from flask import Flask, render_template, request
import joblib
import numpy as np
loaded_model = joblib.load('svm_model.pkl') 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():

  # Nhận dữ liệu từ form
  data = request.form.to_dict()
  print(data)
  
  # Chuyển đổi dữ liệu thành định dạng mà mô hình có thể nhận
  X_new = np.array([[
    int(data['age']),
    int(data['sex']),
    int(data['region']),
    float(data['income']),
    int(data['married']),
    int(data['children']),
    int(data['car']),
    int(data['save_act']),
    int(data['current_act']),
    int(data['mortgage'])
  ]])
  
  print(X_new)

  y_pred_new = loaded_model.predict(X_new) 
  prediction = int(y_pred_new[0]) 
  print(prediction)

  return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
  app.run(debug=True, port=5000)