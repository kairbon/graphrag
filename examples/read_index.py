import pyarrow.parquet as pq

# # 读取 Parquet 文件
# # table = pq.read_table('/Users/aihe/ai/graphrag/ragtest/output/20240713-223350/artifacts/create_base_documents.parquet')
# table = pq.read_table('/Users/aihe/ai/graphrag/ragtest/output/20240713-223350/artifacts/join_text_units_to_relationship_ids.parquet')
#
# # 将表转换为 Pandas DataFrame
# df = table.to_pandas()
#
# # 打印 DataFrame 的前几行
# print(df.head())

import os
import pandas as pd
import pyarrow.parquet as pq

# 设置 Pandas 显示选项
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)     # 显示所有行
pd.set_option('display.max_colwidth', None) # 显示完整的列内容

def read_parquet_file(file_path):
    try:
        table = pq.read_table(file_path)
        df = table.to_pandas()
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def display_file_info(file_path, df):
    print(f"\nFile: {file_path}")
    print(f"Shape: {df.shape}")
    print("Columns:")
    print(df.columns)
    print("First 5 rows:")
    print(df.head())
    print("="*80)

def main(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.parquet'):
                file_path = os.path.join(root, file)
                df = read_parquet_file(file_path)
                if df is not None:
                    display_file_info(file_path, df)


if __name__ == "__main__":
    directory = "/Users/aihe/ai/graphrag/ragtest/output/20240713-223350/artifacts"  # 替换为你的目录路径
    main(directory)