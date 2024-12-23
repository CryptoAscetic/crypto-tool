from docx import Document


def read_docx_file(file_path):
    # 打开.docx文件
    doc = Document(file_path)

    # 获取所有段落的文本
    content = "\n".join([para.text for para in doc.paragraphs])

    return content


# 使用示例
file_path = r'A.docx'
docx_content = read_docx_file(file_path)
print(docx_content)
