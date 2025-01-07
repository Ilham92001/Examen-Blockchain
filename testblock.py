import hashlib
import unittest
from block import Block

class TestBlock(unittest.TestCase):
    def test_generate_hash(self):
        """
        Teste si le hachage généré est correct en fonction des données du bloc.
        """
        block = Block(index=1, transactions=["Test transaction"], previous_hash="0" * 64)
        expected_hash = hashlib.sha256((
            str(block.index) +
            str(block.timestamp) +
            str(block.transactions) +
            str(block.previous_hash) +
            str(block.nonce)
        ).encode()).hexdigest()
        self.assertEqual(block.hash, expected_hash, "Le hachage généré n'est pas correct.")

    def test_proof_of_work(self):
        """
        Teste si la preuve de travail génère un hachage avec le bon nombre de zéros.
        """
        block = Block(index=1, transactions=["Test transaction"], previous_hash="0" * 64)
        difficulty = 4
        block.proof_of_work(difficulty)
        self.assertTrue(
            block.hash.startswith("0" * difficulty),
            f"Le hachage ne commence pas par {difficulty} zéros."
        )

    def test_hash_changes_with_nonce(self):
        """
        Teste si le hachage change lorsque le nonce est modifié.
        """
        block = Block(index=1, transactions=["Test transaction"], previous_hash="0" * 64)
        initial_hash = block.hash
        block.nonce += 1
        new_hash = block.generate_hash()
        self.assertNotEqual(initial_hash, new_hash, "Le hachage n'a pas changé après modification du nonce.")

if __name__ == "__main__":
    unittest.main()