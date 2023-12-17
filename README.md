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
- Nov 13 : I tried to deploy the app using streamlit but it gave me errors. To deploy you need to create a new repository with the files you want to deploy. The error is from the requirements.txt file. It says I need to upgrade. Well I deployed my first app today. The [scholarship recommender system](https://scholarship-recommender-system.streamlit.app/#what-do-you-do-next-with-this-information). The initial problem was with the `requirements.txt` file. Once I just included the libraries. It worked like magic. Here is the first interface
  ![alt](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/94ac33075cc7144b4ec6cee11faf56d2e73f3cdd/images/Initial%20interface.png)
- Nov 15 : - I numbered the scholarship and embedded some useful Youtube videos in a column. I couldn't use codespace in streamlit to update the codes. It kept on saying something about numpy. I went ahead to update the code in Github. I made a post on Youtube to take suggestions on what to include in the app.
- Nov 20 & 22 : I added the Read more button after 10 scholarships have been displayed. Added a drop down button to select the level needed i.e. BSc, Msc, etc. Filter scholarships to recommend scholarships based on area of specialisation and chosen level. Added contact details. This is how the interface looks now
![alt text](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/8f5302fb08dcfd759d8b97a67d6a59f4306a959f/images/app%20interface%20%20Nov%2022.png)

- Nov 28 : I changed the front page a bit. Added a `Find scholarships button`. Came up with a new name 3SA : School and scholarship search app. There's a bug lol. I want the scholarship recommender system to start running only after the  `Find scholarships button` is clicked and everything went wayhire loL. I am doing this to solve the probelm where the web page starts with this 'There is currently no scholarships in for at this moment in the database. Try a closely related field or type All disciplines for your field on interest.
![App interface Nov 28](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/0e2d9bb03abc8eaec23b50c6c150e3e0cb826abc/images/app%20interface%20Nov%2027.png)

- DEC 2 : Solving the problem of Nov 28 was hell lol. But finally it got done. I worked on the front page not starting with there’s no scholarship Now, I don't have this issue of 'There is currently no scholarships in for at this moment in the database. Try a closely related field or type All disciplines for your field on interest.' 
![](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/94ac33075cc7144b4ec6cee11faf56d2e73f3cdd/images/app%20interface%20Dec%202.png)

- DEC 4 : Filtered to include the link but had to drop it again because there were a lot of empty cells. I added the country as an optional filtering. There is a problem where once one clicks on click more for results with more than 10 information. The whole result vanish :-(
![](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/bb309a880aa3df6edc18f6628ec099d299ccdd07/images/app%20interface%20Dec%204%20.png)

- Dec 6 : Watched some videos on streamlit and checked apps others have built to get some inspirations. The idea of expanders/toggle list was interesting as well as including a buy me cofee sections. Included 2 videos : how to write a cold email and prepare for an interview. Added some emojis and colors.

- ![](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/d539de2d2db848e1d936d84234d90e1a2913f698/images/app%20interface%20Dec%206.png)

- Dec 9 : I have finally come to an end with this web app lol. Yay. I made a few changes and additions from the start till the end. I added a buy me coffee button. Money is nice lol 💵. Solved the issue of the vanishing `Read more` button with expanders that store the other names. Used a drop down for the levels and country by selecting the unique countries and levels already in the database. It was a great learning experience. The next few days. I will use to go over the codes. Here is the [web app](https://scholarship-recommender-system.streamlit.app/)
 ![](https://github.com/barbaraaboagye/Scholarship-Recommender-System/blob/798f7559fc832f8600b0629b322584e3cd70ddf4/images/app%20interface%20Dec%209.png)

- Dec 11 : I went over the pre-processing code.
- Dec 13 : I went over the code for the scholarship app (Still not done)
- Dec 17 : I started writing the article titled **HOW TO BUILD A SCHOOL AND SCHOLARSHIP SEARCH APP (3SA) USING PYTHON AND STREAMLIT (PART 1) : DATA CLEANING AND PREPROCESSING**
