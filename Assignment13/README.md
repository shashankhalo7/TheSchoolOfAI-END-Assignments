# Assignment 13

**Group Members:**
* Divyam Shah
* Subramanya Rao
* Shashank Pathak


## Datasets used:
[Cornell Movie-Dialogs Corpus](http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html)


## Notebooks
#### Training a Chatbot using Cornell Movie-Dialogs Corpus
This corpus contains a large metadata-rich collection of fictional conversations extracted from raw movie scripts with around 220,579 conversational exchanges between 10,292 pairs of movie characters, involves 9,035 characters from 617 movies and in total 304,713 utterances. We Used movie-lines and movie_conversations text files to generate 221282 ordered dialogue pairs. As suggested in this [blog](https://pytorch.org/tutorials/beginner/chatbot_tutorial.html), we also filtered out dialogue pairs, in which any of the dialogue had a length less than or equal to 20 and used that to train the model with a 70/30 train val split. This reulted is around 23312 pairs, which we used as Input and Output for the trasnformer models   
 [[Notebook](https://github.com/shashankhalo7/TheSchoolOfAI-END-Assignments/blob/main/Assignment9/Cornell_Movie_Dialogs_Corpus_Learning_Phrase_Representations_using_RNN_Encoder_Decoder_for_Statistical_Machine_Translation.ipynb)] [[Data](http://www.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html)]

![Training Logs]()
