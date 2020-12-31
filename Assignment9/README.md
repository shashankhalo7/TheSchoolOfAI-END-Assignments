# Assignment 3

**Group Members:**
* Shashank Pathak
* Divyam Shah
* Subramanya Rao

## Datasets used:
1. [Question-and-answer dataset](http://www.cs.cmu.edu/~ark/QA-data/) 
2. [Quora question pair](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs) 
3. [Customer Support on Twitter](https://www.kaggle.com/thoughtvector/customer-support-on-twitter)
4. [Cornell Movie-Dialogs Corpus](http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html)


## Notebooks
### 1. Question-and-answer dataset
Question and Answer dataset from CMU corpus. Tab delimied data files from 2008, 2009 and 2010 are combined into one single file merged_qa.csv and used Question and Answers as the Source and terget respectively.
1. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/QA_CMU_Dataset_using_RNN_Encoder_Decoder.ipynb)] [[Data](http://www.cs.cmu.edu/~ark/QA-data/)]
2. Neural Machine Translation by Jointly Learning to Align and Translate [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/QA_CMU_Dataset_using_Neural_Machine_Translation.ipynb)] [[Data](http://www.cs.cmu.edu/~ark/QA-data/)]
### 2. Quora question pair
Quora Questions pair [dataset](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs) . Tab delimied data file 'quora_duplicate_questions.csv' and manually uploaded to colab. We use only questions pair that are semantically equivalent as Source and target for this exercise to train a question paraphrasing model.
1. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/QA_Quora_Dataset_using_RNN_Encoder_Decoder.ipynb)] [[Data](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)] 
2. Neural Machine Translation by Jointly Learning to Align and Translate [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/QA_Quora_Dataset_using_Neural_Machine_Translation.ipynb)] [[Data](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)] 
### 3. Customer Support on Twitter
Customer Support on Twitter dataset is a large, modern corpus of tweets and replies to aid innovation in natural language understanding and conversational models, and for study of modern customer support practices and impact. We used the csv to extract tweets and their corresponding replies by aligning the tweet with the reply_tweet_id amnd mapping it back to the query tweet. We used these as source and target for the Seq2Seq model
1. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/Twitter_CustomerSupport_Dataset_using_RNN_Encoder_Decoder.ipynb)] [[Data](https://www.kaggle.com/thoughtvector/customer-support-on-twitter)]
2. Neural Machine Translation by Jointly Learning to Align and Translate [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/Twitter_CustomerSupport_Dataset_using_Neural_Machine_Translation.ipynb)] [[Data](https://www.kaggle.com/thoughtvector/customer-support-on-twitter)]
### 4. Cornell Movie-Dialogs Corpus
This corpus contains a large metadata-rich collection of fictional conversations extracted from raw movie scripts with around220,579 conversational exchanges between 10,292 pairs of movie characters, involves 9,035 characters from 617 movies and in total 304,713 utterances. We Used movie-lines and movie_conversations text files to generate 221282 ordered dialogue pairs which are used as Input and Output for the Seq2Seq models
1. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/Cornell_Movie_Dialogs_Corpus_Learning_Phrase_Representations_using_RNN_Encoder_Decoder_for_Statistical_Machine_Translation.ipynb)] [[Data](http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html)]
2. Neural Machine Translation by Jointly Learning to Align and Translate [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/Cornell_Movie_Dialogs_Corpus_Neural_Machine_Translation_by_Jointly_Learning_to_Align_and_Translate.ipynb)] [[Data](http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html)]
