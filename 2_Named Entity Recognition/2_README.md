## 2_Named Entity Recognition

### 1. NER Dataset Preparation
1) Explode CORD-NER-corpus.json file to dataframe (.csv)  <i> (1.1, 1.2) </i>
2) Explode CORD-NER-ner.json file into dataframe (.csv) <i> (2.1) </i>. 
Mark the Prefix 'B/I' for each entity type <i> (2.2) </i>. 
Add word_id to each entity <i> (2.3) </i>.
3) Merge result from full sentence (1) and ner data (2). 

### 2. Balanced NER Dataset
- Select 25 entity types. Balance the dataset making the entity count of each type to be in the range (2000, 20000).

### 3. NER-BERT
- Fine-tuned DistilBERT using NER dataset.

### 4. NER-Topic4
