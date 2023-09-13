- Aug 27 : Started with a Resume scanner project - Data collection, Exploratory data analysis & Pre processing.
- Aug 28 : Continued and watched some videos - Feature extraction & Training a classifier
- Aug 29 : Still on it - To learn top keywords to analyse. Started personal projects. Goal is to find the top keywords in CV. Mine gave me student and concrete so I guess it's good.
- Aug 30 : Checked the similarity of my CV to an advertised position using the `cosine similarity`. I will build a web app for this. I think it's an interesting tool to see how best your CV is tailored for a job.
- Aug 31 : Created a prediction system. You upload a CV and the model will tell you which job. When I uploaded my CV it did tell me `Civil Engineering`. Yipee. Also looked into creating a webapp using streamlit.
- Sep 1 : Created a web app with streamlit. I need to learn how to deploy this for the public. At the moment its hosted on my computer.
- Sep 4 : I started creating a project called `StudySmart: Discover Scholarships for Your Program`, or simply a `Scholarship predictor`. The objective is to create a machine learning application that helps students find suitable scholarships worldwide based on their chosen program of study or field of specialization.
    - My initial goal was to allow users input their background and the country they want and the predictor will predict the scholarship. Unfortunately, it wasn't a good approach since all the scholarships were unique so it couldn't predict a new scholarship. New approach is to group the scholarships according to programs and allow users to upload their CV. Based on their CV's (study background) it will predict likely scholarships to apply for. This will be the initial idea and I will build on that.
- Sep 11 : I worked on feature extraction. This was a bit tough especially trying to extract the information from the CV headers. Some headers took more information than neccessary. It's not robust but for the time being I will continue with it and see what I come up with. I used `spacy` for this. I had already extracted the pdf using `fitz` and get the CV content in a string type. In the coming days I will look into grouping the scholarships by `area of specialization`, `country` and `level needed`. I spent close to 2h30 mins today. I didn't achieve what I wanted but it's part of the process. I also watched some videos on `groupby` and `agg`.
- Sep 12: I grouped by area of specialization and splitted country, level needed and area of specialisation such that each scholarship has just on enetry.
- Sep 13 : I think I am still going about this all wrong. Watched a video on prediction of whether a news is false or true.

  ### Personal project

  - Get 5 CVs of high achieving scholars
  - Find the words that are frequent in their CV
  - Look at the frequent words in a job description and compare them
  - Fine the suitability of the CV to the job description
