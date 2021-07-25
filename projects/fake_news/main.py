import pickle
# import sklearn.linear_model.logistic
var=input("Enter statment to check is it true of false")
print(f"Your entered: {var}")

def fakenews(var):
    load_model=pickle.load(open('./model.sav','rb'))
    prediction=load_model([var])
    prob=load_model.predict_prob([var])
    return print(f"The given statment is {prediction[0]}\nThe truth probability is {prob[0][1]}")

if __name__ == "__main__":
    fakenews(var) 