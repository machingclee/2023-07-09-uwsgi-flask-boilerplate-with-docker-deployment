from uuid import uuid4
import os

def main (data_source: dict, 
          target_path: str = os.path.abspath(f"./excel_files/output_excel_{uuid4()}.xlsx")):    
    return target_path
    