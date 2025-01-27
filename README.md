# AfriHG: News Headline Generation for African Languages

[paper](https://arxiv.org/abs/2412.20223) |  [dataset](https://github.com/dadelani/AfriHG/tree/main/data)

## Introduction

We introduce AfriHG, a news headline generation dataset created by combining the [XLSum](https://github.com/csebuetnlp/xl-sum) and [MasakhaNEWS](https://github.com/masakhane-io/masakhane-news) datasets, focusing on 16 widely spoken African languages. We experimented with two sequence-to-sequence (seq2seq) models, mT5-base and AfriTeVa V2, as well as the Aya-101 large language model (LLM). Our results demonstrate that Africa-centric seq2seq models, such as AfriTeVa V2, outperform the massively multilingual mT5-base model. Additionally, we show that fine-tuning AfriTeVa V2 with 313M parameters yields competitive performance compared to prompting Aya-101 LLM, which has over 13B parameters. Using the Multilingual-Rouge metric provided accurate scores for Non-Latin Script Languages, addressing issues identified in the findings from [AfriHG presented at AfricaNLP'24](https://openreview.net/forum?id=fw7g7pNUDl).


## Data Gathering
We obtained the data by combinig the XL-Sum corpus with MasakhaNews corpus (of which most data are scraped from BBC news, and a few other websites listed in MasakhaNews. The full corpus can also be downloaded from [AfriHG Google Drive Link](https://drive.google.com/drive/folders/1O0gtU17d18zrundQPokUbEpC9-f7nGcm?usp=sharing)

### Data Splits

For all languages, we maintained the splits used in the XL-Sum and added all data from Masakhanews to the train data, while Languages like Shona, Xhosa, and Zulu that are not available in XL-Sum where splitted into a Train/Dev/Test split of 80/10/10 ratio used in the XL-Sum.

The original splits were named `train`, `dev` and `test` and they correspond to the `train`, `validation` and `test` splits.

<!-- 
## Data Usage 
```
from datasets import load_dataset
data = load_dataset('masakhanews', 'yor') 

# Please, specify the language code

# A data point example is below:

{
'label': 0, 
'headline': "'The barriers to entry have gone - go for it now'", 
'text': "j Lalvani, CEO of Vitabiotics and former Dragons' Den star, shares his business advice for our CEO Secrets series.\nProduced, filmed and edited by Dougal Shaw", 
'headline_text': "'The barriers to entry have gone - go for it now' j Lalvani, CEO of Vitabiotics and former Dragons' Den star, shares his business advice for our CEO Secrets series.\nProduced, filmed and edited by Dougal Shaw", 
'url': '/news/business-61880859'
}
``` 
-->


Table below summarizes the Data Split and model performance on the AfriHG and In comparation with the XL-Sum Abstractive Summarization results.

| Language       | Script | Train / Dev / Test       | mT5-base (Summary) | mT5-base (Headline) | AfriTeVa V2-base (Headline) | Aya (Headline) |
|----------------|--------|--------------------------|--------------------|---------------------|-----------------------------|----------------|
| Amharic (amh)  | Ge'ez  | 16,915 / 719 / 719       | 20.0 / 7.4 / 18.1  | 17.9 / 6.0 / 16.9   | 19.4 / 6.8 / 18.6           | **22.6 / 8.5 / 21.4** |
| Arabic (arb)   | Arabic | 37,519 / 4,689 / 4,689   | 35.0 / 14.8 / 29.2 | 25.3 / 9.0 / 23.2   | 24.1 / 8.2 / 24.1           | **28.1 / 10.8 / 25.4** |
| English (eng)  | Latin  | 311,694 / 11,535 / 11,535| 37.6 / 15.2 / 29.9 | 36.1 / 13.5 / 31.9  | **37.9 / 14.5 / 33.4**      | 32.3 / 11.7 / 28.2 |
| French (fra)   | Latin  | 15,377 / 1,086 / 1,086   | 35.3 / 16.2 / 28.2 | 30.6 / 13.7 / 27.2  | 33.8 / 15.7 / 29.8          | **35.9 / 17.5 / 31.0** |
| Hausa (hau)    | Latin  | 17,174 / 802 / 802       | 39.4 / 17.7 / 31.7 | 30.2 / 11.1 / 26.9  | **35.0 / 14.9 / 31.5**      | 34.5 / 14.8 / 30.1 |
| Igbo (ibo)     | Latin  | 8,877 / 522 / 522        | 31.6 / 10.2 / 24.5 | 28.5 / 11.2 / 24.6  | 31.0 / 12.7 / 27.2          | **33.4 / 14.9 / 28.7** |
| Oromo (orm)    | Latin  | 16,417 / 757 / 757       | 18.7 / 6.2 / 16.2  | 15.7 / 4.7 / 14.8   | 18.8 / 6.5 / 17.6           | **19.6 / 6.7 / 18.3** |
| Pidgin (pcm)   | Latin  | 18,214 / 1,151 / 1,151   | 39.0 / 15.1 / 29.9 | 31.5 / 10.9 / 27.0  | **33.8 / 12.2 / 29.1**      | 30.5 / 10.5 / 26.2 |
| Kirundi (run)  | Latin  | 9,930 / 718 / 718        | 32.0 / 14.4 / 25.8 | 25.2 / 8.9 / 22.5   | **29.2 / 11.0 / 25.7**      | 27.9 / 10.5 / 25.1 |
| Shona (sna)    | Latin  | 9,573 / 1,064 / 1,064    | - / - / -          | 22.6 / 8.1 / 22.1   | **25.5 / 9.6 / 24.7**       | 23.5 / 8.2 / 22.7 |
| Somali (som)   | Latin  | 10,508 / 745 / 745       | 31.6 / 11.6 / 24.2 | 24.1 / 7.0 / 21.2   | 28.2 / 9.6 / 24.7           | **28.6 / 10.5 / 24.9** |
| Swahili (swa)  | Latin  | 18,914 / 987 / 987       | 37.7 / 17.9 / 30.9 | 33.0 / 13.4 / 29.1  | 37.6 / 15.8 / 33.1          | **38.9 / 16.7 / 33.9** |
| Tigrinya (tir) | Ge'ez  | 12,351 / 681 / 681       | 25.3 / 8.0 / 21.2  | 21.9 / 7.0 / 19.8   | 26.3 / 8.7 / 23.7           | **25.7 / 8.6 / 22.8** |
| Xhosa (xho)    | Latin  | 10,440 / 1,305 / 1,305   | - / - / -          | 13.0 / 4.0 / 12.7   | 15.2 / 5.5 / 14.9           | **16.1 / 5.3 / 15.2** |
| Yoruba (yor)   | Latin  | 15,172 / 793 / 793       | 31.7 / 11.7 / 25.1 | 40.0 / 14.8 / 31.4  | **42.0 / 16.2 / 33.1**      | 36.0 / 13.5 / 28.3 |
| Zulu (zul)     | Latin  | 14,209 / 1,776 / 1,776   | - / - / -          | 16.0 / 5.0 / 15.5   | **17.8 / 5.5 / 17.4**       | 17.0 / 4.9 / 16.2 |
| **Average**    | --     | -                        | - / - / -          | 25.7 / 9.3 / 22.9   | **28.5 / 10.84 / 25.5**     | 28.2 / 10.85 / 24.9 |

**Table 1 shows the data split for all languages in AfriHG, Rouge score (R1/R2/RL) comparing news summarization from [XL-Sum paper](https://arxiv.org/abs/2106.13822) to AfriHG Headline Generation. - / - / - indicates the evaluation values that are not available in the XL-Sum.**


### BibTeX entry and citation info
```
@misc{ogunremi2024afrihgnewsheadlinegeneration,
      title={AfriHG: News headline generation for African Languages}, 
      author={Toyib Ogunremi and Serah Akojenu and Anthony Soronnadi and Olubayo Adekanmbi and David Ifeoluwa Adelani},
      year={2024},
      eprint={2412.20223},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.20223}, 
}

```
