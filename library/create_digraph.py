import time
import pickle
import networkx as nx
import matplotlib.pyplot as plt
import library.bs4dictionary as bs
import library.dictlist as dl

def run(url, number_of_generations):
   
    start_time = time.time()

    # lav et objekt (scrape_result) der holder en dictionary med de scrapede links:
    start_list = []
    start_list.append(url)
    scrape_result = bs.create_dictlist(start_list, number_of_generations)
    
    #tag vores dictionary (scrape_result.pub_dict), og serilizer til filen 'links_serialized':
    filename = 'links_serialized'
    outfile = open(filename, 'wb')
    pickle.dump(scrape_result.pub_dict, outfile)
    outfile.close()
    
    #læs den serialiserede fil ind igen som en dictionary 
    # (vi serialiserede bare fordi vi kan (og skal lære det))
    infile = open(filename,'rb')
    deserial_dict = pickle.load(infile)
    infile.close()

    # vi laver en networks illustration:
    DG = nx.DiGraph(deserial_dict, rank="source") 
    
    nx.draw(DG)
    plt.savefig("graph.png")
    plt.show()

    elapsed_time = time.time() - start_time
    pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    print(pretty_time)
