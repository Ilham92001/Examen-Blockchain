import json

"""
Étape 2 : Modélisation d’une Transaction
"""
class Transaction:
    def __init__(self, exp_id, dest_id, montant):
        """
        Initialise une transaction avec les paramètres donnés.
        
        :param exp_id: Identifiant de l'expéditeur.
        :param dest_id: Identifiant du destinataire.
        :param amount: Montant de la transaction.
        """
        self.exp_id = exp_id
        self.dest_id = dest_id
        self.montant = montant
    
    def to_json(self):
        """
        Sérialise les données de la transaction en format JSON.
        
        :return: Chaîne JSON représentant la transaction.
        """
        return json.dumps({
            "exp_id": self.exp_id,
            "dest_id": self.dest_id,
            "montant": self.montant 
        })
    
    def is_valid(self):
        """
        Valide la transaction.
        
        Règles :
        - L'expéditeur et le destinataire ne doivent pas être nuls ou vides.
        - Le montant doit être un nombre positif.
        
        :return: True si la transaction est valide, False sinon.
        """
        if not self.exp_id or not self.dest_id:
            print("Non valide, données manquantes")
            return False  # L'expéditeur ou le destinataire est invalide
        if not isinstance(self.montant, (int, float)) or self.montant <= 0 :
            if self.montant == 0:
                print("Non valide, montant null")
            return False  # Le montant est invalide
        if self.exp_id == self.dest_id:
            print("Non valide, identifiants égaux")
            return False
        
        print("Transaction valide.")
        return True

    def __repr__(self):
        """
        Représentation lisible de la transaction.
        """
        return f"Transaction(exp_id={self.exp_id}, dest_id={self.dest_id}, montant={self.montant})"
    

# Création d'une transaction
transaction = Transaction(exp_id="Alice", dest_id="Bob", montant=100)
transaction1 = Transaction(exp_id="Nazir", dest_id="Nazir", montant=100)
transaction2 = Transaction(exp_id="Ilham",dest_id="",montant=600)
transaction3 = Transaction(exp_id="Nazir",dest_id="Ilham", montant=0)

print(transaction.to_json())
transaction.is_valid()

print(transaction1.to_json())
transaction1.is_valid()

print(transaction2.to_json())
transaction2.is_valid()

print(transaction3.to_json())
transaction3.is_valid()


# Sérialisation en JSON
transaction_json = transaction.to_json()
print("Transaction en JSON :", transaction_json)

# Exemple de transaction invalide
transaction_invalide = Transaction(exp_id="", dest_id="Bob", montant=-50)
print(transaction_invalide)
print("Transaction valide :", transaction_invalide.is_valid())