import hashlib
import time

"""
Étape 1 : Création d’un Bloc
"""
class Block:
    def __init__(self, index, transactions, previous_hash):
      
        self.index = index
        self.timestamp = time.time()  # Horodatage du moment de la création du bloc
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Initialisation du nonce à 0
        self.hash = self.generate_hash()  # Génération du hachage initial
    
    def generate_hash(self):
        """
        Génère le hachage du bloc en combinant ses attributs.
        
        :return: Hachage SHA-256 en format hexadécimal.
        """
        block_content = (
            str(self.index) +
            str(self.timestamp) +
            str(self.transactions) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_content.encode()).hexdigest()
    

    """
    Étape 3 : Preuve de Travail (Proof of Work)
    """
    def proof_of_work(self, difficulty):
        """
        Résout le problème de preuve de travail en trouvant un nonce qui satisfait la difficulté.
        
        :param difficulty: Nombre de zéros requis au début du hachage.
        :return: Le hachage validé.
        """
        target = "0" * difficulty  # La cible : une chaîne avec 'difficulty' zéros
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.generate_hash()
        return self.hash

    
    def __repr__(self):
        """
        Représentation lisible du bloc.
        """
        return (f"Block(index={self.index}, timestamp={self.timestamp}, "
                f"transactions={self.transactions}, previous_hash={self.previous_hash}, "
                f"nonce={self.nonce}, hash={self.hash})")
    

if __name__ == "__main__":
    # Transactions fictives
    transaction = [
        {"from": "Alice", "to": "Bob", "montant": 10},
        {"from": "Bob", "to": "Charlie", "montant": 5}
    ]

    # Hachage fictif du bloc précédent
    previous_hash = "0" * 64

    # Création d'un bloc
    block = Block(index=1, transactions=transaction, previous_hash=previous_hash)
   
    # Résolution de la preuve de travail avec difficulté 4
    print("Calcul du hachage avec preuve de travail...")
    valid_hash = block.proof_of_work(difficulty=4)

    # Affichage des détails du bloc
    print("Bloc généré :")
    print(f"Index : {block.index}")
    print(f"Horodatage : {block.timestamp}")
    print(f"Transactions : {block.transactions}")
    print(f"Hachage précédent : {block.previous_hash}")
    print(f"Hachage : {block.hash}")
    print(f"Nonce : {block.nonce}")

   
"""
Explication des parties du code
	1.	Attributs de la classe Block :
        •	index : Identifiant unique du bloc.
        •	timestamp : Heure exacte de la création du bloc (en secondes depuis l’époque Unix).
        •	transactions : Liste de transactions associées au bloc.
        •	previous_hash : Hachage du bloc précédent dans la chaîne.
        •	nonce : Valeur ajustable pour la preuve de travail (initialisée à 0).
        •	hash : Hachage calculé pour ce bloc à l’aide de la méthode generate_hash().

	2.	Méthode generate_hash() :
        •	Combine les attributs du bloc (index, timestamp, transactions, previous_hash et nonce) en une chaîne.
        •	Calcule un hachage SHA-256 de cette chaîne pour garantir une signature unique.

	3.	Représentation du bloc (__repr__) :
	    •	Permet d’afficher les informations du bloc de manière lisible pour le débogage ou l’affichage.
"""