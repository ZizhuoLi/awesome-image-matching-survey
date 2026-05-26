# Awesome Learning-based Image Matching

This repository accompanies the survey **Deep Learning Reforms Image Matching: A Survey and Outlook**. It provides a curated, machine-readable catalog of representative learning-based image matching methods organized according to the taxonomy used in the manuscript.

The goal is to make the survey taxonomy easy to browse, reuse, and update as new detector-descriptors, matchers, outlier filters, geometric estimators, dense correspondence models, and pose regressors appear.

## Paper

**Deep Learning Reforms Image Matching: A Survey and Outlook**  
Shihua Zhang, Zizhuo Li, Kaining Zhang, Yifan Lu, Yuxin Deng, Linfeng Tang, Xingyu Jiang, Hao Zhang, and Jiayi Ma.

## Scope

- Taxonomy follows the survey's Sections 3-4.
- `Year` is separated explicitly for quick scanning.
- `Code` prefers the official repository or an author-linked GitHub project.
- `N/A` means I did not confirm a public GitHub repository in this pass.
- The CSV table in `data/methods.csv` is intended as the source file for downstream reuse.

## Taxonomy

1. Learnable Detector-Descriptor
2. Learnable Outlier Filter / Geometric Estimator
3. Middle-End Sparse Matcher
4. End-to-End Semi-Dense Matcher
5. End-to-End Dense Matcher
6. Pose Regressor

## Learnable Detector-Descriptor

| Method | Venue | Year | Code |
| --- | --- | ---: | --- |
| MatchNet | CVPR | 2015 | N/A |
| DeepDesc | ICCV | 2015 | N/A |
| LIFT | ECCV | 2016 | [Official](https://github.com/cvlab-epfl/LIFT) |
| TFeat | BMVC | 2016 | N/A |
| L2-Net | CVPR | 2017 | [Official](https://github.com/yuruntian/L2-Net) |
| HardNet | NeurIPS | 2017 | [Official](https://github.com/DagnyT/hardnet) |
| LF-Net | NeurIPS | 2018 | N/A |
| SuperPoint | CVPRW | 2018 | [Official](https://github.com/magicleap/SuperPointPretrainedNetwork) |
| D2-Net | CVPR | 2019 | [Official](https://github.com/mihaidusmanu/d2-net) |
| R2D2 | NeurIPS | 2019 | [Official](https://github.com/naver/r2d2) |
| DISK | NeurIPS | 2020 | N/A |
| ALIKE | IEEE TMM | 2022 | [Official](https://github.com/Shiaoming/ALIKE) |
| ALIKED | IEEE TIM | 2023 | [Official](https://github.com/Shiaoming/ALIKED) |
| DeDoDe | 3DV | 2024 | [Official](https://github.com/Parskatt/DeDoDe) |
| XFeat | CVPR | 2024 | [Official](https://github.com/verlab/accelerated_features) |

## Learnable Outlier Filter / Geometric Estimator

| Method | Type | Venue | Year | Code |
| --- | --- | --- | ---: | --- |
| OANet | Outlier Filter | ICCV | 2019 | [Official](https://github.com/zjhthu/OANet) |
| NG-RANSAC | Geometric Estimator | ICCV | 2019 | [Official](https://github.com/vislearn/ngransac) |
| CLNet | Outlier Filter | ICCV | 2021 | N/A |
| ConvMatch | Outlier Filter | AAAI | 2023 | N/A |
| NeFSAC | Geometric Estimator | ICCV | 2023 | N/A |
| RLSAC | Geometric Estimator | ICCV | 2023 | N/A |
| DeMatch | Outlier Filter | CVPR | 2024 | N/A |

## Middle-End Sparse Matcher

| Method | Venue | Year | Code |
| --- | --- | ---: | --- |
| SuperGlue | CVPR | 2020 | [Official](https://github.com/magicleap/SuperGluePretrainedNetwork) |
| SGMNet | ICCV | 2021 | [Official](https://github.com/vdvchen/SGMNet) |
| LightGlue | ICCV | 2023 | [Official](https://github.com/cvg/LightGlue) |
| OmniGlue | CVPR | 2024 | [Official](https://github.com/google-research/omniglue) |
| MambaGlue | ICRA | 2025 | [Official](https://github.com/url-kaist/MambaGlue) |

## End-to-End Semi-Dense Matcher

| Method | Venue | Year | Code |
| --- | --- | ---: | --- |
| NC-Net | NeurIPS | 2018 | N/A |
| Sparse-NCNet | ECCV | 2020 | N/A |
| LoFTR | CVPR | 2021 | [Official](https://github.com/zju3dv/LoFTR) |
| ASpanFormer | ECCV | 2022 | [Official](https://github.com/apple/ml-aspanformer) |
| AdaMatcher | CVPR | 2023 | [Project Repo](https://github.com/AbyssGaze/AdaMatcher) |
| CasMTR | ICCV | 2023 | N/A |
| EfficientLoFTR | CVPR | 2024 | [Official](https://github.com/zju3dv/EfficientLoFTR) |

## End-to-End Dense Matcher

| Method | Venue | Year | Code |
| --- | --- | ---: | --- |
| DGC-Net | WACV | 2019 | [Official](https://github.com/AaltoVision/DGC-Net) |
| GOCor | NeurIPS | 2020 | [Library](https://github.com/PruneTruong/DenseMatching) |
| PDC-Net | ICCV | 2021 | [Library](https://github.com/PruneTruong/DenseMatching) |
| COTR | ICCV | 2021 | [Official](https://github.com/ubc-vision/COTR) |
| DKM | CVPR | 2023 | [Official](https://github.com/Parskatt/DKM) |
| RoMa | CVPR | 2024 | [Official](https://github.com/Parskatt/RoMa) |

## Pose Regressor

| Method | Type | Venue | Year | Code |
| --- | --- | --- | ---: | --- |
| DHN | Deep Homography Estimation | arXiv | 2016 | N/A |
| RPNet | Relative Pose Regression | ECCVW | 2018 | N/A |
| IHN | Deep Homography Estimation | CVPR | 2022 | [Project Repo](https://github.com/imdumpl78/IHN) |
| Map-free | Relative Pose Regression | ECCV | 2022 | [Official](https://github.com/nianticlabs/map-free-reloc) |
| RHWF | Deep Homography Estimation | CVPR | 2023 | [Project Repo](https://github.com/imdumpl78/RHWF) |
| SRPose | Relative Pose Regression | ECCV | 2025 | N/A |

## Data File

The machine-readable table is available at [`data/methods.csv`](./data/methods.csv).

## Citation

If this repository is useful for your work, please cite the associated survey paper. A repository citation template is provided in [`CITATION.cff`](./CITATION.cff).

## Contributing

Issues and pull requests are welcome for missing methods, corrected venues, updated official code links, and additional metadata.

## Notes

- This first version focuses on representative methods explicitly highlighted by the survey taxonomy and figure timeline, plus core methods repeatedly discussed in the text.
- Some survey-internal methods still need a second pass if you want a truly exhaustive "every citation in Sections 3-4" edition.
- Planned extensions include a full paper-by-paper catalog from all cited methods in Sections 3-4, paper links for every row, and category subpages such as `detector_descriptor.md` and `sparse_matchers.md`.
