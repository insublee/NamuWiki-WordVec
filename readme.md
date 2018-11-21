# NamuWiki WordVector Project 

This project was started for generating Dodamdodam Educational contents.

Application "Dodam dodam" is a korean education application for foreigners, so we need various and numerous educational contents. But,  we(dodamdodam) are consisted of two server enginners and one client engineer. 

We already have **verified** verbal data for teaching content and its example sentences. However, We do not have enough man-powers to create all linguistic data line-by-line. So, I decided to create general-content generator for our applications, and this project was part of it.

I wanted to find data set which has enough size to learn and consisted of not that perfectly grammerly-correct sentences. So I found [Namiwiki Data set](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%8D%A4%ED%94%84).

## Usage

### Without Learning

I opened this project to **online API** for people who - 

* Cannot understand how to build this project.
* Has not enough computing power to download and process files.
* Just want to testing korean version of word vector.



This api is running on Lambda (AWS). Endpoint is..

http://vector.juung.me

To learn how to use this API

### With Learning

##### Before Build this project

If your devices Operating System is **Windows**, you cannot use underneath methods to install **Mecab-ko** project. [This link](https://groups.google.com/forum/#!topic/eunjeon/Dzohqj4n3QI) may quite helpful.

This project for python 3.6 and over.

I uploaded code using Okt corpus library for Window users, but Mecab-ko library is speedier and well-funtioning than other libraries. So, If your OS is **Mac OS** or **Linux/Unix**, Please use mecab library.

May you just want to use this code without any modification, You have to install jpype for using Okt Libraries.

##### Start for download

1. So, clone this repository and run this command to install all required libraries.

```shell
pip install -r requirements.txt
```

2. Download the .7z file

```shell
python download.py
```

3. Extract it.
4. Run Extracter and Word2Vec Learner

```
python run.py
```

4-1.If you want to receive finish mail to your own email, fill the `/libs/info.json` with your gmail address and api-key (Not just password!)



When you finish your own learning successfully, You'll have 

* name.model
* namu.model.trainables.syn1.npy
* namu.model.trainables.syn1neg.npy
* namu.model.wv.vectors.npy

### Usage

#### Load

```python
# Load Models
model = word2vec.Word2Vec.load('namu.model')
```

#### Most Similar Word

```python
model.wv.most_similar(positive=[...], negative=[...])
```
