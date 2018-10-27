'''
To run the project: python main.py

You can change the url to webscrape from in main.py

You can change the depths of the webscraper in main.py by 
changing the variable number_of_generations.
'''
import library.create_digraph as create


number_of_generations = 2
url = 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'

create.run(url, number_of_generations)
