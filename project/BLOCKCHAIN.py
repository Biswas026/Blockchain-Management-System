
import pandas as pd
import tkinter as tk
import hashlib
from tkinter import filedialog

def hashgenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.generate_hash()

    def generate_hash(self):
        data_to_hash = self.data + self.prev_hash
        return hashgenerator(data_to_hash)

class Blockchain:
    def __init__(self):
        hash_start ="0"
        genesis = Block("gen-data", hash_start)
        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        block = Block(data, prev_hash)
        self.chain.append(block)

    def show_blockchain(self):
        for block in self.chain:
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.prev_hash)
            print("------------------------")

bc = Blockchain()
print("Choose the file displaying the results")
root = tk.Tk()
root.withdraw()
xcel_file=filedialog.askopenfilename(title="select a file",filetypes=[("Excel Files",(".xlsx"))])
df=pd.read_excel(xcel_file)
length=len(df)

while True:
    choice = int(input("Enter your choice: 1.Create Block  2.Display Blockchain  3.Verify  4.Exit"))
    if choice == 1:
        for i in range(0,length):
            data =f"{df['Name'][i]} {df['Reg_NO'][i]} {df['Attendance'][i]} {df['Quiz'][i]} {df['Internal-1'][i]} {df['Internal-2'][i]} {df['Assignment'][i]} {df['Total'][i]}"
            bc.add_block(data)
        print("Blocks added successfully")

    elif choice == 2:
        bc.show_blockchain()

    elif choice == 3:
        bc_clone = Blockchain()
        df = pd.read_excel(xcel_file)
        length = len(df)

        for i in range(0,length):
            data =f"{df['Name'][i]} {df['Reg_NO'][i]} {df['Attendance'][i]} {df['Quiz'][i]} {df['Internal-1'][i]} {df['Internal-2'][i]} {df['Assignment'][i]} {df['Total'][i]}"
            bc_clone.add_block(data)

        flag = True
        for index, value in enumerate(bc_clone.chain):
            if bc_clone.chain[index].hash != bc.chain[index].hash:
                print(bc.chain[index].data +" data is changed to "+ bc_clone.chain[index].data)
                flag = False
                bc = bc_clone
                break
        if flag:
            print("All values are correct.")

    elif choice == 4:
        print("Thank you.")
        break
    else:
        print("Please enter a valid choice.")


