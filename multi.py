from hashlib import sha256
import blockchain
import os
import flask
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import hashlib

blockchain = []


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.data) + str(self.previous_hash)
        hash_value = sha256(block_string.encode()).hexdigest()
        return hash_value

class PatientRecord:
    def __init__(self, patient_id, data):
        self.patient_id = patient_id
        self.data = data

def register_tenant(tenant_id, public_key):
    print(f"Tenant {tenant_id} (public key: {public_key}) registered")
    return True

def add_patient_record(tenant_id, patient_record):
    signature = f"SIGNED_BY_{tenant_id}"
    data = {"patient_record": patient_record, "signature": signature}
    previous_hash = blockchain[-1].hash if blockchain else None
    new_block = Block(data, previous_hash)
    blockchain.append(new_block)
    print(f"Patient record for patient {patient_record.patient_id} added by tenant {tenant_id}")



def get_patient_record(patient_id):
    for block in blockchain:
        data = block.data
        if data["patient_record"].patient_id == patient_id:
            print(f"Retrieved patient record for patient {patient_id} (signature verification pending)")
            return data["patient_record"]
    print(f"Patient record for patient {patient_id} not found")
    return None


def main():
    while True:
        print("\nMulti-Tenant Patient Record Simulator")
        print("1. Register Tenant")
        print("2. Add Patient Record")
        print("3. Get Patient Record")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tenant_id = input("Enter tenant ID (hospital/clinic): ")
            public_key = input("Enter tenant's public key: ")
            if register_tenant(tenant_id, public_key):
                print("Tenant registration successful (simulation)")
        elif choice == "2":
            tenant_id = input("Enter tenant ID: ")
            patient_id = input("Enter patient ID: ")
            data = input("Enter patient data (simulated): ")
            patient_record = PatientRecord(patient_id, data)
            add_patient_record(tenant_id, patient_record)
        elif choice == "3":
            patient_id = input("Enter patient ID: ")
            record = get_patient_record(patient_id)
            if record:
                print(f"Patient data: {record.data}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
