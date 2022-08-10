import time
import torch
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from simpletransformers.ner import NERModel,NERArgs

start_time = time.time()

#change
data = pd.read_csv("balanced_ner_dataset.csv",encoding="latin1" )
data = data.dropna()

data["sent_number"] = LabelEncoder().fit_transform(data["sent_number"] )
data.rename(columns={"sent_number":"sentence_id","sent_tokens":"words","flag":"labels"}, inplace =True)
data["labels"] = data["labels"].str.upper()

X= data[["sentence_id","words"]]
Y =data["labels"]
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size =0.2)

#building up train data and test data
train_data = pd.DataFrame({"sentence_id":x_train["sentence_id"],"words":x_train["words"],"labels":y_train})
test_data = pd.DataFrame({"sentence_id":x_test["sentence_id"],"words":x_test["words"],"labels":y_test})

label = data["labels"].unique().tolist()

# parameters- change
args = NERArgs()
args.num_train_epochs = 30
args.learning_rate = 1e-4
args.overwrite_output_dir =True
args.train_batch_size = 64
args.eval_batch_size = 64

model = NERModel('distilbert', 'distilbert-base-uncased',labels=label,args =args, use_cuda = False)

model.train_model(train_data,eval_data = test_data,acc=accuracy_score)
result, model_outputs, preds_list = model.eval_model(test_data)

#change
torch.save(model, 'model_distilbert_balanced_30ep.pth')

end_time = time.time()
runtime_min = 'Estimate runtime: '+ str((end_time-start_time)/60) + ' minutes.'

#change
file = open('result_status__distilbert_balanced_30ep.txt', 'w')
file.write(str(result) + '\n' + runtime_min)
file.close()