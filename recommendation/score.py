import argparse
import json
import numpy as np

def build_arg_parser():
    parser=argparse.ArgumentParser(description='compute similarity score')

    parser.add_argument('--user1',dest='user1',required=True,help='first user')
    parser.add_argument('--user2',dest='user2',required=True,help='second user')
    
    parser.add_argument('--score-type',dest="score_type",required=True,choices=['Euclidean','Pearson'],help='similarity metric')
    return parser


#calculer la distance euclidienne
def score_euclidien(dataset,user1,user2):
    """Calculer le score Eucliedien"""
    if user1 not in dataset:
        raise TypeError(f"cannot find {user1} in the dataset.")
    if user2 not in dataset:
        raise TypeError(f"cannot find {user2} in the dataset.")
    
    #creer un dictionnaire pour les films evaluer par les 2 utilisateurs
    film_commun={}
    for item in dataset[user1]:
        if item in dataset[user2]:
            film_commun[item]=1
    
    #si aucun film retorner 0
    if len(film_commun)==0:
        return 0

    #Calculer la distance euclidienne et le score
    difference_carree=[]
    for item in dataset[user1]:
        if item in dataset[user2]:
            difference_carree.append(np.square(dataset[user1][item]-dataset[user2][item]))
    
    return 1/(1+np.sqrt(np.sum(difference_carree)))

def score_Pearson(dataset,user1,user2):
    """Calculer le score pearson."""
    if user1 not in dataset:
        raise TypeError(f"Impossible de trouver l utilisateur {user1}")
    if user2 not in dataset:
        raise TypeError(f"imposible de trouver l utilisateur {user2}")
    
    #creer un dictionnaire contenant les films communs
    films_communs={}

    for item in dataset[user1]:
        if item in dataset[user2]:
            films_communs[item]=1
    

    num_ratings=len(films_communs)

    #si ya aucun film en commun on peut pas calculer le score
    if num_ratings==0:
        return 0
    
    #Calculer a somme des evaluations des  films communs

    




if __name__=='__main__':
    args=build_arg_parser().parse_args()
    user1=args.user1
    user2=args.user2
    score_type=args.score_type

    fichier_evaluation='ratings.json.txt'

    with open(fichier_evaluation,'r') as f:
        data=json.loads(f.read())
    

if score_type=="Euclidean":
    print("\n Ecludean score :")
    print(score_euclidien(data,user1,user2))
