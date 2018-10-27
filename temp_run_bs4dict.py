import pickle
import networkx as nx
import matplotlib.pyplot as plt
import bs4dictionary as bs


def run():
    # Har lave et wordpress side med få links:
    # 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'

    number_of_generations = 2
    url = 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'

    # lav et objekt (scrape_result) der holder en dictionary med de scrapede links:
    start_list = []
    start_list.append(url)
    scrape_result = bs.create_dictlist(start_list, number_of_generations)
    
    # tag vores dictionary (scrape_result.pub_dict), og serilizer til filen 'links_serialized':
    filename = 'links_serialized'
    outfile = open(filename, 'wb')
    pickle.dump(scrape_result.pub_dict, outfile)
    outfile.close()
    
    #læs den serialiserede fil ind igen som en dictionary 
    # (vi serialiserede bare fordi vi kan (og skal lære det)
    infile = open(filename,'rb')
    deserial_dict = pickle.load(infile)
    infile.close()
        
    # vi laver en networks illustration:
    DG = nx.DiGraph(deserial_dict) 
    
    nx.draw(DG)
    plt.savefig("graph.png")
    plt.show()
  