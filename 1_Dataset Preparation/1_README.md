## 1_Dataset Preparation

1. Extract vaccine related papers which are published from 2020. And take only title and abstract columns from the CORD-19 dataset.
2. Make Bigram text segments to use in LDA.
3. Find optimal topic count by analyzing the corehence score for topic number (3 to 10). And select the most suitable topic count (6 in this study).
4. Perform LDA on selected topic count. And select the most suitable topic number (4 in this study).
5. Match papers with respective topic number.
6. Extract papers under selected topic number.
7. Expend the filtered corpus into sentences with respective doc_id and sentence_id.
8. Preprocess the corpus. 
