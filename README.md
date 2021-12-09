# m0leCon mini 2021 challenge

m0leCon beginner CTF 2021 was a beginner-friendly capture the flag competition organized by 
[Politecnico di Torino](https://www.polito.it/)'s cybersecurity student team 
[pwnthem0le](https://pwnthem0le.polito.it/). Mainly aimed towards Politecnico di Torino's students the competion 
was open to everyone to join and was held online on 3rd December 2021.

## Descritpion
### The Static Website Foundation (easy difficulty)
"Let's make the Web great again!"<br>
Here at the SWF we believe in a static HTML based web, It's way better than the Web there is now.

### How to launch it
Both the ```Dockerfile``` and the ```docker-compose.yaml``` files are provided to launch the server through 
[Docker](https://www.docker.com/).<br>
Alternatively the server can be started directly through [Python](https://www.python.org/). Through a terrminal, 
first install Flask<br>
```pip3 install Flask```<br>
then go into the ```app``` folder and run the server<br>
```python3 -u main.py```

### Hint
<li>A server response isn't only the webpage</li>

### Flag
ptm{l00k_at_Th3_he4d3rs!}

## Solution
Since in the webpage there's nothing useful, by looking ath the response headers we see one called ```Refresh``` 
containing an url ```/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF?p=banana```. By visiting that url we get
the flag.
