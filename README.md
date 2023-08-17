# Collect, Measure, Repeat: Reliability Factors for Responsible AI Data Collection

We propose a **Responsible AI (RAI) methodology** designed to guide the data collection with **a set of metrics for an iterative in-depth analysis** of the *factors influencing the quality and reliability* of the generated data. We propose a granular set of measurements to inform on the *internal reliability* of a dataset and its *external stability* over time. We validate our approach across nine existing datasets and annotation tasks and four content modalities. 

This repository contains the validation of our proposed **Responsible AI (RAI) methodology** on nine datasets and the [**supplemental material**](HCOMP2023_SupplementalMaterial.pdf) that accompanies our publication. We publish nine different notebooks, each for one of the following datasets:

 * [**Video Concept Relevance (VCR_E, VCR_P, VCR_L, VCR_O, VCR_ALL)**](): Dataset of 208, 234, 223, 59, and respectively 969 video-concept pairs which have been annotated in terms of relevance in five different annotation tasks, namely focusing on relevent events (VCR_E), relevant people (VCR_P), relevant locations (VCR_L), relevant organizations (VCR_O), and, respectively all relevant concepts (VCR_ALL). The concepts were machine-extracted (video subtitles and video stream) from ten short English news broadcasts (i.e., videos) published on YouTube, from a publicly available dataset used by [Inel, Tintarev and Aroyo (2020)](https://dl.acm.org/doi/pdf/10.1145/3340631.3394862), [Mavridis et al. (2018)](https://ceur-ws.org/Vol-2276/paper11.pdf), and [Inel and Aroyo (2022)](https://dl.acm.org/doi/pdf/10.1145/3539596). Each task was repeated three times, at least three months apart, and each repetition used the same raters’ qualifications, and raters were allowed to participate across repetitions. 

* [**Video Human Facial Expressions (IRep)**](): Dataset of 1090 video recordings of human facial recordings, part of the [International Replication (IRep) dataset](https://github.com/google-research-datasets/replication-dataset), published by [Wong, Paritosh, and Aroyo (2020)](https://doi.org/10.18653/v1/2021.acl-long.548). Each video recording is annotated with emotions from 30 available emotions. The video recordings were generally very short, 5 seconds on average. Each video recording was annotated by two raters. The task was repeated three times, each time with raters from a different pool, namely raters from Mexico City, Kuala Lumpur, Budapest, and internationals.

* [**Product Reviews (PR)**](): Dataset of 20 English product reviews for fashion items (accompanied by a photo representative of the respective product), randomly selected from the dataset published by [Chernushenko et al. (2018)](http://arxiv.org/abs/1805.09648). Each product review is annotated with one of three possible issues classes, as described in the study conducted by [Qarout et al. (2019)](https://ojs.aaai.org/index.php/HCOMP/article/view/5264). The task was repeated five times at intervals of one week. The raters were not allowed to participate in more than one repetition.

* [**Crisis Tweets (CT)**](): Dataset of 20 English crisis-related Twitter messages (\emph{e.g.}, earthquake, flood), randomly selected from the dataset published by [Imran, Mitra, and Castillo (2016)](http://www.lrec-conf.org/proceedings/lrec2016/summaries/842.html). Each tweet is annotated with one of nine possible crisis-related options, as described in the study conducted by [Qarout et al. (2019)](https://ojs.aaai.org/index.php/HCOMP/article/view/5264). The task was repeated five times at intervals of one week. Each rater was allowed to participate in just one repetition.

* [**WordSim (WS353)**](): Dataset of [353 English word pairs](https://aclweb.org/aclwiki/WordSimilarity-353_Test_Collection_(State_of_the_art)) published by [Finkelstein et al. (2001)](https://doi.org/10.1145/371920.372094), used as benchmark for semantic similarity and word embeddings. Each pair is annotated in terms of how similar the two words are on a 1 to 10 scale. The task was first run by [Finkelstein et al. (2001)](https://doi.org/10.1145/371920.372094), 13 or 16 raters annotated each pair of words, and each rater annotated all pairs. The second time the task was run by [Welty, Paritosh, and Aroyo (2019)](http://arxiv.org/abs/1911.01875) in 2019 (after 20 years), on AMT. In this repetition, each pair of words was annotated by 13 raters, and each rater was allowed to annotate as many pairs as they wanted.

All results are published in the following paper:

> Oana Inel, Tim Draws and Lora Aroyo: **[Collect, Measure, Repeat: Reliability Factors for Responsible AI Data Collection](https:...)**. [HCOMP 2023](https://um.org/umap2020/).


If you find the paper and the data useful in your research, please consider citing:

```
@inproceedings{inel2023collect,
  title={Collect, Measure, Repeat: Reliability Factors for Responsible AI Data Collection},
  author={Inel, Oana and Draws, Tim and Aroyo, Lora},
  booktitle={To Appear in the Proceedings of the Eleventh AAAI Conference on Human Computation and Crowdsourcing (HCOMP)},
  year={2023},
  organization={AAAI}
}
```
 
### Note

In order to reproduce the analysis in the notebooks, each dataset needs to be downloaded from their respective source. All sources are provided in this repository or in the publication. 
