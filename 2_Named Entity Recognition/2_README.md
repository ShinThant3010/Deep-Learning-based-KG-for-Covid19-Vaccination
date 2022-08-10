## 2_Named Entity Recognition

### 1. NER Dataset Preparation
1) Explode CORD-NER-corpus.json file to dataframe (.csv)  <i> (1.1, 1.2) </i>
2) Explode CORD-NER-ner.json file into dataframe (.csv) <i> (2.1) </i>. Mark the Prefix 'B/I' for each entity type <i> (2.2) </i>. Add word_id to each entity <i> (2.3) </i>.
3) Merge result from full sentence (1) and ner data (2). 

### 2. Balanced NER Dataset
- Select 25 entity types. 
- Balance the dataset making the entity count of each type to be in the range (2000, 20000).
- number of sentences in balanced dataset = 43,432

### 3. NER-BERT
- Fine-tuned DistilBERT using NER dataset using SimpleTransformer and sklearn. 
- number of epoches = 30
- Precision = 0.7494, Recall = 0.7366, F1-score = 0.7429

### 4. NER-Topic4
1) Predict NER using NER model on corpus
2) Explode result NER
3) Post-processing result NER

### Note
- CORD-NER-corpus.json: It includes tokenized sentences of the abstract of a document/paper.
- CORD-NER-ner.json: It includes a list of entity with respective start index, end index and type for each sentence in each document. 
