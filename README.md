# AdvProgNavTCC: Artificial Intelligence (Machine Learning & Deep Learning)

Course repository for the **NAVTTC "Prime Minister's Hunarmand Pakistan Program: Skills for All"** course
*Artificial Intelligence (Machine Learning and Deep Learning)*.

| | |
|---|---|
| **Duration** | 6 months (26 weeks) |
| **Contact hours** | 520 (4 h/day, 20 h/week) |
| **Theory / Practical** | 20% / 80% |
| **Class size** | 20–24 trainees |
| **Specialization** | NLP or Computer Vision |
| **Official curriculum** | [docs/curriculum/](docs/curriculum/AdvanceprogrammingDeeplearningandMachinelearning.pdf) |

## Repository layout

```
.
├── docs/curriculum/   Official NAVTTC curriculum (PDF)
├── syllabus/          Course outline, learning outcomes, full task index
├── setup/             Environment setup (Anaconda, Jupyter, requirements)
├── weeks/             One folder per week
│   └── week-NN-topic/
│       ├── README.md  Learning units, lab tasks, instructor checklist
│       ├── slides/    Lecture slides
│       ├── code/      Instructor demo notebooks / scripts
│       ├── exercises/ Lab tasks for trainees
│       └── solutions/ Reference solutions
├── assessments/       Mid-term (week 15) and final assessment (week 26)
├── projects/          Employable project (weeks 21–26) guidelines and ideas
├── datasets/          Small datasets (large files are git-ignored)
├── resources/         Books, online material, reference links
└── templates/         Notebook / slide / project report templates
```

## Weekly schedule

| Week | Module | Tasks |
|---|---|---|
| 1 | [Introduction & Basics of Python](weeks/week-01-intro-ai-python-basics/) | 1–11 |
| 2 | [Conditional Statements, Loops, Functions & String Handling](weeks/week-02-control-flow-loops-functions-strings/) | 12–21 |
| 3 | [Data Types and Their Differences](weeks/week-03-data-types-exceptions/) | 22–28 |
| 4 | [Introduction to NumPy](weeks/week-04-numpy/) | 29–41 |
| 5 | [Introduction to Pandas](weeks/week-05-pandas/) | 42–49 |
| 6 | [Graphical Interpretation of Data](weeks/week-06-data-visualization-matplotlib/) | 50–63 |
| 7 | [Introduction to Machine Learning](weeks/week-07-intro-machine-learning/) | 64–70 |
| 8 | [Supervised Learning I: Regression](weeks/week-08-supervised-learning-regression/) | 71–74 |
| 9 | [Supervised Learning II: Classification](weeks/week-09-supervised-learning-classification/) | 75–79 |
| 10 | [SVM & Clustering Techniques](weeks/week-10-svm-clustering/) | 80–83 |
| 11 | [Time Series Analysis](weeks/week-11-time-series-hmm/) | 84–85 |
| 12 | [Introduction to Neural Networks I](weeks/week-12-neural-networks-1/) | 86–88 |
| 13 | [Introduction to Neural Networks II](weeks/week-13-neural-networks-2/) | 89 |
| 14 | [Dealing with Textual Data I](weeks/week-14-nlp-textual-data-1/) | 90 |
| 15 | [Mid-Term Assignment](weeks/week-15-midterm/) | — |
| 16 | [Dealing with Textual Data II](weeks/week-16-nlp-textual-data-2/) | 91–92 |
| 17 | [Introduction to OpenCV I](weeks/week-17-opencv-1/) | 93–95 |
| 18 | [Introduction to OpenCV II](weeks/week-18-opencv-2/) | 96–100 |
| 19 | [Introduction to Deep Learning](weeks/week-19-intro-deep-learning/) | 101–102 |
| 20 | [TensorFlow](weeks/week-20-tensorflow/) | 103 |
| 21 | [Employable Project Kick-off](weeks/week-21-employable-project-kickoff/) | — |
| 22 | [Convolutional Neural Networks I](weeks/week-22-cnn-1/) | 104–108 |
| 23 | [Convolutional Neural Networks II](weeks/week-23-cnn-2/) | 109–110 |
| 24 | [Colorizing Photos with Deep Learning](weeks/week-24-photo-colorization/) | 111 |
| 25 | [Chatbot & Text-to-Speech](weeks/week-25-chatbot-text-to-speech/) | 112–113 |
| 26 | [Entrepreneurship & Final Assessment](weeks/week-26-entrepreneurship-final-assessment/) | 114–115 |

The full list of all 115 lab tasks is in [syllabus/task-index.md](syllabus/task-index.md).

## Getting started

See [setup/README.md](setup/README.md). Quick version:

```bash
conda env create -f setup/environment.yml
conda activate advprog-ai
jupyter notebook
```
