# Deep-Learning-based-KG-Construction-for-Covid19-Vaccination

Master's Research work and NII Internship Research supervised by Dr. Chutiporn Anutariya (Asian Institute of Technology, Thailand), Prof. Frederic Andreas (National Institute of Informatics, Japan), and Dr. Teeradaj Racharak (Japan Advanced Institute of Science and Technology (JAIST)).

### Project Description
The research is about construction of content-based knowledge graph using the up-to-date vaccine specific literatures from the CORD-19 dataset.

### Dataset
- Dataset for Knowledge Graph Extraction: [CORD-19](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge)
- Dataset for NER: [CORD-NER](https://xuanwang91.github.io/2020-03-20-cord19-ner/)

### Methodology
1. <b>Dataset Preparation:</b> Latent Dirichlet Allocation (LDA) to focus on vaccine specific information
2. <b>Named Entity Recognition (NER):</b> fine-tuning DistilBERT
3. <b>Relation Extraction:</b> Verb Phrase Extraction, <b>Relation Clustering:</b> Synset Grouping (using Synset information from WordNet Database)
4. <b>Triple Construction:</b> using extracted entities and relations and <b>Analysis:</b> Entity type-based, Relation-based
