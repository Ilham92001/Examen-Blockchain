from block import Block

"""
Étape 4 : Création de la Chaîne de Blocs
"""
class Blockchain:
    def __init__(self):
        """
        Initialise la blockchain avec un bloc de genèse.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Crée le bloc de genèse (le premier bloc de la chaîne).
        
        :return: Bloc de genèse.
        """
        return Block(index=0, transactions=[], previous_hash="0" * 64)

    def add_block(self, block):
        """
        Ajoute un nouveau bloc à la chaîne après vérification de son intégrité.
        
        :param block: Le bloc à ajouter.
        """
        if self.is_valid_new_block(block, self.chain[-1]):
            self.chain.append(block)
        else:
            raise ValueError("Le bloc n'est pas valide et ne peut pas être ajouté.")

    def is_valid_new_block(self, new_block, previous_block):
        """
        Vérifie si un nouveau bloc est valide par rapport au bloc précédent.
        
        :param new_block: Nouveau bloc à valider.
        :param previous_block: Bloc précédent dans la chaîne.
        :return: True si le bloc est valide, sinon False.
        """
        if new_block.previous_hash != previous_block.hash:
            return False
        if new_block.index != previous_block.index + 1:
            return False
        if new_block.hash != new_block.generate_hash():
            return False
        return True

    def is_chain_valid(self, chain):
        """
        Vérifie si une chaîne donnée est valide.
        
        :param chain: La chaîne à vérifier.
        :return: True si la chaîne est valide, sinon False.
        """
        # Vérifier le bloc de genèse
        if chain[0] != self.create_genesis_block():
            return False

        # Vérifier les blocs suivants
        for i in range(1, len(chain)):
            if not self.is_valid_new_block(chain[i], chain[i - 1]):
                return False
        return True

    def compare_chains(self, other_chain):
        """
        Compare la chaîne actuelle avec une autre chaîne pour déterminer la plus longue.
        
        :param other_chain: Une autre blockchain.
        :return: La chaîne la plus longue.
        """
        if len(other_chain) > len(self.chain):
            return other_chain
        return self.chain

    """
    Étape 6 : Simulation d’un Réseau Décentralisé
    """
    def resolve_conflicts(self, neighbor_chains):
        """
        Résout les conflits en remplaçant la chaîne actuelle par la plus longue chaîne valide.
        
        :param neighbor_chains: Liste des chaînes des voisins (réseau simulé).
        :return: True si la chaîne actuelle a été remplacée, sinon False.
        """
        new_chain = None
        max_length = len(self.chain)

        for chain in neighbor_chains:
            if len(chain) > max_length and self.is_chain_valid(chain):
                max_length = len(chain)
                new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True
        return False

    def display_chain(self):
        """
        Affiche la chaîne complète dans un format lisible.
        """
        for block in self.chain:
            print(block)


if __name__ == "__main__":
    # Création de la blockchain principale
    blockchain = Blockchain()

    # Ajout de blocs à la chaîne principale
    block1 = Block(index=1, transactions=["Transaction 1"], previous_hash=blockchain.chain[-1].hash)
    block1.proof_of_work(difficulty=4)
    blockchain.add_block(block1)

    block2 = Block(index=2, transactions=["Transaction 2"], previous_hash=blockchain.chain[-1].hash)
    block2.proof_of_work(difficulty=4)
    blockchain.add_block(block2)

    print("Chaîne principale :")
    blockchain.display_chain()

    # Création d'une autre chaîne concurrente
    new_chain = Blockchain()

    block1_alt = Block(index=1, transactions=["Transaction A"], previous_hash=new_chain.chain[-1].hash)
    block1_alt.proof_of_work(difficulty=4)
    new_chain.add_block(block1_alt)

    block2_alt = Block(index=2, transactions=["Transaction B"], previous_hash=new_chain.chain[-1].hash)
    block2_alt.proof_of_work(difficulty=4)
    new_chain.add_block(block2_alt)

    block3_alt = Block(index=3, transactions=["Transaction C"], previous_hash=new_chain.chain[-1].hash)
    block3_alt.proof_of_work(difficulty=4)
    new_chain.add_block(block3_alt)

    print("\nChaîne concurrente :")
    new_chain.display_chain()

    # Résolution des conflits
    print("\nRésolution des conflits...")
    replaced = blockchain.resolve_conflicts([new_chain.chain])

    if replaced:
        print("La chaîne principale a été remplacée.")
    else:
        print("La chaîne principale est restée inchangée.")

    print("\nNouvelle chaîne principale :")
    blockchain.display_chain()