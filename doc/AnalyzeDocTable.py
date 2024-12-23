from docx import Document


def read_docx_tables(file_path):
    # 打开.docx文件
    doc = Document(file_path)

    tables_data = []  # 存储所有表格的内容

    # 遍历文档中的所有表格
    for table in doc.tables:
        table_content = []  # 存储当前表格的内容

        # 遍历表格的每一行
        for row in table.rows:
            row_data = []  # 存储当前行的内容
            # 遍历行中的每一个单元格
            for cell in row.cells:
                row_data.append(cell.text.strip())  # 获取单元格的文本
            table_content.append(row_data)  # 将行数据添加到表格内容中

        tables_data.append(table_content)  # 将表格内容添加到总数据中

    return tables_data


# 使用示例
file_path = r'A.docx'
tables = read_docx_tables(file_path)

# 打印每个表格的内容
for idx, table in enumerate(tables):
    print(f"Table {idx + 1}:")
    for row in table:
        print(row)
    print("\n")
