# My Machine Learning Journey

<div align="center">
Researcher · Civil Engineer · Youtuber · Machine Learning Engineer (The Goal)
    <br>
    Sharing and documenting my progress and journey as I learn machine learning
     <br>
</div>

<br>

<div align="center">
    <a target="_blank" href="https://github.com/barbaraaboagye/My-MachineLearning-Journey"><img src="https://img.shields.io/github/last-commit/barbaraaboagye/My-MachineLearning-Journey"></a>&nbsp;
      <a target="_blank" href="https://www.youtube.com/@BarbaraAboagye"><img src="https://img.shields.io/youtube/channel/subscribers/UCEYKFq7ZEg81GYxpzNqYZ4Q?style=social"></a>&nbsp;
    <a target="_blank" href="https://fr.linkedin.com/in/barbara-aboagye-233ba8133"><img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social"></a>&nbsp;
    <a target="_blank" href="https://twitter.com/awesome_ama"><img src="https://img.shields.io/twitter/follow/awesome_ama?style=social"></a>
    <br>
</div>

<br>

The resources I am using can be found [here](https://github.com/barbaraaboagye/My-MachineLearning-Journey/blob/492e4be3db9c2480ffd21b20bd580d753da33226/MACHINE%20LEARNING%20ROADMAP.md)

## APPROACH
- Developed a learning roadmap to follow.
- Followed people who work in the machine learning space on twitter and engage and read their tweets
- Taking the [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) from kaggle

## CHANGE OF PLANS

In March 2023 after a months break, I have decided to follow the framework/roadmap of [Made with ML](https://madewithml.com/)
- March 12 - 19 : Finished the python foundation framework
    - Functions, Methods, List,Tuples, Sets, Dictionaries, list comprehension, Decorators, Callback etc
- March 20 - 23 : Finished the numpy foundation
    - Mathematical objects of linear algebra, indexing and mathematical operations, joining tensors, transpose, etc
- March 24 - 27  : Finished Pandas foundation
    - creating dataframes, exploratory data analysis (.describe(), .hist(), .corr()), pre-processing (.dropna(),.drop(),.reset_index()), filtering,indexing,grouping,saving, etc.
- March 28 - April 3 : Finished PyTorch foundation <br>
    - creating tensor, operations on tensors, indexing, slicing, joining,gradients, etc <br>
PS: I had a hard time installing `torch`on my mac 😭 or better said using torch on vscode maybe?. Once i installed the torch on conda, I had to change the kernel to Pytorch. I missed two study session, trying to figure this out. But I figured it out. Better late than never.
    
## BREAK: April 6 to May 1st 

I am taking a pause on this from April 6 to May 1st. I have other pressing commitments I have to work on in April (ee).

## LIFE HAPPENED : Aug 27

I am back again. Started learning through projects 
- Resume scanner : I finished this. The scanner takes a CV and builds a word cloud. It also can take a job description and use the `similarity function` to determine whether you are well suited for the job.

## SCHOLARSHIP DATABASE RECOMMENDER : Sep 4 to Sep 16 

I cleaned the database from the scholarship database and created a Python based scholarship database, where a user enters the program of interest and a list of scholarships or likely schools are suggested. 

## WEB SCRAPING : Sep 18 to Sep 28

- Sep 25: This is hard. I am currently just watching videos. I tried to scrape data off Twitter but it looks like the API is currently not working. I want to use this knowledge or skill to get scholarship data from universities or scholarship sites. Let's see how it goes. I haven't written any codes yet. Just watching videos at the moment.
- Sep 26 : How to use Find and Find_All to find information from a website
- Sep 27 : Started with trying to extract the table data in the scholarship database
- Sep 28 : Finished a web scraping project
I am learning web scraping to be able to extract scholarship data directly from websites and update it to the scholarship database but I can't seem to figure out yet how to achieve this. ***Sighs**

## STREAMLIT APP : Nov 7 to Nov

- Nov 7 : I watched videos on how to use streamlit to create an app and deploy it. I realised my Github has been marked as spam, and I don't have access to my files. I have sent a reclamation form.
- Nov 8 : I created an app for the scholarship recommendation system. It is hosted on my computer atm.
- Nov 9 : My Github works now :-). I couldn't access stuff since September. Apparently it was because I opened another account. I opened another account because I couldn't access the information on here.
- Nov 13 : I tried to deploy the app using streamlit but it gave me errors. To deploy you need to create a new repository with the files you want to deploy. The error is from the requirements.txt file. It says I need to upgrade. Well I deployed my first app today. The [scholarship recommender system](https://scholarship-recommender-system.streamlit.app/#what-do-you-do-next-with-this-information). The initial problem was with the `requirements.txt` file. Once I just included the libraries. It worked like magic.
- Nov 15 : - I numbered the scholarship and embedded some useful Youtube videos in a column. I couldn't use codespace in streamlit to update the codes. It kept on saying something about numpy. I went ahead to update the code in Github. I made a post on Youtube to take suggestions on what to include in the app.
- Nov 20 & 22 : I added the Read more button after 10 scholarships have been displayed. Added a drop down button to select the level needed i.e. BSc, Msc, etc. Filter scholarships to recommend scholarships based on area of specialisation and chosen level. Added contact details. This is how the interface looks now
![alt text](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/8f5302fb08dcfd759d8b97a67d6a59f4306a959f/images/app%20interface%20%20Nov%2022.png)

- Nov 28 : I changed the front page a bit. Added a `Find scholarships button`. Came up with a new name 3SA : School and scholarship search app. There's a bug lol. I want the scholarship recommender system to start running only after the  `Find scholarships button` is clicked and everything went wayhire loL. I am doing this to solve the probelm where the web page starts with this 'There is currently no scholarships in {field} for {level.upper()} at this moment in the database. Try a closely related field or type *All disciplines* for your field of interest.
![App interface Nov 28](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/0e2d9bb03abc8eaec23b50c6c150e3e0cb826abc/images/app%20interface%20Nov%2027.png)

